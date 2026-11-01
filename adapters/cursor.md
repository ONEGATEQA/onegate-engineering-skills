# Cursor adapter

## Installation

1. In your project root, create or edit `.cursorrules`
2. Add a reference to the skill:

```
Read skills/onegate-engineering/SKILL.md and its referenced protocols before any code change.
```

Or copy the skill content directly into `.cursorrules` if you want it self-contained.

## Slash commands

Cursor does not have a native slash-command system equivalent to Claude Code's `.claude/commands/`.
Add the command content from `.claude/commands/*.md` as named sections in `.cursorrules` under headings like `## When asked to verify` or `## When asked for a handoff`.

## Limitations and known behavior

- Cursor's agent does not always reload `.cursorrules` on session resume; verify the skill is active at the start of any resumed session.
- Tool permission controls in Cursor differ from Claude Code. Authorization tier enforcement depends on what tools Cursor exposes to the agent. Review Cursor's tool settings and disable any tools that should not be accessible without Tier 2/3 approval (e.g., automatic push, auto-deploy).
- Cursor does not enforce worktree isolation at the host level. The worktree protocol must be enforced by the agent per `protocols/worktrees.md`.

## Verification

Before relying on this skill in Cursor, run Scenario 1 and Scenario 2 from `skills/behavioral-verification/SKILL.md` in a disposable repository. Record the results in `TESTED.md`.

Compatibility is unverified until tests are recorded.
