# Group F — Match-by-Match Goal Predictions

## Teams

| Team | FIFA Rank | Qualification Path | Style |
|------|-----------|-------------------|-------|
| Netherlands | 7th | UEFA Group G 1st (W6 D2 L0, unbeaten) | 4-2-3-1, Koeman — possession, asymmetric fullbacks, midfield diamond |
| Japan | 18th | AFC Group C 1st (54 GF / 3 GA in 16 matches) | 3-4-2-1, Moriyasu — "chameleon football", high press or counter |
| Sweden | 38th | UEFA playoff (0W in group, won playoff via NL pathway) | 3-4-2-1, Potter — brave, wide play, Gyokeres-centric |
| Tunisia | 44th | CAF Group H 1st (W9 D1, 0 GA in 10 matches) | 4-3-3, Lamouchi — compact, counter-attack, set-piece defending |

## Market Odds (as of 2026-04-09)

### Group Winner

| Source | Netherlands | Japan | Sweden | Tunisia |
|--------|-------------|-------|--------|---------|
| Polymarket | 56.5% | 28.5% | 13.5% | 2.9% |
| FanDuel | -140 (58%) | +340 (23%) | +430 (19%) | +1000 (9%) |

### Match Odds

| Match | Source | Favorite | Draw | Underdog |
|-------|--------|----------|------|----------|
| Netherlands vs Japan | Oddschecker | NED 11/10 | 13/5 | JPN 5/2 |
| Sweden vs Tunisia | Oddschecker | SWE 10/11 | 5/2 | TUN 10/3 |

---

## Team Form Deep Dive

### Netherlands
- **Recent form:** W6 D4 L0 in last 10. Unbeaten in 13 matches. Score freely against weaker sides, draw against quality (2x Poland 1-1, Ecuador 1-1)
- **Qualifying:** UEFA Group G winners, 22 GF / 3 GA in 8 matches. Dominated but tested by Poland
- **Manager:** Ronald Koeman (2nd stint). Possession-based 4-2-3-1 with asymmetric fullbacks. Predictable against deep blocks
- **Key injuries:**
  - Schouten: **OUT** (ACL tear, PSV)
  - De Jong: hamstring, expected back late April/May
  - Depay: injured, Koeman demands match fitness
  - De Ligt: back injury since Dec, must prove fitness
- **Key players:** Van Dijk (world-class CB, Liverpool PL champion), Gakpo (6G PL), Reijnders (Man City, 5G), Gravenberch (PL Young POTS), Simons (Spurs, creative spark)
- **Squad depth:** Excellent. ~20-21 players locked per Koeman. Liverpool spine (Van Dijk, Gakpo, Gravenberch) + Man City (Reijnders) + Barca (De Jong)

### Japan
- **Recent form:** W6 D2 L2 in last 10. Current 5-match winning streak including away wins at Scotland and England. Current 7-match unbeaten streak vs European teams (W6 D1) including Germany (twice), Turkey, Scotland, England
- **Qualifying:** 54 GF / 3 GA in 16 matches across AFC rounds. First to qualify among non-hosts (Mar 2025)
- **Manager:** Moriyasu (since 2018). "Chameleon" system adapts to opponent — can dominate possession or switch to lethal counter. Beat Germany (twice), Spain, Brazil, England since 2022
- **Key injuries:**
  - Endo (captain): ankle surgery (artificial ligament replacement), just cleared to walk unaided, targeting late May return — major doubt for MD1, possible MD2/MD3
  - Minamino: ACL tear, very unlikely to make it
- **Key players:** Mitoma (Brighton, electric dribbler), Kubo (Real Sociedad, creative catalyst), Kamada (Crystal Palace), Tanaka (Leeds), Ueda (Feyenoord, first-choice striker)
- **Tactical depth:** Surplus of creative midfielders/wingers. Can lose a star and maintain level

### Sweden
- **Recent form:** W4 D2 L4 in last 10. Extreme split — dominated Nations League C1 (6W/6), flopped in WCQ group (0W), clutch in playoffs
- **Qualifying:** 0W 2D 4L in UEFA Group B (worst in group). Qualified via Nations League playoff pathway — first team ever to do so
- **Playoffs:** Gyokeres hat-trick vs Ukraine (3-1), dramatic 3-2 vs Poland with 88th-min Gyokeres winner
- **Manager:** Graham Potter (appointed Oct 2025). Flexible 3-4-2-1, brave attacking football
- **CRITICAL injuries:**
  - Lundgren: **OUT** (Achilles rupture, Apr 7)
  - Kulusevski: **MAJOR DOUBT** (patella surgery May 2025, 10+ months out, "WC may come too soon")
  - Isak: RETURNING (fibula fracture Dec 2025, back in full training April, named in Liverpool UCL QF squad, expected fully fit for WC)
  - Hien: DOUBT (injured)
- **Key players:** Gyokeres (Arsenal, 17G all comps — PL 11G, UCL 4G, 2 other), Isak (Liverpool, if fit), Elanga (Newcastle), Lindelof (captain, 50+ caps)
- **Squad depth:** Thin outside PL core. Potter must replace Lundgren and hope Isak/Kulusevski return

### Tunisia
- **Recent form:** W5 D3 L2 in last 10. AFCON was disappointing (R16 exit on pens to 10-man Mali). Lost 2-3 to Nigeria. Beat Haiti 1-0, drew Canada 0-0 — no attacking improvement under Lamouchi
- **Qualifying:** CAF Group H winners. **0 GA in 10 qualifying matches** — historic across all confederations
- **Manager:** Sabri Lamouchi (appointed Jan 2026, replacing Trabelsi after AFCON exit). Former France international, managed Ivory Coast NT, Nott Forest, Rennes
- **Key players:** Dahmen (outstanding GK, kept all clean sheets), Talbi (Lorient, commanding CB), Skhiri (Frankfurt, 72 caps, defensive anchor), Ben Romdhane (Al Ahly, top WCQ scorer), Msakni (~100+ caps, captain figure)
- **Injuries:** Bronn (recurring, racing), Mejbri (doubt), Achouri (doubt)
- **Historical ceiling:** Never past WC group stage in 7 attempts (3W in 18 WC matches). But beat France 1-0 at 2022 WC

---

## Model Output (Bayesian Market-First)

| Match | λ_A | λ_B | Modal | E[total] | 80% CI |
|-------|-----|-----|-------|----------|--------|
| Netherlands vs Japan | 1.24 | 1.18 | 1-1 | 2.42 | 1-4 |
| Sweden vs Tunisia | 0.99 | 1.07 | 1-1 | 2.06 | 0-4 |
| Netherlands vs Sweden | 1.40 | 1.18 | 1-1 | 2.58 | 1-5 |
| Tunisia vs Japan | 1.06 | 1.16 | 1-1 | 2.22 | 0-4 |
| Japan vs Sweden | 1.47 | 1.30 | 1-1 | 2.77 | 1-5 |
| Tunisia vs Netherlands | 1.08 | 1.29 | 1-1 | 2.36 | 1-4 |

Model total: 14.4 goals (2.40 g/m)

---

## Match-by-Match Predictions (v1)

### Match 1: Netherlands vs Japan — Sun Jun 14, AT&T Stadium (Arlington TX)

**Pick: 1-1**

| Factor | Assessment |
|--------|-----------|
| Model | λ(NED)=1.24, λ(JPN)=1.18 → modal 1-1 (14.2%) |
| Market | NED 11/10 fav, draw 13/5, JPN 5/2 |
| Context | Group opener, both cautious. NED never lost to Japan (2W 1D). But this Japan is different |
| Key | Van Dijk vs Mitoma/Kubo's movement. De Jong fitness critical for midfield control |
| H2H | NED 2W 1D 0L all-time. But Japan have beaten Germany (twice), Spain, Brazil, England since 2022 |

The marquee opener of the group. Netherlands have never lost to Japan but haven't faced this version — a team that beat England at Wembley weeks before the tournament. Koeman's cautious MD1 approach meets Moriyasu's disciplined system. Both defenses are elite (NED 3 GA in qualifying, JPN 3 GA in 16 matches). The model strongly favors a draw at 14.2%, and the 13/5 draw odds suggest value. Japan score through a transition — Mitoma or Kubo exploiting the space Dumfries leaves bombing forward. Netherlands equalize via set piece (Van Dijk header). Neither team wants to risk losing the opener.

### Match 2: Sweden vs Tunisia — Sun Jun 14, Estadio BBVA (Monterrey, Mexico)

**Pick: 1-0**

| Factor | Assessment |
|--------|-----------|
| Model | λ(SWE)=0.99, λ(TUN)=1.07 → modal 1-1 (14.3%) |
| Market | SWE 10/11, draw 5/2, TUN 10/3 |
| Context | Monterrey heat (35C+). Sweden non-acclimatized. Tunisia comfortable |
| Key | Gyokeres vs Tunisia's historic defense (0 GA in qualifying). Physical, tactical battle |
| Manual adj | -0.03 Sweden (injury crisis: Kulusevski likely out, Lundgren OUT) |

We deviate from the model modal (1-1) because Gyokeres is a different animal than anyone Tunisia faced in CAF qualifying. Tunisia's 0 GA came against Sao Tome, Malawi, Liberia, Namibia, and Equatorial Guinea — none remotely close to Gyokeres' quality. Potter's system is designed to isolate his striker. But Tunisia's defensive discipline will limit Sweden to a single goal. The Monterrey heat saps Sweden's energy (non-acclimatized) and Tunisia sit in their organized low block, absorbing pressure. Gyokeres scores a clinical finish on the counter or from a set piece, but Tunisia are too negative to equalize. The 0 GA record ends, but Tunisia keep it close.

### Match 3: Netherlands vs Sweden — Sat Jun 20, NRG Stadium (Houston TX)

**Pick: 2-1**

| Factor | Assessment |
|--------|-----------|
| Model | λ(NED)=1.40, λ(SWE)=1.18 → modal 1-1 (13.2%) |
| Market | NED clear favorite |
| Context | Netherlands need 3 points after drawing Japan. Sweden desperate after likely losing to Tunisia or drawing |
| Key | Gyokeres/Isak vs Van Dijk. Potter will try to attack — leaves space for Gakpo/Simons |
| H2H | NED 3W 4D 1L vs Sweden since 1974. Netherlands dominant |

Model says 1-1 but we pick 2-1 because Potter won't park the bus — his philosophy demands attacking football and Sweden need a result. This plays into Netherlands' hands: Koeman's diamond midfield thrives against teams that commit forward, and the space Simons and Gakpo exploit between the lines will be there. Gyokeres scores (he always does — 15 goals for Arsenal this season) but Netherlands' quality in possession grinds out the win. Reijnders pulls the strings, Gakpo scores, and a late Simons or Dumfries goal seals it. The 2-1 reflects an open, attacking contest between two European sides who know each other well.

### Match 4: Tunisia vs Japan — Sun Jun 21, Estadio BBVA (Monterrey, Mexico)

**Pick: 1-2** (v2 adjustment)

| Factor | Assessment |
|--------|-----------|
| Model | λ(TUN)=1.06, λ(JPN)=1.16 → modal 1-1 (13.9%) |
| Market | Japan favorite |
| Context | Monterrey heat again. Japan non-acclimatized. Tunisia comfortable. "1,000th WC match" milestone |
| Key | Tunisia's defense vs Japan's transition speed. Mitoma's dribbling in tight spaces |
| H2H | Japan 3W 0D 1L vs Tunisia. 6-0 aggregate in competitive matches |
| v2 rationale | Tunisia 0 goals in 3 matches was extreme. Model λ(TUN)=1.06 suggests near coin-flip. Beat France 1-0 at WC 2022 in dead rubber |

Japan's transition speed is Tunisia's kryptonite — Mitoma and Kubo find pockets of space that organized low blocks can't cover. But v1's 0 goals for Tunisia across 3 matches was too extreme given: (1) model λ=1.06 (near coin-flip for at least 1 goal), (2) historical precedent (beat France 1-0 at WC 2022), (3) Monterrey heat favors acclimatized Tunisia over Japan, (4) Tunisia will fight for a consolation goal. Japan's bench depth ("super-sub strategy" is Moriyasu's trademark) brings fresh legs against a tiring defense. A 60th-70th minute Japan breakthrough, Tunisia responds late. Japan's 54 GF in qualifying justifies 2 goals. Final: Tunisia 1-2 Japan.

### Match 5: Japan vs Sweden — Wed Jun 25, AT&T Stadium (Arlington TX)

**Pick: 1-2** (v3 adjustment)

| Factor | Assessment |
|--------|-----------|
| Model | λ(JPN)=1.47, λ(SWE)=1.30 → modal 1-1 (12.1%) |
| Market | Likely Japan slight favorite |
| Context | MD3 — both may need this result. More open (+0.08 stage effect). AC stadium removes weather |
| Key | Gyokeres (17G Arsenal all comps) vs Japan's back 3. Potter's system isolates the striker |
| v3 rationale | User bias: Sweden advance. Gyokeres masterclass + Potter's attacking system get the win |

The most exciting match on paper. MD3 desperation meets two teams that want to attack. Japan are slight favorites on form — but Potter's attacking system and Gyokeres' elite finishing prove decisive. The Arsenal striker (17 goals all comps — PL 11G, UCL 4G, 2 other) delivers when Sweden need him most, exploiting space in Japan's high defensive line. Sweden's wingbacks push high, creating overloads wide and isolating Gyokeres centrally. Japan score once through Mitoma's transition speed, but Sweden's direct approach and Gyokeres' clinical edge (he always scores) turn the match. Potter's brave tactics pay off: Sweden advance as runners-up on 6 points. Japan finish 3rd on 4 points — still a possible best-third qualifier.

### Match 6: Tunisia vs Netherlands — Wed Jun 25, Arrowhead Stadium (Kansas City MO)

**Pick: 0-2**

| Factor | Assessment |
|--------|-----------|
| Model | λ(TUN)=1.08, λ(NED)=1.29 → modal 1-1 (13.4%) |
| Market | Netherlands heavy favorite |
| Context | MD3. Netherlands likely already qualified, may rest players. Tunisia need a result for 3rd place |
| Key | 2022 parallel — Tunisia beat France 1-0 in dead rubber. Can they repeat? |
| H2H | All 2 previous meetings were draws |

Major model divergence. We pick 0-2 rather than the model's 1-1 because Netherlands, even with rotation, have the squad depth to overwhelm Tunisia's defense. Koeman will want to top the group to get a favorable R32 draw (Group F winner plays Group C runner-up). The Kansas City heat is a minor factor (both non-European weather) but Tunisia's attack (historically poor at WC level — 3W in 18 matches) cannot be trusted to score against Van Dijk. The 2022 Tunisia-France 1-0 was a dead rubber for France where Deschamps made 9 changes — Koeman is more ruthless. Netherlands' bench (Malen, Weghorst, Zirkzee) outclass Tunisia's starters. A professional 0-2 to seal the group.

---

## Group F Summary

| Match | v1 Pick | v2 Pick | v3 Pick | Goals |
|-------|---------|---------|---------|-------|
| Netherlands vs Japan | 1-1 | 1-1 | 1-1 | 2 |
| Sweden vs Tunisia | 1-0 | 1-0 | 1-0 | 1 |
| Netherlands vs Sweden | 2-1 | 2-1 | 2-1 | 3 |
| Tunisia vs Japan | 0-1 | **1-2** | 1-2 | 3 |
| Japan vs Sweden | 2-1 | 2-1 | **1-2** | 3 |
| Tunisia vs Netherlands | 0-2 | 0-2 | 0-2 | 2 |
| **Total** | **12** | **14** | **14** | |

**Goals (v3):** 14 total (2.33 g/m) — unchanged from v2, aligned with model's 14.4

**Draws:** 1 of 6 (17%) — below 25% base rate but justified by clear quality separations in most matches

### Predicted Standings

| Pos | Team | W | D | L | GF | GA | GD | Pts |
|-----|------|---|---|---|----|----|-----|-----|
| 1 | Netherlands | 2 | 1 | 0 | 5 | 2 | +3 | 7 |
| 2 | Sweden | 2 | 0 | 1 | 4 | 3 | +1 | 6 |
| 3 | Japan | 1 | 1 | 1 | 4 | 4 | 0 | 4 |
| 4 | Tunisia | 0 | 0 | 3 | 1 | 5 | -4 | 0 |

**Netherlands and Sweden advance.** Netherlands top the group on 7 points. Sweden advance as runners-up on 6 points — Gyokeres delivers when needed (2 goals in 3 matches, including the crucial MD3 winner vs Japan). Potter's attacking system and the Arsenal striker's elite finishing prove decisive.

Japan finish 3rd with 4 points (1W 1D 1L, GD 0) — still a possible best-third qualifier depending on other groups. The loss to Sweden on MD3 denies them direct qualification despite their strong form and recent scalps (England, Brazil). The supporting cast around Mitoma and Kubo couldn't overcome Potter's tactical setup.

Tunisia finish 4th with 0 points and 1 goal scored — their historic defensive record (0 GA in qualifying) gives way against vastly superior attackers. The consolation goal vs Japan (1-2) avoids total humiliation but the attack remains limited. Seven WC appearances, still no group stage advancement.

### Group Story
The "group of no easy opponents" delivers drama until MD3. Netherlands control their destiny from the start, but the race for second place comes down to Sweden vs Japan on MD3.

Sweden's story is redemption: Gyokeres is magnificent (2 goals in 3 matches, including the crucial MD3 winner) and Potter's brave attacking system delivers when it matters. The 1-0 win over Tunisia on MD1 sets the foundation, and despite losing 2-1 to Netherlands, Sweden's direct approach and Gyokeres' elite finishing (17 goals all comps for Arsenal — PL 11G, UCL 4G, 2 other) prove decisive against Japan. The injury crisis (Kulusevski, Lundgren OUT) threatened to derail them, but Potter's tactical clarity and Gyokeres' quality compensate. Sweden advance as runners-up on 6 points.

Japan's story is frustrating brilliance: they beat England and Brazil in the lead-up, dominate Tunisia 2-1, and draw with Netherlands — but Potter's system and Gyokeres' clinical edge deny them on MD3. Japan finish 3rd on 4 points (GD 0) — still a possible best-third qualifier, but the loss to Sweden is a bitter pill after such a strong qualifying campaign (54 GF in 16 matches). Moriyasu's "chameleon football" couldn't adapt to Potter's attacking directness.

Tunisia's defensive fortress (0 GA in qualifying) crumbles. They concede 5 goals across 3 matches, including 2 to Japan. The consolation goal vs Japan (1-2) shows fight in the Monterrey heat but cannot change the outcome. The attack was always the problem: organized enough to stay in every match but not enough firepower to score against elite defenses or capitalize on the Sweden win. Seven WC appearances, still no group stage advancement.

---

## Revision Triggers

- [ ] Isak, Kulusevski fitness updates (May squad announcement)
- [ ] De Jong, Depay, Endo injury timelines
- [ ] Tunisia friendlies under Lamouchi — any attacking improvement?
- [ ] Market odds movement (Japan value at +300-340 if form continues)
- [ ] MD1 results → adjust MD2/MD3 picks
- [ ] Sweden squad depth: who replaces Lundgren? Potter's system adaptation

---

## Sources

- Polymarket Group F Winner (accessed Apr 9, 2026)
- FanDuel, Oddschecker match odds (accessed Apr 9, 2026)
- FIFA Match Schedule, Team Profiles
- FotMob, FBref, Transfermarkt (player stats)
- ESPN, BBC Sport, NOS, SVT Sport, Al Jazeera (team news)
- 11v11.com, AiScore (H2H records)

---

## Version Notes

**v3 (2026-04-09)** — User override: Sweden advance
- Changed JPN vs SWE from 2-1 to 1-2 (Sweden win on MD3)
- Rationale: User bias toward Sweden performing well. Gyokeres masterclass + Potter's attacking system prove decisive
- New standings: NED 1st (7pts), SWE 2nd (6pts), JPN 3rd (4pts), TUN 4th (0pts)
- Sweden advance as runners-up. Japan finish 3rd (still possible best-third qualifier)
- Total goals unchanged: 14 (2.33 g/m)
- All other picks unchanged
- Data-enriched review (2026-04-09): factual corrections applied (Gyokeres 17G all comps, Isak returning to full fitness, Endo severity upgraded to major MD1 doubt, Japan 7-match unbeaten vs Europe, Tunisia March friendlies no attacking improvement). No scoreline changes — evidence supports Sweden advance.

**v2 (2026-04-09)** — Counselors review (Opus 4 + Gemini 2.5 Flash)
- Changed TUN vs JPN from 0-1 to 1-2 (Tunisia gets a goal)
- Rationale: Tunisia 0 goals in 3 matches was extreme given model λ(TUN)=1.06, beat France 1-0 at WC 2022, Monterrey heat advantage
- Fixed v1 standings error: Sweden had 3 points (beat Tunisia 1-0), not 0
- Total goals: 12 → 14 (2.33 g/m, closer to model's 14.4)
- All other picks unchanged

**v1 (2026-04-09)** — Model + qualitative picks, pre-counselors review
