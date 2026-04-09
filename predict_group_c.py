"""
Group C predictions using market-first Bayesian approach.

Group C: Brazil, Morocco, Haiti, Scotland

Key dynamics:
- Brazil clear favorite (77% Polymarket, -290 FanDuel) but worst qualifying ever + Rodrygo OUT
- Morocco: 2022 semi-finalists, AFCON champions, perfect 8/8 qualifying, FIFA #8
- Scotland: first WC since 1998, McTominay in career-best form, GK crisis
- Haiti: debutants, €38M squad value, diaspora team
- 1998 parallel: Brazil, Morocco, Scotland were in the same group then too

Sources:
- Polymarket group winner: BRA 77%, MOR 20%, SCO ~3.6%, HAI ~0.4%
- FanDuel: BRA -290, MOR +450, SCO +700, HAI +10000
- Oddschecker BRA-MOR: Brazil 3/5, Draw 3/1, Morocco 5/1
- Oddschecker HAI-SCO: Scotland 4/9, Draw 7/4, Haiti 7/1
- Qualifying: MOR (W8 D0, 22GF/2GA perfect), BRA (W8 D4 L6, worst ever),
  SCO (W4 D1 L1, topped UEFA group), HAI (W3 D2 L1, CONCACAF)
"""

from model import (
    Team, MatchInput, predict_match, format_prediction,
)


# --- Group C Teams ---

brazil = Team(
    name="Brazil",
    attack=0.20,    # Vinicius, Raphinha elite. But no settled No.9, Rodrygo OUT
    defense=0.15,   # Marquinhos, Ancelotti structure. But worst qualifying defense ever
    manager_style="balanced",  # Ancelotti: control over spectacle
    heat_acclimatized=True,   # Brazilian climate
    altitude_acclimatized=False,
    key_absences=["Rodrygo (ACL, OUT)", "Raphinha (hamstring, racing)",
                  "Bruno Guimaraes (thigh)", "Estevao (muscle)", "Militao (injury)"],
)

morocco = Team(
    name="Morocco",
    attack=0.15,    # 22GF in 8 qualifiers, Hakimi 5G/10A from RB, transition threat
    defense=0.25,   # only 2 GA in 8 qualifiers, 2022 semi-final defense. Elite.
    manager_style="defensive",  # compact, counter-attack, Regragui school continued
    heat_acclimatized=True,     # North African climate
    altitude_acclimatized=False,
    key_absences=["Amrabat (surgery, racing)", "Regragui (resigned — new coach Ouahbi)"],
)

scotland = Team(
    name="Scotland",
    attack=-0.05,   # limited beyond set pieces, lost both March friendlies 0-1
    defense=0.10,   # Clarke's Mourinho school, organized. 0.6 xGA/match in qualifying
    manager_style="defensive",  # deep block, counter, set pieces
    heat_acclimatized=False,
    altitude_acclimatized=False,
    key_absences=["Hickey (RWB, injury)", "Gunn (GK, barely playing at Forest)"],
)

haiti = Team(
    name="Haiti",
    attack=-0.35,   # €38M squad, CONCACAF mid-tier. Nazon proven but aging
    defense=-0.25,  # limited squad depth, massive quality gap vs top teams
    manager_style="defensive",  # park the bus against big teams
    heat_acclimatized=True,    # Caribbean climate
    altitude_acclimatized=False,
    key_absences=[],
)


# --- Match Predictions ---

matches = [
    # Match 1: Brazil vs Morocco — Jun 13, MetLife Stadium (East Rutherford NJ)
    MatchInput(
        team_a=brazil,
        team_b=morocco,
        stage="group_md1",
        venue="new_york",
        market_total=2.3,       # tight tactical battle, both strong defensively
        market_sigma=0.18,
        manual_adj_a=-0.05,     # Rodrygo OUT, injury crisis
    ),

    # Match 2: Haiti vs Scotland — Jun 13, Gillette Stadium (Foxborough MA)
    MatchInput(
        team_a=haiti,
        team_b=scotland,
        stage="group_md1",
        venue="boston",
        market_total=2.5,       # Scotland 4/9 favorite, should win
        market_sigma=0.22,
    ),

    # Match 3: Scotland vs Morocco — Jun 19, Gillette Stadium (Foxborough MA)
    MatchInput(
        team_a=scotland,
        team_b=morocco,
        stage="group_md2",
        venue="boston",
        market_total=2.3,       # Morocco strong, Scotland will sit deep
        market_sigma=0.22,
    ),

    # Match 4: Brazil vs Haiti — Jun 19, Lincoln Financial Field (Philadelphia PA)
    MatchInput(
        team_a=brazil,
        team_b=haiti,
        stage="group_md2",
        venue="philadelphia",
        market_total=3.0,       # biggest mismatch — Brazil heavy favorite
        market_sigma=0.20,
    ),

    # Match 5: Scotland vs Brazil — Jun 24, Hard Rock Stadium (Miami FL)
    MatchInput(
        team_a=scotland,
        team_b=brazil,
        stage="group_md3",
        venue="miami",
        market_total=2.5,       # Brazil should win, Miami heat factor
        market_sigma=0.22,
        manual_adj_a=-0.03,     # Scotland non-acclimatized to Miami heat
    ),

    # Match 6: Morocco vs Haiti — Jun 24, Mercedes-Benz Stadium (Atlanta GA, indoor)
    MatchInput(
        team_a=morocco,
        team_b=haiti,
        stage="group_md3",
        venue="atlanta",
        market_total=3.0,       # Morocco dominant, need GD
        market_sigma=0.22,
    ),
]


if __name__ == "__main__":
    print("=" * 60)
    print("GROUP C — SCORELINE PREDICTIONS (Market-First Bayesian)")
    print("=" * 60)

    group_total = 0.0
    predictions = []

    for m in matches:
        pred = predict_match(m)
        print(format_prediction(pred))
        group_total += pred.mu_total
        predictions.append(pred)

    print(f"\n{'='*60}")
    print(f"GROUP C EXPECTED TOTAL: {group_total:.1f} goals")
    print(f"GROUP C AVERAGE: {group_total/6:.2f} goals/match")
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
        ("Brazil vs Morocco", "1-1"),
        ("Haiti vs Scotland", "1-2"),
        ("Scotland vs Morocco", "0-2"),
        ("Brazil vs Haiti", "3-0"),
        ("Scotland vs Brazil", "1-2"),
        ("Morocco vs Haiti", "3-1"),
    ]
    for (name, manual_score), pred in zip(manual, predictions):
        model_score = f"{pred.modal_scoreline[0]}-{pred.modal_scoreline[1]}"
        agree = "✓" if manual_score == model_score else "≠"
        print(f"  {agree} {name:<35} manual={manual_score:>5}  model={model_score:>5}  μ={pred.mu_total:.2f}")
