"""
Group G predictions using market-first Bayesian approach.

Group G: Belgium, Egypt, Iran, New Zealand

Key dynamics:
- Belgium clear favorite (-220 FanDuel, 75% Polymarket) but aging squad in generational transition
- Egypt: Salah-led, unbeaten CAF qualifying (W8 D2, 2 GA), AFCON 4th place
- Iran: strong AFC campaigners (7th WC), Taremi quality, but geopolitical uncertainty + domestic league suspended
- New Zealand: OFC champions, Chris Wood recovering from knee surgery, massive quality gap outside OFC
- All matches on US/Canada West Coast (Seattle, LA, Vancouver)

Sources:
- Polymarket group winner: BEL 75%, EGY 16%, IRN 10%, NZL ~4%
- FanDuel: BEL -220, EGY +390, IRN +700, NZL +1900
- Qualifying: BEL (W5 D2 L0, 27GF/7GA), EGY (W8 D2 L0, 20GF/2GA),
  IRN (W7 D2 L1, ~17GF/~8GA), NZL (W7 D0 L0, 29GF/1GA but OFC only)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group G Teams ---

belgium = Team(
    name="Belgium",
    attack=0.12,    # De Bruyne (34, returning from hamstring), Doku (5G qualifying), Openda struggling at Juve
    defense=0.10,   # Generational downgrade (Kompany/Vertonghen/Alderweireld all retired), Theate/De Winter unproven
    manager_style="balanced",  # Rudi Garcia: technical control, flexible 4-3-3/4-2-3-1
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["De Bruyne (hamstring, returned Mar)", "Lukaku (thigh, skipped Mar by choice)",
                  "Courtois (withdrew from Mar squad)", "Trossard (injured)", "Onana (left camp injured)"],
)

egypt = Team(
    name="Egypt",
    attack=0.08,    # Salah (5G/6A PL, down from prior years), Marmoush (1G/3A adapting at City)
    defense=0.10,   # Only 2 GA in 10 qualifiers, El Shenawy reliable. AFCON run showed resilience
    manager_style="defensive",  # Hossam Hassan: compact low block, rapid counters, Salah decides tight games
    heat_acclimatized=True,     # North African climate
    altitude_acclimatized=False,
    key_absences=[],
)

iran = Team(
    name="Iran",
    attack=0.03,    # Taremi (Olympiacos, fit), but Azmoun doubtful (injury + political exclusion)
    defense=0.03,   # Organized, <1 GA/game in qualifying. But domestic league suspended = fitness concerns
    manager_style="defensive",  # Ghalenoei: compact shape, frustrate + counter, tournament experience
    heat_acclimatized=True,     # Tehran summers
    altitude_acclimatized=False,
    key_absences=["Azmoun (injury + political exclusion, doubtful)",
                  "Domestic players (league suspended, lack competitive minutes)"],
)

new_zealand = Team(
    name="New Zealand",
    attack=-0.20,   # Chris Wood (knee surgery Dec 2025, returning but fitness unknown), squad from A-League/MLS/Scottish Prem
    defense=-0.17,  # Organized under Bazeley but W2 D1 L6 vs non-OFC opposition. Set-piece defensive weakness
    manager_style="defensive",  # Bazeley: compact, disciplined, punches above weight, set pieces
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Chris Wood (knee surgery Dec 2025, racing fitness — no first-team football since Oct)"],
)


# --- Match Predictions ---

matches = [
    # Match 1: Belgium vs Egypt — Mon Jun 15, Lumen Field (Seattle)
    MatchInput(
        team_a=belgium,
        team_b=egypt,
        stage="group_md1",
        venue="seattle",
        market_total=2.3,       # opener, both cautious. Belgium favored but Egypt's defense is elite
        market_sigma=0.18,
    ),

    # Match 2: Iran vs New Zealand — Mon Jun 15, SoFi Stadium (Los Angeles)
    MatchInput(
        team_a=iran,
        team_b=new_zealand,
        stage="group_md1",
        venue="los_angeles",
        market_total=2.3,       # Iran favored, NZ organized but outmatched
        market_sigma=0.20,
    ),

    # Match 3: Belgium vs Iran — Sun Jun 21, SoFi Stadium (Los Angeles)
    MatchInput(
        team_a=belgium,
        team_b=iran,
        stage="group_md2",
        venue="los_angeles",
        market_total=2.4,       # Belgium should control, Iran compact
        market_sigma=0.18,
    ),

    # Match 4: New Zealand vs Egypt — Sun Jun 21, BC Place (Vancouver)
    MatchInput(
        team_a=new_zealand,
        team_b=egypt,
        stage="group_md2",
        venue="vancouver",
        market_total=2.4,       # Egypt strong favorite, NZ limited
        market_sigma=0.20,
    ),

    # Match 5: Egypt vs Iran — Fri Jun 26, Lumen Field (Seattle)
    # "The decisive match" — widely seen as determining 2nd place
    MatchInput(
        team_a=egypt,
        team_b=iran,
        stage="group_md3",
        venue="seattle",
        market_total=2.3,       # tight tactical battle, both defensive sides
        market_sigma=0.18,
    ),

    # Match 6: New Zealand vs Belgium — Fri Jun 26, BC Place (Vancouver)
    MatchInput(
        team_a=new_zealand,
        team_b=belgium,
        stage="group_md3",
        venue="vancouver",
        market_total=2.8,       # Belgium should win comfortably, MD3 more open
        market_sigma=0.20,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP G — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP G EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP G AVERAGE: {group_total/6:.2f} goals/match")
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
        ("Belgium vs Egypt", "1-1"),      # unchanged from v1
        ("Iran vs New Zealand", "2-1"),    # unchanged from v1
        ("Belgium vs Iran", "2-1"),        # v2: was 2-0, Taremi scores
        ("New Zealand vs Egypt", "0-2"),   # unchanged from v1
        ("Egypt vs Iran", "1-1"),          # v2: was 1-0, defensive teams draw
        ("New Zealand vs Belgium", "0-2"), # unchanged from v1
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
