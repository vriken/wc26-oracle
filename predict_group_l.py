"""
Group L predictions using market-first Bayesian approach.

Group L: England, Croatia, Ghana, Panama

Key dynamics:
- England clear favorite (-220 FanDuel, 66% Polymarket) — perfect 8/0/0 qualifying, 0 GA
- Croatia: aging golden gen but still quality — 7/1/0 qualifying, Gvardiol/Kovacic injury race
- Ghana: qualified well but 5 consecutive friendly losses (2 GF, 11 GA), coaching chaos (Low appointment)
- Panama: 2nd ever WC, unbeaten qualifying, compact under Christiansen but limited firepower
- England vs Croatia MD1 is the marquee match (2018 WC SF revenge game)

Sources:
- Polymarket group winner: ENG 66%, CRO 21%
- FanDuel: ENG -220, CRO +340, GHA +700, PAN +4500
- FanDuel qualify: ENG -10000, CRO -475, GHA -155, PAN +220
- Oddschecker ENG-CRO: England 8/11, Draw 3/1, Croatia 4/1
- Polymarket ENG-CRO: ENG 61%, CRO 22%, Draw 17%
- Qualifying: ENG (W8 D0 L0, 22GF/0GA perfect), CRO (W7 D1 L0, ~26GF/~4GA),
  GHA (W8 D1 L1, 23GF/6GA CAF), PAN (W7 D3 L0, ~16GF/~4GA CONCACAF)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group L Teams ---

england = Team(
    name="England",
    attack=0.20,    # Kane (47 all comps), Saka, Palmer, Bellingham. Elite depth
    defense=0.15,   # 0 GA in 8 qualifiers under Tuchel. Guehi-Konsa solid
    manager_style="balanced",  # Tuchel: disciplined shape + rapid transitions
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Colwill (ACL, OUT)", "Maddison (ACL, OUT)",
                  "Stones (fitness, touch-and-go)", "Grealish (doubtful)"],
)

croatia = Team(
    name="Croatia",
    attack=0.10,    # Kramaric, Perisic, young guns (Ivanovic, Musa). Modric still pulls strings
    defense=0.10,   # Solid qualifying (~4 GA in 8), but Gvardiol racing fitness
    manager_style="balanced",  # Dalic: game control, composure, midfield dominance
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Gvardiol (fractured tibia, racing)", "Kovacic (heel surgery, racing)"],
)

ghana = Team(
    name="Ghana",
    attack=0.00,    # Semenyo elite (15G PL), Kudus injury, but 5 friendly losses (2 GF)
    defense=-0.05,  # Good qualifying (6 GA/10) but leaked 11 in 5 friendlies. New coach chaos
    manager_style="balanced",  # Unknown under Low (if appointed). Likely structured possession
    heat_acclimatized=True,    # West African climate
    altitude_acclimatized=False,
    key_absences=["Kudus (quad tendon, racing)", "Partey (injury history, TBD)",
                  "Seidu (ACL, doubtful)", "Lamptey (ankle, doubtful)"],
)

panama = Team(
    name="Panama",
    attack=-0.15,   # Limited firepower — Rodriguez, Fajardo (3 goals each in qualifying)
    defense=-0.10,  # Compact and organized under Christiansen but outclassed vs top teams
    manager_style="defensive",  # Sits deep, counters, positional discipline
    heat_acclimatized=True,     # Central American climate
    altitude_acclimatized=False,
    key_absences=[],
)


# --- Match Predictions ---

matches = [
    # Match 1: England vs Croatia — Wed Jun 17, AT&T Stadium (Arlington TX, indoor)
    MatchInput(
        team_a=england,
        team_b=croatia,
        stage="group_md1",
        venue="dallas",
        market_total=2.3,       # tight tactical battle, opener caution, both strong defensively
        market_sigma=0.18,
    ),

    # Match 2: Ghana vs Panama — Wed Jun 17, BMO Field (Toronto)
    MatchInput(
        team_a=ghana,
        team_b=panama,
        stage="group_md1",
        venue="toronto",
        market_total=2.3,       # competitive match, both limited in attack
        market_sigma=0.22,
        manual_adj_a=-0.05,     # Ghana's dire form: 5 straight friendly losses, coaching chaos
    ),

    # Match 3: England vs Ghana — Tue Jun 23, Gillette Stadium (Foxborough MA)
    MatchInput(
        team_a=england,
        team_b=ghana,
        stage="group_md2",
        venue="boston",
        market_total=2.5,       # England should dominate, but Ghana physical
        market_sigma=0.20,
    ),

    # Match 4: Panama vs Croatia — Tue Jun 23, BMO Field (Toronto)
    MatchInput(
        team_a=panama,
        team_b=croatia,
        stage="group_md2",
        venue="toronto",
        market_total=2.3,       # Panama will park the bus, Croatia patient buildup
        market_sigma=0.22,
    ),

    # Match 5: Panama vs England — Sat Jun 27, MetLife Stadium (East Rutherford NJ)
    MatchInput(
        team_a=panama,
        team_b=england,
        stage="group_md3",
        venue="new_york",
        market_total=2.8,       # Bigger mismatch, England will push for goals
        market_sigma=0.22,
    ),

    # Match 6: Croatia vs Ghana — Sat Jun 27, Lincoln Financial Field (Philadelphia)
    MatchInput(
        team_a=croatia,
        team_b=ghana,
        stage="group_md3",
        venue="philadelphia",
        market_total=2.5,       # Both may need a result, open game
        market_sigma=0.22,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP L — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP L EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP L AVERAGE: {group_total/6:.2f} goals/match")
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
    print("COMPARISON: Manual Picks vs Model")
    print(f"{'='*60}")
    manual = [
        ("England vs Croatia", "1-0"),
        ("Ghana vs Panama", "1-1"),
        ("England vs Ghana", "2-1"),
        ("Panama vs Croatia", "0-2"),
        ("Panama vs England", "1-3"),
        ("Croatia vs Ghana", "2-1"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
