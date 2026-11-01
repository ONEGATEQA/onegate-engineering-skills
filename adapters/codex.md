# Codex adapter

## Installation

1. Copy `skills/onegate-engineering/SKILL.md` to the skills location supported
   by your installed Codex version
2. Reference the skill in your project's `AGENTS.md`:

```markdown
## Engineering skills
Use the OneGate engineering skill for all code changes.
Read the skill and its referenced protocols at session start.
```

Or embed the skill content directly in `AGENTS.md` for a self-contained setup.

## Tool permissions

Codex tool permission flags differ from Claude Code. Before using this skill:
- Review which shell commands are enabled for the agent
- Consider disabling automatic `git push` capability if Tier 2 enforcement is needed
- Review network access settings for infrastructure commands

## Session memory

Codex session handling differs from Claude Code. The `skills/session-recovery/SKILL.md`
skill is especially important. Always run session recovery at the start of any resumed
Codex session, particularly after interrupted work.

## Verification

Run Scenario 1 (ambiguous approval) and Scenario 2 (prompt injection) from
`skills/behavioral-verification/SKILL.md` in a disposable repository before relying
on this skill in Codex. Record results in `TESTED.md`.

Compatibility is unverified until tests are recorded. Claude Code-specific hooks,
commands, and CLAUDE.md features do not carry over to Codex.
