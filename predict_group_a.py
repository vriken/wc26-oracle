"""
Group A predictions using market-first Bayesian approach.

Strategy:
1. Use sportsbook/Polymarket odds to derive implied team strengths
2. Convert match odds to expected goals per team via Poisson model
3. Apply our venue/context adjustments on top
4. Output scoreline probabilities and modal predictions
"""

import math
from model import (
    Team, MatchInput, predict_match, format_prediction,
    STAGE_EFFECTS, VENUE_EFFECTS,
)


def odds_to_implied_prob(moneyline: int) -> float:
    """Convert American moneyline odds to implied probability."""
    if moneyline > 0:
        return 100 / (moneyline + 100)
    else:
        return abs(moneyline) / (abs(moneyline) + 100)


def match_probs_to_lambdas(
    p_win_a: float, p_draw: float, p_win_b: float
) -> tuple[float, float]:
    """
    Convert 3-way match probabilities to per-team Poisson lambdas.

    Uses the relationship between Poisson(λ) outcomes and match results.
    Solved numerically via grid search.
    """
    best_error = float("inf")
    best_la, best_lb = 1.0, 1.0

    # Normalize probabilities
    total = p_win_a + p_draw + p_win_b
    p_win_a /= total
    p_draw /= total
    p_win_b /= total

    from scipy.stats import poisson

    for la_10 in range(1, 50):  # λ_a from 0.1 to 5.0
        for lb_10 in range(1, 50):  # λ_b from 0.1 to 5.0
            la = la_10 / 10
            lb = lb_10 / 10

            # Compute match outcome probabilities from independent Poisson
            p_a_wins = 0.0
            p_draw_calc = 0.0
            p_b_wins = 0.0
            for i in range(8):
                for j in range(8):
                    p = poisson.pmf(i, la) * poisson.pmf(j, lb)
                    if i > j:
                        p_a_wins += p
                    elif i == j:
                        p_draw_calc += p
                    else:
                        p_b_wins += p

            error = (
                (p_a_wins - p_win_a) ** 2
                + (p_draw_calc - p_draw) ** 2
                + (p_b_wins - p_win_b) ** 2
            )
            if error < best_error:
                best_error = error
                best_la, best_lb = la, lb

    return best_la, best_lb


# --- Group A Teams ---
# Strength derived from:
# 1. Sportsbook group winner odds (BetMGM/DraftKings)
# 2. Qualifying records
# 3. Recent form (last 10 matches)
# 4. Manual adjustments for injuries and tactical factors

# Sources:
# - BetMGM group winner: Mexico +100, Czechia +260, SK +290, SA +1400
# - Polymarket group winner: Mexico ~48%, Czechia ~36%, SK ~22%, SA ~4%
# - Oddschecker MEX-SA: Mexico -185, Draw +330, SA +550
# - Polymarket MEX-SK: 51% / 49%
# - Qualifying: SK (W6 D4 L0, 20GF/7GA), SA (W5 D3 L2, 15GF/9GA),
#   CZE (group 2nd + 2x playoff pens)
# - Recent form: MEX (1.0 g/m, xG 1.08), SK (5 games w/o scoring),
#   SA (lost to Panama), CZE (emotional playoff wins)

# Team strength from market-implied ratings + qualifying data
mexico = Team(
    name="Mexico",
    attack=0.10,    # low scoring (1.0 g/m recent) but WC pedigree
    defense=0.15,   # strong under Aguirre (10 clean sheets in 15)
    manager_style="defensive",
    heat_acclimatized=True,
    altitude_acclimatized=True,
    key_absences=["Malagon (GK)", "Ruiz (MF)", "Alvarez (MF, doubtful)"],
)

south_korea = Team(
    name="South Korea",
    attack=-0.10,   # 5 games without scoring, tactical mess
    defense=-0.05,  # conceded 5 to Brazil, 4 to Ivory Coast recently
    manager_style="balanced",
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Park Yong-woo (MF)", "Won Doo-jae"],
)

south_africa = Team(
    name="South Africa",
    attack=-0.20,   # 1.5 g/m in qualifying, coach says "not ready"
    defense=-0.10,  # 0.9 GA/m in qualifying but weaker opposition
    manager_style="defensive",
    heat_acclimatized=True,  # South African climate is warm
    altitude_acclimatized=False,  # Johannesburg is high but not 2,240m
    key_absences=["Foster (fitness concerns)", "Xoki (knee, out)"],
)

czechia = Team(
    name="Czechia",
    attack=0.05,    # 2.2 g/m in qualifying but weak group. Schick is key
    defense=0.05,   # organized, physical. Conceded 5 to Croatia though
    manager_style="balanced",
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=[],  # no major injuries
)


# --- Match Predictions ---

matches = [
    # Match 1: Mexico vs South Africa — Jun 11, Azteca (opener)
    MatchInput(
        team_a=mexico,
        team_b=south_africa,
        stage="group_md1",
        venue="mexico_city",
        market_total=2.3,       # lean under based on Mexico xG + opener trend
        market_sigma=0.20,      # no sharp O/U line yet, wider uncertainty
        manual_adj_a=-0.05,     # injury crisis dampens Mexico attack
    ),

    # Match 2: South Korea vs Czechia — Jun 12, Guadalajara
    MatchInput(
        team_a=south_korea,
        team_b=czechia,
        stage="group_md1",
        venue="guadalajara",
        market_total=2.4,       # both leaky defenses but SK can't score
        market_sigma=0.20,
        manual_adj_a=-0.05,     # SK scoring drought penalty
    ),

    # Match 3: Mexico vs South Korea — Jun 18, Guadalajara
    MatchInput(
        team_a=mexico,
        team_b=south_korea,
        stage="group_md2",
        venue="guadalajara",
        market_total=2.5,       # Polymarket 51/49, historical WC meetings avg 3.5
        market_sigma=0.18,      # Polymarket has some volume here
        manual_adj_a=-0.05,     # Mexico injuries
    ),

    # Match 4: Czechia vs South Africa — Jun 18, Atlanta (AC)
    MatchInput(
        team_a=czechia,
        team_b=south_africa,
        stage="group_md2",
        venue="atlanta",
        market_total=2.5,       # no specific market, use base
        market_sigma=0.25,      # wider uncertainty
    ),

    # Match 5: Czechia vs Mexico — Jun 24, Azteca
    MatchInput(
        team_a=czechia,
        team_b=mexico,
        stage="group_md3",
        venue="mexico_city",
        market_total=2.5,       # Polymarket market thin ($2), use base
        market_sigma=0.25,
        manual_adj_a=-0.08,     # Czechia altitude disadvantage (non-acclimatized)
        manual_adj_b=-0.05,     # Mexico injuries
    ),

    # Match 6: South Africa vs South Korea — Jun 24, Monterrey
    MatchInput(
        team_a=south_africa,
        team_b=south_korea,
        stage="group_md3",
        venue="monterrey",
        market_total=2.4,       # both potentially desperate or dead rubber
        market_sigma=0.25,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP A — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP A EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP A AVERAGE: {group_total/6:.2f} goals/match")
    print(f"{'='*60}")

    # Summary table
    print(f"\n{'Match':<30} {'Modal':>8} {'E[total]':>10} {'80% CI':>10}")
    print("-" * 60)
    for pred in predictions:
        modal = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        ci = f"{pred.ci_80[0]}-{pred.ci_80[1]}"
        print(f"{pred.team_a} vs {pred.team_b:<17} {modal:>8} {pred.mu_total:>10.2f} {ci:>10}")

    # Our manual predictions vs model
    print(f"\n{'='*60}")
    print("COMPARISON: Manual vs Model")
    print(f"{'='*60}")
    manual = [
        ("Mexico vs South Africa", "1-0"),
        ("South Korea vs Czechia", "1-1"),
        ("Mexico vs South Korea", "2-1"),
        ("Czechia vs South Africa", "2-0"),
        ("Czechia vs Mexico", "0-1"),
        ("South Africa vs South Korea", "1-2"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<30} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
