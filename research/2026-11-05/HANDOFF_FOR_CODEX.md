# Handoff to Codex: AppKittie research, week of Nov 2, 2026

**From:** Claude, the discovery, customer-problem and presentation lead.
**To:** Codex, the independent auditor.
**Prepared:** 2026-11-06. **Evidence date:** 2026-11-05.
**Status of this document:** Claude's position only. **No Codex agreement is implied.** The final report will add your audit and keep any unresolved disagreements.

## 0. What to audit
Audit these four areas independently:
1. **Evidence:** do the cited numbers match the retained responses, and are the claims supported?
2. **Economics:** formulas, assumptions, and the gross vs net definitions.
3. **Distribution:** is each claimed acquisition channel actually evidenced?
4. **Implementation scope:** is each "~40-hour first version" realistic, and are the exclusions complete?

Then return findings in the format in section 9.

**Files**
| Path | Contents | Verification |
|---|---|---|
| `raw/*.json` + `raw/SHA256SUMS` | 11 full AppKittie responses (3 searches, 8 details) | **VERIFIED** (raw on disk) |
| `evidence/search_extract.csv` | 105 app rows pulled from the 3 retained searches | Derived from RAW |
| `evidence/detail_extract.jsonl` | 8 detail records (pricing, 90-day trends, Meta transparency) | Derived from RAW |
| `evidence/transcript_only_extract.csv` | Key values from responses that were not saved | **UNVERIFIED** |
| `evidence/review_quotes.md` | Cited review quotes with review IDs | **UNVERIFIED** |
| `MANIFEST.md` | Every call: parameters, time, count, retention | Reference |
| `run1_brief.html` | The Run 1 brief as delivered | Reference |
| `../../docs/RESEARCH_PROTOCOL.md` | Portable runner instructions | Reference |

No AppKittie credits were spent preparing this handoff.

---

## 1. Facts (what AppKittie returned)
Figures are **AppKittie estimates**: monthly revenue in USD and monthly downloads. "RAW" means verifiable from the files; "UNVERIFIED" means transcribed only.

### Co-parenting
| App | Monthly rev (est.) | Downloads | Trend | Pricing | Ads | Source |
|---|---|---|---|---|---|---|
| Documented, Rise Advertising LLC, released 2026-08-19 | $107,556 | 19,678 | 90-day growth reads 0, i.e. no history | $17.99/mo, $179.99/yr | Meta lifetime and 30-day spend $488.75 | RAW |
| OurFamilyWizard | $690,316 | — | Revenue +37.5% over 90 days, downloads −17.0%, MAU +37.5% | $149.99, $219 or $299.99/yr | — | UNVERIFIED |
| TalkingParents | $500,000 | — | 30-day growth 0 | **Not pulled** | — | UNVERIFIED |
| 2houses | $20,000 | — | — | — | — | UNVERIFIED |

### GLP-1
| App | Monthly rev (est.) | Downloads | Trend | Pricing | Ads | Source |
|---|---|---|---|---|---|---|
| PeptidePal | $151,075 | — | Revenue **−15.7%**, downloads **−71.9%**, MAU −8.5% over 90 days | $8.99-14.99/mo, $29.99-59.99/yr | Meta $7,741 over 30 days | RAW |
| Monju | $137,654 | — | — | — | Meta $0.12 over 30 days | RAW (sweep A) |
| MeAgain | $566,042 | — | Revenue +11.9% over 30 days | — | — | UNVERIFIED |
| Shotsy | $360,512 | — | Revenue +19.1%, downloads −25.5%, MAU +42.4% over 90 days | $9.99/14.99/mo, $39.99-59.99/yr | Meta transparency null (unknown) | UNVERIFIED |
| Pep AI | $32,123 | — | — | — | — | UNVERIFIED |

### Crochet
| App | Monthly rev (est.) | Downloads | Trend | Pricing | Ads | Source |
|---|---|---|---|---|---|---|
| Loopsy | $140,338 | — | Revenue +49.3%, downloads +50.4%, MAU +59.9% over 90 days | $4.99/wk, $9.99/mo, $19.99-49.99/yr, $99.99 lifetime | Meta $21,978 over 30 days | RAW |
| YarnPal | $576,959 | — | Revenue +14.7% over 90 days | $3.99/wk, $29.99-49.99/yr | Meta 30-day estimate $0 in search rows | UNVERIFIED |
| WoodSense (woodworking, adjacent) | $234,671 | — | — | — | Meta $79,061 over 30 days | RAW (sweep A) |

### Meal planning
| App | Monthly rev (est.) | Downloads | Trend | Pricing | Ads | Source |
|---|---|---|---|---|---|---|
| mise, released 2026-06-10 | $530,850 | 301,678 | Revenue +316%, downloads +136%, MAU +735% over 90 days | $9.99/mo, $19.99-59.99/yr | Meta transparency **null = unknown, not zero** | RAW |
| Kalguroo | $60,000 | — | — | — | — | UNVERIFIED; **storefront URL is Thailand** |

### Sermon notes
| App | Monthly rev (est.) | Downloads | Trend | Pricing | Ads | Source |
|---|---|---|---|---|---|---|
| HolyNote, released 2026-09-08 | $198,000 | 173,946 | Growth fields read 0, i.e. no history | $9.99/wk, $59.99/yr | Meta $5,192 over 30 days, $11,962 over 90 days | RAW |
| Bible Note | $200,989 | — | Revenue −33.4%, downloads −90.0% over **30 days** (90 days not pulled) | — | — | UNVERIFIED |

### Trading-card scanners
| App | Monthly rev (est.) | Downloads | Trend | Pricing | Ads | Source |
|---|---|---|---|---|---|---|
| HoloDex | $668,257 | — | Revenue +118%, downloads −18.1%, MAU +118% over 90 days | — | Meta $25,793 over 30 days | RAW |
| Foloy | $309,982 | — | — | — | — | UNVERIFIED |
| Digital Grading Co | $302,800 | — | — | — | — | UNVERIFIED |
| FoilSnap | $216,502 | — | — | — | — | UNVERIFIED |
| Cardly | $207,742 | — | Revenue +111% over 90 days, rating −1.0 | — | — | UNVERIFIED |
| Ludex | $160,274 | — | — | — | — | UNVERIFIED |
| Search total | 36 apps matched "TCG card scanner pokemon" | | | | | UNVERIFIED |

### Others
| App | Monthly rev (est.) | Trend | Ads | Source |
|---|---|---|---|---|
| myCar | $581,145 | Revenue −34.5%, downloads −53.3%, MAU −32.9% over 90 days | — | RAW |
| MenuFit | $801,676 | Revenue −0.3%, downloads −33.5% over 90 days | — | UNVERIFIED |
| Sondo (AI music video) | $240,000 | Revenue −40.3%, downloads −75.1% over 90 days | — | UNVERIFIED |
| Juno (chronic illness) | $150,859 | — | Meta $76,919 over 30 days | RAW (sweep A) |
| ARtie Lab | $152,560 | — | Meta $141,686 over 30 days | RAW |
| SocialLite | $161,080 | — | Meta $156,688 over 30 days | RAW |

### Data-quality facts (Claude's own observations, verifiable)
- `countries: ["US"]` filters by **language**: 17 of the 105 RAW search rows have non-US storefront URLs (br, de, kr, tw and others). The geographic scope of revenue is **not documented**.
- **Many estimates are suspiciously round** ($198,000, $250,000, $300,000, $330,000, $400,000, $500,000). That suggests bucketing or a cap, so treat precision as low.
- For new apps (Documented, HolyNote), the 90-day growth fields read **0**. That means no history, not flat growth.
- Per AppKittie's documentation, a missing Meta transparency field means "unavailable, not zero".

## 2. Assumptions (not from AppKittie)
These come from the founder profile in `docs/RESEARCH_PROTOCOL.md`. **None have been validated.**

| Assumption | Value (conservative / base / upside) | Basis |
|---|---|---|
| Apple fee | 15% | Small Business Program eligibility assumed |
| Refunds | 3% | Guess |
| Monthly churn | 15% / 10% / 6% | Guess |
| Install-to-paid conversion | 2% / 3% / 5% | Guess |
| US iOS cost per install | $5 / $3.50 / $2 | Guess, no source |
| Resulting cost to acquire a payer | $250 / $117 / $40 | Cost per install ÷ conversion |
| LLM/API cost per payer per month | $0.20-0.80, varies by app | Guess |
| "$40K/month" target | **Measured at gross consumer price** in the Top-5 payer counts | **Ambiguous:** the owner's target could be gross or net. Net to developer ≈ 82% of gross. |
| Path to $40K | Reach it in 12 months at 10% churn, so new payers per month = 0.143 × target payers | Model choice |
| Paid share of acquisition | 25% | Arbitrary, used only for the budget row |
| Build budget | ~40 focused dev hours per first version | Founder profile |

## 3. Hypotheses (Claude's interpretations, testable)
| ID | Hypothesis | Main evidence | What would falsify it |
|---|---|---|---|
| H1 | Separated parents will pay $149/yr for court-ready records with an AI attorney timeline | Documented's $108K est. with ~$489 Meta spend; OurFamilyWizard reviews citing broken court exports and price | Landing-page test: under 15% pick a paid plan, or attorneys decline to pilot |
| H2 | Documented's demand is **organic** | Meta spend $488.75 | Apple Search Ads, Google or TikTok spend is unknown, so this is **unverified** |
| H3 | OurFamilyWizard's +37% revenue reflects demand | Revenue up while downloads fell 17% | A 3-star review cites "continued price increase". **It may be a price rise, not demand.** |
| H4 | GLP-1 users will pay for photo-based protein logging | One MeAgain review pastes food into ChatGPT | Another MeAgain review (14730864416) suggests photo logging already exists. **Differentiation is weak.** |
| H5 | Crocheters will pay more for checked, human-made patterns | YarnPal "AI slop" reviews | Designers won't join, or YouTube's free patterns cap willingness to pay |
| H6 | Restricted-diet households underserved by mise will switch | mise reviews | mise adds the diets; the "second publisher" evidence is non-US |
| H7 | Bible Note is losing users to HolyNote | Bible Note downloads −90% over 30 days while HolyNote launched | Only 30-day data; could be an estimate artifact |

## 4. Candidates and Claude's proposed status
Status labels follow the protocol: RESEARCH, TEST, BUILD, HOLD/STOP. **Every status below is a proposal pending your audit.**

| # | Candidate | Proposed status | Why | Material gaps |
|---|---|---|---|---|
| 1 | **Co-parenting records (working name "Steadline")** | **TEST** (this week's single new experiment) | 3+ publishers earning $100K+ est.; strong complaint pattern in the leader; a bounded $500 fake-door test resolves the key unknowns (willingness to pay, attorney pull) | TalkingParents pricing missing. Whether courts mandate specific apps is unresearched. H2 and H3 unverified. Revenue geography unknown. |
| 2 | GLP-1 companion | RESEARCH | Deep demand (5 publishers) | Not checked under the new gates. PeptidePal is declining (RAW). Differentiation weak (H4). Apple medical-review risk unassessed. |
| 3 | Crochet with checked patterns | RESEARCH | Loopsy growth is RAW-verified; complaint pattern is strong | Designer supply unvalidated. Ongoing content work may exceed one person's capacity. YarnPal data unverified. |
| 4 | Restricted-diet meal planner | RESEARCH | mise's breakout is RAW-verified | Only one verified US publisher; Kalguroo is a Thailand storefront. Willingness to pay is weak in reviews. mise's paid spend is unknown, not zero. |
| 5 | AI sermon notes | RESEARCH | HolyNote is RAW-verified | Evaluated under the old method only. Bible Note's decline is 30-day and unverified. Price sensitivity is high. |

**Note on the Top-5 table shown to the owner on Nov 5:** it presented all 5 with economics. **Only candidate 1 was evaluated under the current gates.** Candidates 2-5 should be read as RESEARCH, not as test-ready.

## 5. Rejected candidates
| Candidate | Proposed status | Reason | Validity |
|---|---|---|---|
| Trading-card scanners | HOLD | Fails gate 3 (no advantage): 36 matches, leaders rated 4.5-4.8 | Demand evidence is strong. A neglected sub-niche (One Piece or Lorcana, sport-specific grading) is unexplored. |
| myCar (car widgets) | STOP | Sustained decline on 3 signals (RAW) | Valid under the current rules |
| AI music video (Sondo and others) | STOP | Revenue −40%, downloads −75% over 90 days | Data is UNVERIFIED |
| MenuFit (eating out) | HOLD | Single publisher found; downloads −33.5% over 90 days | Niche search was noisy (returned games). Re-check with a category filter. |
| Juno (chronic illness) | HOLD | Single publisher | — |
| ARtie Lab, SocialLite, Calife | HOLD (re-classified) | Rejected in Run 1 for Meta spend over 60% of revenue | **That rule was superseded.** Ad spend and revenue come from different cohorts. Not re-evaluated. |
| Speaker cleaners | HOLD (re-classified) | Rejected in Run 1 for revenue per download under $0.75 | **Rule superseded** (directional only). Low differentiation anyway. |
| Short-drama, AI companion/dating, Big Tech, VPN/IPTV, platform-ToS tools (e.g. Unfollow Tracker) | STOP (category exclusions) | Licensed content, 17+ or dating, Big Tech publisher, regulated or ToS risk | Valid under the exclusion list |

## 6. Known errors and corrections in Claude's earlier outputs
1. **"US" labeling:** briefs labeled geography "US" without qualification. The filter is language-based, and storefront and revenue scope are unknown.
2. **"No paid ads recorded" for mise:** wrong. Meta transparency was null, which means unknown.
3. **PeptidePal** was listed as GLP-1 demand evidence without noting its 90-day decline (revenue −15.7%, downloads −71.9%).
4. **Run 2 lane A had no revenue cap**, so mega-apps dominated. Fixed in the protocol.
5. **Run 1 hard rejects** (Meta spend over 60%, revenue per download under $0.75) used rules later judged invalid.
6. **Mixed bases:** payer counts use the gross price ($40,000 ÷ price) while lifetime value uses net. Labeled in the table, but the target definition needs an owner decision.
7. **"Annual pays back on day one"** for co-parenting: $149.99 × 0.85 × 0.97 = $123.67 net vs the $117 base cost to acquire a payer. That rests entirely on the assumed cost per install and conversion, and ignores renewal churn.
8. **Most raw responses were not saved.** The protocol now requires saving every response to disk at call time.

## 7. Missing evidence and open questions
**Data gaps (fixable with credits):**
- TalkingParents pricing and 90-day trend; OurFamilyWizard re-pull to verify RAW.
- Documented's non-Meta acquisition: Apple Search Ads (`hasAppleAds`), keyword ranking, TikTok.
- Historical revenue for the co-parenting leaders (`get_app_historicals`, 300 days) to separate a price increase from demand.
- Re-pulls to turn UNVERIFIED values into RAW for any candidate going to TEST.
- Keyword difficulty and volume for "custody log", "co-parenting app" and "custody journal" (`get_keyword_difficulty`).
- Android signal for every candidate (the lane-D filter needs fixing first).

**Questions that AppKittie can't answer:**
- **Do US family courts name specific apps in orders,** limiting a new entrant to "personal records"? This needs legal or desk research.
- **Apple guideline exposure:** custody evidence claims (legal), GLP-1 tracking (health), and 4.3 copycat rules.
- **Is the owner's target gross or net revenue?**
- **Real development capacity:** hours per week, and whether 2-3 launches a month fits "max 1 build active".
- **Does AppKittie's revenue estimate cover the US only, or worldwide?** This needs AppKittie documentation or support.

## 8. Implementation scope claims to audit (co-parenting first version, ~40 hours)
**In scope:**
- A log where each entry is locked with a time and location stamp, plus a content hash.
- Photo and receipt capture.
- Screenshot import with text reading (OCR).
- An AI attorney timeline exported as PDF.
- A shareable link.
- An app passcode.

**Explicitly excluded:** messaging between parents, calendars, payments, Android.

**Stack assumption:** Expo + Supabase + RevenueCat + an LLM API.

**Claude's own risk notes:**
- Making the stamping tamper-evident in a way a court will credit may be harder than it sounds.
- Text-reading accuracy on message screenshots is unproven.
- PDF generation is cheap; trustworthy evidence is not.

## 9. Requested audit return format
Save the audit as `research/2026-11-05/audit/codex.md` with this table:

| ID | Section / claim reference | Verdict (CONFIRMED / DISPUTED / UNVERIFIABLE) | Evidence (file + field, or reasoning) | Severity (MATERIAL / MINOR) | Proposed status change |
|---|---|---|---|---|---|

Also:
- Your independent status for each candidate (RESEARCH / TEST / BUILD / HOLD-STOP).
- Any economics you recompute, with formulas.

The final weekday report will show Claude's and Codex's statuses side by side. Any MATERIAL disagreement left unresolved sets the candidate to HOLD until it's settled.

---

## 10. Reconciliation with `origin/codex/persistent-opportunity-engine` (commit 6e9e277)
Codex's branch has its own policy: `AGENTS.md`, `docs/engine.md`, `data/portfolio.json` and `scripts/economics.py`. It was written before the owner's Nov 6 instruction. Claude has **not** edited that branch.

The two policies must become **one** shared protocol. Until they do, these conflicts are open:

| Topic | Claude `docs/RESEARCH_PROTOCOL.md` | Codex `docs/engine.md` | Owner's Nov 6 instruction | Proposed resolution |
|---|---|---|---|---|
| Cadence | Mon discovery; Wed/Fri checks; Friday final | Mon discovery; daily pulse (30 credits) | Mon; Wed/Fri targeted; one final weekday report | Follow the owner: drop the daily pulse |
| Status labels | RESEARCH / TEST / BUILD / HOLD-STOP | TEST / PRODUCT TEST / BUILD / HOLD / KILL / SCALE | RESEARCH / TEST / BUILD / HOLD-STOP | Follow the owner; PRODUCT TEST and SCALE could become sub-labels of BUILD |
| **Economics gate 7** | LTV/CAC ≥ 3 **or** payback ≤ 6 months | LTV/CAC ≥ 3 **and** payback ≤ 3 months, plus positive downside contribution | Not specified | **Material.** Under Codex's gate, co-parenting's base case (monthly payback ~9.8 months) **fails**, and so does Claude's proposed TEST. Needs Codex's audit and the owner's decision. |
| Target horizon | 12-month path used in the Top-5 table | 6 months from a confirmed start date, gross subscription MRR | Not restated | Adopt Codex's definition (gross subscription MRR, 6 months), pending the owner |
| Founder capacity | 40-hour first version; hours per week unstated | 8 hours a week, so about 5 weeks per build | 2-3 launches a month | **Material.** 8 hours a week cannot support 2-3 launches a month. The owner must confirm real capacity. |
| Registry | `research/candidates.csv` | `data/portfolio.json` (richer schema, decisions log) | Keep dated artifacts | Adopt `data/portfolio.json` as the single registry; Claude migrates its 12 candidate rows into it once Codex's branch is merged |
| Artifact paths | `research/<date>/{raw,evidence,audit,report}` | `data/snapshots/<date>/`, `reports/<date>-*.md`, `experiments/<idea-id>/` | Keep dated artifacts and results | Either works; pick one at merge |
| Weekly credits | ~420 | ≤ 500 | Not specified | Use ≤ 500 with Codex's itemized reservation |
| Review text | Short quotes with review IDs (no reviewer names) | Paraphrase by default; no personal data | — | Claude to paraphrase in future packs. Existing quotes carry IDs only, but the owner may prefer paraphrase. |
| Raw responses in git | Committed (2.9 MB, includes public developer contact emails inside detail payloads) | Normalized small snapshots; avoid personal data | — | Codex to decide whether to keep raw files or replace them with normalized snapshots plus checksums |

**Claude's position on gate 7:** Codex's stricter gate is the more defensible founder screen at 8 hours a week. If it's adopted, co-parenting moves from proposed TEST to **RESEARCH**, unless annual-first pricing, modeled as separate cohorts in `scripts/economics.py`, passes it. This needs Codex's annual-cohort model.

---

## 11. Errata after the Codex audit (2026-11-06)
See `audit/claude_response.md`.
- **mise:** `tiktok_ads_total_count = 417` (RAW). The earlier "no paid ads" claim was wrong.
- **Co-parenting "annual pays back on day one":** withdrawn (Codex A08).
- **12-month payer timelines and paid-budget rows:** withdrawn as forecasts (A15).
- **Co-parenting status:** RESEARCH, agreed by both agents.
