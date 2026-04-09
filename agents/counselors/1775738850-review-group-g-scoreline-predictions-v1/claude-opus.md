# Review — Group G Scoreline Predictions (v1)

## Critical Issue: Research File Is Wrong

The research file (`research/group-g-research.md`) covers **Italy, Belgium, Sweden, Cameroon** — but Group G is **Belgium, Egypt, Iran, New Zealand**. Italy and Cameroon didn't even qualify. The only overlapping team is Belgium. This means the research foundation for Egypt, Iran, and New Zealand is missing from the documented research. The picks in `group-g.md` appear to use correct team data, but the sourced research file doesn't back them up. This needs to be rerun.

---

## 1. Individual Scorelines

| Match | Pick | Model Modal | Verdict |
|-------|------|-------------|---------|
| Belgium vs Egypt | 1-1 | 1-1 | **Fine.** Opener caution + Egypt's elite defensive record. Solid. |
| Iran vs New Zealand | 2-1 | 1-0 | **Fine.** NZ scoring from set pieces is plausible. Good deviation. |
| Belgium vs Iran | 2-0 | 1-1 | **Questionable.** Iran's λ is 1.19 — they're not toothless. A clean sheet against a team with Taremi and counter-attacking DNA is optimistic. Iran scored in 9 of 10 qualifiers. 2-1 is more realistic. |
| NZ vs Egypt | 0-2 | 0-1 | **Acceptable.** Egypt should dominate but 0-2 is the right adjustment given Egypt's Salah/Trezeguet quality. |
| Egypt vs Iran | 1-0 | 1-1 | **Too low.** Model expects 2.59 goals, you pick 1. Context (Egypt sitting deep, Iran must attack) actually means MORE space = MORE goals, not fewer. When defensive teams are forced to attack, the game opens up. 1-1 or 2-1 Egypt is better. |
| NZ vs Belgium | 0-2 | 0-2 | **Fine.** Model agrees. |

**Bottom line:** Belgium-Iran should be 2-1, Egypt-Iran should be 1-1 or 2-1.

---

## 2. Total Goals: 12 (2.00 g/m) — TOO LOW

This is the biggest problem. The model says 15.6 goals. You pick 12. That's a **23% deviation** — breaking your own stated rule of "don't deviate >20% without good reason."

Historical context:
- WC group stage average: ~2.67 g/m (~16 goals/group)
- 2.00 g/m would be among the **lowest-scoring groups in modern WC history**
- Even the most defensive WC groups (2006 Group H, 2010 Group A) averaged ~2.2-2.3 g/m
- Three defensive teams doesn't mean no goals — it means tight games that often produce 1-1s and 2-1s, not 1-0s and 0-0s

The "all three teams are defensive" narrative is overfit. Egypt scored 20 in qualifying. Belgium scored 27. Even Iran scored ~17. These teams score goals.

**Recommendation:** Adjust to 14-15 goals. Easiest fixes: Belgium-Iran 2-1 (+1), Egypt-Iran 1-1 (+1), one of the NZ matches gets a goal (+1).

---

## 3. Draw Count: 1 of 6 (17%)

One draw is low but defensible on its own. However, the paradox: you describe this as a group "defined by defensive quality" with three defensive teams, yet predict **fewer draws than the base rate**. Defensive teams produce draws. The logic contradicts the outcome.

With Egypt's low block, Iran's compact frustration tactics, and Belgium's Garcia-era caution, I'd expect **2 draws**, not 1. Belgium-Iran (model modal 1-1) or Egypt-Iran (model modal 1-1) are prime draw candidates.

**Recommendation:** Make Egypt-Iran 1-1 (second draw). This is more coherent with the defensive narrative AND fixes the goals problem.

---

## 4. Group Story Plausibility

BEL 7pts, EGY 7pts, IRN 3pts, NZL 0pts — **plausible but too clean.**

Concerns:
- **NZ on 0 points** ignores the 2010 precedent you yourself cite. NZ drew Italy, Slovakia, and Paraguay — three better teams than Iran. If Wood is fit, Iran-NZ could easily be 1-1. Iran's domestic league suspension and Azmoun's absence are real handicaps.
- **Egypt matching Belgium point-for-point** is bold. Markets give Belgium 75% vs Egypt 16% for the group win. Your picks have them level on points separated only by GD. This implies Egypt are near-Belgium level, which contradicts the market view.
- If you give NZ a draw vs Iran (1-1), Iran drops to 1 point and the group becomes more interesting — BEL 7, EGY 7, IRN 1, NZL 1. That's actually more coherent with the quality gap.

---

## 5. Model Divergences

Every single divergence from the model pushes goals **downward**:

| Match | Model total | Pick total | Direction |
|-------|-------------|------------|-----------|
| Belgium vs Iran | 2.58 | 2 | ↓ |
| Egypt vs Iran | 2.59 | 1 | ↓↓ |
| NZ vs Egypt | 2.60 | 2 | ↓ |

No match is adjusted upward. This is a systematic bias toward low-scoring outcomes, not a considered match-by-match judgment. If you believe the model is well-calibrated (you built it for this purpose), systematically overriding it in one direction is a red flag.

---

## 6. Key Risks & Blindspots

1. **Research integrity:** The research file researched the wrong group. Any Egypt/Iran/NZ data in the picks came from somewhere undocumented. Fix this first.

2. **Iran withdrawal:** If Iran drops out, the entire group restructures. Have a contingency plan.

3. **Chris Wood:** Described as THE question for NZ, but then the picks assume he's basically absent (NZ score 1 goal total in 3 games). If Wood is fit — he scored 20 PL goals last season — NZ's ceiling rises significantly. If he's not, 1 goal in 3 games might even be generous. The binary outcome matters.

4. **Egypt's offensive ceiling:** Salah at "only" 5G/6A in PL this season is still elite-level output. Marmoush adapting at City is a short-term concern. But the picks give Egypt only 4 goals in 3 games — Salah alone could produce that. Egypt scored 4-0 vs Saudi Arabia in March.

5. **Belgium's injury cascade:** The analysis mentions injuries extensively but doesn't fully price them in. If Courtois, Lukaku, Trossard, and De Bruyne are all compromised, Belgium's 7 points looks generous. The 2-0 vs Iran and 0-2 vs NZ require attacking depth that may not be available.

---

## Recommended v2 Picks

| Match | v1 | Recommended v2 | Change Reason |
|-------|-----|----------------|---------------|
| Belgium vs Egypt | 1-1 | **1-1** | Keep |
| Iran vs New Zealand | 2-1 | **1-1** | NZ earn a point; Iran without Azmoun lack the 2nd goal; Wood set-piece threat |
| Belgium vs Iran | 2-0 | **2-1** | Iran score via Taremi — he scores everywhere, always |
| NZ vs Egypt | 0-2 | **0-2** | Keep |
| Egypt vs Iran | 1-0 | **1-1** | Model modal. Both defensive = draw. Iran forced forward ≠ fewer goals |
| NZ vs Belgium | 0-2 | **0-2** | Keep |

**v2 totals:** 15 goals (2.50 g/m) — much closer to model (15.6) and historical average (16)
**Draws:** 3 of 6 (50%) — high, but coherent with "group defined by defensive quality"
**Standings:** BEL 7, EGY 5, IRN 2, NZL 1

Actually, 3 draws might be too many. Alternative: keep Iran-NZ at 2-1 but change Egypt-Iran to 1-1.

**Alternative v2:** 1-1, 2-1, 2-1, 0-2, 1-1, 0-2 = 14 goals (2.33 g/m), 2 draws (33%)
**Standings:** BEL 7, EGY 5, IRN 4, NZL 0

This is more interesting — Iran stay alive going into MD3, making the Egypt-Iran draw more dramatic (both teams happy with a point if Belgium are already through).

---

## Summary

The picks tell a coherent story but are **systematically too low on goals** (12 vs model 15.6, 23% deviation). The defensive narrative is overfit — defensive teams still score, and forced-attacking context (Iran MD3) opens games up. The research file is about the wrong group entirely and needs to be redone. Fix the goals shortfall by giving Iran a goal vs Belgium (2-1) and making Egypt-Iran 1-1.
