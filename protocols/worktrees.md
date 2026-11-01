# Git worktree isolation

Before any change: `pwd`, `git rev-parse --show-toplevel`, `git branch --show-current`, `git rev-parse HEAD`, `git status --short --branch`, and `git worktree list`. Confirm the assigned path and branch. Never assume the shell starts in the correct directory.

Create a new worktree only with approval and after verifying its base SHA, e.g. `git worktree add -b feat/<task-slug> ../work-<task-slug> <base-sha>`. Verify status after creation. Avoid editing another agent's worktree, reusing a stale task branch or touching untracked files without permission. Do not run `git clean`, `git reset --hard`, `git worktree remove`, force-push or branch deletion without explicit approval and a reviewed impact statement.

Commit identity must be verified with `git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT` before committing. The project owner supplies the exact identity; this public skill does not prescribe one. GitHub connector commits may not allow identity overrides; do not assume connector identity matches local Git configuration.
