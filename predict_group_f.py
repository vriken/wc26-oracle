"""
Group F predictions using market-first Bayesian approach.

Group F: Netherlands, Japan, Sweden, Tunisia

Key dynamics:
- Netherlands clear favorite (-140 FanDuel, 56.5% Polymarket) — Van Dijk era, unbeaten in 13
- Japan: explosive qualifying (54 GF / 3 GA in 16 matches), beat England and Brazil recently
- Sweden: Gyokeres-dependent, worst qualifying campaign (0W 6 group matches) but clutch playoff wins
- Tunisia: historic 0 GA in 10 qualifying matches, but never advanced past WC group stage in 7 attempts
- No easy opponent — FOX Sports ranks this among top 3 hardest groups

Sources:
- Polymarket group winner: NED 56.5%, JPN 28.5%, SWE 13.5%, TUN 2.9%
- FanDuel: NED -140, JPN +340, SWE +430, TUN +1000
- Oddschecker NED-JPN: NED 11/10, Draw 13/5, JPN 5/2
- Oddschecker SWE-TUN: SWE 10/11, Draw 5/2, TUN 10/3
- Qualifying: NED (W6 D2 L0, 22GF/3GA), JPN (54GF/3GA in 16 matches, perfect AFC),
  SWE (0W 2D 4L group, 2W playoff), TUN (W9 D1, 22GF/0GA historic)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group F Teams ---

netherlands = Team(
    name="Netherlands",
    attack=0.12,    # 22GF in 8 qualifiers (dominated weaker sides), Gakpo/Simons/Reijnders quality
    defense=0.15,   # Van Dijk era, only 3 GA in qualifying. Solid structure under Koeman
    manager_style="balanced",  # Koeman: possession-based, asymmetric fullbacks, 4-2-3-1
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Schouten (ACL, OUT)", "De Jong (hamstring, racing)",
                  "Depay (fitness doubt)", "De Ligt (back, doubt)"],
)

japan = Team(
    name="Japan",
    attack=0.12,    # 54 GF in 16 qualifiers = 3.4 gpg(!). Beat England 1-0, Brazil 3-2 recently
    defense=0.10,   # 3 GA in 16 qualifiers, compact shape, Moriyasu's tactical discipline
    manager_style="balanced",  # "Chameleon football" — can press or counter depending on opponent
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Endo (ankle, major doubt)", "Minamino (ACL, likely OUT)"],
)

sweden = Team(
    name="Sweden",
    attack=0.08,    # Gyokeres (15G Arsenal) elite, Isak racing fitness, Elanga decent
    defense=0.02,   # Conceded in every playoff match, 10 GA in 6 group qualifiers. Fragile
    manager_style="attacking",  # Potter: brave, possession-based, get ball wide early
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Lundgren (Achilles, OUT)", "Kulusevski (patella, major doubt)",
                  "Isak (fibula, racing fitness)", "Hien (doubt)"],
)

tunisia = Team(
    name="Tunisia",
    attack=-0.08,   # 22 GF in 10 qualifiers but against weak CAF sides. 3W 18 WC matches historically
    defense=0.18,   # 0 GA in 10 qualifiers — historic. Dahmen excellent, Talbi/Bronn/Skhiri organized
    manager_style="defensive",  # compact, counter-attack, protect central zones
    heat_acclimatized=True,     # North African climate
    altitude_acclimatized=False,
    key_absences=["Bronn (recurring injuries, doubt)", "Mejbri (doubt)", "Achouri (doubt)"],
)


# --- Match Predictions ---

matches = [
    # Match 1: Netherlands vs Japan — Sun Jun 14, AT&T Stadium (Arlington TX)
    MatchInput(
        team_a=netherlands,
        team_b=japan,
        stage="group_md1",
        venue="dallas",
        market_total=2.3,       # tight opener, both strong defensively, cautious MD1
        market_sigma=0.18,
    ),

    # Match 2: Sweden vs Tunisia — Sun Jun 14, Estadio BBVA (Monterrey, Mexico)
    MatchInput(
        team_a=sweden,
        team_b=tunisia,
        stage="group_md1",
        venue="monterrey",
        market_total=2.2,       # SWE 10/11 fav, tight. Monterrey heat slows pace
        market_sigma=0.20,
        manual_adj_a=-0.03,     # Sweden injury crisis: Kulusevski likely out, Isak fitness doubt
    ),

    # Match 3: Netherlands vs Sweden — Sat Jun 20, NRG Stadium (Houston TX)
    MatchInput(
        team_a=netherlands,
        team_b=sweden,
        stage="group_md2",
        venue="houston",
        market_total=2.4,       # NED should dominate, Potter will try to attack back
        market_sigma=0.18,
    ),

    # Match 4: Tunisia vs Japan — Sun Jun 21, Estadio BBVA (Monterrey, Mexico)
    MatchInput(
        team_a=tunisia,
        team_b=japan,
        stage="group_md2",
        venue="monterrey",
        market_total=2.1,       # Tunisia will sit deep, Japan must break down low block
        market_sigma=0.20,
    ),

    # Match 5: Japan vs Sweden — Wed Jun 25, AT&T Stadium (Arlington TX)
    MatchInput(
        team_a=japan,
        team_b=sweden,
        stage="group_md3",
        venue="dallas",
        market_total=2.5,       # MD3, more open, both may need result
        market_sigma=0.18,
    ),

    # Match 6: Tunisia vs Netherlands — Wed Jun 25, Arrowhead Stadium (Kansas City MO)
    MatchInput(
        team_a=tunisia,
        team_b=netherlands,
        stage="group_md3",
        venue="kansas_city",
        market_total=2.3,       # Tunisia will park the bus, NED should control
        market_sigma=0.20,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP F — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP F EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP F AVERAGE: {group_total/6:.2f} goals/match")
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
        ("Netherlands vs Japan", "1-1"),
        ("Sweden vs Tunisia", "1-0"),
        ("Netherlands vs Sweden", "2-1"),
        ("Tunisia vs Japan", "1-2"),  # v2: Tunisia gets a goal (was 0-1)
        ("Japan vs Sweden", "1-2"),   # v3: Sweden advance (Gyokeres masterclass)
        ("Tunisia vs Netherlands", "0-2"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
