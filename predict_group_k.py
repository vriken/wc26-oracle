"""
Group K predictions using market-first Bayesian approach.

Group K: Portugal, DR Congo, Uzbekistan, Colombia

Key dynamics:
- Portugal clear favorite (67% Polymarket, -210 FanDuel), Nations League winners 2025
- Colombia: Copa America 2024 finalists, Luis Diaz 7G in qualifying, strong CONMEBOL run
- DR Congo: 52-year return (last WC as Zaire 1974), qualified via longest possible path
- Uzbekistan: WC debutants, first Central Asian nation, Cannavaro coaching, Khusanov at Man City
- Portugal vs Colombia (MD3) is the group decider — Polymarket sees it as near 50/50

Sources:
- Polymarket group winner: POR 67%, COL 30%, DRC ~2%, UZB ~5%
- FanDuel: POR -210, COL +260, DRC +1000, UZB +3500
- Qualifying: POR (W4 D1 L1, UEFA + Nations League winners),
  COL (W7 D7 L4, CONMEBOL 3rd), DRC (CAF + intercontinental playoff),
  UZB (W6 D3 L1, AFC 2nd)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group K Teams ---

portugal = Team(
    name="Portugal",
    attack=0.20,    # Ronaldo, Bruno, Leao, Conceicao. Elite depth. Nations League winners
    defense=0.15,   # Dias, Inacio, Nuno Mendes. Martinez's structured build-up
    manager_style="balanced",  # Martinez: possession-dominant, 71% avg, tactical versatility
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Ronaldo (thigh, returned Apr 3)", "Dias (thigh, missed call-ups)",
                  "Leao (recurring injuries)", "Bernardo Silva (fitness)",
                  "Diogo Costa (adductor)", "Conceicao (muscular)"],
)

colombia = Team(
    name="Colombia",
    attack=0.10,    # Luis Diaz 7G WCQ (2nd in CONMEBOL), Arias, James set pieces
    defense=0.05,   # Lerma/Rios midfield shield, Sanchez aerial. Lost to Croatia, France in March
    manager_style="balanced",  # Lorenzo: physical, disciplined, elite set-piece threat
    heat_acclimatized=True,    # tropical climate + CONMEBOL altitude experience
    altitude_acclimatized=True,  # Bogota 2,640m, regular qualifier venues
    key_absences=["James Rodriguez (hospitalized, returned Apr 6)",
                  "Yerry Mina (recurring injuries)", "Ospina (injured)",
                  "Mosquera (ligament, long-term)"],
)

dr_congo = Team(
    name="DR Congo",
    attack=-0.05,   # Wissa (Newcastle), Bakambu aging but 4G qualifying. Limited creativity
    defense=0.00,   # Mbemba captain, 0.85 GA/match under Desabre. Resilient but not elite
    manager_style="defensive",  # Desabre: defense-first, compact, counter-attack, set pieces
    heat_acclimatized=True,     # equatorial climate
    altitude_acclimatized=False,
    key_absences=[],
)

uzbekistan = Team(
    name="Uzbekistan",
    attack=-0.20,   # Shomurodov 16G club + 5G qualifying, but rest are domestic league level
    defense=-0.15,  # Khusanov (Man City) is world class but rest are Uzbek league. Big drop-off
    manager_style="defensive",  # Cannavaro: 5-4-1, absorb pressure, low block
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=[],
)


# --- Match Predictions ---

matches = [
    # Match 1: Portugal vs DR Congo — Wed Jun 17, NRG Stadium (Houston TX, AC)
    MatchInput(
        team_a=portugal,
        team_b=dr_congo,
        stage="group_md1",
        venue="houston",
        market_total=2.5,       # Portugal dominant but Congo will sit deep
        market_sigma=0.20,
    ),

    # Match 2: Uzbekistan vs Colombia — Wed Jun 17, Estadio Azteca (Mexico City)
    MatchInput(
        team_a=uzbekistan,
        team_b=colombia,
        stage="group_md1",
        venue="mexico_city",
        market_total=2.3,       # Uzbek 5-4-1 low block, Colombia set-piece threat
        market_sigma=0.22,
        manual_adj_b=+0.03,    # Colombia altitude-acclimatized (Bogota 2,640m)
    ),

    # Match 3: Portugal vs Uzbekistan — Tue Jun 23, NRG Stadium (Houston TX, AC)
    MatchInput(
        team_a=portugal,
        team_b=uzbekistan,
        stage="group_md2",
        venue="houston",
        market_total=2.8,       # Portugal should dominate, Uzbekistan ultra-defensive
        market_sigma=0.20,
    ),

    # Match 4: Colombia vs DR Congo — Tue Jun 23, Estadio Akron (Guadalajara)
    MatchInput(
        team_a=colombia,
        team_b=dr_congo,
        stage="group_md2",
        venue="guadalajara",
        market_total=2.3,       # Physical battle, both strong defensively
        market_sigma=0.22,
    ),

    # Match 5: Colombia vs Portugal — Sat Jun 27, Hard Rock Stadium (Miami FL)
    MatchInput(
        team_a=colombia,
        team_b=portugal,
        stage="group_md3",
        venue="miami",
        market_total=2.5,       # group decider, near 50/50 per Polymarket
        market_sigma=0.18,
        manual_adj_a=+0.02,    # Colombia heat-acclimatized, Miami advantage
    ),

    # Match 6: DR Congo vs Uzbekistan — Sat Jun 27, Mercedes-Benz Stadium (Atlanta GA, AC)
    MatchInput(
        team_a=dr_congo,
        team_b=uzbekistan,
        stage="group_md3",
        venue="atlanta",
        market_total=2.3,       # survival match, both need points, tight and physical
        market_sigma=0.25,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP K — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP K EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP K AVERAGE: {group_total/6:.2f} goals/match")
    print(f"{'='*60}")

    # Summary table
    print(f"\n{'Match':<35} {'Modal':>8} {'E[total]':>10} {'80% CI':>10}")
    print("-" * 65)
    for pred in predictions:
        modal = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        ci = f"{pred.ci_80[0]}-{pred.ci_80[1]}"
        print(f"{pred.team_a} vs {pred.team_b:<22} {modal:>8} {pred.mu_total:>10.02f} {ci:>10}")

    # Our manual predictions vs model (v2 after counselors review)
    print(f"\n{'='*60}")
    print("COMPARISON: Manual Picks vs Model (v2)")
    print(f"{'='*60}")
    manual = [
        ("Portugal vs DR Congo", "3-0"),    # v4: Portugal dominant, clean sheet
        ("Uzbekistan vs Colombia", "0-2"),
        ("Portugal vs Uzbekistan", "3-0"),
        ("Colombia vs DR Congo", "1-1"),
        ("Colombia vs Portugal", "1-1"),
        ("DR Congo vs Uzbekistan", "1-1"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
