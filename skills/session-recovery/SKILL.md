---
name: session-recovery
description: Re-orient after session interruption, connection loss, or stale context. Use when resuming any session where work may have been in progress, after connection loss, or when starting from a handoff. Self-contained — embed this into your context at session start.
compatibility: Any agent. No repository access required for Steps 0–2.
tested-on: See TESTED.md in the distribution root.
---

# Session Recovery

AI agent sessions can be interrupted by connection loss, process restart, context limits,
or human intervention. Resuming work without re-orienting is a common source of mistakes:
the agent acts on a stale mental model of the repository state.

This skill forces a complete re-orientation before any action is taken in a resumed session.

---

## When to use this skill

Use at the **start of any session where work may have been in progress**, including:

- Resuming a task from a prior conversation or session
- Reconnecting after a connection error or timeout
- Starting work from a handoff document written by another agent
- Starting work described in a ticket or issue without context from the original session
- Any session where you are unsure whether local state matches what you last knew

---

## Recovery process

### Step 0 — Declare uncertainty

Before doing anything else, state explicitly:

> "I am resuming a session. I do not have direct memory of prior work. I will
> re-verify current state before taking any action."

Do not claim to remember what was done previously. Do not act on what you
think the state was. Verify.

---

### Step 1 — Verify repository state

Run these commands before any file edits or Git operations:

```bash
pwd
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git status --short --branch
git worktree list
git log --oneline -5
git stash list
```

Record the output. Identify:
- Is there uncommitted work? If yes, who authorized it and is it safe to continue?
- Is the branch what you expected? If not, stop and clarify.
- Does HEAD match what the handoff document described? If not, something changed.

---

### Step 2 — Read the handoff document

If a handoff document exists (from `templates/handoff.md`), read it now.
Verify each field against actual repository state:

| Handoff field | Verify against |
|---|---|
| Branch / HEAD | `git branch --show-current` and `git rev-parse HEAD` |
| Files changed | `git diff HEAD~1 --name-only` or `git status` |
| Authorization received | Current session; prior session authorization has expired |
| Tests executed | Test output files if present; do not assume tests still pass |
| Git state (committed/pushed) | `git log --oneline origin/<branch>..HEAD` |

If the handoff is absent, resume from Step 3 without assuming prior state.

---

### Step 3 — Re-read project governance

Read these files, even if you read them before:
- `CLAUDE.md` (Claude Code) or `AGENTS.md` (Codex) in the project root
- Any skill files referenced by the task
- `protocols/authorization.md` — **authorization from a prior session has expired**

Do not rely on memory of what governance said. Re-read it.

---

### Step 4 — Re-establish authorization

Authorization does not carry across sessions. Before taking any Tier 1+ action:
- Confirm the current task and scope with the human
- Obtain fresh authorization for the specific next action
- Do not infer authorization from prior conversation history

State explicitly what you are about to do and wait for confirmation.

---

### Step 5 — Identify the next action

From the verified state, determine:
- What was completed (with evidence from git state)
- What was not completed
- What the next action is

Present this to the human before acting.

---

## Anti-rationalization table

| Excuse the agent uses | Why it's wrong | What to do instead |
|---|---|---|
| "I remember what was happening, I'll continue" | Agent memory of prior sessions is unreliable | Re-verify actual state with git commands |
| "The handoff says it was committed, so it was" | Handoffs can be written optimistically or be stale | Verify with `git log` |
| "I had authorization to push in the last session" | Authorization expires at session boundary | Ask for fresh authorization |
| "The tests were passing before the interruption" | The codebase may have changed | Run the tests again |
| "I'll just finish the last step, it was almost done" | "Almost done" without verification introduces unreviewed changes | Complete the recovery process first |

---

## Red flags requiring human input before proceeding

- Uncommitted work exists with no corresponding handoff or task log
- Repository state does not match the handoff description
- A push or deploy appears to have happened that was not in the handoff
- The branch contains commits not written in this session
- Multiple worktrees exist in unexpected states
