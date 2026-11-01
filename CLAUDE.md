# OneGate Engineering Skills — agent instructions

This file is for agents working **on this repository itself** (adding skills,
fixing protocols, updating tests). Do not copy it into other projects.

For the reusable assets, see `skills/`.

---

## Repository structure

```
skills/                     → Core skills (one SKILL.md per directory)
  onegate-engineering/      → Main workflow skill with anti-rationalization tables
  prompt-injection-defense/ → Injection scanning skill
  session-recovery/         → Session re-orientation skill
  behavioral-verification/  → Runnable scenario tests
protocols/                  → Required protocols (authorization, security, verification, worktrees)
agents/                     → Agent personas (security-auditor, code-reviewer)
.claude/commands/           → Claude Code slash commands
adapters/                   → Per-tool installation guides
templates/                  → Task checklist and handoff template
tests/                      → Static validator
TESTED.md                   → Behavioral test evidence log
```

---

## Conventions

- Every skill lives in `skills/<name>/SKILL.md`
- Every SKILL.md starts with YAML frontmatter: `name`, `description`, `compatibility`, `tested-on`
- Description format: what it does (third person), then "Use when..."
- Every skill must be self-contained: embed any reference content it needs directly
- No broken cross-file paths on partial install
- No external dependencies in skill files

## Contribution rules

Before adding a new skill:
1. Check that no existing skill already covers the use case
2. Confirm the skill is self-contained (test by reading it in isolation)
3. Add a corresponding scenario to `skills/behavioral-verification/SKILL.md`
4. Run `python3 tests/validate.py` — it must pass
5. Add the skill to the README table

Before modifying `protocols/authorization.md`:
- This is the core differentiator. Any change requires careful review.
- Do not reduce tier requirements without documented justification.
- Run all behavioral verification scenarios after changes.

## Authorization for work on this repo

All changes follow `protocols/authorization.md`.
No special exemptions apply because this is the skills repo itself.

## Contact

hash@onegate.qa · [onegate.qa](https://onegate.qa)
