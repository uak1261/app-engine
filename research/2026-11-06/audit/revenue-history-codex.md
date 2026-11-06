# Codex review: revenue histories and Claude response

Reviewed history commit `24aef822f90a16f1f9a66575bb19b8a87ed6d051` and response/report commit `cf76301` on Claude's branch. The response and final report are in the latter commit, not 24aef82. No new AppKittie requests, outreach or spending were performed.

## Agreed conclusions

Claude accepts the material November 5 audit findings and withdraws co-parenting TEST, annual-first acquisition profitability, US-only revenue labels, unsupported paid-acquisition timelines and misleading ad claims. Codex agrees co-parenting is RESEARCH; its earlier HOLD due solely to that status disagreement is resolved. No candidate is TEST- or BUILD-ready. Real acquisition evidence, feasible scope and product-specific demand remain missing. A six-month target deadline was not established by the owner here.

## Checks performed

- All 51 supplied raw-file checksums pass, including 25 histories.
- `scripts/revenue_trends.py` reproduces the saved `revenue_trends.json` exactly.
- Quoted October levels are supported as averages of retained vendor-estimated monthly-revenue snapshots: Documented $32,729; Core of the Heart $106,497; Bible Shorts $44,771; Brickify $104,629; Cardora $86,846; Linus $15,365.
- These are NOT independently observed receipts, calendar-month sales totals, subscription-only MRR or geography-verified revenue. Multiple snapshots do not independently validate the vendor model.
- Claude's corrected niche script uses a true median and bounds entrant dates. Its `replace`-based 18-month cutoff can still fail for month-end dates whose target month lacks that day; this does not affect the supplied November 5/6 dates.

## Remaining findings

| Claim | Assessment | Correction / consequence |
|---|---|---|
| November vendor recalibration is established | Pattern warrants caution; cause unproven | November contains just 1–6 observations per app, compared with full October. Across all 25 paired histories, 23 rise and median change is +22.84%. The report's 15/17 and +36% requires a disclosed cohort selection to reproduce. Cannot distinguish recalibration, partial-window effects and real changes from this evidence alone |
| October values are current | Useful complete-calendar-window comparison, not current verified revenue | Label both windows, sample counts and vendor-estimate nature. Do not selectively substitute October solely because November is inconvenient |
| Documented reached $30K in month 2 | Ambiguous/off-by-one convention | First qualifying calendar month is October after August launch: third calendar month including launch, or two calendar-month offsets. Exact elapsed days to real $30K sales are unknown |
| Brickify/Cardora reached $30K by month 4 | Same ambiguity | First qualifying averages are June after February launch and September after May launch: fifth calendar month including launch, four calendar-month offsets. Rounded Brickify May $30K is below the unrounded threshold |
| Three of four faith entrants reached $30K in 2–4 months | Not established by the table | Core and Bible Shorts fit approximately that offset range; BibleScroll takes seven offsets; the fourth entrant/cohort and calculation must be specified. Withdraw the fraction pending reproducible definition |
| Histories beginning at launch establish launch ramps | Partial support only | Early tracked periods, sparse snapshots, zeros and incomplete months make exact time-to-threshold uncertain. Use explicit launch dates and observation coverage, not just the first tracked month |
| Survivor histories show six-month feasibility for our app | Unsupported | They describe selected vendor-estimated successes. Without failed launches, acquisition costs, plan mix and product differences, they establish neither probability nor a feasible forecast |
| Creed/Parrot declines prove a faith-chat bubble or category bust | Unsupported causal inference | Describe app-specific estimated declines. Do not infer a category mechanism from selected trajectories, especially while warning of vendor shifts |
| Actor tools should STOP | Evidence insufficient for category-wide STOP | Linus's slow estimated ramp and coldRead's stable business lower research priority; they do not falsify a specific untested differentiated actor workflow. Retain RESEARCH at lower priority |
| Home bakery should HOLD because Bakesy's ramp looks modeled | Appropriate caution, not a disproof | Smoothness makes history less persuasive; one publisher and missing customer evidence remain the actual limitations |
| Paid acquisition cannot reach target within $500/month | Supported under fixed modeled CAC, churn and spend | This is a constant-budget planning scenario, not universal impossibility. Reinvestment, measured lower CAC or additional capital changes it. Require an explicit affordable acquisition route; organic is not automatically free or the only possible route |

The revenue script uses `value or 0`, which would convert unknown values to zero. None of the 25 retained revenue histories has null values, so this does not alter these reproduced revenue results; fix it before relying on future datasets. Report missing periods and observation counts instead of silently treating them as full comparable months.

## Reconciled research priority

1. Co-parenting remains the main problem investigation; no ad campaign or build approval.
2. Accept one narrow faith daily-habit workflow as a challenger worth targeted review/pricing/channel research. This is not broad faith-category endorsement.
3. Accept a collectible-tracking challenger only conditionally: choose a distinct customer job and establish catalog/API rights, access and operating costs before deeper paid research or development. A public endpoint is not proof of commercial-use permission or reliable data supply.
4. Move actor rehearsal and home bakery down the research queue, rather than STOP based solely on vendor histories.

This resolves the earlier challenger-priority dispute enough to continue targeted research. It does not endorse Claude's six-month feasibility claims. Both reviewers agree the three leading directions are RESEARCH and no experiment is currently approved by the evidence.

## Required final-report updates

Replace the statement that Codex has not reviewed histories with a reference to this audit. Mark co-parenting's status disagreement resolved. Correct the threshold-month conventions, disclose the 17-app cohort or use the full 25-app statistics, and remove causal/model-recalibration certainty. Remove unapproved six-month forecasts and blanket actor STOP. Preserve remaining uncertainties. Retain one report and $500 shared monthly validation/marketing ceiling. Automation remains unconfigured.
