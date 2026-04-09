# wc26-oracle

2026 FIFA World Cup predictions and tipping tournament analysis.

## Purpose

Personal project for the Nordnet World Cup tipping tournament. Predict exact scorelines for all 104 matches. Predictions can be revised up until match kickoff.

## Prediction Process (per group)

Follow this process for every group. Do not skip steps.

### Step 1: Research (Agent)
Dispatch a research agent to gather for each team:
- Recent results (last 10 matches with scores)
- Qualifying record (path, goals scored/conceded)
- Key players, injuries, star players' club form (goals/assists 2025-26)
- Manager, formation, tactical style
- FIFA ranking
- Squad composition (domestic vs European leagues, heat/altitude acclimatization)
- Head-to-head history between all teams in the group
- Prediction market odds (Polymarket group winner, match odds, O/U lines)
- Sportsbook odds (BetMGM, DraftKings, Oddschecker)

**Search in native languages.** Local sports media breaks injury/squad news faster than English outlets. For each team, search in both English AND the team's language:
- Spanish: ESPN Deportes, TUDN, Récord, Marca, AS
- Portuguese: GE.globo, UOL Esporte, ESPN Brasil
- French: L'Équipe, RMC Sport, RFI
- German: Kicker, Sport1, Bild
- Swedish: SVT Sport, GP, Fotbollskanalen, Aftonbladet
- Dutch: VI, NOS Sport, AD
- Korean: Starnews EN, Yonhap
- Japanese: Sponichi, Nikkan Sports (English summaries)
- Arabic: for MENA teams use English sources (beIN Sports, Al Jazeera Sport)
- Other languages: search "[team] World Cup 2026 injuries" in native language where practical

### Step 2: Model Predictions
Run `predict_group_X.py` using the Bayesian model:
- Set team attack/defense ratings from qualifying + form data
- Set venue, stage, acclimatization flags
- Input market odds where available
- Get per-team λ, modal scoreline, top-5 scorelines, total distribution

### Step 3: Qualitative Picks (v1)
Combine model output with narrative analysis:
- Don't just pick the modal scoreline for every match (avoid all-1-1 trap)
- Consider match context: opener caution, must-win desperation, dead rubber, altitude, heat
- Picks must tell a coherent group story (standings should be plausible)
- Check draw rate (~25% base rate in WC groups — 0 draws in 6 matches is suspicious)
- Check total goals against model expectation (don't deviate >20% without good reason)

### Step 4: Counselors Review (opinion-based)
Dispatch to smart group (opus, gemini-pro, gpt-reasoning):
- Share picks, model output, team data, market odds
- Ask: are scorelines plausible? Is total too low/high? Any blindspots?
- Synthesize their feedback into v2 picks

### Step 5: Counselors Review (data-enriched)
Dispatch again with explicit instruction to USE WEB SEARCH:
- Verify team form, injury updates, market odds independently
- Bring NEW data we might have missed — search broadly, not just for known players
- Search queries must be broad: "[country] World Cup injuries April 2026", not just specific names
- Breaking injury news can be days old and still missing from our analysis (e.g., Lundgren Achilles rupture Apr 7)
- Check player club form stats (goals, assists, minutes played)
- Validate venue/weather assumptions
- This is the most important review — it catches stale data and unknown unknowns

### Step 6: Final Picks
Synthesize all reviews into final version. Document in:
- `groups/group-X.md` — full analysis, picks, model output, sources
- `decisions.md` — decision log entry with version history

## Key Files

- `analysis.md` — tournament-level analysis (total goals, format, rules)
- `decisions.md` — chronological log of every decision with reasoning
- `groups/group-X.md` — per-group analysis and predictions
- `model.py` — Bayesian scoreline prediction model
- `predict_group_X.py` — per-group model predictions
- `wc_matches_1998_2022.csv` — historical match data for backtesting
- `AGENTS.md` — instructions for AI agents
- `agents/counselors/` — raw counselors outputs

## Conventions

- Every prediction must have: the decision, what data it's based on, and why
- Log ALL sources used (URLs, dates accessed)
- Version predictions (v1, v2, etc.) — never overwrite without keeping history
- Include model λ values alongside qualitative picks
- Track revision triggers: what new data would cause us to change a pick

## Data Integrity

- Never fabricate match results, scores, or statistics
- Verify group compositions and fixture data against FIFA.com
- Historical stats must cite source tournaments and years
- If a data point is unverified, say so
- Market odds must include date accessed (they change daily)

## Revision Policy

**Predictions lock 1 minute before kickoff.** Submit in time! Key revision triggers:
- New friendly results (May/June international windows)
- Injury news (squad announcements May 30)
- Market odds movement (>10% shift)
- Earlier group results informing later matchday picks
- Weather/venue updates from FIFA
