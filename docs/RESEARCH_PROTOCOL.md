# AppKittie Opportunity Research Protocol (portable)

Version 2.0, 2026-11-06. Any automated runner can execute this: Claude, Codex, or a script plus an LLM. It does not depend on any one agent's tools. Where it says "call X", use whatever client reaches the AppKittie MCP server: native MCP tools, or JSON-RPC over HTTPS at `https://mcp.appkittie.com` with the `Authorization: Bearer $APPKITTIE_API_KEY` header. Never print, log or commit the key.

## 1. Purpose and portfolio target
- Find app opportunities that deserve a **bounded demand test**, not a build. A build needs real customer evidence from a test.
- **Portfolio target:** $30-50K per month in total, across several apps. **Open decision:** whether this means gross consumer revenue or net to the developer. Reports must state which basis they use.
- **Launch target:** 2-3 a month, subject to validation and development capacity.

## 2. Roles
| Role | Owner | Responsibilities |
|---|---|---|
| Discovery and customer-problem lead, final presenter | Claude | Monday discovery, Wednesday and Friday finalist checks, the side-by-side comparison, the final report |
| Independent auditor | Codex | Re-checks evidence, economics, distribution assumptions and implementation scope against the saved artifacts. Gives an independent status per candidate. |
| Decision owner | Usman | Approves tests and builds, sets founder-profile values, settles disagreements |

**No agent may claim the other's agreement until the other's written audit file exists.**

## 3. Weekly cadence (America/Chicago)
| Day | Activity | Credit cap | Output |
|---|---|---|---|
| Monday | Full discovery and evidence collection (Stages 1-4) | 300 | `research/<date>/` evidence pack + `discovery.md` (draft statuses) |
| Tue-Thu | Codex audit of Monday's pack | 0 new credits unless Codex needs a re-pull (log it) | `research/<date>/audit/codex.md` |
| Wednesday | Targeted checks on finalists only (gaps named in the draft or audit) | 60 | `research/<date>/checks_wed.md` |
| Friday | Targeted checks (60 credits), then **the single final weekly report** with the audit included | 60 | `research/<date>/report/final.md` |

- **One final report a week.** Claude and Codex never deliver separate reports to the owner.
- **No separate daily delivery.** Wednesday's and Friday's checks are working files, not reports.
- **Budget:** about 420 credits a week, about 1,800 a month, against a monthly refill of about 4,700.
- **The final-report day is Friday by default.** The owner can change it.

## 4. Work-in-progress limits (hard)
- At most **1 new recommended experiment per week.**
- At most **2 experiments active** at once.
- At most **1 build active** at once.

If a limit is reached, the report recommends **what to stop or finish first**. It never adds a new item.

## 5. Status definitions
| Status | Meaning | Entry criteria |
|---|---|---|
| **RESEARCH** | Material evidence gaps remain | Default for any candidate that passes the exclusions |
| **TEST** | Ready for a bounded demand experiment | Passes the hard gates in section 8 on evidence that is on disk; experiment pre-registered (section 11); within WIP limits; no unresolved MATERIAL disagreement |
| **BUILD** | Real customer evidence justifies development | A pre-registered test hit its **expand** thresholds; Codex audit of the test result shows no unresolved MATERIAL disagreement; build WIP slot free |
| **HOLD/STOP** | Failed a gate, or unresolved material disagreement | HOLD: a fixable gap or disagreement (state what would reopen it). STOP: failed on evidence (state the evidence). |

**Rules:**
- **Every status names its evidence files.**
- **Claims backed only by unsaved data are labeled UNVERIFIED and cannot carry a TEST or BUILD decision.**

## 6. Evidence handling (mandatory)
1. **Save every AppKittie response to disk at call time:** `research/<date>/raw/<run>_<step>_<tool>_<slug-or-query>.json`. Append its SHA-256 to `raw/SHA256SUMS`.
2. **Log every call in `research/<date>/MANIFEST.md`:** tool, full parameters, UTC time, count returned, file name, estimated credits. Log errors too (401, 404).
3. **Label every number in a report:** RAW (with file and field), UNVERIFIED (transcribed or memory), or ASSUMPTION (founder profile).
4. **Never fill gaps with invented data.** Missing means "unknown".
5. **AppKittie data facts:**
   - Revenue and downloads are **monthly estimates**; precision is often coarse (round numbers).
   - `countries` filters by **app language, not storefront**. Record the storefront from the app URL.
   - Missing `meta_ads_transparency` means unavailable, **not zero**.
   - New apps show 0 for 90-day growth fields. That means no history.
   - Large `get_app_detail` responses (up to ~1 MB) must be parsed with a JSON tool, not read whole.
   - A 404 on a guessed slug is free. Always take slugs from search results.
   - Pricing: search ~1 credit per app returned; details 1; reviews 1 per review; keyword tools ~10.

## 7. Monday discovery (cap 300 credits)
Common filters: `excludedCategories: ["games"]`, `countries: ["US"]`. Research each store separately; never combine iOS and Android numbers.

### Stage 1: lanes (~160 credits)
| Lane | Store | Filters | Limit |
|---|---|---|---|
| A. Recent breakouts | apple_mobile | releasedAfter = today − 18 months, minRevenue 20000, maxRevenue 400000, sortBy revenue | 35 |
| B. Established, underserved | apple_mobile | releasedBefore = today − 24 months, minRevenue 30000, maxRevenue 300000, maxRating 4.4, minReviews 500, sortBy revenue | 35 |
| C. Sustained growers | apple_mobile | releasedAfter = today − 36 months, minRevenue 30000, maxRevenue 400000, sortBy revenue_growth; **discard growth above 1,000%** | 30 |
| D. Android breakouts | google_mobile | releasedAfter = today − 18 months, minRevenue 15000, maxRevenue 400000, sortBy revenue; **drop Google Play game genres** (Action, Puzzle, Casual, Strategy, Role Playing, Simulation, Casino, Arcade, Card, Board, Word, Racing, Sports) | 30 |
| E. Organic engines | apple_mobile | releasedAfter = today − 24 months, minRevenue 20000, maxRevenue 400000, organicSources [tiktok, instagram, youtube], hasMetaAdSpend false | 30 |

### Stage 2: exclusions and grouping
**Exclude:**
- Big Tech or household-brand publishers, and studios with 10+ hits.
- Licensed or pirated content (IPTV, streaming aggregators, downloaders, VPN).
- Regulated categories: diagnosis, prescribing, lending, gambling, crypto trading.
- Adult or dating apps.
- Two-sided marketplaces and social networks.
- Apps that need hardware or proprietary data.
- Apps that violate platform terms.

Group the survivors into narrowly named niches.

**Flags to investigate, never automatic rejects:**
- Revenue down more than 25% over 90 days. Reject only if downloads, MAU and rating confirm it. Mention seasonality.
- Meta spend above 60% of revenue. This only marks the niche as dependent on paid ads.
- Revenue per download. Directional only; compare within a niche.
- A single publisher. Weak evidence of demand.

### Stage 3: shortlist (~35 credits)
1. Run `get_app_detail` on the strongest independent app in each of the top 10-12 niches. Collect:
   - Pricing from in-app purchases.
   - 90-day revenue, downloads, MAU and rating trends.
   - Meta and TikTok spend.
   - Organic sources, release date, publisher.
2. For up to 3 niches, run a depth check: `search_apps` with the niche keyword, `textSearchFields: ["title","description"]` and the niche's category, limit 8. Count the independent publishers earning $30K or more.

### Stage 4: deep dive on the best 2-3 (~100 credits)
1. **Reviews:** 20 from the leader and 15 from a second competitor, US, using an offset to reach older reviews. Extract:
   - What users pay for (with quotes and review IDs).
   - What fails (with quotes and IDs).
   - What makes them switch.
2. **Economics:** section 9.
3. **Score:** section 10.

## 8. Hard gates (all must pass for TEST)
1. **A specific paying audience and problem,** in one sentence.
2. **Proof people already pay for it,** ideally 2 or more independent publishers. Note the storefront.
3. **One concrete, achievable advantage.** "Same app, cheaper, nicer UI" fails. It must be original enough to clear Apple guideline 4.3 and Google Play's repetitive-content policy.
4. **At least one channel from the founder profile that you can reach,** with evidence it works in this niche.
5. **A useful first version in about the founder's build budget,** on the shared stack.
6. **Support, content, moderation and API costs** that one operator can handle.
7. **Plausible economics:** base-case lifetime value ≥ 3× the cost to acquire a payer, or payback ≤ 6 months. If paid ads fail this, an organic channel must carry the plan, and that channel must have evidence.

## 9. Economics (show formulas; label all inputs)
- **Monthly-equivalent price:** annual ÷ 12; weekly × 4.33.
- **Net monthly per payer** = price × (1 − store fee) × (1 − refunds) − variable cost.
- **Lifetime value** = net monthly ÷ churn.
- **Cost to acquire a payer** = cost per install ÷ install-to-paid conversion.
- **Payback months** = cost to acquire ÷ net monthly.
- **Annual-plan cash check:** the net annual price at purchase vs the cost to acquire a payer. Note the renewal-churn caveat.
- **Payers for the target** = target ÷ (gross price **or** net per payer). **State the basis.**
- **New payers a month to reach the target in 12 months** at churn c = target payers × c ÷ (1 − e^(−12c)).
- **Installs a month** = new payers ÷ conversion.
- **Paid budget** = paid share × new payers × cost to acquire a payer.
- **Paid-only ceiling:** a monthly budget B plateaus at (B ÷ cost to acquire) ÷ churn payers.

Run every figure under the conservative, base and upside scenarios.

## 10. Scoring (only after all gates pass)
A starting judgment, not a prediction. A high score earns a test, nothing more.

| Dimension | Weight |
|---|---|
| Reachable distribution | 25 |
| Monetization and contribution economics | 20 |
| Demand evidence | 15 |
| Retention / repeat use | 15 |
| Differentiation | 15 |
| Build and operating simplicity | 10 |

## 11. Experiments (pre-registration required)
Create `experiments/EXP-<yyyy>-<nn>-<slug>/plan.md` from `experiments/TEMPLATE.md` **before spending anything.** It must contain:
- The question.
- The funnel.
- The budget (≤ $500 unless the owner approves more).
- The duration.
- The primary metric.
- **Stop / revise / expand thresholds.**
- The data captured.

Write the results to `results.md` with the raw exports in `data/`. **Thresholds can't be changed after launch.** A deviation must be logged and explained.

## 12. Founder profile (owner-editable; cite values as ASSUMPTION)
| Parameter | Value |
|---|---|
| Build budget per first version | 40 focused dev hours (30-50 range) |
| Shared stack | Expo (React Native) + EAS, Supabase, RevenueCat, hosted LLM API, Next.js on Vercel for landing pages |
| Test budget per idea | $500 |
| Channels | Meta ads, TikTok/Instagram creators (paid seeding), app store search, LinkedIn and professional networks, niche communities |
| Store fee | 15% (Apple Small Business Program, assumed enrolled) |
| Churn / conversion / cost per install (C/B/U) | 15% / 10% / 6% · 2% / 3% / 5% · $5 / $3.50 / $2 |
| Refunds | 3% |
| Variable cost | Estimated LLM/API cost per active payer per month |

## 13. Candidate registry
`research/candidates.csv` is the single list carried across weeks. Fields:
- id, niche, status, status_date, owner_status_claude, owner_status_codex
- disagreement (Y/N), evidence_files, next_action, experiment_id

Update it with every report. Never delete rows; change their status.

## 14. Final weekly report format (`research/<date>/report/final.md`)
1. **Decision summary:** the one experiment recommended this week (or none), WIP status, and what to stop.
2. **Side-by-side comparison table:** one column per finalist. Rows:
   - Evidence, with sources, dates, region, platform and confidence.
   - Target customer and reason to switch.
   - Competitor pricing, and our pricing hypothesis.
   - Economics in conservative, base and upside.
   - Payers, installs, budget and time to the target.
   - First version, with explicit exclusions.
   - The $500 test with stop, revise and expand thresholds.
   - The strongest reason it fails.
   - **Claude status | Codex status | Final status.**
3. **Audit incorporation:** every MATERIAL Codex finding and how it was resolved, or that it **remains unresolved.**
4. **Unresolved disagreements:** a table of claim, Claude's position, Codex's position, evidence, and the impact on status. **Do not force consensus.** Unresolved MATERIAL disagreement means HOLD.
5. **Watchlist and rejects,** with reasons and what would reopen each.
6. **Experiment results to date,** from `experiments/`.
7. **Expert recommendation:**
   - Verdict, naming one candidate.
   - Why.
   - The next 7 days.
   - What would change the recommendation.
   - Portfolio view.
   - Contrarian check.
8. **Run stats:** credits by day, calls, and RAW vs UNVERIFIED counts.

Style: lead with the decision. No filler. No em dashes.
