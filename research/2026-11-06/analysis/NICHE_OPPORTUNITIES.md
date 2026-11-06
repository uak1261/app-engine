# Niche opportunity map: Nov 6, 2026 (Claude discovery, pending Codex audit)

**Status:** every niche below is **RESEARCH** or **HOLD**. Nothing here is TEST-ready: no reviews were pulled, and no gates other than demand structure were checked. **No Codex agreement is implied.**

## Method (reproducible)
1. **Category sweep (288 credits):** 16 non-game iOS categories, `countries ["US"]`, monthly revenue $20K-150K, sorted by revenue, top 18 per category. This band is where independent apps live; the $30-50K portfolio target sits inside it.
2. **Niche depth checks (100 credits):**
   - 10 keyword searches, `textSearchFields [title, description]`, category-filtered, monthly revenue ≥ $5K, top 10.
   - This reaches the long tail, which revenue concentration needs.
3. **Niche boundaries:** set by Claude with regexes over titles in `niche_map.json`. **This is a judgment call; audit it.**
4. **Metrics:** computed by `scripts/niche_metrics.py` from the raw files:
   - Publishers earning ≥ $20K.
   - Leader share and HHI (a concentration index; above 2,500 is concentrated).
   - Entrants launched in the last 18 months that already earn ≥ $20K.
   - Median 30-day revenue growth.
   - Average rating of the top 3.
   - How many apps have known Meta ad spend.
5. **Caveats:**
   - Revenue figures are AppKittie monthly estimates, often rounded.
   - The sweep is biased toward the top of each category's band.
   - Meta spend is mostly unknown (null), and unknown is not zero.
   - Ratings are store averages, not review samples.

## Results
| Niche | Publishers ≥$20K | Niche revenue (est.) | Leader share / HHI | New entrants ≥$20K (≤18 months) | Median 30d growth | Top-3 rating | Read |
|---|---|---|---|---|---|---|---|
| **Class-action settlement finders** | 6 | $597K | 42% / 2,367 | **5** | +23% | 4.72 | A niche forming right now: every app launched 2025-26. Moderately concentrated. Acquisition channel unknown (no Meta data). |
| **Christian faith-tech** (focus, screen-time, Bible habits) | **7** | $800K | **16% / 1,446** | 4 | +15% | 4.85 | Fragmented and hot. High ratings mean low quality gap, so the angle must be a specific job. |
| **Gig-worker mileage and receipts** | 6 | $711K | 42% / 2,491 | 0 | +8% | 4.80 | Mature, with proven willingness to pay. The November spike may be seasonal. Clear job: tax savings. |
| **Underserved-language learning** | 4 | $543K | 26% / 2,503 | 1 (HeyRua, Irish, launched Aug 2026, ~$141K) | +29% | 4.79 | Repeatable pattern: one language per app. Content is the cost. |
| Collectibles identification and trackers | 4 | $884K | 59% / 4,037 | 4 | +14% | 4.67 | Dominated by one studio (Next Vision), so App Store copycat (4.3) risk. Look for an independent sub-niche. |
| Actor tools (line-learning, self-tape) | 3 | $290K | 41% / 3,007 | 0 (Linus at $20K) | flat | 3.93 | Small but under-served (Actors Access is rated 2.6). Narrow professional audience. |
| Trade-licence exam prep | 1 | $168K | 89% | 0 | +13% | 4.67 | SkillCat makes ~$21 per download. The tail is tiny: either an unserved gap or a small market. |
| Home food micro-business (Bakesy) | 1 | $156K | 89% | 0 | flat | 4.67 | ~$28 per download from a single publisher. Pattern: "Bakesy for another micro-business". |
| Rec sports organizers | 9 | $1.2M | 34% | 0 | flat | 4.48 | HOLD: mostly network-effect platforms. |
| Pro-driver navigation | 7 | $2.6M | **76%** | 0 | +33% | 4.29 | HOLD: Trucker Path dominates. |
| Recipe import from social | 6 | $2.3M | **87%** | 1 | flat | 4.70 | HOLD: ReciMe dominates, with ~$253K Meta spend in 30 days. |
| Hunting, fishing and boating maps | 5 | $389K | 33% | 0 | flat | 4.57 | HOLD: small pool; incumbents outside the sample. |

## Gaps before any of these can reach TEST
- No reviews pulled, so the reason to switch is unknown for every new niche.
- Pricing and 90-day trends not pulled (no detail calls were made).
- Acquisition channel unknown for the class-action and faith-tech leaders.
- The gig-mileage November growth needs 90-day and 300-day history to rule out seasonality.

## Credits
About 389 used: 1 probe, 288 sweep, 100 depth. **This exceeds the 300 Monday cap**; it was an ad-hoc run the owner requested. Logged in `../MANIFEST.md`.
