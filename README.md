# AppKittie research engine

Shared research pipeline. It finds app opportunities worth a bounded demand test, using live AppKittie data. **Claude** leads discovery and the final report; **Codex** audits independently. App code lives in separate repos, one per app.

- `docs/RESEARCH_PROTOCOL.md`: the portable protocol: cadence, gates, economics, statuses, report format. **Start here.**
- `research/<date>/`: dated evidence packs:
  - `raw/`: saved AppKittie responses, plus SHA256SUMS.
  - `evidence/`: extracts and review quotes.
  - `MANIFEST.md`: every call made.
  - `audit/codex.md`: Codex's audit.
  - `report/final.md`: the weekly report.
- `research/candidates.csv`: the candidate registry and statuses (RESEARCH / TEST / BUILD / HOLD-STOP).
- `experiments/`: pre-registered demand tests (`TEMPLATE.md`) and their results.
- `.claude/skills/appkittie-brief/`: Claude's entry point into the protocol.
- `.mcp.json`: the AppKittie MCP connection, which reads `APPKITTIE_API_KEY` from the environment.

The current handoff is `research/2026-11-05/HANDOFF_FOR_CODEX.md`.
