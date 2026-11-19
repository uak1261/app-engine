# Custody-log and co-parenting apps: what worked, what didn't (Claude, 2026-11-19, pending Codex audit)

**Sources:**
- AppKittie search, detail and history (RAW in `raw/`).
- 115 US reviews, fetched 2026-11-19. Raw review files are **not committed** (personal data); they are paraphrased below with review IDs.

**Caveats:**
- Revenue figures are vendor estimates.
- Nov 2026 values are inflated by a vendor-wide shift; Aug-Oct is the reliable window.
- **Frozen estimates (unreliable):** TalkingParents ($500K for 12 months), 2houses ($20K), coParenter ($4K), Peaceful ($3K).

## Top 10
| # | App | Model | Price | Aug-Oct est./mo | Trend | Verdict |
|---|---|---|---|---|---|---|
| 1 | OurFamilyWizard (2012) | Two-parent hub; court and practitioner channel | $149.99 / $219 / $299.99 a year | $412-506K | Growing; +5,365 reviews in 90 days | Worked: court channel |
| 2 | AppClose (2016) | Two-parent hub; was free, now paywalled | $8.99/mo, $98.99/yr | $357-407K | Steady | Worked: court channel; backlash over the paywall |
| 3 | TalkingParents (2016) | Monitored communication, call minutes | $9-39/mo plus call-minute packs | $500K (frozen) | Unknown | Court channel; support complaints |
| 4 | **TextPort** (2025) | **Solo**: iMessage thread → timestamped PDF/CSV | $4.99-9.99/wk, $14.99/mo, $59.99/yr | **$197-294K** | $61K → ~$290K in 12 months | **Worked: one job, court-ready output** |
| 5 | **Documented** (2026-08) | **Solo**: sealed personal log + PDF | $17.99/mo, $179.99/yr | $0 → $33K (Oct) | Nov mean $101K, but the latest snapshot is $66K | **Worked fast**; PDF crashes; review credibility questioned |
| 6 | 2houses (2013) | Two-parent hub | $14.99-27.99/mo, $89.99-169.99/yr | $20K (frozen) | Flat | Stalled |
| 7 | Kidtime (2023) | Calendar, repositioned as a solo record | $7.99-14.99/mo | ~$4-5K | Flat | Stalled despite the solo angle |
| 8 | BestInterest (2024) | AI tone filter for high conflict; WIRED, Dr. Ramani | $9.99-14.99/mo, up to $269.99/yr | $6K → $5K | −30% over 90 days | Loved product, no distribution |
| 9 | coParenter (2016) | Two-parent plus mediation | $8.99-19.99/mo | ~$4K (frozen) | Flat | Failed: reliability and support |
| 10 | Peaceful CoParenting (2020) | Two-parent messenger | $14.99/mo, $59.99-84.99/yr | ~$3K | Flat | Stalled |

## What worked
1. **The court and professional channel.** The top 3 tell users they are "court-ordered" or "trusted by courts in all 50 states" and offer practitioner accounts. They earn **$350-700K a month from only 16-25K downloads a month**: high revenue per user, almost no virality, and a captive customer.
2. **A single job with a court-ready output that works solo.**
   - TextPort: export a text thread to a timestamped PDF. Reviews describe it as "presentable for court purposes" (14779637113) and doing in minutes what screenshots couldn't (14756238945).
   - Documented: a sealed log, "timestamped interactions" (14763515128).
   - Both need **no co-parent buy-in**, and both are the only post-2023 entrants to break out.
3. **Annual or weekly pricing on high intent.** Buyers arrive at a crisis moment (court date, attorney request) and pay immediately.

## What didn't work
1. **Two-parent communication challengers without a court mandate** (2houses, coParenter, Peaceful, Fayr, Truece, BestInterest): stuck at $3-20K for years. They need both parents to adopt, which is the cold-start problem, and they can't displace a court-ordered app.
2. **Reliability and support failures.**
   - coParenter: login outages and no support response, during court deadlines (13856263943, 12701048071).
   - Incumbents bleed the same way: OurFamilyWizard freezes and dropped calls (14796751196, 14753538763); AppClose call and notification bugs (14662863181); TalkingParents sign-outs and slow support (14648108057, 14295869112).
3. **Paywalling or removing core features from captive users.**
   - AppClose put the calendar behind a paywall (14708176691) and moved from free to paid (14646282172).
   - TalkingParents removed its free tier (14694776694).
   - OurFamilyWizard is annual-only (14792193619), removed login history (14760003390) and removed multiple schedules (14746968743).
   - These generate anger but little churn, because users are court-mandated. **This is a wedge for a solo app, not a reason incumbents lose.**
4. **A great product without distribution.** BestInterest gets strong 5-star reviews for its AI tone filter (14660426733, 14623051946) but is ~$5K and falling. Its AI feature was also unreliable ("tone guardian unavailable", 14270895359).
5. **Rigid calendars:** Kidtime can't handle complex custody schedules (14792080929, 14716981139).
6. **Review credibility risk:**
   - Documented: "reviews seem very forced" (14681656421).
   - TextPort: a run of very short, uniform 5-star reviews. **Treat both apps' ratings with caution.**

## Implications for Steadline
- The pattern that works is **solo use, one job, a court-ready export**. Steadline's sealed log plus Case File fits it.
- **Message export is a proven, separately paid job** (TextPort ~$200-290K). Importing screenshots or exported threads into the Case File is worth testing. Native iMessage access on iOS has platform limits, so check feasibility before promising it.
- **Distribution matters more than features.** Attorneys and courts are the only channel that has produced $300K+ businesses. Treat the Nov 9-15 attorney signal as decisive.
- **Do not build two-parent messaging.** Every challenger that tried it stalled.
- **Differentiate on reliability:** a PDF that never crashes, responsive support, and no paywall on exporting your own record.
