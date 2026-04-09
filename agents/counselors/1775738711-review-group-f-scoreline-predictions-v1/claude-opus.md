Now I have the full picture. Let me write the review.

---

# Review — Group F Scoreline Predictions (v1)

## Critical Data Integrity Issue

**The research file (`research/group-f-research.md`) describes the wrong group.** It covers Mexico, Netherlands, Japan, and Kenya — not the actual Group F of Netherlands, Japan, Sweden, Tunisia. The predictions in `groups/group-f.md` appear to be based on correct data (detailed Sweden/Tunisia info is present), but the research file is mismatched. This should be fixed before any further review cycles rely on it.

---

## 1. Individual Scoreline Assessment

| Match | Pick | Model Modal | Verdict |
|-------|------|-------------|---------|
| NED vs JPN | 1-1 | 1-1 (14.2%) | **Good.** Follows model. Two elite defenses (3 GA each in qualifying). Cautious MD1 opener. Justified. |
| SWE vs TUN | 1-0 | 1-1 (14.3%) | **Defensible but risky.** The "Gyokeres > CAF opponents" logic is sound, but shutting out Tunisia entirely is aggressive. They scored 22 in qualifying and have Msakni/Ben Romdhane. |
| NED vs SWE | 2-1 | 1-1 (13.2%) | **Good.** Best pick of the group. Potter's attacking philosophy against superior quality = open game. Well-reasoned deviation. |
| TUN vs JPN | 0-1 | 1-1 (13.9%) | **Too low.** Japan scored 54 goals in 16 qualifiers (3.4 g/m). Against a Tunisia sitting deep in Monterrey heat, 1-0 undersells Japan's attacking depth. A 1-2 or 0-2 is more realistic. |
| JPN vs SWE | 2-1 | 1-1 (12.1%) | **Good.** MD3 desperation, AC stadium, both attacking. Model's highest λ pair (1.47 + 1.30 = 2.77). The pick tells a coherent story. |
| TUN vs NED | 0-2 | 1-1 (13.4%) | **Biggest divergence — partially justified.** Netherlands should dominate. But 0 goals for Tunisia is harsh. Tunisia beat France 1-0 in a similar WC dead rubber in 2022. A 1-2 is more historically calibrated. |

## 2. Total Goals: 12 (2.00 g/m) — Too Low

| Benchmark | Goals/Match | Group Total |
|-----------|------------|-------------|
| WC group historical avg | 2.67 | 16.0 |
| Model expected | 2.40 | 14.4 |
| **Our picks** | **2.00** | **12** |

The picks are **17% below the model** and **25% below WC historical average**. The CLAUDE.md threshold says "don't deviate >20% without good reason." You're right at the edge with the model but well past it on the historical benchmark.

**Where are the missing goals?**
- SWE-TUN at 1-0 (model expects 2.06): missing ~1 goal
- TUN-JPN at 0-1 (model expects 2.22): missing ~1.2 goals
- TUN-NED at 0-2 (model expects 2.36): missing ~0.4 goals

The pattern is clear: **Tunisia is being zeroed out in every match**, which drags the group total down. Tunisia may be limited, but 0 goals in 3 matches against 3 different opponents is extreme. Even the worst WC group performers (Saudi Arabia 2002: 0 goals; Costa Rica 2006: 3 goals conceded, 3 scored) usually scratch at least 1 goal across a group.

**Recommendation:** Add 2-3 goals. Give Tunisia at least 1 goal across 3 matches (most likely against Sweden in Monterrey heat, or a consolation vs Netherlands). Bump TUN-JPN to 1-2 (adds 2 goals, puts group at 14).

## 3. Draw Count: 1 of 6 (17%)

Below the 25% base rate (1.5 draws per 6 matches), but this is less concerning than the goal total. The quality separations justify fewer draws:
- NED > SWE and TUN (clear)
- JPN > SWE and TUN (clear)
- Only NED-JPN is evenly matched → draw

**Verdict:** 1 draw is defensible for this group. No change needed.

## 4. Group Story: NED 7, JPN 7, SWE 0, TUN 0

**The bottom half is too harsh.** Two teams on 0 points in a 3-match group stage is rare at World Cups and requires both underdogs to lose every single match.

**Sweden at 0 points is the weakest call.** Gyokeres has 15 goals for Arsenal this season. Isak (if fit) is a top-10 Premier League striker. Potter's system produced a playoff hat-trick vs Ukraine and an 88th-minute winner vs Poland. This is not a 0-point team. Losing all 3 matches requires losing to Tunisia — a team ranked 6 places below them that just had a disappointing AFCON.

Even with the injury crisis (Kulusevski major doubt, Lundgren OUT), Sweden should be favored against Tunisia. Your own pick has them winning that match 1-0! But then you have them lose the next two — meaning Sweden's only possible result is 3 points from Tunisia, and you gave them exactly 0 vs NED and JPN. That's actually 3 points, not 0.

**Wait — your standings table says SWE 0 pts, but your picks have SWE beating TUN 1-0.** That's 3 points. **The standings table is wrong.** Let me recalculate:

| Match | Result | NED | JPN | SWE | TUN |
|-------|--------|-----|-----|-----|-----|
| NED-JPN | 1-1 | +1 | +1 | | |
| SWE-TUN | 1-0 | | | +3 | 0 |
| NED-SWE | 2-1 | +3 | | 0 | |
| TUN-JPN | 0-1 | | +3 | | 0 |
| JPN-SWE | 2-1 | | +3 | 0 | |
| TUN-NED | 0-2 | +3 | | | 0 |

Corrected standings:

| Pos | Team | W | D | L | GF | GA | GD | Pts |
|-----|------|---|---|---|----|----|-----|-----|
| 1 | **Netherlands** | 2 | 1 | 0 | 5 | 2 | +3 | **7** |
| 2 | **Japan** | 2 | 1 | 0 | 4 | 2 | +2 | **7** |
| 3 | Sweden | 1 | 0 | 2 | 2 | 4 | -2 | **3** |
| 4 | Tunisia | 0 | 0 | 3 | 0 | 4 | -4 | **0** |

**Sweden should be on 3 points, not 0.** The standings table in the group file has a calculation error. This also makes the group story more plausible — Sweden get their win against Tunisia but can't compete with the top two.

## 5. Model Divergences

You deviate from the model modal (1-1) in 5 of 6 matches. The model gives 1-1 as modal in every single game — which itself signals that the model's resolution is too coarse for differentiated picks. The divergences are generally in the right direction:

| Divergence | Justified? |
|-----------|-----------|
| SWE-TUN: 1-0 instead of 1-1 | Partially. Gyokeres argument is good but total shutout risky |
| NED-SWE: 2-1 instead of 1-1 | Yes. Potter's style creates an open game |
| TUN-JPN: 0-1 instead of 1-1 | Direction right, total too low. Should be 1-2 |
| JPN-SWE: 2-1 instead of 1-1 | Yes. MD3 + highest combined λ |
| TUN-NED: 0-2 instead of 1-1 | Direction right, Tunisia shutout is aggressive |

## 6. Key Risks and Blindspots

1. **Tunisia 0 goals in 3 matches is the biggest risk.** They have experienced WC players (Msakni ~100 caps, Skhiri 72 caps) and beat France 1-0 at WC 2022. Predicting 0 goals from 270+ minutes is extreme. Give them at least 1.

2. **Sweden's injury situation may improve.** Isak is "expected back late April, likely available." Kulusevski is "major doubt" but not confirmed out. If either returns, Sweden's ceiling rises significantly. The picks seem to assume worst-case injuries.

3. **Monterrey heat cuts both ways.** You cite it as hurting Sweden (non-acclimatized) in SWE-TUN but also hurting Japan (non-acclimatized) in TUN-JPN. Consistency: if heat saps Sweden, it should also sap Japan — giving Tunisia more of a chance to score.

4. **Japan's 54 GF came against AFC opposition.** The 3.4 g/m rate was against China, Indonesia, Bahrain, etc. Against actual quality (Australia, USA, Mexico), Japan's scoring rate drops dramatically. The 1-0 win at Wembley and 0-0 with Mexico are more calibrative than the 7-0 vs China.

5. **The research file is for the wrong group.** This is a process risk — if anyone references it for future revisions, they'll be reading about Mexico and Kenya instead of Sweden and Tunisia.

---

## Recommended v2 Adjustments

| Match | v1 | Suggested v2 | Rationale |
|-------|-----|-------------|-----------|
| NED vs JPN | 1-1 | **1-1** | Keep. Well-calibrated. |
| SWE vs TUN | 1-0 | **1-1** | Give Tunisia a goal. Monterrey heat + organized defense = Tunisia nick one on the counter. Keeps draw count at 2 (closer to base rate). |
| NED vs SWE | 2-1 | **2-1** | Keep. Best pick. |
| TUN vs JPN | 0-1 | **1-2** | Japan should score more (λ=1.16, H2H dominance). Tunisia get a consolation in Monterrey. Adds 2 goals. |
| JPN vs SWE | 2-1 | **2-1** | Keep. |
| TUN vs NED | 0-2 | **0-2** or **1-2** | Lean keep, but 1-2 more historically calibrated (Tunisia beat France 1-0 in analogous spot). |

**v2 total (conservative):** 14 goals (2.33 g/m) — closer to model's 14.4
**v2 total (if TUN-NED → 1-2):** 15 goals (2.50 g/m) — close to WC average

**v2 draws:** 2 of 6 (33%) — closer to 25% base rate

**Fix the standings table** — Sweden should be on 3 points with current picks.

---

## Summary

The picks tell a coherent story but are **too pessimistic on goals** (2.00 g/m vs 2.67 historical) and **too harsh on Tunisia** (0 goals in 3 matches is extreme). The top-two call (NED + JPN) is well-supported by data. The main fix is adding 2-3 goals, primarily by giving Tunisia at least 1 goal and letting Japan score a second against them. The standings table has a calculation error (Sweden should be 3 pts, not 0).
