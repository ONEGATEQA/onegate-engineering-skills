# Verification protocol

Define evidence by change type, using the project's actual commands (never assume a package manager or test runner):

| Change | Minimum verification |
|---|---|
| Pure logic | Focused unit tests, regression cases, lint/type checks where available |
| API/auth/data | Negative authorization tests and integration tests against a controlled environment |
| UI | Component tests plus rendered/runtime verification for changed flows; accessibility and localization checks where applicable |
| Mobile | Target-platform build and relevant widget/integration tests; device testing for platform behavior |
| Database/migrations | Reviewed migration, rollback/recovery plan, isolated test database and explicit execution approval |
| Infrastructure | Validated plan, security/cost impact and separate apply approval |

Capture command, directory, environment, test counts, failures and what was not tested. If tests are infeasible, state the reason, risk and required follow-up; never silently substitute code inspection for passing tests. Distinguish tests written from tests actually run.
