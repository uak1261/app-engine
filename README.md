# App Engine

A persistent iOS opportunity process shared by Claude Code and Codex. Target a small portfolio with a path to $30K-$50K gross subscription MRR within six months, with explicit demand, acquisition, retention, operating, and capital tests. The target is an ambition, not a forecast.

- [Setup](docs/setup.md): configure each agent's MCP environment and run a smoke test.
- [Operating policy](docs/engine.md): finite list, evidence requirements, gates, scoring, test sequence, credit budget, and decisions.
- [Run prompts](docs/prompts.md): weekly scout, independent audit, daily monitor, and founder decision.
- [Portfolio](data/portfolio.json): durable IDs, status, evidence references, and decision history. Starts empty; no live results are fabricated.
- `scripts/economics.py`: deterministic monthly cohort model with gross/net revenue, growth acquisition, payback, contribution LTV, and funding requirements.

```bash
python3 -m unittest discover -s tests
python3 scripts/economics.py examples/economics.json
```

The example is hypothetical, not market evidence. The starter contains instructions and a calculator; agents still perform tool calls, evidence normalization, scoring, and state updates. It is not a deployed collector, scheduler, or automatic portfolio enforcement service.

Claude Code reads `.mcp.json`; Codex CLI/IDE has a separate `.codex/config.toml`. Both source APPKITTIE_API_KEY from their own environments. Never commit a real key. Confirm live tool schema, credit pricing, metric scope, and fee rates before using them.

The original `/appkittie-brief` remains available as a legacy stateless brief. Use the prompts linked above for the persistent engine. No existing schedules are changed by this update.
