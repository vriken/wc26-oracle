"""
Group E predictions using market-first Bayesian approach.

Group E: Germany, Ivory Coast, Ecuador, Curacao

Key dynamics:
- Germany clear favorite (71% Polymarket, -220 FanDuel) but back-to-back group exits 2018/2022
- Ivory Coast: AFCON 2024 winners, 0 GA in 10 qualifiers, unbeaten qualifying
- Ecuador: 2nd in CONMEBOL (behind Argentina), only 14 GF in 18 qualifiers but 5 GA
- Curacao: smallest nation ever at WC (~156k pop), debutants, unbeaten qualifying in CONCACAF
- Almost zero head-to-head history — 5 of 6 pairings have never met

Sources:
- Polymarket group winner: GER 71%, ECU 21%, CIV 8.2% (up from ~6%), CUR ~2%
- FanDuel: GER -220, ECU +380, CIV +600, CUR +4500
- To qualify: GER -5000, ECU -800, CIV -370, CUR +800
- RotoWire projected pts: GER 6.9, ECU 5.1, CIV 4.0, CUR 0.8
- Qualifying: GER (W4 D0 L2, UEFA Group A), ECU (W8 D8 L2, CONMEBOL 2nd),
  CIV (W8 D2 L0, CAF unbeaten, 0 GA), CUR (W7 D3 L0, CONCACAF unbeaten)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group E Teams ---

germany = Team(
    name="Germany",
    attack=0.18,    # Wirtz-Musiala-Havertz elite trio (if fit). 16GF/4GA in 6 qualifiers
    defense=0.12,   # Solid structure under Nagelsmann but leaked 3 to Switzerland, 1 to Ghana in friendlies
    manager_style="attacking",  # Nagelsmann: vertical, explosive, high press
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Musiala (touch-and-go, not confirmed fit, targeting May squad)",
                  "Havertz (fully fit, 2G/2A since comeback)", "Pavlovic (injury)",
                  "Emre Can (ACL, OUT)", "Kleindienst (knee, doubtful)"],
)

ivory_coast = Team(
    name="Ivory Coast",
    attack=0.05,    # ~25GF in 10 qualifiers but vs weak opposition. Diomande breakout (11G/8A at Leipzig)
    defense=0.10,   # 0 GA in 10 qualifiers. AFCON 2024 winners. 4-0 vs S Korea, 1-0 vs Scotland in March
    manager_style="balanced",  # Fae: defensively solid mid-block, quick transitions
    heat_acclimatized=True,    # West African climate
    altitude_acclimatized=False,
    key_absences=["Diomande (fully fit, returned April 4 vs Bremen)"],
)

ecuador = Team(
    name="Ecuador",
    attack=0.00,    # Only 14GF in 18 CONMEBOL qualifiers. Eight 0-0 draws. Drew 1-1 vs NED/MOR in March
    defense=0.12,   # Fewest GA in CONMEBOL qualifying (5). Pacho+Hincapie at PSG/Arsenal
    manager_style="defensive",  # Beccacece: defense-first, compact, counter-attack
    heat_acclimatized=True,     # Equatorial climate
    altitude_acclimatized=True, # Quito at 2,850m
    key_absences=["Plata (fit, assisted vs Morocco, 89 mins)", "Valencia (hamstring, expected fit)"],
)

curacao = Team(
    name="Curacao",
    attack=-0.30,   # Scored well in CONCACAF qualifiers but against Barbados/St Lucia/Bermuda
    defense=-0.25,  # Lost 0-2 to China, 1-5 to Australia in March. GK (Room) free agent. Obispo injured
    manager_style="defensive",  # Rutten: pragmatic low block, frustrate opponents
    heat_acclimatized=True,     # Caribbean climate
    altitude_acclimatized=False,
    key_absences=["Obispo (undisclosed, key CB)", "Locadia (undisclosed)",
                  "Fonville (undisclosed)"],
)


# --- Match Predictions ---

matches = [
    # Match 1: Germany vs Curacao — Sun Jun 14, NRG Stadium (Houston TX, AC)
    MatchInput(
        team_a=germany,
        team_b=curacao,
        stage="group_md1",
        venue="houston",
        market_total=3.0,       # biggest mismatch — Germany heavy favorite
        market_sigma=0.20,
        manual_adj_a=-0.03,     # Musiala uncertain, opener caution despite mismatch
    ),

    # Match 2: Ivory Coast vs Ecuador — Sun Jun 14, Lincoln Financial Field (Philadelphia PA)
    MatchInput(
        team_a=ivory_coast,
        team_b=ecuador,
        stage="group_md1",
        venue="philadelphia",
        market_total=2.2,       # two defensive teams, MD1 caution. Under 2.5 strong
        market_sigma=0.20,
    ),

    # Match 3: Germany vs Ivory Coast — Sat Jun 20, BMO Field (Toronto)
    MatchInput(
        team_a=germany,
        team_b=ivory_coast,
        stage="group_md2",
        venue="toronto",
        market_total=2.4,       # Germany quality vs CIV defensive solidity
        market_sigma=0.18,
    ),

    # Match 4: Ecuador vs Curacao — Sat Jun 20, Arrowhead Stadium (Kansas City)
    MatchInput(
        team_a=ecuador,
        team_b=curacao,
        stage="group_md2",
        venue="kansas_city",
        market_total=2.5,       # Ecuador should win but struggle to score
        market_sigma=0.22,
        manual_adj_b=-0.02,     # Curacao non-acclimatized to KC heat, no AC
    ),

    # Match 5: Curacao vs Ivory Coast — Thu Jun 25, Lincoln Financial Field (Philadelphia PA)
    MatchInput(
        team_a=curacao,
        team_b=ivory_coast,
        stage="group_md3",
        venue="philadelphia",
        market_total=2.5,       # CIV should dominate but MD3 motivation variable
        market_sigma=0.22,
    ),

    # Match 6: Ecuador vs Germany — Thu Jun 25, MetLife Stadium (East Rutherford NJ)
    MatchInput(
        team_a=ecuador,
        team_b=germany,
        stage="group_md3",
        venue="new_york",
        market_total=2.3,       # Ecuador's defense-first vs Germany's attack. Tight game
        market_sigma=0.18,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP E — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP E EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP E AVERAGE: {group_total/6:.2f} goals/match")
    print(f"{'='*60}")

    # Summary table
    print(f"\n{'Match':<35} {'Modal':>8} {'E[total]':>10} {'80% CI':>10}")
    print("-" * 65)
    for pred in predictions:
        modal = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        ci = f"{pred.ci_80[0]}-{pred.ci_80[1]}"
        print(f"{pred.team_a} vs {pred.team_b:<22} {modal:>8} {pred.mu_total:>10.02f} {ci:>10}")

    # Our manual predictions vs model
    print(f"\n{'='*60}")
    print("COMPARISON: Manual Picks (v2) vs Model")
    print(f"{'='*60}")
    manual = [
        ("Germany vs Curacao", "3-0"),        # v4: reverted — Curacao unlikely to score vs Germany
        ("Ivory Coast vs Ecuador", "1-2"),    # v4: Ecuador win, CIV not strong enough for draw
        ("Germany vs Ivory Coast", "2-1"),
        ("Ecuador vs Curacao", "2-0"),
        ("Curacao vs Ivory Coast", "0-2"),
        ("Ecuador vs Germany", "1-1"),        # v2: was 0-1, align with model modal
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
