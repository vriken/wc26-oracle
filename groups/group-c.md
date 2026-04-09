# Group C — Match-by-Match Goal Predictions

## Teams

| Team | FIFA Rank | Qualification Path | Style |
|------|-----------|-------------------|-------|
| Brazil | 6th | CONMEBOL 5th (W8 D4 L6, worst ever) | 4-3-3, Ancelotti — control over spectacle, elite wide forwards |
| Morocco | 8th | CAF 1st (W8 D0 L0, perfect record) | 4-2-3-1 (Ouahbi), compact defense, explosive transitions, Hakimi as game-changer |
| Scotland | 43rd | UEFA Group C 1st (W4 D1 L1) | 3-5-2, Mourinho school — deep block, set pieces, counter-attack |
| Haiti | 83rd | CONCACAF Group C 1st (W3 D2 L1) | 4-2-3-1, park the bus, transition moments, diaspora squad |

## Market Odds (as of 2026-04-09)

### Group Winner

| Source | Brazil | Morocco | Scotland | Haiti |
|--------|--------|---------|----------|-------|
| Polymarket | 77% | 20% | ~3.6% | ~0.4% |
| FanDuel | -290 (74%) | +450 (18%) | +700 (13%) | +10000 (1%) |

### Match Odds

| Match | Source | Favorite | Draw | Underdog |
|-------|--------|----------|------|----------|
| Brazil vs Morocco | Oddschecker | Brazil 3/5 | 3/1 | Morocco 5/1 |
| Haiti vs Scotland | Oddschecker | Scotland 4/9 | 7/4 | Haiti 7/1 |
| Scotland vs Morocco | Oddschecker | Morocco ~evens | ~5/2 | Scotland ~3/1 |

---

## Team Form Deep Dive

### Brazil
- **Recent form:** W6 D2 L4 in last 12. Mixed — 5-0 South Korea, 3-1 Croatia, but 4-1 loss to Argentina, 2-1 loss to France
- **Qualifying:** Worst CONMEBOL campaign in history. 5th of 10, level on points with 3 other teams
- **Manager:** Carlo Ancelotti (appointed Jan 2025). Less than a year to build chemistry. Control-first approach
- **CRITICAL injuries:**
  - Rodrygo: **OUT** (ACL + meniscus tear, Mar 2, surgery, 10-month recovery)
  - Vanderson: **OUT** (hamstring surgery, ~3 months — ruled out of WC). Wesley (Roma) frontrunner at RB
  - Raphinha: hamstring injury Mar 26, ruled out until May. Racing for squad deadline May 18
  - Bruno Guimarães: thigh injury since Feb, return late April
  - Estevão: muscular injury, 6 consecutive Chelsea matches missed
  - Militão: out at Real Madrid since December
  - Alisson: thigh issue, withdrew from March squad
- **Key players:** Vinícius Jr (16G/12A all comps), Raphinha (11G/3A La Liga), Marquinhos (103 caps)
- **No. 9 race:** Igor Thiago (Brentford, **18G PL** — leads the race), Endrick (Lyon loan, 6G/5A in 14 apps, Ligue 1 POTM), Richarlison (Spurs, 9G/3A), Cunha (Man Utd, 7G/2A)
- **Neymar:** Unlikely to make squad. Only 5 apps in 17 Santos matches

### Morocco
- **Recent form:** W10 D2 L0 in last 12 competitive. World record 19 consecutive wins before Mali draw
- **2025 AFCON champions** (awarded title after Senegal walkoff controversy)
- **Qualifying:** Perfect 8/8, 22 GF / 2 GA — elite defensive record
- **Coaching change:** Regragui resigned after AFCON → Ouahbi (promoted from U-20, won U-20 WC). Runs **4-2-3-1** (slightly more conservative). Assistant: Joao Sacramento (ex-Mourinho). Only 3 months before WC. Biggest wildcard
- **Key players:** Hakimi (5G/10A all comps, PSG UCL champion — scored in UCL final), Brahim Díaz (Real Madrid), El Khannouss (Stuttgart), Bounou (veteran GK)
- **Injuries/absences:** Amrabat surgery (racing), Ziyech **OUT** (hamstring at Wydad AC), El Kaabi **OUT** (excluded from recent squads), Aguerd recovered, Saïss muscle issue
- **Squad value:** ~€456M, almost entirely Europe-based

### Scotland
- **Recent form:** W4 D1 L3 in last 8. Strong qualifying but lost both March friendlies 0-1 (Japan, Ivory Coast)
- **Qualifying:** Topped UEFA Group C ahead of Denmark and Greece. Beat Denmark 4-2 in decisive match (McTominay overhead kick)
- **Manager:** Steve Clarke (since 2019, 74+ games). Mourinho school — defensive discipline, set pieces
- **Key players:** McTominay (7G/3A Serie A, champion with Napoli), Robertson (Liverpool captain, 92 caps), McGinn (Villa, set pieces)
- **GK crisis:** Gunn only played 45 min at Forest this season. Craig Gordon 43yo and injured
- **Injuries:** Hickey (RWB, unspecified), Hanley (last played Feb), Nathan Patterson (barely featuring)
- **First WC since 1998.** Never advanced past a WC group stage in history

### Haiti
- **Recent form:** W3 D3 L2 in last 8. Qualified but friendlies showed gap (0-1 Tunisia, 1-1 Iceland)
- **First WC appearance since 1974** (52-year drought). Only Caribbean nation to qualify twice
- **ALL qualifying matches at neutral venues** due to Haiti's security crisis — no home advantage ever
- **Key players:** Nazon (44 goals/74 caps, 100% penalty conversion 9/9), Pierrot (33 goals), Bellegarde (Wolves, PL)
- **Squad value:** ~€38M (lowest in group by far). Average age 27.7
- **Realistic level:** CONCACAF mid-tier (Honduras/Costa Rica equivalent). Ceiling is a draw vs Scotland

---

## Model Output (Bayesian Market-First)

| Match | λ_A | λ_B | Modal | E[total] | 80% CI |
|-------|-----|-----|-------|----------|--------|
| Brazil vs Morocco | 1.13 | 1.25 | 1-1 | 2.37 | 1-4 |
| Haiti vs Scotland | 0.84 | 1.61 | 0-1 | 2.45 | 1-5 |
| Scotland vs Morocco | 0.99 | 1.41 | 0-1 | 2.40 | 1-4 |
| Brazil vs Haiti | 2.17 | 0.84 | 2-0 | 3.01 | 1-5 |
| Scotland vs Brazil | 1.08 | 1.55 | 1-1 | 2.63 | 1-5 |
| Morocco vs Haiti | 2.22 | 0.82 | 2-0 | 3.04 | 1-5 |

Model total: 15.9 goals (2.65 g/m)

---

## Match-by-Match Predictions (v1)

### Match 1: Brazil vs Morocco — Sat Jun 13, MetLife Stadium (East Rutherford NJ)

**Pick: 1-1**

| Factor | Assessment |
|--------|-----------|
| Model | λ(BRA)=1.13, λ(MOR)=1.25 → modal 1-1 (13.1%) |
| Market | Brazil 3/5 fav, draw 3/1 |
| Context | Group opener, both cautious. 1998 replay. Ancelotti vs new coach |
| Key | Morocco's defense (2 GA in 8 qualifiers) vs Brazil's Vinícius. Rodrygo absence hurts width |
| Manual adj | -0.05 Brazil (injury crisis) |

Brazil have the individual talent to win but Morocco's defensive organization is elite (2022 semi-final pedigree, 2 GA in qualifying). Both teams will be cautious in the opener. Ancelotti's control-first approach meets Ouahbi's inherited defensive structure. The draw is the second most-backed outcome in betting markets. Model agrees: 1-1 at 13.1%.

**1998 parallel:** Brazil beat Morocco 3-0 in 1998. But that was a different Brazil — Ronaldo, Rivaldo, Roberto Carlos. This Brazil is more vulnerable.

### Match 2: Haiti vs Scotland — Sat Jun 13, Gillette Stadium (Foxborough MA)

**Pick: 1-2**

| Factor | Assessment |
|--------|-----------|
| Model | λ(HAI)=0.84, λ(SCO)=1.61 → modal 0-1 (13.9%), 1-2 at 9.4% |
| Market | Scotland 4/9 fav, Haiti double chance +185 |
| Context | Scotland's crucial match — must win to have any hope of progressing |
| Key | McTominay's quality vs Haiti's disciplined low block. Set pieces likely decisive |

We deviate from the model modal (0-1) because: Scotland will press for a comfortable win knowing they face Morocco and Brazil next. Haiti will score — they have Nazon (44 intl goals) and scored in most qualifiers. The +185 double chance line suggests bookmakers give Haiti real upset potential. A 1-2 is more realistic than a clean sheet given Scotland's GK crisis (Gunn barely playing).

### Match 3: Scotland vs Morocco — Fri Jun 19, Gillette Stadium (Foxborough MA)

**Pick: 0-2**

| Factor | Assessment |
|--------|-----------|
| Model | λ(SCO)=0.99, λ(MOR)=1.41 → modal 0-1 (12.8%), 0-2 at 9.0% |
| Market | Morocco ~evens fav |
| Context | Morocco's transition game vs Scotland's deep block. Hakimi's pace is the difference |
| Key | 1998 parallel: Morocco 3-0 Scotland. Morocco's quality should tell here |

Scotland will sit deep and make it ugly, but Morocco's transition quality (Hakimi 5G/10A from RB) will eventually break through. Clarke will try to replicate the 0-0 draw at Denmark, but Morocco are significantly more dangerous in transition than Denmark. We go 0-2 rather than 0-1 because Morocco typically add a late goal against compact defenses that tire.

### Match 4: Brazil vs Haiti — Fri Jun 19, Lincoln Financial Field (Philadelphia PA)

**Pick: 3-0**

| Factor | Assessment |
|--------|-----------|
| Model | λ(BRA)=2.17, λ(HAI)=0.84 → modal 2-0 (11.6%), 3-0 at 8.4% |
| Market | Brazil heavy favorite |
| Context | Biggest mismatch. Brazil need a convincing win for GD after likely drawing Morocco |
| Key | Vinícius vs €38M squad. Haiti will park the bus but quality gap is enormous |

We go above the model modal because Brazil will be desperate for goals, especially if they drew Morocco on MD1. The quality gap (€800M+ vs €38M) is massive. Haiti's defensive discipline will hold for a half, but Brazil's bench depth alone outmatches Haiti's starting XI. Ancelotti will be ruthless. 3-0 is the floor — 4-0 or 5-0 are in play.

### Match 5: Scotland vs Brazil — Wed Jun 24, Hard Rock Stadium (Miami FL)

**Pick: 1-2** *(v1: 0-2 → v2: 1-1 → v3: 1-2 — user override)*

| Factor | Assessment |
|--------|-----------|
| Model | λ(SCO)=1.08, λ(BRA)=1.55 → modal 1-1 (12.1%) |
| Market | Brazil heavy favorite, draw ~19-21% implied |
| Context | Miami heat (30°C+), but heat adjustment already in model (-0.03) |
| Key | McTominay (7G/3A Serie A, 4G/1A UCL) is a genuine goal threat from midfield |

**v3 rationale:** Brazil win respects market (55% implied) and their motivation to top the group for a better R32 draw. Scotland still score via McTominay — model expects λ(SCO)=1.08, and he scores against anyone (4G/1A UCL). Brazil's injury crisis (7 absences inc. Vanderson) limits their ceiling but Igor Thiago (18 PL goals) gives them a real No. 9. Compromise between draw (too optimistic for Scotland) and shutout (contradicts model).

### Match 6: Morocco vs Haiti — Wed Jun 24, Mercedes-Benz Stadium (Atlanta GA, indoor)

**Pick: 3-1**

| Factor | Assessment |
|--------|-----------|
| Model | λ(MOR)=2.22, λ(HAI)=0.82 → modal 2-0 (11.8%), 3-1 at ~5% |
| Market | Morocco heavy favorite |
| Context | Morocco need goals for GD tiebreaker vs Brazil. Indoor venue (no weather factor) |
| Key | If group is decided on GD (both on 7 pts), Morocco will push for maximum goals |

We go above the model because: Morocco will likely need goal difference to beat Brazil to the group title. Indoor venue removes any weather factor. Haiti will be playing for pride in their likely final match. Nazon scores a consolation (he always does — 44 intl goals). Morocco's quality tells: Hakimi, Brahim, El Khannouss vs a tired Haiti.

---

## Group C Summary (v3 — FINAL)

| Match | v1 | v2 | v3 | Goals | Change |
|-------|----|----|-----|-------|--------|
| Brazil vs Morocco | 1-1 | 1-1 | 1-1 | 2 | — |
| Haiti vs Scotland | 1-2 | 1-2 | 1-2 | 3 | — |
| Scotland vs Morocco | 0-2 | 0-2 | 0-2 | 2 | — |
| Brazil vs Haiti | 3-0 | 3-0 | 3-0 | 3 | — |
| Scotland vs Brazil | 0-2 | 1-1 | **1-2** | 3 | v3: Brazil win, Scotland score (market + model compromise) |
| Morocco vs Haiti | 3-1 | 3-1 | 3-1 | 4 | — |
| **Total** | **16** | **16** | **17** | | +1 from SCO-BRA |

**Goals:** 17 total (2.83 g/m) — slightly above WC average, justified by Igor Thiago emergence

**Draws:** 1 of 6 (17%) — below 25% base rate but the only natural draw (BRA-MOR opener) is well-justified

### Predicted Standings

| Pos | Team | W | D | L | GF | GA | GD | Pts |
|-----|------|---|---|---|----|----|-----|-----|
| 1 | Morocco | 2 | 1 | 0 | 6 | 2 | +4 | 7 |
| 2 | Brazil | 2 | 1 | 0 | 6 | 2 | +4 | 7 |
| 3 | Scotland | 1 | 0 | 2 | 3 | 5 | -2 | 3 |
| 4 | Haiti | 0 | 0 | 3 | 2 | 8 | -6 | 0 |

**Morocco tops the group on head-to-head** — both on 7pts, +4 GD, but Morocco beat Scotland 2-0 while Brazil beat Scotland 2-1. H2H between BRA-MOR is 1-1 draw. Next tiebreaker: GA — both have 2. Then GF — both have 6. Then fair play / drawing of lots. Morocco likely edges it on disciplinary record (fewer cards historically).

**Brazil qualifies in 2nd** — injury crisis (Rodrygo + Vanderson OUT) costs them top spot despite winning 2 of 3. Consistent with market (77% group winner) but Morocco's defensive superiority tells.

**Scotland on 3 points** — McTominay scores vs Brazil but it's not enough. Classic Scotland: competitive but eliminated at the group stage. First WC since 1998, same outcome.

**Haiti finish last** but score 2 goals — respectable for debutants.

### Group Story
The 1998 replay delivers a similar narrative: Brazil and Morocco dominate, Scotland fight but fall short, the weakest team (Haiti replacing Norway) provides moments but can't compete. Morocco and Brazil finish level on 7 points — separated only by tiebreakers. The key difference from 1998 is Morocco is far stronger in 2026 — AFCON champions, perfect qualifying, Hakimi era — while Brazil's injury crisis (7 key absences) makes them more vulnerable than any Brazilian WC squad in memory.

---

## Revision Triggers

- [ ] Raphinha, Bruno Guimarães, Estevão fitness updates (May squad announcement, deadline May 18)
- [ ] Amrabat surgery recovery timeline
- [ ] Igor Thiago form/minutes at Brentford (if starting No. 9, Brazil vs Haiti ceiling rises)
- [ ] Vanderson recovery confirmation (should remain OUT)
- [ ] Ziyech fitness for WC squad (Ouahbi's May decision)
- [ ] Endrick continued form at Lyon
- [ ] Scotland GK resolution (Gunn game time at Forest)
- [ ] MD1 results → adjust MD2/MD3 picks
- [ ] Market odds movement (Brazil -290 → check if Morocco narrows)

---

## Sources

- Polymarket Group C Winner (accessed Apr 9, 2026)
- FanDuel, Oddschecker, DraftKings match odds (accessed Apr 9, 2026)
- FIFA Match Schedule, Team Profiles
- RotoWire Group C Preview (AI simulations)
- FotMob, FBref, Transfermarkt (player stats)
- ESPN, BBC Sport, L'Équipe, GE.globo (team news)
- 1998 World Cup records (11v11.com, thesoccerworldcups.com)

---

*Version: v3 (2026-04-09) — Data-enriched review complete. Picks confirmed, research updated (Vanderson OUT, Igor Thiago 18PL, Ziyech/El Kaabi OUT, Ouahbi 4-2-3-1)*
