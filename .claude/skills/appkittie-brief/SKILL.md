---
name: appkittie-brief
description: Run the shared AppKittie research pipeline (Monday discovery, Wednesday/Friday finalist checks, one final weekly report that includes the Codex audit). Use when asked to run the AppKittie research, discovery, finalist checks, or the weekly opportunity report.
---

# AppKittie research pipeline

The single source of truth is **`docs/RESEARCH_PROTOCOL.md`**. Read it first and follow it exactly. This file only adds Claude-specific notes.

## Claude's role
Discovery lead, customer-problem analyst, and final presenter. Codex audits independently.

## Claude-specific notes
- **Pick the activity by day (America/Chicago):**
  - Monday: discovery, 300-credit cap.
  - Wednesday or Friday: finalist checks, 60-credit cap.
  - Friday: then write the final report.
  - If unsure, ask; never run discovery twice in a week.
- **Save every AppKittie response to `research/<date>/raw/` at call time,** with a manifest row, before analysing it. If MCP tool output gets truncated or saved elsewhere, copy it in. A number with no saved response must be labeled UNVERIFIED.
- **Before the Friday report:** read `research/<date>/audit/codex.md`. If it's missing, say "Codex audit not received" and set every proposed TEST to RESEARCH. **Never imply Codex agreement without its file.**
- **Statuses:** only RESEARCH, TEST, BUILD, HOLD/STOP, as defined in the protocol.
- **Respect the WIP limits:** 1 new experiment a week, at most 2 experiments active, at most 1 build active. Check `research/candidates.csv` and `experiments/`.
- **No separate daily delivery.** Only the Friday final report goes to the owner.
