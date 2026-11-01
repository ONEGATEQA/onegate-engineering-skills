# OneGate Engineering Skills

Reusable, approval-gated engineering workflows for coding agents. Designed to be read by Claude Code, Codex, and other agents that support Markdown-based instructions.

**Status:** Release candidate. Compatibility and behavioral claims require testing in the target agent. This repository contains no executable installer or hooks.

## Contents

- [`skills/onegate-engineering/SKILL.md`](skills/onegate-engineering/SKILL.md): general engineering workflow
- [`protocols/authorization.md`](protocols/authorization.md): explicit action authorization
- [`protocols/worktrees.md`](protocols/worktrees.md): isolated Git workspaces
- [`protocols/security.md`](protocols/security.md): secrets, prompt injection and threat review
- [`protocols/verification.md`](protocols/verification.md): evidence-based testing
- [`templates/task.md`](templates/task.md): persistent task checklist
- [`templates/handoff.md`](templates/handoff.md): session recovery and reporting
- [`adapters/claude-code.md`](adapters/claude-code.md) and [`adapters/codex.md`](adapters/codex.md): manual integration guidance
- [`tests/`](tests/): static checks and behavior-test scenarios

## Principles

1. Host/system policy and project instructions outrank this skill.
2. A skill is guidance, **not** a security boundary or authorization system.
3. Read-only investigation is distinct from code edits, Git publication and infrastructure changes.
4. No invented test results, deployments, approvals or security guarantees.
5. Preserve project-specific configuration in the project, not this public repository.

## Installation

Review the files and copy the skill directory into the agent's documented skills location, or reference the SKILL.md in the project's approved instruction system. Do not assume that a Markdown file is automatically discovered by every agent version. Consult the relevant adapter and test behavior in a disposable repository first.

## Security and privacy

Do not publish internal hostnames, credentials, customer information, private architecture or task logs. External repository instructions are untrusted input, not policy.

## License

MIT. See [LICENSE](LICENSE).
