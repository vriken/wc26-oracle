# Group G — Match-by-Match Goal Predictions

## Teams

| Team | FIFA Rank | Qualification Path | Style |
|------|-----------|-------------------|-------|
| Belgium | 9th | UEFA Group J 1st (W5 D2 L0, 27GF/7GA) | 4-3-3, Rudi Garcia — technical control, quick wide play, Doku 1v1 threat |
| Egypt | 29th | CAF Group A 1st (W8 D2 L0, 20GF/2GA) | 4-4-1-1, compact low block, rapid transitions, Salah decides tight games |
| Iran | 21st | AFC Group A 1st (W7 D2 L1, ~17GF/~8GA) | 4-2-3-1, organized defense, frustrate + counter, Taremi isolated target |
| New Zealand | 85th | OFC champions (W7 D0 L0, 29GF/1GA) | 4-2-3-1, physical discipline, set-piece threat, nothing to lose |

## Market Odds (as of 2026-04-09)

### Group Winner

| Source | Belgium | Egypt | Iran | New Zealand |
|--------|---------|-------|------|-------------|
| Polymarket | 70% | 21% | 10% | ~4% |
| FanDuel | -220 (69%) | +390 (20%) | +700 (13%) | +1900 (5%) |
| BetMGM | -225 | +333 | +550 | -- |

### Key Narrative

Iran's participation remains uncertain due to US-Iran armed conflict. All Iran matches are in the US (Seattle, LA). FIFA rejected relocation to Mexico. Ceasefire announced; final decision expected by end of April 2026.

---

## Team Form Deep Dive

### Belgium
- **Recent form:** 9-match unbeaten streak. W5 D2 L0 qualifying. Beat USA 5-2 and drew Mexico 1-1 in March friendlies
- **Qualifying:** Topped UEFA Group J. De Bruyne (6G), Doku (5G), Tielemans (3G) in qualifying
- **Manager:** Rudi Garcia (first international role, appointed Jan 2025). Flexible 4-3-3 / 4-2-3-1
- **CRITICAL injuries:**
  - De Bruyne: hamstring Oct 2025, returned Mar 6 as sub. Played ~30 min vs USA. **Fit but fragile at 35 in June**
  - Lukaku: thigh tear late 2025, recovered. Skipped March by choice. **64 minutes across 5 sub appearances all season at Napoli. Only 1 goal (stoppage-time winner at Verona). Second injury (iliopsoas inflammation). Disciplinary issue with Napoli. Hojlund has taken his starting spot. WC fitness genuine concern**
  - Courtois: withdrew from March squad (unspecified)
  - Trossard: ruled out of March squad (injured)
  - Onana: left March camp injured
- **Key players:** De Bruyne (Napoli, 4G in 800 min, FotMob 7.23), Doku (Man City, 1G/4A PL, 5G qualifying), Tielemans (Villa, captain)
- **Generational transition:** Kompany, Vertonghen, Alderweireld all retired. Theate, De Winter, Mechele as replacements — significant defensive downgrade

### Egypt
- **Recent form:** W8 D2 L0 qualifying (unbeaten). AFCON 2025: 4th place (beat Cote d'Ivoire 3-2 in QF, lost semis to Senegal, lost 3rd place to Nigeria on pens)
- **March friendlies:** 4-0 Saudi Arabia, 0-0 Spain — drew with a top-5 team
- **Qualifying:** Only 2 GA in 10 matches. Salah scored 9 qualifying goals (all-time CAF WC qualifying record: 20)
- **Manager:** Hossam Hassan (Egypt's all-time top scorer as player). Compact defensive shape, relies on Salah/Marmoush star quality
- **Key players:** Salah (Liverpool, 5G/6A PL — down from 28G/18A last season. Announced Liverpool departure March 24. Shot accuracy dropped 58%→42%, conversion 25%→14%), Marmoush (Man City, 1G/3A, adapting), El Shenawy (Al Ahly GK), Trezeguet (5 qualifying goals)
- **No major injuries:** Squad largely fit. The 0-0 draw with Spain in March is an encouraging defensive benchmark

### Iran
- **Recent form:** Beat Costa Rica 5-0 but lost to Nigeria 1-2 in March (both in Antalya). Qualified on MD8
- **Qualifying:** Topped AFC Group A, 8 points clear of 3rd place. Lost only to Qatar away
- **Manager:** Ghalenoei (most successful Iranian club coach). Formation questions — used 5-4-1 vs Nigeria with Taremi isolated
- **Key players:** Taremi (Olympiacos, 10G/2A in Greek Super League ~1,075 min, plus 2G/2A in Champions League. FotMob 7.5. Top 99th percentile npxG. On fire), Beiranvand (experienced GK), Ezatolahi (defensive anchor)
- **CRITICAL concerns:**
  - Azmoun: expelled at 'highest level of government.' Iran judiciary threatened asset seizure. Permanent exclusion confirmed. **Key attacking partner for Taremi — his absence is massive**
  - Domestic league suspended — most squad players lack competitive match fitness
  - Geopolitical uncertainty — may withdraw from tournament entirely. FIFA's Infantino met Iranian federation in Antalya. Ceasefire 'incredibly precarious'
- **Tournament pedigree:** 7th World Cup. Best results: 1 win each in 1998, 2018, 2022 group stages

### New Zealand
- **Recent form:** W2 D1 L6 vs non-OFC opposition since qualifying. Beat Chile 4-1 (red card advantage, without Wood) but lost to Finland 0-2, Ecuador 0-2, Colombia 1-2
- **Qualifying:** Perfect OFC run (W7, 29GF/1GA). Wood scored 9 of 29 goals
- **Manager:** Darren Bazeley (climbed 18+ FIFA ranking places). Physical, organized, set-piece quality
- **Key players:** Chris Wood (Forest, 20G in 35-36 PL last season — returned to Nottingham Forest first-team training April 8, available for Europa League QF vs Porto. Scored for U21s. Recovery ahead of schedule)
- **Other options:** Ben Waine (scored vs Chile), Elijah Just (young, pacy), Stamenic (set pieces), Garbett (creative)
- **Realistic level:** Post-qualifying W2 D1 L6 tells the story. 2010 precedent (3 draws vs Italy, Slovakia, Paraguay) shows they can compete on organization alone. Ceiling is a draw

---

## Model Output (Bayesian Market-First)

| Match | λ_A | λ_B | Modal | E[total] | 80% CI |
|-------|-----|-----|-------|----------|--------|
| Belgium vs Egypt | ~1.24 | ~1.18 | 1-1 | ~2.42 | 1-4 |
| Iran vs New Zealand | ~1.49 | ~0.97 | 1-0 | ~2.45 | 1-4 |
| Belgium vs Iran | ~1.39 | ~1.19 | 1-1 | ~2.58 | 1-4 |
| New Zealand vs Egypt | ~0.95 | ~1.65 | 0-1 | ~2.60 | 1-5 |
| Egypt vs Iran | ~1.37 | ~1.22 | 1-1 | ~2.59 | 1-4 |
| New Zealand vs Belgium | ~1.06 | ~1.90 | 0-2 | ~2.96 | 1-5 |

Model total: ~15.6 goals (2.60 g/m)

---

## Match-by-Match Predictions (v2)

### Match 1: Belgium vs Egypt — Mon Jun 15, Lumen Field (Seattle)

**Pick: 1-1** (unchanged from v1)

| Factor | Assessment |
|--------|-----------|
| Model | λ(BEL)~1.24, λ(EGY)~1.18 → modal 1-1 |
| Market | Belgium -220 favorite, Egypt +390 |
| Context | Group opener, both cautious. Belgium's first WC match under Rudi Garcia |
| Key | Egypt's qualifying defense (2 GA in 10) vs De Bruyne's creativity. Salah on the counter |

Belgium have the higher ceiling but Egypt's defensive discipline is genuinely elite — 2 goals conceded in 10 qualifying matches, plus a 0-0 draw with Spain in March. Both teams will be cautious in the opener. De Bruyne (35 in June, returning from hamstring) won't be at full throttle. Egypt are content to sit deep and let Salah/Marmoush exploit transitions. The draw is the coherent outcome.

**History note:** Belgium and Egypt have met 3 times, splitting 1-1 with 1 draw. This is their first WC meeting.

### Match 2: Iran vs New Zealand — Mon Jun 15, SoFi Stadium (Los Angeles)

**Pick: 2-1** (unchanged from v1)

| Factor | Assessment |
|--------|-----------|
| Model | λ(IRN)~1.49, λ(NZL)~0.97 → modal 1-0, 2-1 plausible |
| Market | Iran favored, NZ best bet to finish last (-185) |
| Context | Iran's crucial match — must win to stay alive for 2nd place. NZ nothing to lose |
| Key | Taremi vs NZ's set-piece defensive weakness (exposed by Finland). Wood's fitness unknown |

We go 2-1 over the model's 1-0 because: NZ scored in most of their meaningful friendlies (1 vs Colombia, 4 vs Chile, 1 vs Norway). They are organized and will create something from set pieces — Wood's aerial threat (if fit) or Stamenic's delivery. But Iran's quality edge through Taremi is decisive. Iran need this win badly given Belgium and Egypt await. Taremi scores, Iran take 3 points but NZ don't go quietly.

**Geopolitical angle:** If Iran are playing in the US despite the conflict, the emotional charge adds intensity to this match.

### Match 3: Belgium vs Iran — Sun Jun 21, SoFi Stadium (Los Angeles)

**Pick: 2-1** (v2 revision from 2-0)

| Factor | Assessment |
|--------|-----------|
| Model | λ(BEL)~1.39, λ(IRN)~1.19 → modal 1-1, but 2-1 in top 5 |
| Market | Belgium heavy favorite |
| Context | Belgium need a win after drawing Egypt on MD1. Iran will sit deep |
| Key | Belgium's attacking depth vs Iran's compact defense. De Bruyne with an extra week of fitness |

Belgium will be determined after dropping points to Egypt on MD1. De Bruyne should be sharper with a week more fitness. Iran will deploy their frustration tactics (compact shape, Taremi isolated), but Belgium have the quality to break them down — Doku's 1v1 ability creates the width Iran's compact block can't cover. Iran's domestic league suspension means match fitness issues surface in the second half.

**v2 revision:** Changed from 2-0 to 2-1 to account for Taremi's proven scoring ability — he scored in 9 of 10 qualifying matches and scores everywhere (Olympiacos debut brace, both March friendlies). Iran will get something on the counter or a set piece even when chasing. Belgium still win but Iran don't go scoreless.

**Never met before:** First-ever meeting between Belgium and Iran in any competition.

### Match 4: New Zealand vs Egypt — Sun Jun 21, BC Place (Vancouver)

**Pick: 0-2** (unchanged from v1)

| Factor | Assessment |
|--------|-----------|
| Model | λ(NZL)~0.95, λ(EGY)~1.65 → modal 0-1, 0-2 in top 3 |
| Market | Egypt strong favorite |
| Context | Egypt building on MD1 draw vs Belgium, pressing for qualification. NZ after a MD1 loss |
| Key | Salah vs NZ's limited defensive quality. Egypt patient in possession vs low blocks |

Egypt's defensive solidity means NZ are unlikely to score — their only route is set pieces, and Egypt's Al Ahly-based defensive core is experienced at dealing with aerial threats in CAF competition. Salah and Marmoush will find space on transitions. Egypt score two: one from a Salah counter and one from a set piece (Trezeguet specialty). NZ fight hard but the quality gap shows. Indoor venue (BC Place) neutralizes any weather factor.

### Match 5: Egypt vs Iran — Fri Jun 26, Lumen Field (Seattle)

**Pick: 1-1** (v2 revision from 1-0)

| Factor | Assessment |
|--------|-----------|
| Model | λ(EGY)~1.37, λ(IRN)~1.22 → modal 1-1 |
| Market | Egypt slight favorite. This is "the decisive match" for 2nd place |
| Context | MD3 — Egypt on 4 pts (D+W), Iran on 4 pts (W+D). Both need points, draw favors Egypt |
| Key | Egypt's defensive discipline vs Iran's need to attack. Salah vs Taremi |

The most important match in Group G. **v2 revision:** Changed from 1-0 to 1-1 (aligning with model modal). Two defensive teams (Egypt 2 GA qualifying, Iran <1 GA/game qualifying) in a high-stakes match naturally produce a draw, not a decisive result. Egypt on 4 points can afford the draw, while Iran on 4 points need a win but struggle to score when forced to attack (0-1 Qatar loss). Both teams score: Salah gets Egypt's goal on a counter, Taremi equalizes late to keep Iran alive. The tactical stalemate is the coherent outcome.

**H2H:** Egypt beat Iran 2-1 in their most recent meeting (2022).

### Match 6: New Zealand vs Belgium — Fri Jun 26, BC Place (Vancouver)

**Pick: 0-2** (unchanged from v1)

| Factor | Assessment |
|--------|-----------|
| Model | λ(NZL)~1.06, λ(BEL)~1.90 → modal 0-2 |
| Market | Belgium heavy favorite |
| Context | Belgium already through (7 pts from W+D). May rest key players. NZ playing for pride |
| Key | Belgium's depth still outmatches NZ. MD3 is more open (stage_eff +0.08) |

Model and manual agree on 0-2. Belgium will likely have qualified already (4 pts minimum from MD1 draw + MD2 win), and may rest De Bruyne and Lukaku. But Belgium's bench (De Ketelaere, Lammens' generation) is still a level above NZ's best XI. NZ will be organized — the 2010 precedent (3 draws) shows All Whites can make life difficult — but after two losses and a possible Wood fitness decline, the energy isn't there. Belgium win comfortably without needing to overexert.

**2010 parallel:** NZ drew Italy 1-1 at the 2010 WC. A similar upset draw isn't impossible, but Belgium will have more to play for (GD for seeding) than Italy did.

---

## Group G Summary

| Match | v1 Pick | v2 Pick | Goals |
|-------|---------|---------|-------|
| Belgium vs Egypt | 1-1 | 1-1 | 2 |
| Iran vs New Zealand | 2-1 | 2-1 | 3 |
| Belgium vs Iran | 2-0 | **2-1** | 3 |
| New Zealand vs Egypt | 0-2 | 0-2 | 2 |
| Egypt vs Iran | 1-0 | **1-1** | 2 |
| New Zealand vs Belgium | 0-2 | 0-2 | 2 |
| **Total** | | | **14** |

**Goals:** 14 total (2.33 g/m) — closer to WC average (2.67), reflecting the defensive identity of the group while accounting for individual quality (Taremi, Salah)

**Draws:** 3 of 6 (50%) — high but coherent with the "three defensive teams" narrative. Egypt-Belgium opener sets the tone, Belgium-Iran and Egypt-Iran both feature compact sides that don't concede easily

### Predicted Standings

| Pos | Team | W | D | L | GF | GA | GD | Pts |
|-----|------|---|---|---|----|----|-----|-----|
| 1 | Belgium | 2 | 1 | 0 | 5 | 2 | +3 | 7 |
| 2 | Egypt | 1 | 2 | 0 | 4 | 2 | +2 | 5 |
| 3 | Iran | 1 | 1 | 1 | 4 | 4 | 0 | 4 |
| 4 | New Zealand | 0 | 0 | 3 | 1 | 6 | -5 | 0 |

**Belgium and Egypt advance.** Belgium top the group on 7 points. Egypt qualify 2nd with 5 points (1W 2D), edging Iran on goal difference (+2 vs 0).

Iran finish 3rd with 4 points (1W 1D 1L) — a competitive showing with a real chance at best third-place qualification (neutral GD, higher than many third-place finishers historically).

New Zealand finish last with 0 points and 1 goal. Chris Wood's fitness was always the key variable.

### Group Story

Group G is defined by defensive quality and the refusal of quality attackers to disappear. Belgium, Egypt, and Iran all have strong defensive identities, producing 14 goals in 6 matches and 3 draws — a high draw rate but coherent with the compact, organized styles all three bring. The opener sets the tone: Belgium and Egypt cancel each other out 1-1, establishing the respect that shapes the rest of the group. Belgium edge Iran 2-1 on MD2 (Taremi scores even in defeat), while Egypt cruise past New Zealand 2-0. The decisive MD3 match — Egypt vs Iran — ends 1-1: Salah scores on the counter, Taremi equalizes late. Both teams defend resolutely, neither willing to gamble. The draw suits Egypt (who advance on +2 GD) but leaves Iran's fate in the hands of other groups. Belgium finish the job with a routine 2-0 over New Zealand and top the group on 7 points.

The Belgium generational transition question gets a partial answer: good enough to top a mid-strength group, but the draws with Egypt and Iran (2-1 instead of dominant wins) suggest they aren't the force they were. Egypt emerge as the story — Salah's final World Cup campaign delivers a knockout round appearance for only the second time in their history. Iran, with 4 points and Taremi's quality on display, have a legitimate third-place qualification case.

---

## Revision Triggers

- [ ] Iran participation decision (expected end of April)
- [ ] Chris Wood first-team return at Forest (Apr 9 Porto match target)
- [ ] De Bruyne / Lukaku fitness for June (Napoli end-of-season load)
- [ ] Courtois availability (GK decision: Courtois vs Lammens)
- [ ] Azmoun status (fit? politically cleared?)
- [ ] Egypt May friendlies — watch defensive setup vs quality opposition
- [ ] MD1 results → adjust MD2/MD3 picks

---

## Sources

- Polymarket Group G Winner (accessed Apr 9, 2026)
- FanDuel, BetMGM match odds (accessed Apr 1-9, 2026)
- FIFA Match Schedule, Team Profiles
- RotoWire Group G Preview (AI simulations)
- FotMob, LiveScore, Sofascore (player stats)
- ESPN, Al Jazeera, BBC Sport (team news, Iran geopolitical coverage)
- 11v11.com, AiScore, FBref (head-to-head records)

---

## Version History

**v3 (2026-04-09):** Data-enriched review complete, no scoreline changes. Factual updates:
- De Bruyne age: 34 → 35 in June
- Lukaku: Updated to reflect 64 min across 5 sub appearances at Napoli, second injury (iliopsoas inflammation), disciplinary issue, WC fitness concern
- Salah: Corrected to down from 28G/18A (not 17G/13A). Added Liverpool departure announcement March 24, shot accuracy 58%→42%, conversion 25%→14%
- Taremi: Upgraded — 10G/2A in Greek Super League (~1,075 min), 2G/2A Champions League, FotMob 7.5, 99th percentile npxG
- Azmoun: Updated to expelled at 'highest level of government,' judiciary threatened asset seizure, permanent exclusion
- Chris Wood: Returned to first-team training April 8, available for Porto match, recovery ahead of schedule
- Iran geopolitical: Added FIFA Infantino met federation in Antalya, ceasefire 'incredibly precarious'
- Polymarket odds: BEL 75%→70%, EGY 16%→21%

**v2 (2026-04-09):** Counselors review feedback applied. Changes:
1. Belgium vs Iran: 2-0 → **2-1** (Taremi scored in 9/10 qualifiers, too good to blank)
2. Egypt vs Iran: 1-0 → **1-1** (model modal, two defensive teams naturally draw in high-stakes MD3)

Rationale: v1 had systematic downward bias (12 goals, 23% below model's 15.6). All manual overrides reduced goals vs model. Counselors flagged Taremi's quality (scored everywhere) and defensive team dynamics (draws more likely than decisive results). New total: 14 goals (2.33 g/m), draws 3/6 (50%). Egypt drops from 7pts to 5pts but still advance on GD. Iran rises to 4pts with realistic third-place hopes.

**v1 (2026-04-09):** Model + qualitative picks, pre-counselors review

**Known issue:** Research file references wrong group (Italy/Sweden/Cameroon) but picks used correct teams (Belgium/Egypt/Iran/NZ). No impact on prediction quality.
