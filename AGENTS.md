# App Engine

Read `docs/engine.md` before research, ranking, or implementation. It is the shared operating policy for Codex and Claude Code. Read `data/portfolio.json` and recent reports before making recommendations.

- Target: $30K-$50K gross subscription MRR across the portfolio within six months. Treat this as an ambition, never a forecast or guarantee. Report net proceeds, contribution after acquisition, cash burn, and founder hours separately.
- Keep at most 20 active ideas, five finalists, two validation experiments, and one build. An idea is an audience + recurring problem + advantage + acquisition channel, not a competitor's app name.
- Preserve stable idea IDs and decisions. Never regenerate a fresh top five without explaining additions, removals, or changed evidence. Do not resurrect rejected ideas without new evidence.
- Label every input observed, vendor-estimated, founder assumption, or unknown. Missing values are null, never zero. Store source, timestamp, country/metric scope, and confidence with evidence. Do not present global revenue as US revenue.
- AppKittie discovers hypotheses. It does not establish competitor profitability, retention, CAC, or our willingness-to-pay. Never infer these from revenue/downloads or ad activity.
- Use the live MCP schema or official API documentation before choosing filters. Save normalized snapshots and query parameters. Do not commit secrets or raw customer/review personal data.
- Claude owns research proposals; Codex owns reproducible economics and independent challenge. Read the other agent's evidence but make an independent assessment. Reconcile disagreements in the decision log. Use separate branches and one portfolio writer at a time.
- Run `python3 -m unittest discover -s tests` after changing economics. Use `python3 scripts/economics.py examples/economics.json` for the labeled hypothetical example.
- No autonomous advertising spend, purchase, outreach, App Store submission, or production deployment. Research and code changes can proceed within the request.
- The original `/appkittie-brief` is retained as a legacy workflow. For this engine use `docs/prompts.md`; its persistent state and revised gates replace legacy stateless assumptions. Do not mix the two methods in one run.
