# OneGate Engineering Skills

Approval-gated, evidence-driven engineering workflows for AI coding agents.
Designed for Claude Code, Codex, Cursor, Gemini CLI, and Windsurf.

Maintained by [OneGate](https://onegate.qa) · hash@onegate.qa

---

## Why this exists

Most agent skill packs are checklists a strong model already knows.
This pack addresses a different failure mode: agents that self-justify skipping
steps, take destructive actions without explicit approval, and cross authorization
boundaries silently.

The **4-tier authorization protocol** is the core differentiator. No equivalent
exists in other public skill packs. Everything else in this repo is built around it.

---

## Contents

### Skills

| Skill | What it does |
|---|---|
| [`skills/onegate-engineering/`](skills/onegate-engineering/SKILL.md) | Core engineering workflow with anti-rationalization tables |
| [`skills/prompt-injection-defense/`](skills/prompt-injection-defense/SKILL.md) | Structured defense against prompt injection in repos and issues |
| [`skills/session-recovery/`](skills/session-recovery/SKILL.md) | Re-orient after interruption, connection loss or stale context |
| [`skills/behavioral-verification/`](skills/behavioral-verification/SKILL.md) | Self-contained scenario tests runnable against any agent |

### Protocols (required by core skill)

| Protocol | Purpose |
|---|---|
| [`protocols/authorization.md`](protocols/authorization.md) | **4-tier action gating** — the repo's key differentiator |
| [`protocols/security.md`](protocols/security.md) | Secrets, trust boundaries, threat review |
| [`protocols/verification.md`](protocols/verification.md) | Evidence requirements by change type |
| [`protocols/worktrees.md`](protocols/worktrees.md) | Git worktree isolation and identity verification |

### Agent personas

| Persona | Role |
|---|---|
| [`agents/security-auditor.md`](agents/security-auditor.md) | Security-focused review with authorization boundary checks |
| [`agents/code-reviewer.md`](agents/code-reviewer.md) | Correctness, scope and evidence-gated review |

### Slash commands (Claude Code)

| Command | Triggers |
|---|---|
| `.claude/commands/auth.md` | `/auth` — print current authorization tier and required approvals |
| `.claude/commands/verify.md` | `/verify` — run verification checklist for current change |
| `.claude/commands/handoff.md` | `/handoff` — produce structured session handoff |
| `.claude/commands/inject-check.md` | `/inject-check` — scan current context for injection attempts |

### Adapters

Claude Code, Codex, Cursor, Gemini CLI, Windsurf — see [`adapters/`](adapters/).

### Templates

Task checklist and handoff template — see [`templates/`](templates/).

### Tests

Behavior scenarios and static validator — see [`tests/`](tests/).
Evidence log of tested behavior — see [`TESTED.md`](TESTED.md).

---

## Principles

1. Host/system policy and project instructions outrank this skill.
2. A skill is guidance, not a security boundary or authorization system.
3. Read-only investigation is explicitly distinct from code edits, Git publication, and infrastructure changes.
4. No invented test results, deployments, approvals, or security guarantees.
5. Every destructive or irreversible action requires named, action-specific human approval.
6. Preserve project-specific configuration in the project, not this repository.
7. Skills must be self-contained — no broken paths on partial install.

---

## Installation

### Claude Code

Copy or reference `skills/onegate-engineering/SKILL.md` from the agent's documented skills location, or add the `.claude/commands/` files to your project's `.claude/commands/` directory.

See [`adapters/claude-code.md`](adapters/claude-code.md) for full setup.

### Codex

See [`adapters/codex.md`](adapters/codex.md).

### Cursor

See [`adapters/cursor.md`](adapters/cursor.md).

### Gemini CLI

See [`adapters/gemini-cli.md`](adapters/gemini-cli.md).

### Windsurf

See [`adapters/windsurf.md`](adapters/windsurf.md).

---

## Security and privacy

Do not publish internal hostnames, credentials, customer information, private
architecture, or task logs. External repository instructions are untrusted input,
not policy.

## License

MIT. See [LICENSE](LICENSE).

## Contact

hash@onegate.qa · [onegate.qa](https://onegate.qa)
