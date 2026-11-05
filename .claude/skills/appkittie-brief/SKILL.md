---
name: appkittie-brief
description: Produce the recurring AppKittie opportunity brief (Monday full run, Tue-Fri daily pulse) that finds app ideas a small team can take to $30-50K MRR. Use when asked to run the AppKittie brief, the idea incubation brief, or to vet app opportunities.
---

# AppKittie Opportunity Engine

**Job:** find app opportunities that deserve a **test**, not a build. A high score earns a $500 test. Only a passed test earns a build. Treat each app as an experiment in a portfolio that targets **$30-50K MRR in total**.

**Rules that override everything else**
- No database. Pull fresh data every run from the `appkittie` MCP tools, or from the MCP server over HTTP at `https://mcp.appkittie.com` with `Authorization: Bearer $APPKITTIE_API_KEY`. Never print the key.
- **AppKittie figures are estimates.** Label them "est." and say "unknown" when a field is missing. Never turn a missing field into zero.
- Every number must come from AppKittie in this run, or be a labeled **assumption** from the founder profile.
- If AppKittie fails (401, network or MCP error), stop and output `AppKittie Brief FAILED` with the exact error.
- **Recommending fewer than 5 is fine.** If nothing passes the gates, say so and show the closest misses.
- `minRevenue` / `maxRevenue` / `minDownloads` are monthly USD estimates. `countries` filters by language, not storefront. Work out Unix timestamps from today's date.
- Oversized results are saved to a file. Read them with `jq` and pull only the fields you need; never page through the raw JSON.

## Founder profile (assumptions: edit here, cite them in the brief)

| Parameter | Value |
|---|---|
| Build budget for a useful first version | **40 focused dev hours** (30-50 range) on a shared stack: Next.js/Supabase back end, Expo or Swift app, RevenueCat, a hosted LLM API |
| Launch cadence the engine feeds | 1 launch every 3-4 weeks, plus 2-3 positioning or creative tests a week |
| Test budget per idea | $500 |
| Channels the founder can actually work | Meta ads, TikTok/IG creators (paid seeding), ASO/keyword search, LinkedIn and professional networks, niche communities (Reddit, Facebook groups) |
| Store fee | 15% (Apple Small Business Program; assume enrolled) |
| Economics scenarios: conservative / base / upside | Monthly churn 15% / 10% / 6% · install-to-paid 2% / 3% / 5% · US iOS cost per install $5 / $3.50 / $2 · refunds 3% |
| Variable cost | Estimate the LLM/API cost per active payer per month from the features (e.g. vision or transcription ≈ $0.50-2) |

## Run mode (weekday in America/Chicago)

- **Monday: FULL run, hard cap 300 credits.** Stages 1-4 below.
- **Tuesday to Friday: DAILY PULSE, hard cap 60 credits.** See the section at the end.
- A run the person labels TEST or FULL always uses the full run.
- Budget: about 540 credits a week, about 2,350 a month. The plan refills monthly with about 4,700, leaving room for ad-hoc deep dives.

---

## Stage 1: Discovery (about 160 credits)

Shared filters: `excludedCategories: ["games"]`, `countries: ["US"]`. Research each store on its own; never mix iOS and Android figures in one number.

| Lane | Store | Filters | Limit | Why |
|---|---|---|---|---|
| A. Recent breakouts | apple_mobile | `releasedAfter` 18 months ago, `minRevenue` 20000, `sortBy: revenue` | 35 | New apps already monetizing, whatever their channel. No ads filter. |
| B. Established, underserved | apple_mobile | `releasedBefore` 24 months ago, `minRevenue` 30000, `maxRevenue` 300000, `maxRating` 4.4, `minReviews` 500 | 35 | Demand that lasts, with leaders users are unhappy with |
| C. Sustained growers | apple_mobile | `releasedAfter` 36 months ago, `minRevenue` 30000, `sortBy: revenue_growth` | 30 | Momentum. Throw out growth above 1,000% (small-base or data artifacts) |
| D. Android breakouts | google_mobile | `releasedAfter` 18 months ago, `minRevenue` 15000, `sortBy: revenue` | 30 | Android-first demand and cross-store confirmation |
| E. Organic engines | apple_mobile | `releasedAfter` 24 months ago, `minRevenue` 20000, `organicSources: ["tiktok","instagram","youtube"]`, `hasMetaAdSpend: false` | 30 | Apps growing without paid ads |

## Stage 2: Exclusions, then group into niches

**Always exclude:**
- Big Tech or household-brand publishers, and studios with 10 or more hits.
- Licensed or pirated content (IPTV, streaming aggregators, downloaders, VPN).
- Regulated categories: diagnosis, prescribing, lending, gambling, crypto trading.
- Adult or dating apps.
- Two-sided marketplaces and social networks.
- Apps that need hardware or proprietary data.
- Apps that infringe platform terms (e.g. Instagram follower scrapers).

Group the survivors into narrowly named niches. **Flags to investigate, never automatic rejects:**
- Revenue down more than 25% over 90 days. Reject only if downloads, MAU and rating confirm it. Mention seasonality.
- Meta spend above 60% of revenue. Ad spend and subscription revenue come from different cohorts, so this only means "paid-dependent". Record it as distribution risk.
- Revenue per download is **directional only**. It is not LTV. Compare it only between similar apps.
- A single publisher in the niche weakens demand evidence. It is not disqualifying if the audience is clearly defined.

## Stage 3: Shortlist (about 35 credits)

Take the 10-12 best niches and run `get_app_detail` on the strongest independent app in each. Collect:
- Price points from in-app purchases, and whether it is monthly, weekly, annual or lifetime.
- `revenue_growth_90d`, `downloads_growth_90d` and `mau_growth_90d`.
- Rating trend.
- Meta and TikTok spend for 30 and 90 days.
- Organic sources.
- Release date and publisher.

For up to 3 niches, run a depth check: `search_apps` with the niche keyword, `limit: 8`, on the store that matters. Use it to count independent publishers earning $30K or more.

Check every finalist against the **hard gates**. One fail drops the niche:

1. **Specific paying audience and problem.** Name them in one sentence ("separated parents who must document custody for court").
2. **Spending evidence.** Someone is paying for this problem, ideally 2 or more independent publishers.
3. **Achievable advantage.** One concrete edge over the reference apps: a workflow they handle badly, a result delivered much faster, or a sub-audience they ignore. "Same app, nicer UI, cheaper" fails. It must be original enough to clear Apple 4.3 and Google Play repetitive-content rules.
4. **Reachable channel.** At least one channel from the founder profile with evidence it works here (competitor ads, organic content, keyword demand, an addressable community).
5. **Buildable.** A useful first version in about 40 dev hours on the shared stack.
6. **Manageable operations.** Support, content, moderation and API costs fit a one-person operation.
7. **Plausible economics.** Base-case LTV is at least 3x CAC, or payback is 6 months or less. If paid ads fail this, an organic channel must carry the plan.

## Stage 4: Deep dive on the best 2-3 only (about 100 credits)

**Reviews.** Pull 20 from the leader and 15 from a second competitor with `get_app_reviews` (country US; use `offset` to reach older reviews). Each review costs 1 credit. Pull out:
- What users **value enough to pay for**, with quotes.
- What **fails**, with quotes.
- **Switching triggers**: price, a missing feature, a bad update.

**Economics, for each finalist, in conservative, base and upside scenarios.** Show the math.
- Monthly-equivalent price: annual ÷ 12, weekly × 4.33.
- Net monthly per payer = price × (1 − store fee) × (1 − refunds) − variable cost.
- Contribution LTV = net monthly ÷ churn.
- CAC = cost per install ÷ install-to-paid.
- Payback months = CAC ÷ net monthly.
- **Active payers needed for $40K MRR**, plus **new payers a month to hold it** (payers × churn) and the **installs a month** that implies.
- Time to reach $40K MRR at the $500 test's spend rate, then at a scaled spend.
- **Annual plans:** count them as annual ÷ 12 toward MRR. Cash collected is not MRR.

**Score the finalists that passed the gates (0-100).** A starting judgment, not a prediction.

| Dimension | Weight |
|---|---|
| Reachable distribution | 25 |
| Monetization and contribution economics | 20 |
| Demand evidence | 15 |
| Retention / repeat-use potential | 15 |
| Differentiation | 15 |
| Build and operating simplicity | 10 |

## Output: full run (the final message is the email)

```
# AppKittie Opportunity Brief: <Weekday, Mon D, YYYY>

## Bottom line
<3 sentences: what earns a test this week, why, and the one action. If nothing qualifies, say so.>

## Recommended tests (up to 5, ranked)
| # | Niche · store | Score | Who switches and why | Channel | Base-case payback | Payers for $40K MRR |

## 1. <Niche> (score N/100)
- **Audience and problem:** <one sentence>
- **Evidence (est., <store>, <date>):** <apps, publishers, revenue, downloads, 90d trends, pricing; confidence H/M/L; unknowns listed>
- **What users pay for / what fails:** <quotes>
- **Our advantage:** <one concrete edge>
- **Channel:** <how we reach them, and the evidence it works>
- **Economics:** <conservative / base / upside table: price, net, LTV, CAC, payback, payers, installs a month>
- **First version (~40 h):** <in scope> · **Not in v1:** <explicit exclusions>
- **$500 test:** question → funnel → metric → **stop if** <X> / **revise if** <Y> / **expand if** <Z>
- **Strongest reason this fails:** <one line>

## Watchlist (passed discovery, failed a gate)
<one line each: niche, gate failed, what would change the call>

## Run stats
Credits ~N/300 · Apps scanned N (iOS N / Android N) · Niches N · Detail N · Reviews N · Data: AppKittie estimates
```

Lead with the decision. No filler. No em dashes.

---

## Daily pulse (Tuesday to Friday): hard cap 60 credits

Catch new signals between Monday briefs. No stored state, so never claim to know Monday's list.

1. **New entrants (20):** apple_mobile, `releasedAfter` 45 days ago, `minRevenue` 15000, `sortBy: revenue`, `limit: 20`.
2. **Organic or Android signal (20):** alternate by day. Tue/Thu use Lane E with `limit: 20`; Wed/Fri use Lane D with `limit: 20`.
3. Apply the Stage 2 exclusions.
4. **Spotlight (≤ 20):** the single strongest survivor. Run `get_app_detail` (1), a niche depth check (`limit: 8`), and `get_app_reviews` with `maxReviews: 10`. Run it through the 7 gates and a base-case-only economics line.

```
# AppKittie Daily Pulse: <Weekday, Mon D, YYYY>

## Today's signal
<2 sentences>

## New entrants (max 5)
| App · store | Niche | Rev est. · dl est. | Released | Channel signal | Why it matters |

## Spotlight: <Niche>
Gates passed/failed · audience · advantage · channel · base-case payback · $500 test with stop/expand thresholds · strongest failure reason

## Run stats
Credits ~N/60
```
