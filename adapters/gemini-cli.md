# Gemini CLI adapter

## Installation

Gemini CLI reads `GEMINI.md` from the project root as project-level instructions.

1. Create or edit `GEMINI.md` in your project root
2. Add a reference to the skill:

```markdown
## Engineering workflow

Read `skills/onegate-engineering/SKILL.md` and its referenced protocols
(`protocols/authorization.md`, `protocols/security.md`, `protocols/verification.md`,
`protocols/worktrees.md`) before any code change.
```

Or copy the skill content directly into `GEMINI.md`.

## Commands

Gemini CLI supports `.gemini/commands/` with `.toml` files. To add slash commands:

Create `.gemini/commands/auth.toml`:
```toml
[command]
name = "auth"
description = "Print current authorization tier and required approvals"
prompt = "<contents of .claude/commands/auth.md>"
```

Repeat for `verify`, `handoff`, and `inject-check`.

## Limitations

- Gemini CLI tool permissions differ from Claude Code. Review which tools are enabled and whether they include write-capable or publish-capable operations.
- Session memory behavior differs. The session-recovery skill is especially important; run it at the start of any resumed Gemini CLI session.

## Verification

Before relying on this skill with Gemini CLI, run Scenario 1 and Scenario 2 from `skills/behavioral-verification/SKILL.md` in a disposable repository. Record results in `TESTED.md`.

Compatibility is unverified until tests are recorded.
