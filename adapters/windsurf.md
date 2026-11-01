# Windsurf adapter

## Installation

Windsurf reads `.windsurfrules` from the project root as project-level instructions.

1. Create or edit `.windsurfrules` in your project root
2. Add a reference to the skill:

```
Read skills/onegate-engineering/SKILL.md and its referenced protocols before any code change.
Enforce authorization tier requirements from protocols/authorization.md.
```

Or copy the skill content directly into `.windsurfrules`.

## Cascade-level rules

For workspace-wide rules that apply across all projects, add the skill reference to
Windsurf's global rules settings (Settings → Cascade → Rules).

## Limitations

- Windsurf's Cascade agent does not have a direct equivalent to Claude Code's tool approval UI. Authorization tier enforcement relies on the agent following the protocol; there is no host-level block on push or deploy.
- The `.windsurfrules` file is loaded at session start; changes during a session may not take effect until the next session.
- Windsurf does not currently support slash commands in the same format as Claude Code. Use `.windsurfrules` sections (e.g., `## Verification`) to embed command behavior.

## Verification

Before relying on this skill in Windsurf, run Scenario 1 (ambiguous approval) from `skills/behavioral-verification/SKILL.md` in a disposable repository. Windsurf's Cascade agent has known tendencies to be more proactive; verify that it correctly requires explicit push confirmation.

Record results in `TESTED.md`. Compatibility is unverified until tests are recorded.
