# Agent Instructions

Instructions for AI agents (Claude, Cursor, Copilot, etc.) working on this project.

## What This Project Is

A prediction project for the 2026 FIFA World Cup tipping tournament at Nordnet. We predict exact scorelines for all 104 matches.

## How to Work

- Read `CLAUDE.md` for the full prediction process (6 steps per group)
- Read `analysis.md` for tournament-level context (format, rules, historical data)
- Read `decisions.md` for the decision log and version history
- Read `groups/group-X.md` for existing group analysis
- Raw counselors outputs are in `agents/counselors/`
- Don't repeat research that's already documented. Build on what's there.

## Prediction Process

See `CLAUDE.md` for the detailed 6-step process. Key points:
1. Research agent gathers team form, injuries, market odds
2. Bayesian model produces per-team λ and scoreline distributions
3. Qualitative picks (v1) combine model + narrative
4. Counselors review (opinion-based) → v2
5. Counselors review (data-enriched, with web search) → v3/final
6. Document everything in `groups/` and `decisions.md`

## Decision Documentation

Every choice must include:
1. **What** — the specific scoreline
2. **Based on** — model λ values, market odds, team data, counselors feedback
3. **Why** — reasoning for this score over alternatives
4. **Version** — which iteration (v1, v2, etc.) and what changed
5. **Sources** — URLs with access dates

## Model Usage

- `model.py` — core Bayesian model (independent Poisson per team)
- `predict_group_X.py` — per-group predictions
- Run with: `source .venv/bin/activate && python predict_group_X.py`
- Key insight from backtesting: WC-only data is too sparse for team differentiation. Use market odds as primary team-strength signal, model adjustments for venue/context.

## Tournament Facts (verified)

- 48 teams, 12 groups of 4, 104 total matches
- June 11 – July 19, 2026
- Hosts: USA (11 venues), Mexico (3), Canada (2)
- Groups confirmed at FIFA draw Dec 5, 2025
- 5 debutants: Cape Verde, Curacao, Jordan, Uzbekistan, Haiti

## Submitted Tiebreaker Answer

**284 total goals** (2.73 goals/match implied)

## Prediction Deadline

Predictions lock **1 minute before kickoff**. Can be revised up until then.
