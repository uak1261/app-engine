---
name: appkittie-brief
description: Produce the recurring Top 5 app opportunity brief from live AppKittie data. Use when asked to run the AppKittie brief, the idea incubation brief, or to find apps with $30-50K/month potential.
---

# AppKittie Top 5 Opportunity Brief

Goal: from live AppKittie data, pick the 5 app opportunities a small team could realistically take to **$30K-$50K revenue per month**, and explain why in a brief an executive can read in 3 minutes.

No database. Pull fresh data through the `appkittie` MCP server every run, reason over it, write the brief. Never invent numbers: every figure in the brief must come from an AppKittie tool result in this run. If the MCP server is unavailable, stop and report that instead of producing a brief.

## Credit budget (hard cap: 300 credits per run)

AppKittie charges ~1 credit per app returned by search and 1 per detail lookup; keyword tools ~10.

1. **Sweep (~150-200 credits):** `search_apps` across 3-4 queries, each limited to ~50 results:
   - Released in the last 180 days, excluding Games, primary language English, sorted by revenue.
   - Same, with "has Meta ads" on (proof that paid acquisition works).
   - Growth 30d > 10%, any release date, revenue ≥ $50K/mo, excluding Games.
   Dedupe across queries.
2. **Detail (~25 credits):** `get_app_detail` on the ~25 strongest candidates after the screen below.
3. **Optional (≤50 credits):** keyword tools for the final 5 niches only, to gauge search demand.

Check the tool schemas at the start of each run; filter names may differ from the wording above.

## Screen (auto-reject)

- Publisher is Big Tech or a household brand (Meta, Google, Microsoft, Amazon, ByteDance, Apple, etc.).
- Depends on licensed or pirated content (IPTV, streaming aggregators, music downloaders).
- Regulated: medical diagnosis, lending or credit, gambling, prescription drugs.
- Games.
- Revenue driven by a celebrity, IP license, or network effect a new entrant cannot copy.

## Group into niches, then score

Group the surviving apps into niches (for example "sermon note-taking", "AI short-video editor"). Score each **niche**, not each app, 0-100:

| Factor | Weight | How to judge |
|---|---|---|
| Revenue headroom | 25 | Leader earns ≥ 3× $50K/mo, and #2-#5 still earn ≥ $20K/mo |
| Momentum | 20 | 30d growth positive; apps released in the last 6 months already earning |
| Monetization efficiency | 15 | High revenue per download; subscription or weekly paywall present |
| Paid acquisition proof | 15 | Meta/TikTok ads running steadily (sustained, not one burst) |
| Fragmentation | 10 | No single app takes > 60% of niche revenue |
| Quality gap | 10 | Leaders rated < 4.5, or repeated complaints in reviews |
| Build feasibility | 5 | MVP shippable in ≤ 4 weeks by 1-2 engineers |

Revenue sanity check for the $30-50K/mo target: at $9.99/month (~$8.50 net) that is ~3,500-5,900 paying users; at $4.99/week (~$18/month net) ~1,700-2,800. Say which pricing model each pick assumes.

If it is unclear whether AppKittie revenue is monthly or lifetime, say so in the brief and use relative ranking.

## Output format

```
# AppKittie Opportunity Brief — <date>

## Bottom line
<3 sentences: the strongest pick, the pattern across this week's picks, what changed since the last brief if known>

## Top 5
| # | Niche | Score | Reference apps (rev / dl / growth) | Path to $30-50K/mo | Wedge |
|---|---|---|---|---|---|

### 1. <Niche>
- **Evidence:** <figures from AppKittie, with app names>
- **Why a new entrant can win:** <quality gap, fragmentation, user complaints>
- **MVP (≤4 weeks):** <core feature set>
- **Monetization:** <price model, paying users needed>
- **Kill risks:** <top 2>
- **$500 smoke test:** <landing page + Meta ad angle to test demand>

...repeat for 2-5...

## Rejected this run
<3-5 high-revenue apps that failed the screen, one line each on why>

## Run stats
Credits used: ~N · Apps scanned: N · Detail lookups: N
```

Keep it tight. Lead with the decision. No filler.
