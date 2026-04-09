"""
Group I predictions using market-first Bayesian approach.

Group I: France, Senegal, Norway, Iraq

Key dynamics:
- France: #1 FIFA, defending runners-up, deepest squad in tournament. Mbappe 37G club season
- Senegal: AFCON champions (disputed), 14th FIFA, unbeaten qualifying (W7 D3), Mane's last WC
- Norway: first WC since 1998, perfect 8/8 qualifying (37GF!), Haaland 16G in qualifiers.
  BUT Odegaard major injury concern (5 separate injuries this season)
- Iraq: 48th and final qualifier, first WC in 40 years, 21-match qualifying gauntlet

Sources:
- FanDuel: FRA -175, NOR +250, SEN +700, IRQ +3000
- DraftKings: FRA -200, NOR +260, SEN +550, IRQ +3500
- Polymarket: France 14% to win tournament (2nd overall behind Spain)
- Qualifying: FRA (W5 D1, 16GF/3GA), SEN (W7 D3, 22GF/3GA, unbeaten),
  NOR (W8 D0, 37GF/5GA, perfect), IRQ (21 matches across 5 rounds)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group I Teams ---

france = Team(
    name="France",
    attack=0.22,    # Mbappe 37G, Dembele Ballon d'Or, elite depth. Slight Kounde absence drag
    defense=0.18,   # Saliba/Upamecano/Konate rotation, Tchouameni-Camavinga pivot. 3 GA in 6 qualifiers
    manager_style="balanced",  # Deschamps: pragmatic possession, explosive transitions
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Kounde (injured, Kalulu called up)", "Kamara (ruled out)",
                  "Mbappe (knee, expected fit)", "Saliba (injury, expected fit)"],
)

senegal = Team(
    name="Senegal",
    attack=0.08,    # Mane 34yo but still productive, Jackson at Bayern, Ndiaye, Sarr. Solid not elite
    defense=0.08,   # Koulibaly anchor, Mendy in goal, 3 GA in 10 qualifiers. Organized
    manager_style="attacking",  # Pape Thiaw: offensive 4-3-3, 72% win rate
    heat_acclimatized=True,     # Senegalese climate + Saudi-based veterans
    altitude_acclimatized=False,
    key_absences=["Koulibaly (hamstring strain, awaiting MRI)"],
)

norway = Team(
    name="Norway",
    attack=0.12,    # Haaland (16G in 8 qualifiers, 55 in 48 caps) + Sorloth. BUT Haaland form dip
    defense=0.03,   # decent but not elite, Ajer anchors. 5 GA in 8 qualifiers (inflated by weak groups)
    manager_style="attacking",  # Solbakken: high press, possession-dominant, Haaland counter
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Odegaard (knee, CRITICAL — 5 injuries this season, only 1/3 of Arsenal minutes)",
                  "Aursnes (thigh)", "Heggem (muscle/lumbago)", "Thorsby (unavailable MD1)"],
)

iraq = Team(
    name="Iraq",
    attack=-0.20,   # Aymen Hussein all-time scorer but domestic-league level, Al-Hamadi in League One
    defense=-0.15,  # pragmatic under Arnold but massive quality gap vs top opposition
    manager_style="defensive",  # Arnold: defensive resilience, counter-attack, team culture
    heat_acclimatized=True,     # Middle Eastern climate
    altitude_acclimatized=False,
    key_absences=["Amyn (stretchered off vs Bolivia)"],
)


# --- Match Predictions ---

matches = [
    # Match 1: France vs Senegal — Tue Jun 16, MetLife Stadium (East Rutherford NJ)
    MatchInput(
        team_a=france,
        team_b=senegal,
        stage="group_md1",
        venue="new_york",
        market_total=2.5,       # cautious opener, 2002 rematch tension
        market_sigma=0.18,
    ),

    # Match 2: Iraq vs Norway — Tue Jun 16, Gillette Stadium (Foxborough MA)
    MatchInput(
        team_a=iraq,
        team_b=norway,
        stage="group_md1",
        venue="boston",
        market_total=2.8,       # Norway should dominate but Iraq's emotion + Arnold's setup
        market_sigma=0.22,
    ),

    # Match 3: France vs Iraq — Mon Jun 22, Lincoln Financial Field (Philadelphia PA)
    MatchInput(
        team_a=france,
        team_b=iraq,
        stage="group_md2",
        venue="philadelphia",
        market_total=3.0,       # biggest mismatch — France heavy favorite
        market_sigma=0.20,
    ),

    # Match 4: Norway vs Senegal — Mon Jun 22, MetLife Stadium (East Rutherford NJ)
    MatchInput(
        team_a=norway,
        team_b=senegal,
        stage="group_md2",
        venue="new_york",
        market_total=2.5,       # tight tactical battle, swing match for 2nd place
        market_sigma=0.20,
        manual_adj_a=-0.03,     # Odegaard absence impact — Norway worse without him
    ),

    # Match 5: Norway vs France — Fri Jun 26, Gillette Stadium (Foxborough MA)
    MatchInput(
        team_a=norway,
        team_b=france,
        stage="group_md3",
        venue="boston",
        market_total=2.8,       # France may rotate if qualified. Norway desperate
        market_sigma=0.20,
    ),

    # Match 6: Senegal vs Iraq — Fri Jun 26, BMO Field (Toronto ON)
    MatchInput(
        team_a=senegal,
        team_b=iraq,
        stage="group_md3",
        venue="toronto",
        market_total=2.8,       # Senegal should win, need result. Iraq fatigued
        market_sigma=0.22,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP I — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP I EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP I AVERAGE: {group_total/6:.2f} goals/match")
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
        ("France vs Senegal", "2-1"),
        ("Iraq vs Norway", "1-2"),      # v2: 0-2 → 1-2 (Iraq consolation goal)
        ("France vs Iraq", "3-1"),      # v2: 3-0 → 3-1 (Iraq 2nd goal)
        ("Norway vs Senegal", "2-1"),    # v4: Norway win, Haaland too strong for Senegal
        ("Norway vs France", "1-2"),
        ("Senegal vs Iraq", "2-0"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
