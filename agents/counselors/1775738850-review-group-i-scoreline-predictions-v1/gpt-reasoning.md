● skill(counselors)

I’m gathering the Group I context and recent repo changes first, then I’ll dispatch parallel counselor reviews and synthesize the strongest critiques into a clear recommendation.

● Read group-i-research.md
  │ research/group-i-research.md
  └ 1 line read

✗ Read counselors.md
  │ ~/.claude/commands/counselors.md
  └ Permission denied and could not request permission from user

● Read group-i.md
  │ groups/group-i.md
  └ 235 lines read

● Read predict_group_i.py
  └ 179 lines read

● Search (grep)
  │ "Group I|group-i|France|Senegal|Norway|Iraq" in
  │ {analysis.md,decisions.md,groups/*.md,research/*.md,predict_group_*.py}
  └ 24 files found

✗ Check recent diffs for Group I files (shell)
  │ git --no-pager diff HEAD -- groups/group-i.md predict_group_i.py research/group-i-research.md &&
  │ printf '\n---STAGED---\n' && git --no-pager diff --staged -- groups/group-i.md
  │ predict_group_i.py research/group-i-research.md
  └ Permission to run this tool was denied due the following rules: `shell` and `shell`

I’ve got the core Group I docs. Next I’m pulling the missing research slices and launching the parallel counselor pass so I can compare my own read against independent model opinions.

✗ Read counselors.md
  │ ~/.claude/commands/counselors.md
  └ Permission denied and could not request permission from user

● Read group-i-research.md
  │ research/group-i-research.md
  └ L1:220 (219 lines read)

● Read analysis.md
  └ L1:220 (158 lines read)

✗ Check git diff for Group I files (shell)
  │ cd /Users/akeros/Documents/Personal/wc26-oracle && git --no-pager diff HEAD -- groups/group-i.md
  │ predict_group_i.py research/group-i-research.md && printf '\n---STAGED---\n' && git --no-pager
  │ diff --staged -- groups/group-i.md predict_group_i.py research/group-i-research.md
  └ Permission to run this tool was denied due the following rules: `shell`, `shell`, and `shell`

The shell route for external counselors is blocked here, so I’m taking the next-best path: parallel independent sub-agents with different models, all reading the same Group I materials and critiquing the picks from different angles.

● General-purpose(claude-opus-4.6) Review Group I picks
  └ Agent started in background with agent_id: groupi-opus-review. You can use re...

● General-purpose(gpt-5.4) Review Group I picks
  └ Agent started in background with agent_id: groupi-gpt-review. You can use rea...

● General-purpose(claude-sonnet-4.6) Review Group I picks
  └ Agent started in background with agent_id: groupi-sonnet-review. You can use ...

One thing is already jumping out: the model keeps spitting `1-1` in spots where the narrative says “clear favorite,” which usually means the architecture is under-separating strong teams from resilient underdogs. I’m checking whether that’s a Group I quirk or a broader model behavior before I synthesize.

● Read model.py
  └ L1:260 (260 lines read)

● Read group-i-research.md
  │ research/group-i-research.md
  └ L220:420 (200 lines read)

● Search (grep)
  │ "manual_adj|market_total|manager_style|group_md1|group_md2|group_md3|predict_match|lambda|mu_tot
  │ al" (model.py)
  └ 46 lines found

● Read (General-purpose agent — Review Group I picks)
  └ Running

● Read (General-purpose agent — Review Group I picks)
  └ Running

● Read (General-purpose agent — Review Group I picks)
  └ Running

I found a concrete logic error, not just a football opinion: with your own picked scores, **Norway** finishes above Senegal on goal difference, so the written “Senegal advance” story is internally inconsistent and would contaminate downstream knockout projections. I’m waiting on the parallel model reviews now, but that part already needs fixing.

● Read (General-purpose agent — Review Group I picks)
  └ Completed

● Read (General-purpose agent — Review Group I picks)
  └ Running

● Read (General-purpose agent — Review Group I picks)
  └ Running

One external review is in and it agrees on the main structural issue: the Iraq shutout drives too much of the under. I’m waiting on the other two so I can separate real consensus from one-model bias.

● Read (General-purpose agent — Review Group I picks)
  └ Completed

● Read (General-purpose agent — Review Group I picks)
  └ Completed

## Bottom line

The **winners are mostly right**, but v1 has two real problems: it’s **too anti-Iraq**, and the **published standings logic is wrong**.

## Biggest issue

With your current picks, **Senegal do not advance on head-to-head** over Norway. Their H2H is **1-1**. On goal difference, **Norway finish 2nd**.

Best fix: change **Iraq–Norway from 0-2 to 1-2**. That:
- moves the group to **16 goals**
- gives Iraq a more realistic floor
- makes the table coherent: **France 9, Senegal 4 (+1), Norway 4 (0), Iraq 0**

## Match calls

Keep:
- `France 2-1 Senegal`
- `France 3-0 Iraq`
- `Norway 1-1 Senegal`
- `Norway 1-2 France`

Weakest call:
- `Iraq 0-2 Norway` → prefer **`1-2`**

`Senegal 2-0 Iraq` is fine, but `2-1` is also live.

## Calibration

- **15 goals** is acceptable vs historical ~16, but **light vs your own model (16.9)**
- **1 draw** is slightly low, but fine; don’t force a second

## Architecture / risk

Your model is under-separating teams, then the manual layer is **systematically zeroing Iraq out**. That’s the real blind spot.

No real security issue here, but there is a **decision-integrity risk**: “market-first” is overstated when `market_total`/`sigma` appear manually chosen rather than sourced from explicit match odds.

## Recommendation

**Change only `Iraq–Norway` to `1-2`.** Everything else can stand for v1.

