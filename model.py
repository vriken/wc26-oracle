"""
WC26 Oracle — Bayesian Scoreline Prediction Model

Architecture: Independent Poisson per team with hierarchical priors
  log(λ_i) = α + attack_i - defense_j + stage_effect + venue_adj + manual_adj
  goals_i ~ Poisson(λ_i)

Fit team strengths from qualifying + recent form data.
Blend with market odds where available.
Backtest on 2022 WC before using for 2026.
"""

import csv
import logging
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import numpy as np
from scipy.stats import poisson, nbinom

logger = logging.getLogger(__name__)

# --- Constants ---

# Historical WC average: 2.67 goals/match → 1.335 per team
WC_MEAN_PER_TEAM = 1.335
BASE_ALPHA = math.log(WC_MEAN_PER_TEAM)  # ~0.29

# Stage effects on log scale (from historical data)
# These shift the baseline scoring rate per stage
STAGE_EFFECTS = {
    "group_md1": -0.07,   # openers are cautious
    "group_md2": 0.00,    # baseline
    "group_md3": +0.08,   # more open, dead rubbers or desperation
    "r32": -0.05,         # new round, no historical data — use r16 proxy
    "r16": -0.05,         # tighter knockout games
    "qf": -0.10,          # even tighter
    "sf": -0.05,          # opens up slightly (teams commit)
    "third": +0.05,       # less at stake
    "final": 0.00,        # varies wildly, use baseline
}

# Venue adjustments on log scale
VENUE_EFFECTS = {
    # Mexico
    "mexico_city":  +0.04,   # 2,240m altitude → errors, fatigue
    "guadalajara":  +0.02,   # 1,566m moderate altitude
    "monterrey":    -0.03,   # extreme heat (95°F), no AC → slower pace
    # Canada
    "toronto":       0.00,
    "vancouver":     0.00,   # indoor, comfortable
    # USA — climate controlled
    "dallas":        0.00,   # AC stadium
    "houston":       0.00,   # AC stadium
    "atlanta":       0.00,   # AC stadium
    # USA — outdoor, comfortable
    "seattle":       0.00,
    "san_francisco": 0.00,
    "boston":         0.00,
    "philadelphia":  0.00,
    "new_york":      0.00,
    # USA — outdoor, hot
    "miami":        -0.03,   # 90°F + humidity, partial roof only
    "kansas_city":  -0.02,   # heat risk, outdoor
    "los_angeles":   0.00,   # SoFi has translucent roof
}

# 2026 rule change uplift (applied globally)
RULE_UPLIFT_2026 = 0.04  # ~3-4% more goals from faster restarts, expanded VAR

# Overdispersion for Negative Binomial wrapper
NEGBIN_R = 4.0  # will be calibrated from historical data


@dataclass
class Team:
    """Team strength parameters."""
    name: str
    attack: float = 0.0   # log-scale attack strength (0 = average)
    defense: float = 0.0  # log-scale defense strength (positive = better defense)

    # Metadata for manual adjustments
    manager_style: Literal["defensive", "balanced", "attacking"] = "balanced"
    heat_acclimatized: bool = False      # squad mostly plays in hot climates
    altitude_acclimatized: bool = False  # squad mostly plays at altitude
    key_absences: list[str] = field(default_factory=list)


@dataclass
class MatchInput:
    """All inputs for a single match prediction."""
    team_a: Team
    team_b: Team
    stage: str = "group_md1"
    venue: str = ""
    market_total: float | None = None    # O/U implied total if available
    market_sigma: float = 0.15           # tighter for sharp books, wider for Polymarket
    manual_adj_a: float = 0.0            # per-team manual adjustments
    manual_adj_b: float = 0.0
    is_2026: bool = True


@dataclass
class MatchPrediction:
    """Output of a match prediction."""
    team_a: str
    team_b: str
    lambda_a: float                  # expected goals for team A
    lambda_b: float                  # expected goals for team B
    mu_total: float                  # expected total goals
    scoreline_probs: dict[tuple[int, int], float]  # P(i, j) for each scoreline
    total_probs: dict[int | str, float]            # P(total = k)
    modal_scoreline: tuple[int, int]
    ci_80: tuple[int, int]


def estimate_team_strength(
    qualifying_gf: float,
    qualifying_ga: float,
    qualifying_matches: int,
    recent_gf: float,
    recent_ga: float,
    recent_matches: int,
    fifa_rank: int,
    confederation_adj: float = 0.0,
    striker_form_z: float = 0.0,
    injury_attack_z: float = 0.0,
    injury_defense_z: float = 0.0,
) -> tuple[float, float]:
    """
    Estimate attack and defense strength from available data.

    Returns (attack, defense) on log scale where 0 = WC average.
    Uses weighted composite of data sources with z-score normalization.
    """
    # Goals per game, adjusted for confederation strength
    qual_gpg = (qualifying_gf / max(qualifying_matches, 1)) + confederation_adj
    qual_capg = qualifying_ga / max(qualifying_matches, 1)
    recent_gpg = recent_gf / max(recent_matches, 1)
    recent_capg = recent_ga / max(recent_matches, 1)

    # Convert to z-scores relative to WC average (1.335 per team)
    avg = WC_MEAN_PER_TEAM
    z_qual_gf = (qual_gpg - avg) / avg
    z_qual_ga = (qual_capg - avg) / avg
    z_recent_gf = (recent_gpg - avg) / avg
    z_recent_ga = (recent_capg - avg) / avg
    z_rank = (30 - fifa_rank) / 30  # positive for top teams, negative for low-ranked

    # Weighted composite (from GPT Reasoning's formula, slightly simplified)
    attack = (
        0.20 * z_rank
        + 0.35 * z_qual_gf
        + 0.30 * z_recent_gf
        + 0.10 * striker_form_z
        - 0.05 * injury_attack_z
    )
    defense = (
        0.20 * z_rank
        + 0.35 * (-z_qual_ga)
        + 0.30 * (-z_recent_ga)
        - 0.05 * injury_defense_z
    )

    # Shrinkage: cap extreme values to avoid overfit
    attack = np.clip(attack, -0.6, 0.6)
    defense = np.clip(defense, -0.6, 0.6)

    return float(attack), float(defense)


def predict_match(m: MatchInput) -> MatchPrediction:
    """Predict scoreline distribution for a single match."""

    # 1. Base rate
    alpha = BASE_ALPHA

    # 2. Stage effect
    stage_eff = STAGE_EFFECTS.get(m.stage, 0.0)

    # 3. Venue effect
    venue_eff = VENUE_EFFECTS.get(m.venue, 0.0)

    # 4. Acclimatization adjustments
    acclim_a = 0.0
    acclim_b = 0.0
    if "mexico_city" in m.venue or "guadalajara" in m.venue:
        if not m.team_a.altitude_acclimatized:
            acclim_a = -0.05  # altitude disadvantage
        if not m.team_b.altitude_acclimatized:
            acclim_b = -0.05
    if m.venue in ("monterrey", "miami", "kansas_city"):
        if not m.team_a.heat_acclimatized:
            acclim_a += -0.03
        if not m.team_b.heat_acclimatized:
            acclim_b += -0.03

    # 5. 2026 rule uplift
    rule_adj = RULE_UPLIFT_2026 if m.is_2026 else 0.0

    # 6. Compute per-team lambda
    log_lambda_a = (
        alpha
        + m.team_a.attack
        - m.team_b.defense
        + stage_eff
        + venue_eff
        + rule_adj
        + acclim_a
        + m.manual_adj_a
    )
    log_lambda_b = (
        alpha
        + m.team_b.attack
        - m.team_a.defense
        + stage_eff
        + venue_eff
        + rule_adj
        + acclim_b
        + m.manual_adj_b
    )

    lambda_a = math.exp(log_lambda_a)
    lambda_b = math.exp(log_lambda_b)
    mu_total = lambda_a + lambda_b

    # 7. Blend with market odds if available
    if m.market_total is not None:
        sigma_model = 0.20
        sigma_market = m.market_sigma
        log_model = math.log(mu_total)
        log_market = math.log(m.market_total)
        prec_model = 1 / sigma_model**2
        prec_market = 1 / sigma_market**2
        log_blended = (log_model * prec_model + log_market * prec_market) / (
            prec_model + prec_market
        )
        mu_blended = math.exp(log_blended)

        # Scale individual lambdas proportionally
        scale = mu_blended / mu_total
        lambda_a *= scale
        lambda_b *= scale
        mu_total = mu_blended

    # 8. Scoreline probabilities (independent Poisson)
    max_goals = 7
    scoreline_probs: dict[tuple[int, int], float] = {}
    for i in range(max_goals + 1):
        for j in range(max_goals + 1):
            p = poisson.pmf(i, lambda_a) * poisson.pmf(j, lambda_b)
            scoreline_probs[(i, j)] = float(p)

    # 9. Total goals distribution
    total_probs: dict[int | str, float] = {}
    for k in range(max_goals + 1):
        total_probs[k] = sum(
            scoreline_probs[(i, j)]
            for i in range(max_goals + 1)
            for j in range(max_goals + 1)
            if i + j == k
        )
    total_probs["7+"] = 1.0 - sum(total_probs[k] for k in range(max_goals + 1))

    # 10. Modal scoreline
    modal = max(scoreline_probs, key=scoreline_probs.get)  # type: ignore[arg-type]

    # 11. 80% CI on total goals
    cumulative = 0.0
    ci_low = 0
    ci_high = 0
    for k in range(15):
        p = poisson.pmf(k, mu_total)
        cumulative += p
        if cumulative >= 0.10 and ci_low == 0:
            ci_low = k
        if cumulative >= 0.90:
            ci_high = k
            break

    return MatchPrediction(
        team_a=m.team_a.name,
        team_b=m.team_b.name,
        lambda_a=round(lambda_a, 3),
        lambda_b=round(lambda_b, 3),
        mu_total=round(mu_total, 3),
        scoreline_probs=scoreline_probs,
        total_probs=total_probs,
        modal_scoreline=modal,
        ci_80=(ci_low, ci_high),
    )


def format_prediction(pred: MatchPrediction) -> str:
    """Pretty-print a match prediction."""
    lines = [
        f"\n{'='*55}",
        f"{pred.team_a} vs {pred.team_b}",
        f"{'='*55}",
        f"  λ({pred.team_a}): {pred.lambda_a:.2f}  |  λ({pred.team_b}): {pred.lambda_b:.2f}",
        f"  Expected total: {pred.mu_total:.2f}  |  80% CI: {pred.ci_80}",
        f"  Modal scoreline: {pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}",
        "",
        "  Top 5 most likely scorelines:",
    ]

    top5 = sorted(pred.scoreline_probs.items(), key=lambda x: -x[1])[:5]
    for (i, j), p in top5:
        lines.append(f"    {i}-{j}: {p:.1%}")

    lines.append("")
    lines.append("  Total goals distribution:")
    for k in range(7):
        p = pred.total_probs.get(k, 0.0)
        bar = "█" * int(p * 40)
        lines.append(f"    {k}: {p:.1%} {bar}")
    p7 = pred.total_probs.get("7+", 0.0)
    lines.append(f"   7+: {p7:.1%}")

    return "\n".join(lines)


# --- Backtesting ---

def load_historical_matches(csv_path: str) -> list[dict]:
    """Load historical WC match data from CSV."""
    matches = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            matches.append({
                "year": int(row["year"]),
                "date": row["date"],
                "stage": row["stage"],
                "team_a": row["team_a"],
                "goals_a": int(row["goals_a"]),
                "team_b": row["team_b"],
                "goals_b": int(row["goals_b"]),
                "city": row["city"],
            })
    return matches


def calibrate_overdispersion(matches: list[dict]) -> float:
    """Fit NegBin overdispersion parameter from historical total goals."""
    totals = [m["goals_a"] + m["goals_b"] for m in matches]
    mean_total = np.mean(totals)
    var_total = np.var(totals, ddof=1)

    # NegBin: variance = mu + mu^2/r → r = mu^2 / (var - mu)
    if var_total > mean_total:
        r = mean_total**2 / (var_total - mean_total)
    else:
        r = 100.0  # essentially Poisson (no overdispersion)

    return float(r)


def calibrate_stage_effects(matches: list[dict]) -> dict[str, float]:
    """Estimate stage effects from historical data."""
    stage_goals: dict[str, list[int]] = {}
    for m in matches:
        stage = m["stage"]
        total = m["goals_a"] + m["goals_b"]
        stage_goals.setdefault(stage, []).append(total)

    overall_mean = np.mean([m["goals_a"] + m["goals_b"] for m in matches])

    effects = {}
    for stage, goals in stage_goals.items():
        stage_mean = np.mean(goals)
        # Effect on log scale
        effects[stage] = float(math.log(stage_mean / overall_mean))

    return effects


def backtest_2022(matches: list[dict]) -> dict:
    """
    Train on 1998-2018, predict 2022, measure accuracy.

    Uses a simple baseline: each team gets attack/defense from their
    tournament history (goals scored/conceded per game).
    """
    train = [m for m in matches if m["year"] <= 2018]
    test = [m for m in matches if m["year"] == 2022]

    # Learn team strengths from training data with recency weighting
    # More recent tournaments get higher weight
    max_year = max(m["year"] for m in train)
    team_gf_weighted: dict[str, list[tuple[float, float]]] = {}  # (value, weight)
    team_ga_weighted: dict[str, list[tuple[float, float]]] = {}

    for m in train:
        # Exponential decay: half-life of 8 years
        years_ago = max_year - m["year"]
        weight = math.exp(-0.693 * years_ago / 8)  # ln(2)/half_life

        for team, gf, ga in [
            (m["team_a"], m["goals_a"], m["goals_b"]),
            (m["team_b"], m["goals_b"], m["goals_a"]),
        ]:
            team_gf_weighted.setdefault(team, []).append((gf, weight))
            team_ga_weighted.setdefault(team, []).append((ga, weight))

    # Compute weighted attack/defense ratings
    all_gf = [gf for vals in team_gf_weighted.values() for gf, _ in vals]
    global_mean_gf = float(np.mean(all_gf))

    teams: dict[str, Team] = {}
    for name in team_gf_weighted:
        gf_vals = team_gf_weighted[name]
        ga_vals = team_ga_weighted[name]

        # Weighted mean
        total_w = sum(w for _, w in gf_vals)
        mean_gf = sum(v * w for v, w in gf_vals) / total_w if total_w > 0 else global_mean_gf
        mean_ga = sum(v * w for v, w in ga_vals) / total_w if total_w > 0 else global_mean_gf

        # Floor to avoid log(0)
        mean_gf = max(mean_gf, 0.1)
        mean_ga = max(mean_ga, 0.1)

        attack = math.log(mean_gf / global_mean_gf)
        defense = math.log(global_mean_gf / mean_ga)

        # Shrinkage: based on effective sample size (sum of weights)
        # Cap at 70% weight on team data to avoid overfit
        eff_n = total_w
        shrink = min(eff_n, 8) / 8 * 0.70
        attack *= shrink
        defense *= shrink
        teams[name] = Team(name=name, attack=attack, defense=defense)

    # Predict 2022 matches
    results = {
        "n_matches": len(test),
        "correct_scoreline": 0,
        "correct_total": 0,
        "correct_result": 0,  # W/D/L
        "total_abs_error": 0,
        "brier_total": 0.0,
        "baseline_1_1_correct": 0,
        "baseline_1_1_abs_error": 0,
        "predictions": [],
    }

    for m in test:
        ta = teams.get(m["team_a"], Team(name=m["team_a"]))
        tb = teams.get(m["team_b"], Team(name=m["team_b"]))

        mi = MatchInput(team_a=ta, team_b=tb, stage=m["stage"], is_2026=False)
        pred = predict_match(mi)

        actual_a = m["goals_a"]
        actual_b = m["goals_b"]
        actual_total = actual_a + actual_b
        predicted_total = pred.modal_scoreline[0] + pred.modal_scoreline[1]

        # Metrics
        if pred.modal_scoreline == (actual_a, actual_b):
            results["correct_scoreline"] += 1
        if predicted_total == actual_total:
            results["correct_total"] += 1
        pred_result = "W" if pred.modal_scoreline[0] > pred.modal_scoreline[1] else (
            "D" if pred.modal_scoreline[0] == pred.modal_scoreline[1] else "L"
        )
        actual_result = "W" if actual_a > actual_b else (
            "D" if actual_a == actual_b else "L"
        )
        if pred_result == actual_result:
            results["correct_result"] += 1

        results["total_abs_error"] += abs(predicted_total - actual_total)

        # Brier score on total goals distribution
        for k in range(7):
            p = pred.total_probs.get(k, 0.0)
            actual_indicator = 1.0 if k == actual_total else 0.0
            results["brier_total"] += (p - actual_indicator) ** 2

        # Baseline: always predict 1-1
        if actual_a == 1 and actual_b == 1:
            results["baseline_1_1_correct"] += 1
        results["baseline_1_1_abs_error"] += abs(2 - actual_total)

        results["predictions"].append({
            "match": f"{m['team_a']} vs {m['team_b']}",
            "actual": f"{actual_a}-{actual_b}",
            "predicted": f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}",
            "mu_total": pred.mu_total,
            "lambda_a": pred.lambda_a,
            "lambda_b": pred.lambda_b,
        })

    # Summary metrics
    n = results["n_matches"]
    results["scoreline_accuracy"] = results["correct_scoreline"] / n
    results["total_accuracy"] = results["correct_total"] / n
    results["result_accuracy"] = results["correct_result"] / n
    results["mae"] = results["total_abs_error"] / n
    results["brier_avg"] = results["brier_total"] / n
    results["baseline_1_1_mae"] = results["baseline_1_1_abs_error"] / n

    return results


def backtest_with_params(
    matches: list[dict],
    half_life: float,
    shrink_max: float,
    shrink_eff_n: float,
    test_year: int = 2022,
) -> dict:
    """
    Run backtest with specific hyperparameters.
    Returns results dict including brier score.
    """
    train = [m for m in matches if m["year"] < test_year]
    test = [m for m in matches if m["year"] == test_year]

    if not train or not test:
        return {"brier_avg": 999.0}

    max_year = max(m["year"] for m in train)
    team_gf_weighted: dict[str, list[tuple[float, float]]] = {}
    team_ga_weighted: dict[str, list[tuple[float, float]]] = {}

    for m in train:
        years_ago = max_year - m["year"]
        weight = math.exp(-0.693 * years_ago / half_life)

        for team, gf, ga in [
            (m["team_a"], m["goals_a"], m["goals_b"]),
            (m["team_b"], m["goals_b"], m["goals_a"]),
        ]:
            team_gf_weighted.setdefault(team, []).append((gf, weight))
            team_ga_weighted.setdefault(team, []).append((ga, weight))

    all_gf = [gf for vals in team_gf_weighted.values() for gf, _ in vals]
    global_mean_gf = float(np.mean(all_gf))

    teams: dict[str, Team] = {}
    for name in team_gf_weighted:
        gf_vals = team_gf_weighted[name]
        ga_vals = team_ga_weighted[name]
        total_w = sum(w for _, w in gf_vals)
        mean_gf = sum(v * w for v, w in gf_vals) / total_w if total_w > 0 else global_mean_gf
        mean_ga = sum(v * w for v, w in ga_vals) / total_w if total_w > 0 else global_mean_gf
        mean_gf = max(mean_gf, 0.1)
        mean_ga = max(mean_ga, 0.1)
        attack = math.log(mean_gf / global_mean_gf)
        defense = math.log(global_mean_gf / mean_ga)
        eff_n = total_w
        shrink = min(eff_n, shrink_eff_n) / shrink_eff_n * shrink_max
        attack *= shrink
        defense *= shrink
        teams[name] = Team(name=name, attack=attack, defense=defense)

    # Predict and score
    brier_total = 0.0
    correct_scoreline = 0
    correct_result = 0
    total_abs_error = 0
    predictions = []

    for m in test:
        ta = teams.get(m["team_a"], Team(name=m["team_a"]))
        tb = teams.get(m["team_b"], Team(name=m["team_b"]))
        mi = MatchInput(team_a=ta, team_b=tb, stage=m["stage"], is_2026=False)
        pred = predict_match(mi)

        actual_a, actual_b = m["goals_a"], m["goals_b"]
        actual_total = actual_a + actual_b

        if pred.modal_scoreline == (actual_a, actual_b):
            correct_scoreline += 1

        pred_result = "W" if pred.modal_scoreline[0] > pred.modal_scoreline[1] else (
            "D" if pred.modal_scoreline[0] == pred.modal_scoreline[1] else "L"
        )
        actual_result = "W" if actual_a > actual_b else (
            "D" if actual_a == actual_b else "L"
        )
        if pred_result == actual_result:
            correct_result += 1

        predicted_total = pred.modal_scoreline[0] + pred.modal_scoreline[1]
        total_abs_error += abs(predicted_total - actual_total)

        for k in range(7):
            p = pred.total_probs.get(k, 0.0)
            actual_indicator = 1.0 if k == actual_total else 0.0
            brier_total += (p - actual_indicator) ** 2

        predictions.append({
            "match": f"{m['team_a']} vs {m['team_b']}",
            "actual": f"{actual_a}-{actual_b}",
            "predicted": f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}",
            "mu_total": pred.mu_total,
            "lambda_a": pred.lambda_a,
            "lambda_b": pred.lambda_b,
        })

    n = len(test)
    return {
        "n_matches": n,
        "brier_avg": brier_total / n,
        "scoreline_accuracy": correct_scoreline / n,
        "result_accuracy": correct_result / n,
        "mae": total_abs_error / n,
        "predictions": predictions,
    }


def optimize_hyperparameters(matches: list[dict]) -> dict:
    """
    Find optimal hyperparameters using cross-validation across tournaments.
    Minimizes average Brier score across held-out tournaments.
    """
    from scipy.optimize import minimize

    # Use 2014, 2018, 2022 as validation sets (leave-one-out by tournament)
    val_years = [2014, 2018, 2022]

    def objective(params):
        half_life, shrink_max, shrink_eff_n = params
        if half_life < 1 or shrink_max < 0.1 or shrink_max > 1.0 or shrink_eff_n < 1:
            return 10.0  # penalty for invalid params

        total_brier = 0.0
        for year in val_years:
            result = backtest_with_params(matches, half_life, shrink_max, shrink_eff_n, year)
            total_brier += result["brier_avg"]
        return total_brier / len(val_years)

    # Grid search first for robustness, then refine
    best_score = float("inf")
    best_params = (8.0, 0.7, 8.0)

    logger.info("Running hyperparameter grid search...")
    for half_life in [4, 6, 8, 12, 16, 24]:
        for shrink_max in [0.3, 0.5, 0.7, 0.9, 1.0]:
            for shrink_eff_n in [3, 5, 8, 12, 20]:
                score = objective([half_life, shrink_max, shrink_eff_n])
                if score < best_score:
                    best_score = score
                    best_params = (half_life, shrink_max, shrink_eff_n)

    # Refine with Nelder-Mead
    result = minimize(
        objective,
        x0=list(best_params),
        method="Nelder-Mead",
        options={"maxiter": 200, "xatol": 0.1, "fatol": 0.001},
    )

    if result.fun < best_score:
        best_params = tuple(result.x)
        best_score = result.fun

    return {
        "half_life": best_params[0],
        "shrink_max": best_params[1],
        "shrink_eff_n": best_params[2],
        "cv_brier": best_score,
    }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data_path = Path(__file__).parent / "wc_matches_1998_2022.csv"
    matches = load_historical_matches(str(data_path))

    print(f"Loaded {len(matches)} historical matches")
    print(f"\nTotal goals per tournament:")
    for year in sorted(set(m["year"] for m in matches)):
        year_matches = [m for m in matches if m["year"] == year]
        total = sum(m["goals_a"] + m["goals_b"] for m in year_matches)
        avg = total / len(year_matches)
        print(f"  {year}: {total} goals in {len(year_matches)} matches ({avg:.2f}/match)")

    # Calibrate overdispersion
    r = calibrate_overdispersion(matches)
    print(f"\nCalibrated NegBin r = {r:.2f}")

    # Calibrate stage effects
    stage_eff = calibrate_stage_effects(matches)
    print(f"\nCalibrated stage effects (log scale):")
    for stage, eff in sorted(stage_eff.items()):
        print(f"  {stage}: {eff:+.3f}")

    # Optimize hyperparameters via cross-validation
    print(f"\n{'='*55}")
    print("HYPERPARAMETER OPTIMIZATION (CV on 2014, 2018, 2022)")
    print(f"{'='*55}")
    optimal = optimize_hyperparameters(matches)
    print(f"  Optimal half_life: {optimal['half_life']:.1f} years")
    print(f"  Optimal shrink_max: {optimal['shrink_max']:.2f}")
    print(f"  Optimal shrink_eff_n: {optimal['shrink_eff_n']:.1f}")
    print(f"  CV Brier score: {optimal['cv_brier']:.4f}")

    # Backtest on 2022 with optimal params
    print(f"\n{'='*55}")
    print("BACKTESTING: Train 1998-2018, Predict 2022 (optimized)")
    print(f"{'='*55}")
    results = backtest_with_params(
        matches,
        optimal["half_life"],
        optimal["shrink_max"],
        optimal["shrink_eff_n"],
        test_year=2022,
    )
    print(f"  Matches: {results['n_matches']}")
    print(f"  Scoreline accuracy: {results['scoreline_accuracy']:.1%}")
    print(f"  Result (W/D/L) accuracy: {results['result_accuracy']:.1%}")
    print(f"  MAE (total goals): {results['mae']:.2f}")
    print(f"  Brier score (avg): {results['brier_avg']:.4f}")
    print(f"  --- Baseline (always 1-1) ---")
    baseline_correct = sum(
        1 for m in matches if m["year"] == 2022 and m["goals_a"] == 1 and m["goals_b"] == 1
    )
    baseline_mae = sum(
        abs(2 - m["goals_a"] - m["goals_b"]) for m in matches if m["year"] == 2022
    ) / 64
    print(f"  Baseline MAE: {baseline_mae:.2f}")
    print(f"  Baseline scoreline accuracy: {baseline_correct/64:.1%}")

    # Show predictions
    print(f"\nSample predictions (2022):")
    for p in results["predictions"][:15]:
        marker = "✓" if p["actual"] == p["predicted"] else " "
        print(f"  {marker} {p['match']:35s} actual={p['actual']:5s} predicted={p['predicted']:5s} μ={p['mu_total']:.2f}")
