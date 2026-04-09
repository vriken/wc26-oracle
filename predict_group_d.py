"""
Group D predictions using market-first Bayesian approach.

Group D: USA (co-host), Turkiye, Australia, Paraguay

Key dynamics:
- USA co-host — massive home advantage at SoFi, Lumen Field. But alarming March losses (2-5 BEL, 0-2 POR)
- Turkiye: first WC since 2002 (semi-finalists). W8-D1-L1 in last 10. Calhanoglu/Guler/Yildiz trio
- Australia: strong AFC qualifier, but Miller ACL OUT, Souttar fitness race. Popovic's 3ATB well-drilled
- Paraguay: best defense in group (10 GA in 18 CONMEBOL qualifiers). Beat ARG, BRA, URU at home. Alfaro pragmatism
- Polymarket favors Turkiye (39%) over USA (34%) to top the group — diverges from US sportsbooks

Sources:
- Polymarket group winner: TUR 39%, USA 34%, PAR ~15%, AUS ~12%
- DraftKings: USA +130, TUR +180, PAR +425, AUS +700
- Oddschecker: USA vs PAR: USA evens, Draw 14/5, Paraguay 59/20
- Oddschecker: AUS vs TUR: Australia 4/1, Draw 13/5, Turkiye 10/11
- Qualifying: USA (auto host), TUR (W4 D1 L1 UEFA group + 2 playoff wins),
  AUS (W6 AFC 2nd round perfect + direct 3rd round), PAR (W7 D7 L4, 6th CONMEBOL)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group D Teams ---

usa = Team(
    name="USA",
    attack=0.10,    # Pulisic (Serie A), McKennie UCL form, but Agyemang OUT, Pulisic in funk
    defense=0.05,   # 3ATB under Pochettino, but 2-5 Belgium and 0-2 Portugal exposed fragility
    manager_style="attacking",  # Pochettino: aggressive, vertical, high wing-backs
    heat_acclimatized=True,     # playing at home, acclimatized
    altitude_acclimatized=False,
    key_absences=["Agyemang (ruptured Achilles, OUT)", "Carter-Vickers (Achilles, OUT)",
                  "Robinson (groin, uncertain)", "Adams (torn MCL, targeting Apr 11 return)",
                  "Pulisic (worst form spell — 15 consecutive matches scoreless)"],
)

turkiye = Team(
    name="Turkiye",
    attack=0.15,    # Calhanoglu (9G Serie A), Guler (Real Madrid), Yildiz (10G Serie A). Best trio in group
    defense=0.10,   # Solid qualifier defense (12 GA in 8, but 6 from Spain alone). Playoff clean sheets
    manager_style="balanced",  # Montella: possession + creative midfield, pragmatic when needed
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Calhanoglu (declared fit Apr 7 after calf Jan, adductor Mar)",
                  "Yildiz (calf + new thigh contusion Apr 2026)", "Can Uzun (injured, depth)"],
)

australia = Team(
    name="Australia",
    attack=-0.05,   # No elite goalscorer. Duke/Boyle limited. Irankunda (19yo, 2G vs Curacao Mar) is X-factor
    defense=0.05,   # Popovic's 3ATB well-organized. 0 GA in AFC 2nd round. But Miller OUT, Souttar racing
    manager_style="defensive",  # 3ATB, disciplined, width from wing-backs, set-piece threat
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Miller (ruptured Achilles, OUT — starting RWB in last 14)",
                  "Souttar (racing fitness)", "Goodwin (groin)",
                  "Silvera (broken metatarsal)"],
)

paraguay = Team(
    name="Paraguay",
    attack=-0.05,   # Limited creativity. Almiron aging (32, MLS). Enciso poor loan form. Sanabria solid but not elite
    defense=0.10,   # Best defense in CONMEBOL qualifiers (10 GA in 18). G. Gomez aerial. Alfaro's organization
    manager_style="defensive",  # Classic 4-4-2 low block, counter-attack, lethal transitions
    heat_acclimatized=True,     # South American climate
    altitude_acclimatized=False,
    key_absences=[],
)


# --- Match Predictions ---

matches = [
    # Match 1: USA vs Paraguay — Fri Jun 12, SoFi Stadium (Los Angeles)
    MatchInput(
        team_a=usa,
        team_b=paraguay,
        stage="group_md1",
        venue="los_angeles",
        market_total=2.5,       # USA evens fav, Paraguay will park the bus and counter
        market_sigma=0.18,
        manual_adj_a=0.08,      # massive home crowd advantage (co-host opener at SoFi)
    ),

    # Match 2: Australia vs Turkiye — Sat Jun 13, BC Place (Vancouver)
    MatchInput(
        team_a=australia,
        team_b=turkiye,
        stage="group_md1",
        venue="vancouver",
        market_total=2.5,       # Turkiye 10/11 fav. Australia will be compact but outgunned
        market_sigma=0.20,
    ),

    # Match 3: USA vs Australia — Thu Jun 19, Lumen Field (Seattle)
    MatchInput(
        team_a=usa,
        team_b=australia,
        stage="group_md2",
        venue="seattle",
        market_total=2.5,       # USA should dominate, Australia deep block
        market_sigma=0.20,
        manual_adj_a=0.06,      # home advantage continues (Seattle crowd)
    ),

    # Match 4: Turkiye vs Paraguay — Fri Jun 20, Levi's Stadium (Santa Clara)
    MatchInput(
        team_a=turkiye,
        team_b=paraguay,
        stage="group_md2",
        venue="san_francisco",
        market_total=2.3,       # two well-organized sides, low-block vs possession
        market_sigma=0.22,
    ),

    # Match 5: Turkiye vs USA — Wed Jun 25, SoFi Stadium (Los Angeles)
    MatchInput(
        team_a=turkiye,
        team_b=usa,
        stage="group_md3",
        venue="los_angeles",
        market_total=2.5,       # the group decider, both strong, MD3 openness
        market_sigma=0.20,
        manual_adj_b=0.05,      # USA home crowd at SoFi for the decider
    ),

    # Match 6: Paraguay vs Australia — Wed Jun 25, Levi's Stadium (Santa Clara)
    MatchInput(
        team_a=paraguay,
        team_b=australia,
        stage="group_md3",
        venue="san_francisco",
        market_total=2.5,       # two evenly matched, fighting for survival/3rd
        market_sigma=0.22,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP D -- SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP D EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP D AVERAGE: {group_total/6:.2f} goals/match")
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
        ("USA vs Paraguay", "2-1"),         # v2: was 2-0, added Paraguay counter goal
        ("Australia vs Turkiye", "1-2"),    # v2: was 0-2, added Australia transition goal
        ("USA vs Australia", "2-1"),
        ("Turkiye vs Paraguay", "1-1"),
        ("Turkiye vs USA", "1-1"),
        ("Paraguay vs Australia", "2-1"),   # v2: was 1-0, open game with desperate teams
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
