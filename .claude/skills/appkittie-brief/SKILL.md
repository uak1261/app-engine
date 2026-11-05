---
name: appkittie-brief
description: Produce the recurring Top 5 app opportunity brief from live AppKittie data. Use when asked to run the AppKittie brief, the idea incubation brief, or to find apps with $30-50K/month potential.
---

# AppKittie Top 5 Opportunity Brief

Goal: from live AppKittie data, pick the 5 app opportunities a 1-2 person team could realistically take to **$30K-$50K revenue per month** within 6-9 months, and explain why in a brief an executive reads in 3 minutes.

No database. Pull fresh data from AppKittie every run (the `appkittie` MCP tools, or the MCP server over HTTP at `https://mcp.appkittie.com` with `Authorization: Bearer $APPKITTIE_API_KEY`). Never print the key. Every number in the brief must come from an AppKittie result in this run. If AppKittie fails (401, network, MCP error), stop and output `AppKittie Brief FAILED` with the exact error; never fabricate.

AppKittie `minRevenue` / `maxRevenue` / `minDownloads` are **monthly estimates in USD**. Compute Unix timestamps for date filters from today's date.

## Credit budget: hard cap 300 per run

| Step | Tool | Credits |
|---|---|---|
| 4 sweeps × 35 apps | `search_apps` | ~140 |
| Detail on 15 finalists | `get_app_detail` | 15 |
| 90d revenue trend on 8 | `get_app_historicals` (metrics: revenue, downloads; period 90d) | 8 |
| Niche depth check, 5 niches × 8 apps | `search_apps` with `search` = niche keyword | ~40 |
| Reviews, 5 niche leaders × 15 | `get_app_reviews` (`maxReviews: 15`, country US) | ~75 |

Track credits as you go. Stop expanding when you near 300.

## Step 1: Sweeps (exact filters)

Common to all sweeps: `source: apple_mobile`, `countries: ["US"]`, `excludedCategories: ["games"]`, `limit: 35`.

| Sweep | Extra filters | Purpose |
|---|---|---|
| A. Paid-proven newcomers | `releasedAfter` = 18 months ago, `minRevenue: 30000`, `maxRevenue: 400000`, `hasMetaAdSpend: true`, `sortBy: revenue` | New apps already earning in our band with ads that pay back |
| B. Revenue accelerators | `releasedAfter` = 24 months ago, `minRevenue: 30000`, `maxRevenue: 400000`, `sortBy: revenue_growth` | Rising niches right now. Ignore any `revenue_growth_30d` above 1,000%: those are data artifacts from old or non-US apps |
| C. Lean high-ARPU | `releasedAfter` = 24 months ago, `minRevenue: 30000`, `maxRevenue: 400000`, `maxDownloads: 50000`, `sortBy: revenue` | Earns well per user: small teams win here |
| D. TikTok-proven | `releasedAfter` = 18 months ago, `minRevenue: 30000`, `maxRevenue: 400000`, `hasTikTokAds: true`, `sortBy: revenue` | Second paid channel with proven economics |

Dedupe by app slug.

**Large results:** `search_apps` with 35 results and `get_app_detail` can exceed the tool output limit and be saved to a file. Extract fields with `jq` (title, developer, revenue, downloads, `historical_counts.revenue_growth_30d/90d`, `meta_ads_estimated_spend_30d_usd`, `tiktok_ads_total_count`, `in_app_purchases`) instead of reading the whole file. Note `countries: ["US"]` filters by language, not storefront, so non-US apps can still appear.

## Step 2: Hard screen (reject before spending more credits)

Reject an app if any is true:

- **Revenue band:** monthly revenue < $30K or > $400K (above that, the leader's brand or budget is the moat).
- **Monetization efficiency:** monthly revenue / monthly downloads < $0.75.
- **Publisher:** Big Tech or a household brand (Meta, Google, Microsoft, Amazon, ByteDance, Apple, Adobe, Spotify, Disney, etc.) or a known studio with 10+ hit apps.
- **Content or legal risk:** IPTV, streaming aggregators, media downloaders, VPN, anything relying on licensed or pirated content.
- **Regulated:** medical diagnosis, prescription, lending or credit, gambling, sports betting, crypto trading.
- **Not buildable by 1-2 people in ≤ 6 weeks:** two-sided marketplaces, social networks, hardware dependence, proprietary datasets, heavy ops (delivery, human services).
- **Copycat risk:** a clone of a single famous app with no niche (generic "AI chat", generic "photo editor").
- **Adult, dating or 17+ content.**

## Step 3: Group survivors into niches

Name each niche narrowly (for example "sermon note-taking", "AI receipt scanner for contractors", "heritage-language learning"). A niche qualifies only if **≥ 2 distinct publishers** earn ≥ $30K/month in it. One app alone is a fluke, not a market. Use the niche depth check (`search_apps` with the niche keyword, `limit: 8`, same common filters) to confirm.

## Step 4: Verify finalists

For the 15 best apps: `get_app_detail` (IAPs and price points, Meta/TikTok ad spend `summary.periods.last_30d`, rating, publisher). For the top 8: `get_app_historicals` 90d.

Use `historical_counts.revenue_growth_90d` from `get_app_detail` (cheaper than historicals). Reject if revenue fell > 25% over the last 90 days (fading trend), or if ad spend in the last 30 days is more than 60% of revenue (buying revenue at a loss).

## Step 5: Score niches (0-100)

| Factor | Weight | Full marks when |
|---|---|---|
| Proven band | 25 | 3+ publishers earn $30-400K/mo in the niche |
| Momentum | 20 | Median 30d revenue growth > +10%; 90d trend up |
| Monetization efficiency | 15 | Revenue/download ≥ $3; subscription with weekly or annual plan |
| Paid acquisition proof | 15 | Meta or TikTok spend sustained over 30 and 90 days, spend well under revenue |
| Quality gap | 15 | Leader rated < 4.5, or recurring complaints in reviews (cite them) |
| Build feasibility | 10 | MVP in ≤ 4 weeks by 1-2 engineers with off-the-shelf AI APIs |

Pick the top 5 niches. Ties go to the niche with the clearer wedge.

## Step 6: Reviews

For the top app in each of the 5 niches, pull 15 US reviews. Extract the 2-3 most repeated complaints with short quotes. These define the wedge.

## Revenue path math (show it per pick)

Net per paying user per month, after Apple's 15% small-business rate:
- $9.99/month → ~$8.50
- $4.99/week → ~$18
- $49.99/year → ~$3.55

Paying users needed for $30K / $50K: monthly ~3,500 / ~5,900; weekly ~1,700 / ~2,800; annual ~8,500 / ~14,100. State which model each pick should use, based on what its reference apps charge (from IAPs).

## Output format

Final message (and the email) is the brief only, in this format:

```
# AppKittie Opportunity Brief: <Weekday, Mon D, YYYY>

## Bottom line
<3 sentences: strongest pick and why, the common pattern across picks, one action for this week>

## Top 5 at a glance
| # | Niche | Score | Reference apps (monthly rev · monthly dl · 30d growth) | Pricing to copy | Paying users for $40K/mo |
|---|---|---|---|---|---|

## 1. <Niche> (score N/100)
- **Evidence:** <AppKittie figures, app names and publishers>
- **Why a newcomer can win:** <fragmentation, quality gap, review complaints with quotes>
- **Wedge:** <the one differentiated angle>
- **MVP in 4 weeks:** <3-5 core features>
- **Monetization:** <model + price + users needed>
- **Acquisition:** <channel proven by reference apps' ad spend>
- **Kill risks:** <top 2>
- **$500 smoke test:** <landing page promise + ad angle>

<repeat for 2-5>

## Rejected this run
<4-6 high-revenue apps that failed the screen, one line each with the rule they failed>

## Run stats
Credits used: ~N · Apps scanned: N · Niches evaluated: N · Data: AppKittie estimates (US, App Store)
```

Tone: lead with the decision, no filler, no em dashes.
