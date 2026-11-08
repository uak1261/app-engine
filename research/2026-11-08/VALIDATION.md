# Steady $20K+ earners (Aug-Oct 2026) and Steadline validation: Claude, 2026-11-08, pending Codex audit

## Method
- **Window:** Aug, Sep and Oct 2026. November is excluded because of the vendor-wide estimate shift.
- **Universe:** 25 earlier histories, 60 new histories from the Nov 6 sweep, and 4 co-parenting histories.
- **Four signals:**
  - **V1 (AppKittie, modeled):** monthly estimated revenue ≥ $20K in all 3 months, max/min ≤ 1.5. Script: `scripts/steady_earners.py`.
  - **V2 (frozen check):** coefficient of variation ≥ 0.005. Identical monthly values (e.g. $141.3K ×3, $100.0K ×3) are treated as placeholder estimates.
  - **V3 (App Store reviews, observed by AppKittie's scraper):** ≥ 300 new reviews in the window.
  - **V4 (NichesHunter, a separate vendor, observed):** appears in the US top-100 *download* chart of its category on **both** 2026-08-15 and 2026-10-15. Low-download subscription apps cannot appear, so absence is inconclusive.
- **Results:** 84 apps have Aug-Oct data; 54 pass V1. Excluded: games, hardware-dependent, licensed-content and service-ops apps.

## Top 5: passing V1-V3 plus chart presence
| App | Aug / Sep / Oct est. ($K) | New reviews (90d) | US Reference / H&F chart rank (Aug 15 → Oct 15) | Read |
|---|---|---|---|---|
| Creed: Bible Chat | 205 / 214 / 160 | 22,785 | #22 → #19 | Real usage, but **Oct −25%** (bust risk) |
| Faithe: Bible Videos | 101 / 105 / 103 | 1,747 | #33 → #45 | Steady |
| Curio: Antique Identifier | 101 / 104 / 104 | 2,764 | not in top 100 → #32 | Steady, rising chart |
| Brickify: LEGO tracker | 82 / 99 / 105 | 2,576 | #41 → #54 | Steady growth, indie |
| Wayk: Alarm Clock | 81 / 84 / 101 | 2,279 | #61 → #56 (H&F) | Growing, new niche |

**Two-source only** (high revenue, low downloads, so not visible in charts):
- OurFamilyWizard: 506 / 412 / 504, +5,365 reviews.
- AppClose: 407 / 357 / 363, +906 reviews.

**Unreliable estimates:**
- TalkingParents: exactly $500K for 9 straight months, with −4 reviews in the window.
- Male Hair Editor, Ruler, Moonly, Smartist, Lake: frozen values.

**Market-level confirmation (NichesHunter, US Reference top 100):**
- Bible and faith apps: 32 on Aug 15, 33 on Oct 15.
- Collectibles and scanners: 16 on both dates.

Both markets are active and crowded.

## Steadline: market validation
| Evidence | Value | Source |
|---|---|---|
| Incumbents, Aug-Oct | OurFamilyWizard ~$474K avg (reviews +5,365); AppClose ~$375K (+906); TalkingParents frozen at $500K (unreliable) | AppKittie history + observed reviews |
| Breakout entrant | Documented, launched 2026-08-19: $0 → $2.2K → $32.7K (Aug-Oct); +271 reviews | AppKittie RAW |
| Challenger base rate | Of 9 challengers (launched 2017-2026), **only Documented exceeds $10K/mo.** Shared $10K (FR), Co-parenting $8K (SE), Kidtime ~$5K (3 years), BestInterest ~$5K (2.4 years), Peaceful/Truece/Fayr ~$3K, 2ForKids $2K. | `search_coparenting.json` + histories |
| Download charts | No co-parenting app in the US Productivity top 100 (Oct 15). Discovery is search- and referral-driven, not viral. | NichesHunter |
| Paid economics | Fails at base assumptions; $500/mo buys ~4 payers | Codex audit A08/A09 |
| Steadline build state | Landing page, sample Case File, waitlist, seal/crypto engine, pattern counts. Test EXP-2026-01 locked for Nov 9-15 (gate: ≥ 2 of 3 signals). | `uak1261/steadline` main @ 6490338 |
