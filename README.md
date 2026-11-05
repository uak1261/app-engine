# AppKittie Idea Incubation Brief

A recurring brief that finds the top 5 app opportunities with potential to reach $30-50K/month, using live AppKittie data. No backend and no stored data: each run calls the AppKittie MCP server, reasons over the results, and writes the brief.

- `.mcp.json`: connects to `https://mcp.appkittie.com` and reads the API key from the `APPKITTIE_API_KEY` environment variable.
- `.claude/skills/appkittie-brief/SKILL.md`: the brief method, credit cap, screen, scoring and output format.

## Setup (once)
1. Cloud environment settings: add `APPKITTIE_API_KEY` (your AppKittie API key).
2. Network access: allow `mcp.appkittie.com`.
3. Start a new session and run `/appkittie-brief` to test.
