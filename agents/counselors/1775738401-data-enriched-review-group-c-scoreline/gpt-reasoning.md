● Read group-c-research.md
  │ research/group-c-research.md
  └ 1 line read

● Read group-c.md
  │ groups/group-c.md
  └ 245 lines read

● Read predict_group_c.py
  └ 180 lines read

● Web Search Latest April 2026 injury updates and squad news for Scotland national team World Cup 2…
  └ {"type":"text","text":{"value":"Here is the latest update for the Scotland na...

● Web Search Latest April 2026 injury updates and squad news for Morocco national team World Cup 20…
  └ {"type":"text","text":{"value":"Here's the latest (April 2026) injury updates...

● Web Search Latest April 2026 injury updates and squad news for Brazil national team World Cup 202…
  └ {"type":"text","text":{"value":"Here's a thorough update (April 2026) on the ...

● Web Search Latest April 2026 betting odds movement for 2026 World Cup Group C and match odds for …
  └ {"type":"text","text":{"value":"Here are the latest April 2026 betting odds a...

● Web Search Latest April 2026 injury updates and squad news for Haiti national team World Cup 2026…
  └ {"type":"text","text":{"value":"Here is the latest update on Haiti's national...

I’ve got the baseline. Now I’m tightening the review with a second pass on the raw research plus targeted web checks for player form and pricing, so the recommendation isn’t anchored to stale assumptions.

● Search (grep)
  │ "(Vinicius|Vinícius|Hakimi|McTominay|Gunn|Ouahbi|No\. 9|Rodrygo|Raphinha|Bruno Guimaraes|Bruno
  │ Guimarães|Amrabat|Hickey|Nazon)" (research/group-c-research.md)
  └ 47 lines found

● Search (grep)
  │ "^(##|###|\*\*|[-] \*\*)" (research/group-c-research.md)
  └ 5 lines found

● Web Search April 2026 Vinicius Junior club stats goals assists all competitions 2025-26 and recen…
  └ {"type":"text","text":{"value":"As of April 2026, just before the World Cup, ...

● Web Search April 2026 Scott McTominay club stats goals assists 2025-26 Napoli and recent form bef…
  └ {"type":"text","text":{"value":"As of April 2026, Scott McTominay has been a ...

● Web Search April 2026 Brazil vs Scotland World Cup betting odds Oddschecker FanDuel draw price an…
  └ {"type":"text","text":{"value":"For the June 24, 2026, World Cup match betwee...

● Web Search April 2026 Morocco vs Haiti World Cup betting odds Oddschecker FanDuel over under line…
  └ {"type":"text","text":{"value":"Here’s a comprehensive look at the April 2026...

● Web Search April 2026 Achraf Hakimi club stats goals assists all competitions 2025-26 and recent …
  └ {"type":"text","text":{"value":"Here are Achraf Hakimi’s club stats for PSG a...

I found one important disconnect already: your qualitative story is bolder than the market in exactly the wrong place. Morocco topping the group is a fine upside thesis, but pairing that with a Brazil–Scotland draw overstates Scotland’s ceiling relative to current prices and squad health.

✗ Fetching web content https://www.oddschecker.com/football/world-cup/scotland-v-brazil/winner
  └ Error: Failed to fetch https://www.oddschecker.com/football/world-cup/scotland-v-brazil/winner -
    status code 403

● Fetching web content https://sportstar.thehindu.com/football/brazil-squad-for-fifa-world-cup-2026…
  └ Contents of https://sportstar.thehindu.com/football/brazil-squad-for-fifa-wor...

● Fetching web content https://www.skysports.com/football/news/12017/13520319/world-cup-2026-angus-…
  └ Contents of https://www.skysports.com/football/news/12017/13520319/world-cup-...

● Fetching web content https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articl…
  └ Failed to simplify HTML to markdown. Here is the raw content:

● Fetching web content https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/teams/…
  └ Failed to simplify HTML to markdown. Here is the raw content:

● Web Search "Maroc Coupe du Monde blessures 2026" L'Équipe avril 2026 Ouahbi Hakimi Amrabat Aguerd…
  └ {"type":"text","text":{"value":"Voici les informations importantes concernant...

● Web Search "Brasil Copa do Mundo lesões 2026" ge.globo UOL Esporte abril 2026 Rodrygo Raphinha Br…
  └ {"type":"text","text":{"value":"Na preparação para a Copa do Mundo de 2026, a...

● Web Search What tactical changes has Mohamed Ouahbi introduced to Morocco by April 2026 compared …
  └ {"type":"text","text":{"value":"Mohamed Ouahbi’s appointment as Morocco’s hea...

● Web Search Has a clear Brazil No. 9 emerged by April 2026 under Carlo Ancelotti? Compare Endrick,…
  └ {"type":"text","text":{"value":"As of April 2026, a clear, undisputed Brazil ...

## Verdict

I would **not ship v2 as-is**.

The weak link is **`Scotland vs Brazil = 1-1`**. It’s a narrative fix, not a market-faithful one. Current prices still make Brazil a clear favorite there, with the draw only about **19-21% implied** (Oddschecker/Oddspedia), and Scotland’s squad health is worse than your sheet captures.

## New data that matters

Brazil:
- March squad churn is real: **Gabriel Magalhaes out**, **Alex Sandro out**, **Alisson out**, but the attack pool is deeper than your doc implies. Ancelotti is testing **Kaio Jorge / Joao Pedro / Cunha / Igor Thiago / Endrick** types, so the “no No. 9” point is true, but less catastrophic than framed.  
- **Vinicius is in elite club form**: roughly **17-18G, 13A** in all comps.

Scotland:
- The GK concern is confirmed: **Angus Gunn has only 45 club minutes** and is still being recalled.
- It’s broader than Gunn: **Craig Gordon injured, Hickey out, Doig out, Doak not fully back, Shankland out** (Sky Sports / Scotsman reporting). That lowers Scotland’s floor.

Morocco:
- The big takeaway is **continuity, not revolution** under Ouahbi. The defensive structure is largely intact.
- **Hakimi is in strong club form** and Morocco do not appear to have a fresh major injury crisis among core starters.
- That supports Morocco as good, but not necessarily “Brazil + Scotland draw = Morocco top” good.

Haiti:
- No major fresh injury wave found. They look healthy enough to be annoying, but still clearly fourth.

## Market/tradeoff read

Your current table **double-counts Brazil fragility**:
- `Brazil 1-1 Morocco` already fades Brazil.
- `Scotland 1-1 Brazil` fades them again.
- Meanwhile, the group market appears **more pro-Brazil than your doc says**.

That creates too much blast radius from one aggressive call: the Scotland draw flips the whole group winner story.

## Recommendation

Keep:
- `Brazil vs Morocco 1-1`
- `Haiti vs Scotland 1-2`
- `Scotland vs Morocco 0-2`
- `Brazil vs Haiti 3-0`

Change:
- **`Scotland vs Brazil` from `1-1` to `0-1`**
- **`Morocco vs Haiti` from `3-1` to `2-1`**

That gives you a cleaner architecture:
- respects Morocco’s strength,
- respects Brazil’s market power,
- avoids overrating Scotland,
- trims the too-aggressive Morocco-Haiti over.

## Data-integrity / “security” note

Do **not** overweight low-liquidity prediction markets or soft rumor sources. Use **bookmaker consensus + official squad reporting** as your source of truth.

