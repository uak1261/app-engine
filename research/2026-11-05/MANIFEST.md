# AppKittie call manifest: Nov 5, 2026

**Retention key**
- **RAW:** full response kept in `raw/`, with a checksum in `raw/SHA256SUMS`.
- **TRANSCRIPT:** the response was seen in the session but not saved; key values are in `evidence/transcript_only_extract.csv` and `evidence/review_quotes.md`. Treat as **UNVERIFIED**.
- **NONE:** an error, or nothing usable.

**Shared conventions**
- `countries: ["US"]` filters by *app language*, not storefront: 17 of the 105 rows in RAW searches have non-US storefront URLs.
- Revenue and downloads are AppKittie **monthly estimates**. Their geographic scope (US-only or worldwide) is **not documented**.

**Credits:** the counts below are Claude's estimates (1 per app returned, 1 per detail, 1 per review). They were not checked against the AppKittie balance.

## Run 0: auth test (~13:20 UTC)
| Call | Params | Result | Retention |
|---|---|---|---|
| search_apps | limit 1, sortBy revenue, apple_mobile | YouTube (first key) | NONE |
| Earlier attempts | | HTTP 401 with the old, revoked key | NONE |

## Run 1: old method, Top-5 brief (2026-11-05 13:33-13:35 UTC, ~257 credits est.)
Shared params for sweeps: `source: apple_mobile`, `countries: ["US"]`, `excludedCategories: ["games"]`, `limit: 35`.

| # | Call | Params (beyond shared) | Returned | Retention |
|---|---|---|---|---|
| 1 | search_apps (sweep A) | releasedAfter 1746403200 (2025-05-05), minRevenue 30000, maxRevenue 400000, hasMetaAdSpend true, sortBy revenue | 35 of 156 | RAW `run1_sweepA_search_apps.json` |
| 2 | search_apps (sweep B) | minRevenue 30000, maxRevenue 400000, sortBy revenue_growth | 35 of 5,924 | TRANSCRIPT (mostly old apps with >1,000% growth artifacts) |
| 3 | search_apps (sweep C) | releasedAfter 1730764800 (2024-11-05), min 30000, max 400000, maxDownloads 50000, sortBy revenue | 35 of 762 | TRANSCRIPT |
| 4 | search_apps (sweep D) | releasedAfter 1746403200, min 30000, max 400000, hasTikTokAds true, sortBy revenue | 35 of 47 | RAW `run1_sweepD_search_apps.json` |
| 5 | search_apps (niche) | search "sermon notes bible", apple_mobile, exclude games, minRevenue 10000, sortBy revenue, limit 8 | 2 | TRANSCRIPT |
| 6 | search_apps (niche) | search "crochet knitting woodworking craft", same | 6 | TRANSCRIPT |
| 7 | search_apps (niche) | search "GLP-1 peptide injection tracker", same | 8 of 9 | TRANSCRIPT |
| 8 | search_apps (niche) | search "AI music video generator", same | 8 of 1,710 | TRANSCRIPT |
| 9 | search_apps (niche) | search "co-parenting custody log", same | 8 of 10 (mostly noise) | TRANSCRIPT |
| 10 | get_app_detail | Shotsy | 1 | TRANSCRIPT |
| 11 | get_app_detail | Documented | 1 | RAW `run1_detail_documented.json` |
| 12 | get_app_detail | HolyNote | 1 | RAW `run1_detail_holynote.json` |
| 13 | get_app_detail | Loopsy | 1 | RAW `run1_detail_loopsy.json` |
| 14 | get_app_detail | Sondo | 1 | TRANSCRIPT |
| 15 | get_app_detail | PeptidePal | 1 | RAW `run1_detail_peptidepal.json` |
| 16 | search_apps (niche) | search "chronic illness symptom tracker", same | 2 | TRANSCRIPT |
| 17-20 | get_app_reviews | OurFamilyWizard, MeAgain, Bible Note, YarnPal; maxReviews 15, US | 60 | TRANSCRIPT (quotes) |
| 21 | get_app_detail | Cardly | 1 | TRANSCRIPT |
| 22 | get_app_reviews | Cardly; maxReviews 15, US | 15 | TRANSCRIPT (quotes) |

Run 1 also produced a test brief emailed through Gmail; the HTML is kept at `research/2026-11-05/run1_brief.html`. **Run 1 used rules that were later superseded** (Meta spend over 60% of revenue as a hard reject, revenue per download under $0.75 as a hard reject, a 15-review sample). Its rejections are re-classified in the handoff.

## Run 2: new method (2026-11-05 13:50-13:52 UTC, ~253 credits est.)
| # | Call | Params | Returned | Retention |
|---|---|---|---|---|
| 1 | search_apps (lane A) | apple_mobile, US, exclude games, releasedAfter 1746403200, minRevenue 20000, sortBy revenue, limit 35 (**no maxRevenue**: a mistake, later fixed in the protocol) | 35 of 1,208 | RAW `run2_laneA_search_apps.json` |
| 2 | search_apps (lane B) | releasedBefore 1730764800, min 30000, max 300000, maxRating 4.4, minReviews 500, sortBy revenue, limit 35 | 35 of 836 | TRANSCRIPT |
| 3 | search_apps (lane C) | releasedAfter 1699142400 (2023-11-05), min 30000, sortBy revenue_growth, limit 30 | 30 of 1,675 | TRANSCRIPT |
| 4 | search_apps (lane D) | google_mobile, releasedAfter 1746403200, min 15000, sortBy revenue, limit 30 | 30 of 2,640 (mostly games and Big Tech) | TRANSCRIPT |
| 5 | search_apps (lane E) | apple_mobile, releasedAfter 1730764800, min 20000, organicSources [tiktok, instagram, youtube], hasMetaAdSpend false, sortBy revenue, limit 30 | 30 of 354 | TRANSCRIPT |
| 6 | get_app_detail | myCar | 1 | RAW `run2_detail_mycar.json` |
| 7 | get_app_detail | MenuFit | 1 | TRANSCRIPT |
| 8 | get_app_detail | guessed slug for mise | HTTP 404 | NONE |
| 9 | get_app_detail | Documented | 1 | RAW `run2_detail_documented.json` |
| 10 | get_app_detail | OurFamilyWizard | 1 | TRANSCRIPT |
| 11 | get_app_detail | YarnPal | 1 | TRANSCRIPT |
| 12 | get_app_detail | guessed slug for HoloDex | HTTP 404 | NONE |
| 13 | get_app_detail | mise (correct slug) | 1 | RAW `run2_detail_mise.json` |
| 14 | get_app_detail | HoloDex (correct slug) | 1 | RAW `run2_detail_holodex.json` |
| 15 | search_apps (niche) | search "co-parenting custody", apple_mobile, min 10000, revenue, limit 8 | 8 of 24 | TRANSCRIPT |
| 16 | search_apps (niche) | search "restaurant menu macros eating out", same | 8 of 44 (all restaurant games) | TRANSCRIPT |
| 17 | search_apps (niche) | search "TCG card scanner pokemon", same | 8 of 36 | TRANSCRIPT |
| 18 | search_apps (niche) | search "AI meal planner grocery list", exclude games, same | 8 of 1,709 (mostly Big Tech noise; only Kalguroo is relevant) | TRANSCRIPT |
| 19 | get_app_reviews | Documented, maxReviews 10, US | 9 | TRANSCRIPT (quotes) |
| 20 | get_app_reviews | OurFamilyWizard, maxReviews 15, offset 15, US | 15 | TRANSCRIPT (quotes) |
| 21 | get_app_reviews | mise, maxReviews 15, US | 15 | TRANSCRIPT (quotes) |
| 22 | get_app_reviews | YarnPal, maxReviews 15, offset 15, US | 15 | TRANSCRIPT (quotes) |

## Non-AppKittie evidence (Nov 5-6)
- **Domains:** GoDaddy availability checks. These are point-in-time and expire quickly.
  - Available: getkept.com, keptapp.com, steadline.com, custodytimeline.com, stampedapp.com, docketparent.com, kinlogapp.com, parentrail.app.
  - Unavailable: keptlog.com, kept.app.
  - Raw responses were not kept in the repo.
- **USPTO screenshots supplied by the user** (not retrieved by Claude):
  - "KEPT", Janus AI Solutions LLC, serial 50171161, live and pending, IC 009/041/042.
  - "STEADLINE", serial 50063846, filed 2026-08-21, live and pending, **IC 025 (clothing) only**.
