"""
Group H predictions using market-first Bayesian approach.

Group H: Spain, Cape Verde, Saudi Arabia, Uruguay

Key dynamics:
- Spain overwhelming favorite (82% Polymarket, -450 FanDuel), Euro 2024 champs, Yamal/Pedri/Rodri
- Uruguay strong 2nd but internal tensions under Bielsa, inconsistent form, Nunez fitness concern
- Saudi Arabia mid-tier AFC, terrible recent form (0-4 Egypt, 1-2 Serbia), Renard under pressure
- Cape Verde debutants, smallest WC nation by land area, diaspora squad, beat Cameroon in qualifying

Sources:
- Polymarket group winner: ESP 82%, URU 13%, KSA ~3.5%, CPV ~1.5%
- FanDuel: ESP -450, URU +500, KSA +2200, CPV +7000
- BetMGM: ESP-CPV: Spain 1.08 / Draw 9.00 / CPV 21.00
- BetMGM: KSA-URU: KSA 5.75 / Draw 4.10 / URU 1.43
- Qualifying: ESP (W5 D1, 21GF/2GA), URU (W6 D7 L4, 4th CONMEBOL),
  KSA (W3 D4 L3, scraped through AFC 4th round), CPV (W7 D2 L1, topped CAF Group D)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group H Teams ---

spain = Team(
    name="Spain",
    attack=0.20,    # Yamal 19G/13A, Pedri, Oyarzabal. 21GF in 6 qualifiers. Elite width
    defense=0.20,   # 2 GA in qualifying, Euro 2024 champs, Rodri anchoring. Elite
    manager_style="attacking",  # De la Fuente: possession + vertical transitions
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Rodri (ACL recovery, managing workload)", "Nico Williams (pubalgia, racing)",
                  "Carvajal (ACL recovery)"],
)

cape_verde = Team(
    name="Cape Verde",
    attack=-0.30,   # Livramento (Casa Pia), Mendes aging. Diaspora squad, mid-tier European leagues
    defense=-0.20,  # Beat Cameroon, organized under Bubista. But quality gap to top teams is vast
    manager_style="defensive",  # compact, set pieces, transition play
    heat_acclimatized=True,     # West African archipelago
    altitude_acclimatized=False,
    key_absences=[],
)

saudi_arabia = Team(
    name="Saudi Arabia",
    attack=-0.15,   # 7GF in 10 3rd-round matches, Al-Dawsari 33yo. Inconsistent finishing
    defense=-0.10,  # Conceded in every Arab Cup match. Renard's offside trap being exposed
    manager_style="balanced",   # Renard: high press + offside trap (aggressive but leaky)
    heat_acclimatized=True,     # Saudi climate
    altitude_acclimatized=False,
    key_absences=["Al-Faraj (long-term injury, unlikely)"],
)

uruguay = Team(
    name="Uruguay",
    attack=0.10,    # Valverde elite (8G/9A all comps), but Nunez match fitness concern
    defense=0.10,   # Araujo, Gimenez experienced. But 5-1 loss to USA, many draws
    manager_style="attacking",  # Bielsa: intense press, high energy
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Darwin Nunez (not registered at Al-Hilal since Feb, match fitness)",
                  "Araujo (muscle issue, expected fit)"],
)


# --- Match Predictions ---

matches = [
    # Match 1: Spain vs Cape Verde — Mon Jun 15, Mercedes-Benz Stadium (Atlanta GA, indoor)
    MatchInput(
        team_a=spain,
        team_b=cape_verde,
        stage="group_md1",
        venue="atlanta",
        market_total=3.0,       # biggest mismatch — Spain 1.08 odds, indoor venue
        market_sigma=0.18,
    ),

    # Match 2: Saudi Arabia vs Uruguay — Mon Jun 15, Hard Rock Stadium (Miami FL)
    MatchInput(
        team_a=saudi_arabia,
        team_b=uruguay,
        stage="group_md1",
        venue="miami",
        market_total=2.3,       # Uruguay 1.43 fav but cautious opener, Miami heat
        market_sigma=0.20,
    ),

    # Match 3: Spain vs Saudi Arabia — Sun Jun 21, Mercedes-Benz Stadium (Atlanta GA, indoor)
    MatchInput(
        team_a=spain,
        team_b=saudi_arabia,
        stage="group_md2",
        venue="atlanta",
        market_total=2.8,       # Spain dominant but Saudi press can cause chaos (see 2022 Argentina)
        market_sigma=0.20,
    ),

    # Match 4: Uruguay vs Cape Verde — Sun Jun 21, Hard Rock Stadium (Miami FL)
    MatchInput(
        team_a=uruguay,
        team_b=cape_verde,
        stage="group_md2",
        venue="miami",
        market_total=2.5,       # Uruguay should win, Miami heat again
        market_sigma=0.22,
        manual_adj_b=-0.03,     # Cape Verde more acclimatized but Uruguay not — however CV already flagged
    ),

    # Match 5: Cape Verde vs Saudi Arabia — Fri Jun 26, NRG Stadium (Houston TX, indoor)
    MatchInput(
        team_a=cape_verde,
        team_b=saudi_arabia,
        stage="group_md3",
        venue="houston",
        market_total=2.3,       # tight match, both fighting for 3rd/survival
        market_sigma=0.25,
    ),

    # Match 6: Uruguay vs Spain — Fri Jun 26, Estadio Akron (Guadalajara, Mexico)
    MatchInput(
        team_a=uruguay,
        team_b=spain,
        stage="group_md3",
        venue="guadalajara",
        market_total=2.3,       # tight, tactical. Altitude factor (1,566m)
        market_sigma=0.20,
        manual_adj_a=-0.03,     # Bielsa internal tensions, inconsistent form
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP H — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP H EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP H AVERAGE: {group_total/6:.2f} goals/match")
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
        ("Spain vs Cape Verde", "3-0"),
        ("Saudi Arabia vs Uruguay", "1-2"),  # v2: Al-Dawsari consolation goal
        ("Spain vs Saudi Arabia", "2-1"),    # v2: Renard's chaos creates KSA goal
        ("Uruguay vs Cape Verde", "2-1"),    # v2: Cape Verde set piece (Pico Lopes)
        ("Cape Verde vs Saudi Arabia", "1-1"),
        ("Uruguay vs Spain", "1-2"),         # v2: Valverde scores (8G/9A, can't be blanked)
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
