# Setup and first run

1. Check out the persistent-engine branch in both coding environments. Use separate work branches. Set APPKITTIE_API_KEY through each environment's secret configuration or an uncommitted local shell environment. A .env file is not automatically loaded by either configuration here.
2. Claude Code uses the existing `.mcp.json`; the documented hosted endpoint is `https://mcp.appkittie.com/mcp`. Codex CLI/IDE uses `.codex/config.toml` in a trusted project, or copy that server table into the user's `~/.codex/config.toml`. Hosted coding environments may require their own MCP configuration and network allowlist. Repository access alone is insufficient.
3. Start a session in each environment. Inspect available MCP tools and call the free supported-countries tool before paid queries. Confirm errors, metric scopes, and credits without printing the key. This smoke test has not been performed by this starter.
4. Confirm `data/portfolio.json` founder assumptions: start date, hours, test budget, monthly acquisition budget, total acceptable loss, and actual Apple fee. Null budgets block capital feasibility, not research.
5. Paste the weekly scout prompt from `docs/prompts.md` into Claude Code. Pass the resulting branch/report/evidence paths to Codex using the audit prompt. Choose a portfolio writer for reconciliation.
6. Run tests with `python3 -m unittest discover -s tests`. Run the hypothetical calculator with `python3 scripts/economics.py examples/economics.json`. Supply a separate input for each real scenario. Keep unknowns explicit rather than borrowing the example as a benchmark.
7. Update existing scheduled runners to use the daily monitor and weekly scout prompts only after a successful manual run. Require them to fetch current state and persist reports. No schedule or live API connection is activated by these files.

The original `.claude/skills/appkittie-brief/SKILL.md` remains intact as a legacy brief. Its no-history method and economics OR gate are superseded only when using this new persistent workflow. Do not invoke the old slash command for the new engine.
