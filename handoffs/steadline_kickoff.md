# Steadline kickoff (from app-engine to the new `steadline` repo)

**Owner decision (2026-11-06):** pursue co-parenting records as **Steadline**.

**Engine status at handoff:** RESEARCH, agreed by Claude and Codex. Not BUILD-ready. The first work is therefore **validation assets plus a narrow prototype**, not a full app.

## What the evidence supports (from app-engine)
- **Demand signals (AppKittie estimates; revenue geography unknown):**
  - Documented: launched 2026-08; ~$33K/mo in Oct 2026 (RAW history).
  - OurFamilyWizard: ~$386K → $504K/mo, Dec 2025 → Oct 2026 (RAW history).
  - TalkingParents: ~$500K/mo (UNVERIFIED).
- **Hypothesis, unverified:** parents in court-mandated apps (OurFamilyWizard, TalkingParents) also need a **personal** record and an **attorney-ready timeline**, which those apps don't provide well.
- **Economics (Codex audit A08/A09):** paid acquisition does not pay back at base assumptions. With a **$500/month total budget**, growth must come from app store search, attorneys, and communities.
- **Name screening:**
  - USPTO "STEADLINE" filing found only in class 025 (clothing); no software-class conflict seen in the owner's screenshot.
  - steadline.com was available on 2026-11-05.
  - **Neither is legal clearance.**

## Week 1 scope (proposed)
1. **Landing page** (Next.js on Vercel):
   - Headline: "A calm, time-stamped record of co-parenting. Your attorney gets a clean timeline."
   - A pricing step ($14.99/mo or $149/yr, intent only, no charge).
   - Waitlist saved to Supabase, plus an analytics event per step.
2. **Sample timeline export:** a realistic, fictional PDF to show parents and attorneys. This is the core validation asset.
3. **Interview kit:** a 10-question script for parents and a 6-question script for attorneys. **Outreach only after the owner authorizes it, and through the owner's chosen channel.**
4. **Pre-registered experiment plan** (`experiments/EXP-2026-01-steadline/plan.md`) with stop / revise / expand thresholds, **before any ad spend.**

## Explicitly not in Week 1
- The iOS app build.
- Messaging between parents, calendars, payments.
- Android.
- Any claim of "court-admissible", "tamper-proof" or legal outcomes.

## Repo setup checklist (owner)
1. Create the GitHub repo `uak1261/steadline` (private).
2. Give the Claude GitHub app and Codex access to it.
3. Start a new Claude Code session with `steadline` attached. To read evidence, also attach `uak1261/app-engine` (read-only).
4. Codex: same repo. Agree on separate branches (`claude/*`, `codex/*`) and that **the owner merges.**
5. Later, when needed (not now): Vercel and Supabase connections, a domain, the Apple Developer account, and an LLC.

## Collaboration rules (carried over)
- Claude: product, UX, landing page, customer-problem work.
- Codex: independent review of claims, economics and scope, plus reproducible models.
- No ad spend, outreach, App Store submission or production deploy without the owner's explicit approval.
- Disagreements are recorded, not forced into agreement.
