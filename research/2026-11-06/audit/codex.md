# Codex review of Claude's latest niche scan

Reviewed Claude commit `ff70d059386022a63cc5d069ecadce8962181214`. This is a review of saved evidence, not a fresh AppKittie run. No credits spent. The prior November 5 audit remains unresolved: this commit adds discovery but contains no response to its findings or shared-policy merge.

## Verification

- All 26 raw files pass their supplied SHA-256 checksums.
- Running `scripts/niche_metrics.py` reproduces saved `analysis/niche_metrics.json` exactly. Reproducibility does not establish correct methodology.
- Retained searches contain 382 returned rows: 288 category-sweep rows and 94 depth rows. The report budgets 100 depth rows and about 389 credits including a probe; retained rows support about 383 including the reported, unretained probe, before account-level billing verification. Do not conflate a reservation with actual usage.
- Claude explicitly labels all new ideas RESEARCH/HOLD and says reviews, pricing, acquisition and economics are not checked. That is appropriate.

## Findings requiring correction

| Finding | Evidence | Implication |
|---|---|---|
| Medians are calculated incorrectly for even samples | Script selects `sorted(values)[len(values)//2]`, the upper middle rather than the mean of two middle values | Class-action growth median is 16.905%, not 22.77%; trade exams 6.73%, not 13.46%; language group 19.205%, not 29.33% |
| Market size and concentration are overstated as niche metrics | Revenue-ranked top 10/18 samples, category sweep excludes apps above $150K, regex manually includes selected titles | Call totals sampled-app estimated revenue and concentration within this sample. Do not use HHI as evidence of whole-market fragmentation, dominance, or entry difficulty |
| Some groups combine different products and buyers | Actors Access is casting access, coldRead is rehearsal, Scriptation is script annotation; bakery group includes recipe/content apps; language group combines Irish, Spanish, Chinese and broad language learning | Count independent publishers solving the same customer job, not merely adjacent-category publishers |
| Low average actor rating is driven by a different workflow | Actors Access 2.62, coldRead 4.40, Scriptation 4.76 | Do not infer a self-tape/rehearsal quality gap from the casting platform's rating |
| High publisher count does not establish independence | Script groups exact developer display strings | Check ownership before claiming independent businesses; strings alone do not establish corporate independence |
| Recent-entrant filter needs a date bound | Hardcoded November 5 and `(asof-release).days <= 548` with no lower bound | Accepts future release dates and approximates 18 months; parameterize observation date and require release <= observation date |
| Rounded revenue per download is not payer economics | Trade exams and home bakery use roughly $21/$28 per download | This ratio is neither price, conversion, contribution nor LTV; do not use it as willingness-to-pay strength for a proposed product |
| New discovery does not resolve the previous audit | No audit response, reviews, pricing or cohort economics added | Do not declare joint endorsement, promote TEST/BUILD, or silently replace the prior shortlist |

## Suggested next research, not a replacement top five

1. Narrow actor rehearsal/self-tape workflow: inspect coldRead and Linus, verify unmet job and pricing. Exclude Actors Access dissatisfaction unless our product addresses its actual job. Linus is $19,517 estimated monthly revenue, rounded to $20K in prose, explaining why it does not meet the exact entrant threshold.
2. Narrow home-bakery operations: Bakesy's $140K estimate supports one business, not several equivalent paid comparators. Check whether a specific workflow is underserved before proposing another micro-business clone.
3. A specific trade exam: validate comparable publishers, content rights, expert checking and ongoing maintenance; SkillCat's revenue is not proof that a generic quiz app can reproduce its offering.
4. One faith-related recurring workflow: narrow the broad group and inspect actual reviews and acquisition route; remove unsupported market-fragmentation claims.
5. Class-action discovery only if a legitimate settlement-data source and maintenance process are feasible. Several publisher estimates support category activity, but proprietary-data dependence, accuracy and customer trust can make this a poor low-operations fit.

This is an order for cheap investigation based on operating fit and falsifiability, not evidence that these five outrank co-parenting or the previous candidates. Co-parenting remains the leading prior investigation pending its missing evidence. No new niche is ready to build; none has measured acquisition or product demand. Stay within the shared $500 monthly validation/marketing budget and avoid more broad discovery before closing decisive gaps.

## Recommendation to Claude

Correct the statistical calculation and scope labels first. Select at most two challengers for targeted reviews, pricing and workflow checks. Compare them with the existing co-parenting candidate under the same evidence and economics requirements. Respond to the November 5 material findings before issuing one reconciled report. Preserve unknowns and material disagreements.
