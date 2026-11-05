# Persistent iOS opportunity engine

## Objective and constraints

Find, validate, and operate a small portfolio with a path to $30K-$50K gross subscription MRR by month six. Start the clock when the founder confirms the start date. Annual cash collection is not MRR. AppKittie estimated revenue may include non-subscription purchases; label it as estimated revenue unless the mix is established.

Assume eight founder hours a week and a 40-hour first version until corrected. That means five weeks of build capacity before marketing and support, not a one-week launch. Favor one primary product with a backup. A shared app template can reduce engineering time, but each product needs distinct utility and design.

`data/portfolio.json` is the durable registry. Reports propose changes; the weekly decision reconciles and commits them. Track rejected ideas too. Limits count discovery, shortlisted, testing, building, and live ideas as active; archived ideas remain searchable. A new idea beyond the cap must replace an existing one with a documented reason.

## Discovery lanes

iOS first, English-language audience, US distribution strategy. Verify which AppKittie filters describe language, storefront, or global metrics before using them. Never assume `countries=US` makes all metrics US-only. Use matching countries, stores, currency, and windows in comparisons.

| Lane | Starting heuristic | Purpose |
|---|---|---|
| Recent traction | Released within 24 months, est. monthly revenue $10K-$300K | Find accessible businesses with evidence of payment |
| Persistent growers | Positive absolute and percentage 30/90-day movement | Separate momentum from small-base spikes |
| Established dissatisfaction | Older apps, sustained revenue, recent workflow complaints | Find enduring problems with specific gaps |
| Reachable distribution | Search intent, repeatable creator demos, relevant communities, or persistent ads | Identify an acquisition mechanism the founder can execute |
| Narrow professional utility | Small audience, high-value repeated task | Test higher pricing and lower required payer counts |

These ranges are search heuristics, not hard eligibility rules. Look at two to four independent publishers per niche, including flat or declining comparators. Sample beyond chart winners. Do not require Meta ads, low ratings, high revenue/download ratios, or a recent launch. Ad longevity suggests continued testing, not positive ROAS. Missing ad signals do not establish organic acquisition.

## Evidence and finite list

Each idea record must contain: `id`, `status`, `audience`, `job`, `recurring_trigger`, `advantage`, `channel`, `competitors`, `evidence`, `unknowns`, `scores`, `scenarios`, `experiment`, `owner`, `updated_at`, and `next_decision_date`.

For each evidence item save: source URL or tool name, tool parameters without credentials, retrieval time, store, metric geography, metric window, value, evidence type, and confidence. Keep small normalized snapshots; do not depend on chat memory. Reviews require review IDs/URLs, dates, sampled stars, and country. Count recurring complaints across publishers and report the sampling denominator. Do not infer prevalence from a handful of negative reviews. Paraphrase by default.

States: discovery -> shortlisted -> testing -> building -> live -> scale or kill. Any state may move to watch or kill with reasons. Scores never automatically trigger a build. Prelaunch acquisition/landing-page tests can authorize a minimal product test; only measured purchases and product usage support scaling. Unknowns block promotion where the relevant gate requires evidence.

## Gates before spending build time

1. Name a specific paying audience, repeated problem, and reason to use an iPhone app.
2. Show payment evidence in at least two independent publishers, or document a strong alternative such as directly observed paid demand. A single hit is insufficient by itself.
3. Name a differentiated outcome and reachable switching audience. Cosmetic changes or lower pricing alone fail. Avoid copying assets, branding, or distinctive UI. Check Apple review rules 4.1, 4.2, and 4.3 for the proposed product.
4. Show one distribution channel with a concrete test and an identifiable audience. A competitor's ad is a lead, not proof of attainable CAC.
5. Fit a useful first version within 40 focused hours and founder capacity. Include QA, purchases/restore, analytics, onboarding, privacy, review submission, and support preparation in the estimate.
6. Default to excluding games, social networks, two-sided marketplaces, proprietary-data dependencies, licensed-content dependencies, and workflows requiring ongoing expert or regulated services. Flag health, finance, children, sensitive-data, moderation, and platform-access dependencies for scope review before promotion.
7. In the modeled base case require BOTH contribution LTV/CAC >= 3 AND acquisition payback <= 3 months. Require positive monthly unit contribution in the downside case. These are founder screening heuristics, not industry promises. If a paid channel fails, an organic strategy needs an explicit labor budget and acquisition experiment, not CAC=0.
8. Calculate required monthly acquisitions and cash to reach the target within the remaining horizon. If founder acquisition/risk budgets are unknown, label capital feasibility UNRESOLVED. Do not recommend scale before confirming them.

## Score after gates, not instead of gates

Rate each dimension 0-5, multiply rating / 5 by weight. Keep evidence confidence separate; a score of 85 is not an 85% chance of success. Unknown dimensions remain unknown and make the score provisional. Give anchors and evidence for each rating.

| Dimension | Weight | 0 / 3 / 5 anchors |
|---|---:|---|
| Reachable distribution | 25 | No route / plausible channel with competitor evidence / our measured repeatable acquisition |
| Contribution economics | 20 | Negative unit contribution / modeled gates pass / measured cohorts pass with headroom |
| Demand | 15 | Speculation / multiple independent paid comparators / direct paid demand for our proposition |
| Repeat usage and retention | 15 | One-off task / recurring trigger, retention unmeasured / our retained paying cohorts |
| Distinct advantage | 15 | Cosmetic clone / review-supported workflow improvement / users demonstrate preference and switching |
| Build and operating fit | 10 | Outside capacity / scoped MVP within capacity / functioning product and measured support load |

Proposed ranking bands: >=75 eligible for validation if gates pass; 60-74 investigate one decisive unknown; below 60 archive unless an unusually cheap test resolves the weakness. Do not fill five slots when fewer qualify. Break ties by fastest affordable falsification, then founder hours. Scores based on competitor proxies usually cannot reach the highest anchors.

## Economics

Use `scripts/economics.py` for monthly subscriptions. Run conservative, base, and upside scenarios separately. Inputs need source labels outside the calculator. Blended monthly price means actual revenue-weighted price after discounts, not the highest listed IAP. For annual/weekly plans, maintain separate cohorts and billing schedules; the monthly calculator must not be presented as an annual cash-flow model.

- Monthly contribution per payer = price x (1-refund rate) x (1-store fee) - variable cost.
- Variable cost includes AI/API use, free-user/trial cost allocated per payer, storage, hosting, and variable support. Stress test heavy usage.
- Paid CAC = CPI / install-to-paid conversion, with a consistent attribution/conversion window and fully matured trials. Blended CAC includes creator fees, creative production, and attributable channel labor; report cash and labor separately.
- Contribution LTV approximation = monthly contribution / monthly payer churn. This assumes constant churn, price, and cost and is a sensitivity analysis until mature cohorts exist.
- New payers arrive at month end, so `payers[t] = payers[t-1] x (1-churn) + new_payers[t]`. This simplifies billing and overstates revenue if arrivals are spread across the month. Cash outputs are planning approximations.
- Show target maintenance acquisitions separately from growth acquisitions. Include development/prelaunch months with zero acquisitions. Use remaining months after launch, not six selling months when the build consumes two.
- Model both $30K and $50K endpoints. Report gross MRR, net proceeds, contribution before/after acquisition, required spend, and cumulative funding gap plus fixed/build costs. A business can hit revenue while losing money.

## Validation sequence

1. Problem check: 5-10 relevant users, current workaround and recent spending. Support the mechanism, not a statistically representative market claim.
2. Proposition/channel test: two distinct promises or creative angles. Use a transparent concept/waitlist page. Measure qualified visit cost and explicit price intent. Email signups do not establish install-to-paid conversion or retention.
3. Product test: minimal useful iOS product with onboarding, activation event, purchase funnel, refunds, and repeated usage instrumentation. Test real price with real customers. A few purchases are directional, not a scale signal.
4. Cohort check: report D1/D7/D30 meaningful-use retention as appropriate to task frequency, trial-to-paid on matured trials, renewals by plan, cancellations, refunds, AI cost, and support time. Annual renewals cannot be known in a six-month window.

Before each test write a falsifiable hypothesis, sample/spend/time cap, success/kill thresholds, and one permitted iteration. Derive conversion thresholds from maximum CAC, not generic conversion benchmarks. With zero conversions in n independent installs, the approximate 95% upper conversion bound is 3/n; use it only as an approximate diagnostic. Spend alone is not a sample-size target. A $500 cap is an initial discovery budget and can be inconclusive. Stop at the cap and report INCONCLUSIVE rather than inventing certainty.

## Cadence, ownership, and credit control

Monday full discovery: Claude proposes changes and two validation candidates. Codex independently checks evidence scope, economics, build feasibility, and strongest failure case. Founder chooses at most one new product commitment in a weekly 30-minute review. Daily pulse: monitor existing finalists and active tests, report material changes and one action; do not replace the shortlist each day. Reserve roughly 20% of research for challengers.

Weekly research ceiling 500 credits: 100 discovery rows + 20 detail/history calls + 40 niche-depth rows + 120 review rows + 60 ad/creator rows + 40 keyword credits + 120 for four daily pulses at 30 each. This totals 500 under currently documented billing. Reserve BEFORE calls, track actual costs, and reduce samples if plan limits differ. Reviews cost per returned review; keyword requests can be much more expensive than detail calls. Cache unchanged evidence within the run and avoid both agents purchasing identical evidence. A second agent reviews the same snapshots first.

Save normalized evidence under `data/snapshots/YYYY-MM-DD/`, reports under `reports/YYYY-MM-DD-{scout,audit,pulse,decision}.md`, and test plans/results under `experiments/<idea-id>/`. Each run records start/end time, status, credits, changed ideas, and next action. On authentication or data failure report FAILED/PARTIAL and preserve prior state; never substitute stale values without labeling them.

GitHub access does not transfer MCP credentials between Claude and Codex. Configure each execution environment. Interactive MCP access does not create a scheduler. Keep the current daily/weekly jobs only if their runner can check out this branch, inject the key, call tools, and persist outputs. Otherwise wire a separate runner after confirming its auth, billing, and secret behavior. This starter does not install or activate scheduled jobs.

## Weekly decision output

Show at most five ideas: stable ID, audience/problem, competitor payment evidence, proposed advantage, channel, score/confidence, base/downside economics, target acquisitions/spend, gate status, changed evidence, verdict, owner, next action. Verdicts: TEST / PRODUCT TEST / BUILD / HOLD / KILL / SCALE. End with one founder decision, the strongest objection, and what evidence would reverse it.

## Sources checked 2026-11-05

- https://www.appkittie.com/docs
- https://github.com/AppKittie/aso-mcp-skills/blob/main/README.md
- https://learn.chatgpt.com/docs/extend/mcp?surface=cli
- https://developer.apple.com/app-store/review/guidelines/

Recheck live schemas and billing before running. Fee rates depend on account, program, region, and transaction terms; confirm the actual rate instead of assuming enrollment.
