# Codex audit: Claude's November 5 AppKittie handoff

## Decision

Prioritize co-parenting records for a bounded problem-and-workflow investigation, not a build or paid acquisition launch. No candidate currently has sufficient evidence for BUILD. Claude proposes TEST for co-parenting; Codex assigns RESEARCH. Under Claude's proposed reconciliation rule, the final promotion decision remains HOLD until that material disagreement is resolved. The other four remain RESEARCH.

This audit evaluates retained November 5 evidence, not fresh market conditions. No AppKittie credits, advertising, or outreach were used. Codex has not obtained a subsequent Claude response and does not claim joint endorsement.

## Provenance and checks

- Claude branch: `claude/brave-edison-1w73tu`, exact commit `52bf3d5fe5470870c76c823eeb6b8ee805dbb5e5`.
- Codex policy branch: `codex/persistent-opportunity-engine`, exact commit `6e9e2773ee433a2c6f11d9e0d3dcdbeca9a67a0d`.
- Both were fetched and inspected in temporary exported directories. Neither branch was merged, reset, or replaced. Audit outputs are new local files in the existing checkout.
- All 11 retained raw-response checksums passed. This establishes consistency with the supplied checksum list, not independent vendor authenticity or accuracy.
- All eight detail extracts matched raw revenue, downloads, rating, review count, and the five audited growth fields. The eight records include Documented twice; they represent seven unique apps.
- The three retained searches each contain 35 rows; the CSV contains 105 rows. Results can overlap and are not necessarily unique apps.
- Review quotes and transcript-only competitor claims cannot be independently verified from this handoff; no full review responses were retained.
- Existing monthly calculator tests: 7 passed. The calculator's stricter gate and monthly-only billing limitation remain unchanged; test success does not validate the business assumptions.

Source references below are paths at the Claude commit above unless otherwise specified. Do not describe them as files present in the current checkout.

## Findings

| ID | Section / claim | Verdict | Evidence / reasoning | Severity | Proposed status change |
|---|---|---|---|---|---|
| A01 | Handoff §1: retained app-detail estimates | CONFIRMED | `evidence/detail_extract.jsonl` agrees with retained `raw/*detail*.json` for audited fields. These remain vendor estimates. | MATERIAL | Supports RESEARCH, not validation of our product |
| A02 | Earlier US-only revenue labels | DISPUTED | Query country filter describes language; a storefront URL does not establish revenue geography. Handoff correctly withdraws US-only attribution. | MATERIAL | Require unknown geography labels |
| A03 | Earlier mise has no paid ads | DISPUTED | `raw/run2_detail_mise.json`, `data.tiktok_ads_total_count = 417`; Meta transparency is null. Known creative count is not active-ad count, spending, or profitability. | MATERIAL | Remove organic-only claim |
| A04 | Documented is organic because Meta spend is $488.75 | UNVERIFIABLE | Retained Meta estimate supports only that observed channel estimate; other spending, acquisition channels, and attribution are unknown. | MATERIAL | Co-parenting stays RESEARCH |
| A05 | Documented/HolyNote zero 90-day growth means no history | UNVERIFIABLE | Responses contain zero; both were younger than 90 days at retrieval. Treat as insufficient evidence for a 90-day trend, not a proven encoding rule or flat growth. | MATERIAL | Trend unavailable pending history |
| A06 | Low-quality competitor workflows and customer quotes | UNVERIFIABLE | `evidence/review_quotes.md` explicitly labels transcribed excerpts unverified; no retained full sample. Selection cannot establish complaint prevalence. | MATERIAL | Verify before promotion |
| A07 | Co-parenting's multiple independent paying comparators | UNVERIFIABLE | Documented is raw-backed; OurFamilyWizard and TalkingParents headline figures/prices are transcript-only. | MATERIAL | RESEARCH rather than TEST |
| A08 | Annual-first makes co-parenting acquisition pay for itself | DISPUTED | At $149/year, 15% fee, 3% refunds: $122.85 receipts before servicing; subtract $6 annual variable cost and $116.67 assumed CAC leaves about $0.18 before fixed costs. CAC and mix are unmeasured. | MATERIAL | No automatic promotion |
| A09 | All five pass paid acquisition screen | DISPUTED | Monthly-only base paybacks range 9.84–18.85 months; LTV/CAC 0.53–1.02. None passes even the legacy six-month OR 3× screen. | MATERIAL | Require evidenced alternative acquisition and measured test |
| A10 | Full co-parenting scope fits 40 hours | UNVERIFIABLE | OCR, trustworthy timestamps, secure storage/sharing, reliable exports, purchases, deletion, QA and release work lack estimates. Hashing alone does not establish independent capture time or court acceptance. | MATERIAL | Scope prototype before BUILD |
| A11 | GLP-1 photo protein logging differentiates | DISPUTED | Transcribed MeAgain review says photo logging already exists. This challenges the thesis but needs verification. Retained PeptidePal has revenue −15.7%, downloads −71.9%, MAU −8.48% over 90 days. | MATERIAL | RESEARCH; investigate existing feature |
| A12 | Checked crochet patterns are an automated low-operations business | UNVERIFIABLE | Designer supply, rights, compensation and human pattern checking have not been established. These are ongoing work and costs. | MATERIAL | RESEARCH |
| A13 | Exact full-basket pricing without store-price data | DISPUTED | Prices require a source, location, pack sizes and updates. Without these, offer editable estimates, not exact or live basket costs. Allergy suitability also needs explicit ingredient checking. | MATERIAL | Narrow meal-planner scope |
| A14 | Sermon-note differentiation and second publisher | UNVERIFIABLE | HolyNote details retained; Bible Note figures and complaints transcribed. Lower prices and sync fixes alone do not establish a durable switching advantage. | MATERIAL | RESEARCH |
| A15 | Twelve-month path at 25% paid acquisition fits budget | DISPUTED | Earlier table requires $11K–$21K monthly ads, far above $500 total/month. Remaining 75% acquisition is assumed, not measured. | MATERIAL | Withdraw timeline as forecast |
| A16 | Eight hours/week, three-month AND gate, six-month target are owner decisions | DISPUTED | They appear in the Codex branch, but this conversation supplies different capacity intent and no approved target deadline. Owner corrected budget to $500/month total marketing/validation. | MATERIAL | Reconcile before merging policy |
| A17 | Persisting docs creates automated reports | DISPUTED | Both branches describe workflows; neither inspection demonstrates an operating scheduler, cross-model runner or delivery integration. | MATERIAL | Automation remains unverified |

## Independent candidate decisions

| Rank for next investigation | Candidate | Claude proposal | Codex status | Final promotion status | Decisive next check |
|---|---|---|---|---|---|
| 1 | Co-parenting personal records | TEST | RESEARCH | HOLD: material disagreement | Verify leader/review evidence; determine whether parents can use a supplementary log; test sample-export utility with target users and attorneys |
| 2 | Checked crochet patterns | RESEARCH | RESEARCH | RESEARCH | Validate designer participation, rights, checking labor and paid demand before committing to a content catalog |
| 3 | Restricted-diet meal planning | RESEARCH | RESEARCH | RESEARCH | Pick one audience; verify its complaints and willingness to pay; demonstrate editable basket estimates with a legitimate price source |
| 4 | Structured sermon notes | RESEARCH | RESEARCH | RESEARCH | Verify second publisher and complaints; test a distinctive group workflow and willingness to pay rather than a cheaper transcription clone |
| 5 | GLP-1 companion | RESEARCH | RESEARCH | RESEARCH | Verify existing photo logging and find an unserved non-advice workflow; do not include dosing or tapering recommendations |

This is an investigation priority ranking, not a scored list of gate-passing products. It intentionally differs from Claude's order. The two earlier independent top-five lists were not compared on equal evidence; neither is declared the market's best five.

## Recomputed economics

Machine-readable results: `economics.json` alongside this audit. All prices for our products and costs are assumptions reconstructed from Claude's earlier table, not measured customer behavior. No subscription mix is established, so monthly and annual cases remain separate.

Formulas: contribution = price × 0.85 × 0.97 − monthly variable cost; CAC = CPI / paid conversion; approximate monthly-plan LTV = contribution / churn; payback = CAC / contribution. Base CPI $3.50, conversion 3%, churn 10%. Six-month allowable CAC = contribution × 6, before fixed costs. Lifetime purchases require a separate model.

| Idea | Assumed monthly price / variable cost | Monthly contribution | Base LTV/CAC | Base payback | CAC ceiling for six-month payback |
|---|---|---|---|---|---|
| Co-parenting | $14.99 / $0.50 | $11.86 | 1.02× | 9.84 months | $71.16 |
| GLP-1 | $12.99 / $0.80 | $9.91 | 0.85× | 11.77 months | $59.46 |
| Crochet | $7.99 / $0.20 | $6.39 | 0.55× | 18.26 months | $38.33 |
| Meal planning | $9.99 / $0.30 | $7.94 | 0.68× | 14.70 months | $47.62 |
| Sermon notes | $7.99 / $0.40 | $6.19 | 0.53× | 18.85 months | $37.13 |

At a constant $116.67 paid CAC, the entire $500 monthly ceiling purchases about 4.29 new payers/month before creative or other marketing costs. At assumed 10% monthly churn, the monthly-plan steady-state ceiling is about 42.9 payers. For co-parenting at $14.99/month, that is approximately $642 gross MRR, not $40K. This is a sensitivity calculation, not a forecast; meaningful growth needs a different measured acquisition mechanism, reinvestment, or additional capital.

Annual cohorts need renewal assumptions, service costs, cash timing and actual plan mix; monthly churn must not be used as annual renewal evidence. Annual upfront receipts do not establish six-month contribution payback or lifetime profitability.

## Policy reconciliation for the first report

| Topic | Baseline supported by this conversation | What is not established |
|---|---|---|
| Capacity | Automate development toward 2–3 launches/month; estimate actual execution and owner work per app | Unlimited effective capacity or guaranteed launch rate; discard the old eight-hour assumption |
| Economics | Retain the repository's existing modeled screen: six-month payback OR 3× LTV/CAC; show downside separately | The stricter three-month AND rule was not approved here. Even six months does not promote co-parenting on current inputs |
| Revenue | Show $30K–$50K gross subscription MRR and net proceeds/contribution separately as a working reporting convention | Owner-approved deadline or take-home-profit target; no invented six-month deadline |
| Budget | $500/month shared across validation, marketing and ads; use a ledger across experiments | $500 per idea; whether model/AppKittie subscriptions are inside that cap remains unconfirmed |
| Cadence | Weekly discovery/audit, targeted Wed/Fri checks only when decision-relevant, brief weekday status | Daily full discovery or an activated schedule |
| Final report | Friday is a reasonable working default; current delivery is this chat plus saved artifact | Specific time, recurring delivery destination, scheduler and cross-model execution remain unconfigured |
| Shared policy | Use the richer registry/economics with agreed cadence and status labels | Branches have not been merged; two policies still exist remotely |

Do not change calculator code to manufacture a pass. A shared-policy merge should first replace stale assumptions in both instruction entry points, retain one registry, and label the annual-model limitation. The existing monthly calculator can provide numbers; its embedded gate flag must not be reused under a different policy without a tested change.

## Next action

Proceed with co-parenting research only: inspect a concrete sample export with parents and family-law practitioners, and establish whether a supplementary personal log solves a problem the mandated communication app does not. Any interview or outreach needs explicit authorization and a channel; none was sent here. Verify missing competitor/review evidence before spending on ads. Do not promise court acceptance, tamper-proof history, or legal outcomes.

Send this audit to Claude for its actual response. Only then can the report show a reconciled position. No evidence currently authorizes a BUILD recommendation.
