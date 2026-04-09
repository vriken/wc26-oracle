# Second Opinion Request

## Question
# Review Request — Group C Scoreline Predictions

## Question
Review our v1 scoreline predictions for 2026 World Cup Group C (Brazil, Morocco, Scotland, Haiti). Are the scorelines plausible? Is the total too high or too low? Any blindspots?

## Context

### Files to Review
@groups/group-c.md
@predict_group_c.py
@research/group-c-research.md
@model.py

## Instructions
Focus on architecture, tradeoffs, blast radius, and security implications. Evaluate alternatives and recommend one approach with conviction. Be opinionated — don't hedge.

Specifically evaluate:
1. **Individual scorelines** — is each pick the right call given the matchup?
2. **Group total** — 16 goals (2.67 g/m). Too high? Too low? WC average is ~2.67
3. **Draw count** — 1 draw in 6 matches (17%). WC group base rate is ~25%. Should we add another?
4. **Group story** — do the standings (BRA 7, MOR 7, SCO 3, HAI 0) make sense?
5. **Model divergences** — we diverge from the model modal in 5 of 6 matches. Are these justified?
6. **Key risks** — Rodrygo OUT, Morocco coaching change, Scotland GK crisis, Haiti debutants
7. **1998 parallel** — Brazil, Morocco, Scotland were in same group in 1998. Are we over-indexing on this?

### Our v1 Picks
| Match | Pick | Model Modal |
|-------|------|-------------|
| Brazil vs Morocco | 1-1 | 1-1 |
| Haiti vs Scotland | 1-2 | 0-1 |
| Scotland vs Morocco | 0-2 | 0-1 |
| Brazil vs Haiti | 3-0 | 2-0 |
| Scotland vs Brazil | 0-2 | 1-1 |
| Morocco vs Haiti | 3-1 | 2-0 |

### Key Data Points
- Brazil: Rodrygo ACL OUT, worst qualifying ever, Ancelotti <1 year
- Morocco: 2022 SF, AFCON champs, perfect 8/8 qualifying, new coach Ouahbi (3 months)
- Scotland: first WC since 1998, McTominay career-best, GK Gunn barely playing
- Haiti: debutants, €38M squad, Nazon 44 goals

### Market Odds
- Polymarket group winner: BRA 77%, MOR 20%, SCO 3.6%, HAI 0.4%
- Brazil vs Morocco: Brazil 3/5, Draw 3/1, Morocco 5/1
- Haiti vs Scotland: Scotland 4/9, Draw 7/4, Haiti 7/1

## Instructions
You are providing an independent second opinion. Be critical and thorough.
- Analyze the question in the context provided
- Identify risks, tradeoffs, and blind spots
- Suggest alternatives if you see better approaches
- Be direct and opinionated — don't hedge
- Structure your response with clear headings
- Keep your response focused and actionable
