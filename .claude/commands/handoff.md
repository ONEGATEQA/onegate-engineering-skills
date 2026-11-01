Produce a structured session handoff using the template in `templates/handoff.md`.

Steps:
1. Run `git branch --show-current`, `git rev-parse HEAD`, `git status --short`, `git log --oneline -5`
2. List all files changed in this session
3. State which tests were run and their results
4. State the exact git state: uncommitted / committed / pushed / merged
5. State what authorization was received and its exact scope
6. State the next required action and what approval it needs

Fill every field of the handoff template. Do not leave any field blank.
If information is unknown, write "unknown — verify before resuming."

Do not describe future work as completed. Do not advance the state label without evidence.

After producing the handoff, save it to `<task-slug>-handoff-<YYYY-MM-DD>.md` in the
project's approved task log location.
