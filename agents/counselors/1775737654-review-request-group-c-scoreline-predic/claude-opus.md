# Second Opinion — Group C Scoreline Predictions

## Verdict

The picks are solid overall. The group story is coherent, the total is calibrated, and most divergences are justified. **One pick is wrong: Scotland vs Brazil should be 1-1, not 0-2.** Everything else I'd leave alone or adjust at the margins.

---

## 1. Individual Scorelines

| Match | Pick | My Take |
|-------|------|---------|
| Brazil vs Morocco 1-1 | **Agree** | Model modal, market-supported, opener caution. Clean pick. |
| Haiti vs Scotland 1-2 | **Agree** | Nazon is a real goal threat (44 intl goals, 9/9 pens). Gunn's rust raises the floor for Haiti. +185 double chance line validates this. |
| Scotland vs Morocco 0-2 | **Agree** | Morocco's transition quality is a level above anything Scotland faced in qualifying. Hakimi will feast on tired wing-backs. Late second goal is the archetype for this matchup. |
| Brazil vs Haiti 3-0 | **Agree** | €800M vs €38M. Brazil needing GD after a draw. Ancelotti won't show mercy. 3-0 is the floor, as you note. |
| Scotland vs Brazil 0-2 | **Disagree — change to 1-1** | See below. |
| Morocco vs Haiti 3-1 | **Lean disagree — consider 2-1** | 3-1 is at ~5% model probability. That's aggressive. See below. |

### Scotland vs Brazil: The Big Miss

This is the most questionable pick. The model says 1-1 (12.1%), you pick 0-2 (8.7%). Your rationale is heat, history, and fatigue, but:

- **λ(SCO) = 1.08.** The model expects Scotland to score ~1 goal. Shutting them out contradicts your own model.
- **McTominay exists.** 7G/3A in Serie A, overhead kick vs Denmark, 4G/1A in UCL. He's a goal threat from midfield against anyone. Scotland scoring 0 while he's on the pitch is inconsistent.
- **The heat adjustment is already baked in** (-0.03 manual_adj_a). You're double-counting by citing heat again in the qualitative layer.
- **Scotland scored vs Brazil in 1998** (John Collins penalty). They'll get chances from set pieces. Robertson's delivery + McTominay's aerial threat = at least one good opportunity.
- **Brazil's incentives may be mixed.** If they're on 4 points after MD2, a draw guarantees qualification. Ancelotti is a pragmatist — he might manage the match rather than go all-out, especially with a R32 match 4 days later.
- **0 goals in 2 of 3 matches for Scotland is harsh.** They scored 11 in 6 qualifiers and have genuine Premier League/Serie A quality in attack.

**Recommendation: 1-1.** This matches the model modal, adds a needed second draw, and creates a more interesting (and plausible) group outcome where Morocco tops on 7 pts vs Brazil's 5.

### Morocco vs Haiti: Slightly Overcooked

3-1 is at ~5% model probability — the lowest-probability pick in the group. The GD narrative is compelling, but:

- Morocco's system doesn't produce blowouts. Their qualifying results against comparable opponents: Tanzania 2-0, Zambia 2-1. They win controlled, not emphatic.
- Giving Haiti a goal here AND vs Scotland (2 total) is right for the narrative, but 2-1 achieves the same thing with higher model backing.

That said, if you change Match 5 to 1-1 (dropping total to 15), keeping 3-1 here preserves the total at a reasonable level. So this is a conditional recommendation: **if you change Match 5, keep Match 6. If you keep Match 5, downgrade Match 6 to 2-1.**

---

## 2. Group Total: 16 Goals (2.67 g/m)

Right on WC average. Model says 15.9. No issue here.

If you take my Match 5 recommendation (1-1 instead of 0-2), total drops to 15 (2.50 g/m) — slightly below average but within normal range. The 2026 expanded format and new restart rules (your RULE_UPLIFT_2026 = 0.04) may push actuals slightly higher, so 15-16 is the sweet spot.

---

## 3. Draw Count: 1 of 6 (17%)

**Too low.** WC group base rate is ~25% (1.5 draws per group). Having only 1 draw in a group with two evenly-matched top teams AND a disciplined defensive side (Scotland) is suspicious.

Changing Match 5 to 1-1 gives 2 draws (33%) — slightly above average but much more plausible given that both top-2 teams play defensive/transition styles.

---

## 4. Group Story

Current standings (BRA 7, MOR 7, SCO 3, HAI 0) are clean but potentially too neat. Both top teams on 7 with GD as the separator is elegant but rare.

With my recommended change (Match 5 → 1-1):

| Pos | Team | W | D | L | GF | GA | GD | Pts |
|-----|------|---|---|---|----|----|-----|-----|
| 1 | **Morocco** | 2 | 1 | 0 | 6 | 2 | +4 | **7** |
| 2 | **Brazil** | 1 | 2 | 0 | 5 | 2 | +3 | **5** |
| 3 | Scotland | 1 | 1 | 1 | 3 | 4 | -1 | **4** |
| 4 | Haiti | 0 | 0 | 3 | 2 | 8 | -6 | **0** |

This story is **better**:
- Morocco tops — justified by AFCON title, perfect qualifying, 8th in the world. The +450 group winner odds suggest the market sees this path.
- Brazil qualifies comfortably in 2nd but their injury crisis costs them the top spot. Consistent with "worst qualifying ever" narrative.
- Scotland on 4 points with a genuine shot at best-3rd qualification — more dramatic and realistic than a clean elimination on 3 pts.
- Haiti still finish last but score 2 goals — respectable debutants.

---

## 5. Model Divergences

5 of 6 divergences is a lot. Each individual one might be defensible, but collectively they imply you think the model is systematically wrong. Check whether that's intentional.

The pattern: 4 of 5 divergences go toward **more goals** for the stronger team. This suggests a bias toward narrative-driven blowouts over the model's regression to the mean. The model's mean-reverting tendency exists for a reason — WC group matches are often cagier than expected.

**Justified divergences:** Haiti-Scotland (1-2 vs 0-1), Brazil-Haiti (3-0 vs 2-0). These have clear qualitative reasons.

**Marginal divergences:** Scotland-Morocco (0-2 vs 0-1). Fine but could go either way.

**Unjustified:** Scotland-Brazil (0-2 vs 1-1). Change this.

---

## 6. Key Risks

| Risk | Assessment |
|------|-----------|
| **Rodrygo OUT** | Adequately priced in (-0.05 adj). If anything, losing Rodrygo hurts Brazil's tactical flexibility more than raw attack — Ancelotti had Viní-Rodrygo-Raphinha as an interchangeable trident. Now the right side is weaker. |
| **Morocco coaching change** | **Under-weighted.** Ouahbi has 3 months and zero senior competitive matches before the WC opener vs Brazil. The defensive structure is inherited, but in-match tactical adjustments are where a new coach struggles most. If Brazil go 1-0 up, can Ouahbi change the game? This is the biggest unknown in the group. |
| **Scotland GK crisis** | Properly reflected — you've given Scotland 0 goals conceded in only 1 of 3 matches. But consider: if Gunn makes a mistake vs Haiti, your entire group story collapses. Scotland losing or drawing Haiti is the catastrophic scenario for your standings. |
| **Haiti debutants** | WC debutant syndrome cuts both ways. Saudi Arabia lost 0-5 to Russia in the 2018 opener, then beat Argentina 2-1 in 2022. Haiti's ceiling is higher than 0 points — a draw vs Scotland is genuinely possible (the market prices it). Your picks already account for this by giving Haiti a goal in 2 of 3 matches. |

**Blindspot: Brazil's No. 9 problem.** With Rodrygo out AND no settled striker (Endrick? Cunha? Igor Thiago?), Brazil might struggle to convert against a well-organized Haiti low block. 3-0 assumes Brazil break through easily — what if Haiti's discipline holds and it's a nervy 1-0 until the 70th minute? The λ(BRA)=2.17 might be generous given the striker question.

---

## 7. 1998 Parallel

**You're not over-indexing.** The structural similarity (BRA+MOR advance, SCO eliminated) is supported by current form and market odds, not nostalgia. You already diverge from 1998 on the key match (BRA 1-1 MOR vs BRA 3-0 MOR in 1998). The 1998 parallel is useful context, not a prediction driver. Fine.

---

## Summary Recommendations

| # | Action | Impact |
|---|--------|--------|
| 1 | **Change Scotland vs Brazil from 0-2 to 1-1** | Adds needed draw, matches model modal, fixes Scotland scoring inconsistency, creates stronger group story |
| 2 | Keep Morocco vs Haiti at 3-1 (compensates for total drop) | Maintains 15-goal total (2.50 g/m), keeps Haiti scoring narrative |
| 3 | Monitor Morocco coaching situation closely | Ouahbi's first competitive match is vs Brazil — this is the group's biggest wildcard |
| 4 | Flag Brazil's No. 9 problem as a revision trigger | If no striker emerges by squad announcement, consider downgrading Brazil vs Haiti to 2-0 |
