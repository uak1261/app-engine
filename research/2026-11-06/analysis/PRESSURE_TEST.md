# iOS pressure test: revenue trajectories (Claude, 2026-11-06, pending Codex audit)

**Data:** `get_app_historicals` (period all) for 25 apps; raw files `../raw/hist_*.json`; computed by `scripts/revenue_trends.py` into `revenue_trends.json`. A monthly value is the mean of AppKittie's daily *estimated monthly revenue* snapshots.

## Data-quality findings (material)
1. **November 2026 shift across the board:** from Oct to Nov 2026, 15 of 17 unrelated established apps rose; the median change is about +36% and the largest +183%. That pattern points to a vendor estimate recalibration (or a partial-month effect), not demand. **October values are used as "current".**
2. **September 2026 dip:** 7 of 17 apps fell 10-33% in the same month. Also likely model-driven.
3. **Smooth straight-line ramps** in older apps (e.g. Bakesy 69 → 103 in steady +3K/month steps) suggest interpolated estimates. Read them as direction, not measurement.
4. **History starts at tracking start, not launch,** for apps launched before about Nov 2025.
5. **Survivorship bias:** every app sampled is already earning. Its "months to $30K" is a **best case**, not a base rate, and failed launches don't appear.

## Launch ramps (apps whose history starts at launch)
| App (niche) | Launch | Months to first month ≥ $30K | Level in Oct 2026 | Shape |
|---|---|---|---|---|
| Documented (co-parenting) | 2026-08 | **2** | $33K (Nov $107K, recalibration month) | Steep |
| Core of the Heart (faith) | 2026-03 | **2-3** | $106K | Fast, then plateau ~$100-106K |
| Bible Shorts (faith) | 2026-07 | **3-4** | $45K (Nov $100K) | Steep |
| BibleScroll (faith) | 2026-02 | **7** | $113K | Slow 5 months, then fast |
| Brickify (LEGO tracker) | 2026-02 | **4** | $105K | Steady, plateau ~$100K |
| Cardora (sports cards) | 2026-05 | **4** | $87K | Steep |
| GetPaid (class action) | 2026-06 | **2-3** | $35K | Fast, then plateau ~$32-39K |
| ClaimHunt (class action) | 2025-11 | **8** | $46K | Slow |
| Collect (class action) | 2025-09 | **~10** | $76K | Slow, then steep |
| Payout (class action) | 2025-08 | **~10** | $31K | Slow |
| HeyRua (Irish) | 2026-08 | 2 | $126K | **0 → $126K in one month: an artifact, or an Apple feature** |
| Linus (actors) | 2025-07 | not reached in 16 months | $15K | Slow |

## Boom-bust warnings
| App | Peak | Oct 2026 | Read |
|---|---|---|---|
| Creed (Bible chat) | $214K in Sep 2026 | $160K (Nov $105K) | Faith AI chat bubble deflating |
| Parrot (Spanish) | $333K in Aug 2026 | $107K | −68% |
| SkillCat | $206K in Aug 2026 | $152K | Partly the Sep model dip |

## Verdict per niche (6-month target: $40-50K gross MRR)
| Niche | Ramp evidence | Competition | Ease (~40 h, iOS) | Plausible in 6 months? | Verdict |
|---|---|---|---|---|---|
| Co-parenting records | Documented: $30K+ in month 2 | 3 leaders plus Documented | Medium (trustworthy timestamps, PDF, legal wording) | **Yes, best evidence** | RESEARCH → TEST after Codex audit |
| Faith daily-habit apps | 3 of 4 entrants hit $30K+ within 2-4 months | Fragmented (leader 16%), crowding fast; Creed shows bust risk | Easy for devotion/scripture; **hard for screen-time blocking** (Apple's Family Controls entitlement needs approval) | **Yes** | RESEARCH → TEST candidate (pick one job) |
| Collection trackers (unserved category) | Brickify and Cardora: $30K+ in month 4 | One studio clones in cards and antiques; open in categories with free catalog data | Easy when a public catalog API exists | **Plausible** | RESEARCH → TEST candidate (pick the category) |
| Class-action finders | Typical 7-10 months; GetPaid plateaued at ~$35K | 10+ apps in 18 months | Easy to build; ongoing data operations; claim-accuracy and legal risk | **Unlikely** | HOLD |
| Gig mileage and receipts | No newcomers; leaders 5-10 years old with flat ramps | Entrenched | Hard (background GPS accuracy, battery) | No | HOLD |
| Less-common languages | HeyRua step looks like an artifact; Parrot bust | Fragmented | Content-heavy | Unclear | RESEARCH (low priority) |
| Actor tools | Linus under $20K after 16 months | Small market | Easy | No | STOP |
| Trade exam prep | One leader; no tail | — | Content accuracy needed | Unknown | RESEARCH (cheap depth check on CDL, electrician, real estate) |
| Home-food business tools | One leader; modeled-looking ramp | — | Easy | Unknown | HOLD |
