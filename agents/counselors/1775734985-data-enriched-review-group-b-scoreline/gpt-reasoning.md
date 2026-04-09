I’m gathering the repo’s current Group B rationale and then cross-checking it against fresh public reporting and markets so I can give you a hard-nosed data update, not just vibes.

● Read group-b-research.md
  │ research/group-b-research.md
  └ 1 line read

● Read decisions.md
  └ L1:260 (236 lines read)

● Read group-b.md
  │ groups/group-b.md
  └ 288 lines read

● Web Search What are the latest April 2026 updates on Edin Dzeko's shoulder injury for Bosnia and …
  └ {"type":"text","text":{"value":"The latest updates from April 2026 regarding ...

● Web Search What are the latest April 2026 Switzerland national team squad and injury updates ahea…
  └ {"type":"text","text":{"value":"Here's a summary of the latest Switzerland na...

● Web Search What are the current 2025-26 season club-form statistics as of April 2026 for Jonathan…
  └ {"type":"text","text":{"value":"Based on the latest available data from April...

● Web Search Research three things with citations: 1) historical host nation opening match records …
  └ {"type":"text","text":{"value":"Here's a comprehensive research-backed respon...

● Web Search As of April 2026, what are the latest injury and availability updates for Canada's men…
  └ {"type":"text","text":{"value":"Here is a summary of the latest available upd...

● Web Search What are the typical June weather conditions and stadium roof/indoor details for Toron…
  └ {"type":"text","text":{"value":"Here’s a detailed overview of the typical Jun...

● Web Search What are the current market odds in April 2026 for 2026 FIFA World Cup Group B winner …
  └ {"type":"text","text":{"value":"Here are the latest available market odds and...

● Web Search What is the latest on Qatar's 2026 World Cup preparation and form under Julen Lopetegu…
  └ {"type":"text","text":{"value":"As of April 2026, Qatar—under the leadership ...

I’ve got the repo context. Now I’m tightening the evidence quality on the weak spots from search results: direct source checks for Canada, Džeko, Qatar prep, markets, and venues so the recommendation is grounded.

● Search (grep)
  │ "^## |^### " (research/group-b-research.md)
  └ 49 lines found

● Fetching web content https://www.bundesliga.com/en/2bundesliga/news/edin-dzeko-injury-bosnia-herz…
  └ Contents of https://www.bundesliga.com/en/2bundesliga/news/edin-dzeko-injury-...

✗ Fetching web content https://www.oddschecker.com/football/world-cup
  └ Error: Failed to fetch https://www.oddschecker.com/football/world-cup - status code 403

● Fetching web content https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articl…
  └ Failed to simplify HTML to markdown. Here is the raw content:

● Fetching web content https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articl…
  └ Failed to simplify HTML to markdown. Here is the raw content:

● Fetching web content https://www.tsn.ca/soccer/article/race-for-the-roster-canadas-injury-crisis-…
  └ Contents of https://www.tsn.ca/soccer/article/race-for-the-roster-canadas-inj...

● Fetching web content https://polymarket.com/event/fifa-world-cup-group-b-winner
  └ Contents of https://polymarket.com/event/fifa-world-cup-group-b-winner:

● Fetching web content https://inside.fifa.com/news/host-nations-in-opening-matches-of-fifa-world-c…
  └ Contents of https://inside.fifa.com/news/host-nations-in-opening-matches-of-f...

I’ve confirmed one real market move already: Bosnia is up materially in Polymarket versus your stored April 9 snapshot, with Switzerland giving back share. I’m pulling the repo’s original assumptions side-by-side now.

● Read group-b-research.md
  │ research/group-b-research.md
  └ L37:110 (74 lines read)

● Read group-b-research.md
  │ research/group-b-research.md
  └ L176:275 (100 lines read)

● Read group-b-research.md
  │ research/group-b-research.md
  └ L284:456 (173 lines read)

● Read group-b-research.md
  │ research/group-b-research.md
  └ L365:439 (75 lines read)

● Fetching web content https://www.tsn.ca/soccer/article/race-for-the-roster-canadas-injury-crisis-…
  └ Contents of https://www.tsn.ca/soccer/article/race-for-the-roster-canadas-inj...

● Web Search Find recent direct source reporting from Swiss media (Blick, SRF Sport, Tages-Anzeiger…
  └ {"type":"text","text":{"value":"Based on direct source reporting from major S...

● Web Search Find recent direct source reporting from Canadian soccer media in April 2026 on Ismael…
  └ {"type":"text","text":{"value":"Here is a summary of direct Canadian media re...

● Web Search Find recent direct source reporting on current 2025-26 club stats for Breel Embolo, Ed…
  └ {"type":"text","text":{"value":"Here's a summary of the most recent and relia...

I’ve got enough to call the main tactical questions, but I’m doing one last pass on player-form specifics and head-to-head so the recommendation isn’t leaning on any shaky stat line.

● Fetching web content https://www.transfermarkt.com/granit-xhaka/leistungsdaten/spieler/111455
  └ Contents of https://www.transfermarkt.com/granit-xhaka/leistungsdaten/spieler...

● Fetching web content https://www.transfermarkt.com/edin-dzeko/leistungsdaten/spieler/28396
  └ Contents of https://www.transfermarkt.com/edin-dzeko/leistungsdaten/spieler/2...

● Fetching web content https://www.transfermarkt.us/breel-embolo/leistungsdaten/spieler/237662
  └ Contents of https://www.transfermarkt.us/breel-embolo/leistungsdaten/spieler/...

● Fetching web content https://www.transfermarkt.com/jonathan-david/leistungsdaten/spieler/533738
  └ Contents of https://www.transfermarkt.com/jonathan-david/leistungsdaten/spiel...

● Web Search Verify recent head-to-head results among Canada, Switzerland, Bosnia and Herzegovina, …
  └ {"type":"text","text":{"value":"Here are the concrete, verifiable internation...

● Web Search Verify official or highly reliable stadium details for BMO Field, Levi's Stadium, SoFi…
  └ {"type":"text","text":{"value":"Here are confirmed details on the structure a...

## Verdict

Your shape is basically right. I would **keep five of the six picks** and make **one change only: `Canada 2-0 Qatar` instead of `2-1`**.

## What the new data says

**Canada:** the injury story is more about **match sharpness than outright absences**. TSN’s April roster piece still flags Davies, Eustaquio, Johnston and Bombito as injured, but also says **almost all should clear before the World Cup**. Davies’ bigger issue is now ACL-plus-hamstring rhythm, not tournament availability. That supports caution, not panic.

**Bosnia / Džeko:** this is the big swing factor. `Bundesliga.com` says Džeko’s shoulder injury puts him out for Schalke’s run-in, with a roughly **4-6 week** recovery window. He’s optimistic, but **he is not training normally right now**. That caps Bosnia’s upside.

**Switzerland:** I found **no concrete April injury alarm** from Swiss coverage. They still look like the healthiest, steadiest team. Club form is solid too: Xhaka `29 apps, 1G, 5A`; Embolo `28 apps, 9G, 3A` (`Transfermarkt`).

**Qatar:** Lopetegui is preparing seriously, with a U.S. base and tactical work built around Afif, but the hard data still screams weakest team. Their recent results remain poor, and markets still treat them that way. Afif’s club form is real, though: roughly `16 apps, 9G, 11A` at Al Sadd.

## Market read

The most important market move is **Bosnia drifting up, not Canada collapsing**. Current `Polymarket` has roughly:

`Switzerland 53%`  
`Canada 25.5%`  
`Bosnia 19.5%`  
`Qatar 3.6%`

That’s a meaningful Bosnia upgrade versus your April 9 snapshot, but **not enough to justify flipping the group**.

## Answers to your questions

**Do the injury updates change any predictions?**  
Yes, but only a little. They **reinforce `Canada 1-1 Bosnia`** because Canada’s squad looks available-but-rusty, while Bosnia’s talisman looks available-but-limited.

**Is Qatar’s total of 2 right?**  
Yes. I would say **2 is the ceiling, not the floor**. I would not raise it.

**Is `Canada 1-1 Bosnia` the right opener?**  
Yes. Keep it. Co-host precedent says Canada are more likely to **avoid defeat** than to definitely win. Džeko’s shoulder and Canada’s rust cancel each other out.

**Is Switzerland’s 7 points defensible?**  
Absolutely. That is still the best group call.

## Recommendation

Final v3 from me:

`Canada 1-1 Bosnia`  
`Qatar 0-2 Switzerland`  
`Switzerland 2-1 Bosnia`  
`Canada 2-0 Qatar`  
`Switzerland 1-1 Canada`  
`Bosnia 2-1 Qatar`

That trims Qatar slightly, keeps Switzerland on 7, and fits the freshest data best.

