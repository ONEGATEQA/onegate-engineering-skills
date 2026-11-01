Print the current authorization tier for the active task and state what approvals are required before the next action.

Check:
1. Current worktree and branch (`git branch --show-current`, `git worktree list`)
2. What action is pending (if any)
3. What tier that action requires under `protocols/authorization.md`
4. Whether explicit authorization has been received for that action in this session

Output format:
```
Current tier: [0 Observe / 1 Local write / 2 Git publish / 3 Infrastructure]
Pending action: <describe it>
Authorization received: [yes — <exact scope> / no — required before proceeding]
Next step: <what you need from the human, or what you will do]
```

Do not proceed past this output until the human confirms the next action.
