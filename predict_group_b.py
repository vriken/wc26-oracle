"""
Group B predictions using market-first Bayesian approach.

Group B: Canada (co-host), Bosnia & Herzegovina, Qatar, Switzerland

Key dynamics:
- Switzerland clear favorite (56% Polymarket, -110 FanDuel)
- Canada co-host: all 3 matches on home soil (Toronto, Vancouver, Vancouver)
- Bosnia eliminated Italy in playoffs — emotional high, but Dzeko shoulder injury
- Qatar weakest team (2W 3D 5L recent, nearly all-domestic squad)

Sources:
- Polymarket group winner: SUI 56%, CAN 26%, BOS ~13%, QAT ~5%
- FanDuel: SUI -110, CAN +260, BOS +270, QAT +3500
- Oddschecker CAN-BOS: Canada +110, Draw +260, Bosnia +280
- Oddschecker QAT-SUI: Qatar +1000, Draw +440, Switzerland -334
- Qualifying: SUI (W4 D2 L0, ~14GF/2GA), QAT (scraped through 4th round)
- Recent: SUI (unbeaten qualifying, lost 3-4 to Germany in friendly),
  CAN (7W 4L 3D in 2025, injury crisis), BOS (2 playoff wins on pens),
  QAT (2W 3D 5L last 10)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group B Teams ---

switzerland = Team(
    name="Switzerland",
    attack=0.15,    # 14GF in 6 qualifiers (2.33 g/m), Embolo 4 goals
    defense=0.20,   # only 2 GA in 6 qualifiers, Akanji world-class at Inter
    manager_style="balanced",
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=[],  # healthy squad
)

canada = Team(
    name="Canada",
    attack=0.05,    # David 8G/6A all comps at Juve, Buchanan hat-trick on debut
    defense=0.00,   # mixed results, injury concerns in defense (Bombito, Johnston)
    manager_style="attacking",  # Marsch "Maplepressing"
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Davies (ACL recovery)", "Promise David (out)", "Kone (muscle)",
                  "Eustaquio (collision)", "Johnston (injured)", "Bombito (injured)"],
)

bosnia = Team(
    name="Bosnia & Herzegovina",
    attack=0.00,    # Dzeko 6G/8 apps at Schalke IF fit, Demirovic solid
    defense=-0.10,  # conceded in every playoff match, limited squad depth
    manager_style="balanced",
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Dzeko (shoulder, major doubt)"],
)

qatar = Team(
    name="Qatar",
    attack=-0.30,   # 2W 3D 5L recent, domestic league quality gap
    defense=-0.20,  # conceded 7 in 3 games at 2022 WC, 3 to Tunisia recently
    manager_style="balanced",  # Lopetegui possession-based
    heat_acclimatized=True,  # Qatar climate
    altitude_acclimatized=False,
    key_absences=[],
)


# --- Match Predictions ---

matches = [
    # Match 1: Canada vs Bosnia — Jun 12, BMO Field, Toronto
    MatchInput(
        team_a=canada,
        team_b=bosnia,
        stage="group_md1",
        venue="toronto",
        market_total=2.3,       # opener, both cautious, Oddschecker close odds
        market_sigma=0.20,
        manual_adj_a=+0.05,    # home advantage (co-host opener)
        manual_adj_b=-0.05,    # Dzeko injury uncertainty
    ),

    # Match 2: Qatar vs Switzerland — Jun 13, Levi's Stadium, Santa Clara
    MatchInput(
        team_a=qatar,
        team_b=switzerland,
        stage="group_md1",
        venue="san_francisco",
        market_total=2.5,       # Switzerland -334 heavy favorite
        market_sigma=0.18,
    ),

    # Match 3: Switzerland vs Bosnia — Jun 18, SoFi Stadium, LA
    MatchInput(
        team_a=switzerland,
        team_b=bosnia,
        stage="group_md2",
        venue="los_angeles",
        market_total=2.4,       # Switzerland should control, Bosnia fight
        market_sigma=0.22,
    ),

    # Match 4: Canada vs Qatar — Jun 18, BC Place, Vancouver
    MatchInput(
        team_a=canada,
        team_b=qatar,
        stage="group_md2",
        venue="vancouver",
        market_total=2.5,       # mismatch, Canada at home
        market_sigma=0.22,
        manual_adj_a=+0.05,    # home advantage
    ),

    # Match 5: Switzerland vs Canada — Jun 24, BC Place, Vancouver
    MatchInput(
        team_a=switzerland,
        team_b=canada,
        stage="group_md3",
        venue="vancouver",
        market_total=2.5,       # potential group decider
        market_sigma=0.20,
        manual_adj_b=+0.05,    # Canada home advantage
    ),

    # Match 6: Bosnia vs Qatar — Jun 24, Lumen Field, Seattle
    MatchInput(
        team_a=bosnia,
        team_b=qatar,
        stage="group_md3",
        venue="seattle",
        market_total=2.5,       # Bosnia should win, Qatar desperate
        market_sigma=0.25,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP B — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP B EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP B AVERAGE: {group_total/6:.2f} goals/match")
    print(f"{'='*60}")

    # Summary table
    print(f"\n{'Match':<35} {'Modal':>8} {'E[total]':>10} {'80% CI':>10}")
    print("-" * 65)
    for pred in predictions:
        modal = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        ci = f"{pred.ci_80[0]}-{pred.ci_80[1]}"
        print(f"{pred.team_a} vs {pred.team_b:<22} {modal:>8} {pred.mu_total:>10.2f} {ci:>10}")

    # Our manual predictions vs model
    print(f"\n{'='*60}")
    print("COMPARISON: Manual Picks vs Model")
    print(f"{'='*60}")
    manual = [
        ("Canada vs Bosnia", "1-1"),
        ("Qatar vs Switzerland", "0-2"),
        ("Switzerland vs Bosnia", "2-1"),
        ("Canada vs Qatar", "2-1"),
        ("Switzerland vs Canada", "1-1"),
        ("Bosnia vs Qatar", "2-1"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
