"""
Group J predictions using market-first Bayesian approach.

Group J: Argentina (defending champions), Algeria, Austria, Jordan (WC debutant)

Key dynamics:
- Argentina dominant favorite (75% Polymarket, -290 FanDuel), defending champions, Messi's last WC
- Austria: Rangnick's gegenpressing, first WC since 1998, ranked 24th, strong qualifying (W6 D1 L1)
- Algeria: Petkovic's tournament pedigree, Amoura (10 WCQ goals), AFCON QF, ranked 28th
- Jordan: WC debutants, Al-Taamari (Rennes) sole top-league player, Arab Cup finalists
- Algeria vs Austria (MD3) is the decider for 2nd — 1982 "Disgrace of Gijon" rematch adds emotional weight

Sources:
- Polymarket group winner: ARG 75%, AUT ~15%, ALG ~8%, JOR ~2%
- FanDuel: ARG -290, AUT +500, ALG +650, JOR +5000
- Qualifying: ARG (W12 D2 L4, 31GF/10GA, 1st CONMEBOL), AUT (W6 D1 L1, 22GF/4GA, 1st UEFA),
  ALG (W8 D1 L1, 24GF/8GA, 1st CAF), JOR (W4 D4 L2, 16GF/6GA, 2nd AFC)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group J Teams ---

argentina = Team(
    name="Argentina",
    attack=0.25,    # Messi (29G MLS), Alvarez (17G all comps), Lautaro fit. Best attack in CONMEBOL qualifying (31GF)
    defense=0.20,   # Emi Martinez (72% save rate, 7 CS), Romero, 10GA in 18 qualifiers. Foyth OUT but depth covers
    manager_style="balanced",  # Scaloni: fluid 4-3-3, press + transition. Won WC 2022, Copa 2021+2024
    heat_acclimatized=True,    # Argentine climate, players across warm leagues
    altitude_acclimatized=False,
    key_absences=["Foyth (Achilles, OUT)", "Carboni (knee, OUT)", "Lo Celso (fitness TBD)"],
)

algeria = Team(
    name="Algeria",
    attack=0.05,    # Amoura (10 WCQ goals), Gouiri (5G Ligue 1), Mahrez (35yo, Saudi league). Good but not elite
    defense=0.00,   # 8GA in 10 qualifiers (0.8/match). AFCON QF exit to Nigeria exposed gaps. Average at WC level
    manager_style="attacking",  # Petkovic: attack-minded 4-3-3, can shift to 3-4-2-1 defensively
    heat_acclimatized=True,     # North African climate
    altitude_acclimatized=False,
    key_absences=[],
)

austria = Team(
    name="Austria",
    attack=0.05,    # Arnautovic (47 NT goals but 37yo), Gregoritsch, Sabitzer. Functional not flashy
    defense=0.05,   # 4GA in 8 qualifiers (0.5/match). Rangnick pressing limits chances. Alaba fitness wildcard
    manager_style="balanced",   # Rangnick: gegenpressing, compact, quick transitions. Euro progressor x2
    heat_acclimatized=False,    # Central European
    altitude_acclimatized=False,
    key_absences=["Alaba (ACL recovery, wildcard fitness)", "Wober (fitness TBD)"],
)

jordan = Team(
    name="Jordan",
    attack=-0.25,   # Al-Taamari (3G Ligue 1), Olwan (Qatar league). Limited top-level quality
    defense=-0.15,  # Compact defensive block but untested vs WC-caliber attacks. Arab Cup final lost 3-2
    manager_style="defensive",  # Sellami: deep block, rapid counter. 4-5-1 / 3-4-3
    heat_acclimatized=True,     # Middle Eastern climate
    altitude_acclimatized=False,
    key_absences=[],
)


# --- Match Predictions ---

matches = [
    # Match 1: Argentina vs Algeria — Tue Jun 16, GEHA Field at Arrowhead Stadium (Kansas City MO)
    MatchInput(
        team_a=argentina,
        team_b=algeria,
        stage="group_md1",
        venue="kansas_city",
        market_total=2.5,       # Argentina dominant but opener caution + heat
        market_sigma=0.18,
    ),

    # Match 2: Austria vs Jordan — Wed Jun 17, Levi's Stadium (Santa Clara CA)
    MatchInput(
        team_a=austria,
        team_b=jordan,
        stage="group_md1",
        venue="san_francisco",
        market_total=2.5,       # Austria favored but Jordan will sit deep
        market_sigma=0.22,
    ),

    # Match 3: Argentina vs Austria — Mon Jun 22, AT&T Stadium (Arlington TX)
    MatchInput(
        team_a=argentina,
        team_b=austria,
        stage="group_md2",
        venue="dallas",
        market_total=2.5,       # tactical battle, Rangnick will press high — risky vs Argentina
        market_sigma=0.20,
    ),

    # Match 4: Jordan vs Algeria — Mon Jun 22, Levi's Stadium (Santa Clara CA)
    MatchInput(
        team_a=jordan,
        team_b=algeria,
        stage="group_md2",
        venue="san_francisco",
        market_total=2.3,       # Algeria favored but Jordan organized. Could be tight
        market_sigma=0.22,
    ),

    # Match 5: Jordan vs Argentina — Sat Jun 27, AT&T Stadium (Arlington TX)
    MatchInput(
        team_a=jordan,
        team_b=argentina,
        stage="group_md3",
        venue="dallas",
        market_total=2.8,       # Argentina may rotate if qualified. Jordan nothing to lose
        market_sigma=0.22,
        manual_adj_b=-0.03,     # Argentina rotation if already qualified
    ),

    # Match 6: Algeria vs Austria — Sat Jun 27, GEHA Field at Arrowhead Stadium (Kansas City MO)
    MatchInput(
        team_a=algeria,
        team_b=austria,
        stage="group_md3",
        venue="kansas_city",
        market_total=2.5,       # decider for 2nd place, both will commit
        market_sigma=0.20,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP J — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP J EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP J AVERAGE: {group_total/6:.2f} goals/match")
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
        ("Argentina vs Algeria", "2-0"),
        ("Austria vs Jordan", "2-1"),
        ("Argentina vs Austria", "2-1"),
        ("Jordan vs Algeria", "1-2"),  # v2: changed from 0-1 (counselors review)
        ("Jordan vs Argentina", "1-2"),
        ("Algeria vs Austria", "1-1"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
