Run the verification checklist for the current change and report results.

Steps:
1. Identify the change type (logic / API / UI / mobile / database / infrastructure)
2. Look up the minimum verification requirements in `protocols/verification.md`
3. Run the applicable test commands for this project
4. Capture: exact command, working directory, output, pass/fail counts
5. Report what was NOT tested and why

Output format:
```
## Verification report — <date>

Change type: <type>
Minimum requirements: <from protocols/verification.md>

### Tests run
| Command | Directory | Result |
|---|---|---|
| <cmd> | <dir> | PASS/FAIL (<N> passed, <M> failed) |

### Not tested
- <item>: <reason>

### Overall status
VERIFIED / PARTIAL (<gaps listed above) / BLOCKED (<reason>)
```

Do not claim VERIFIED unless all minimum requirements for the change type are met.
If tests cannot be run, state BLOCKED with the reason — do not substitute code inspection.
