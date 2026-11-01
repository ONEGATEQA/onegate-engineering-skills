# Claude Code adapter

## Installation

### Option A — Project-level (recommended)

1. Copy `skills/onegate-engineering/SKILL.md` to your project's skills directory
   (check Claude Code documentation for the current supported path)
2. Copy `.claude/commands/*.md` to your project's `.claude/commands/` directory
3. Add a reference in your project's `CLAUDE.md`:

```markdown
## Engineering skills
Use the OneGate engineering skill for all code changes.
Read skills/onegate-engineering/SKILL.md and its referenced protocols at session start.
```

### Option B — Direct CLAUDE.md embed

Copy the contents of `skills/onegate-engineering/SKILL.md` directly into your project's `CLAUDE.md`. Keep the protocol files alongside it in a `protocols/` directory, or embed their content directly.

Self-contained embed is recommended: it ensures the protocols are always available even if the skills directory is not in scope.

## Slash commands

Copy or symlink `.claude/commands/*.md` to your project's `.claude/commands/` directory:

- `/auth` — print current authorization tier
- `/verify` — run verification checklist
- `/handoff` — produce session handoff
- `/inject-check` — scan context for injection attempts

Verify commands are discovered: `claude /auth` in the project directory.

## Tool permissions

Review Claude Code's tool permission settings for your project. Consider:

- Disable automatic `git push` in tool approvals if you want Tier 2 enforcement at the host level
- Disable automatic shell command execution for infrastructure commands if you want Tier 3 enforcement at the host level

Host-level controls are stronger than skill-level guidance.

## Verification

Before relying on this skill in Claude Code, run all 7 scenarios from
`skills/behavioral-verification/SKILL.md` in a disposable repository.
Record agent version and results in `TESTED.md`.

Compatibility is verified against Claude Code as documented in `TESTED.md`.
