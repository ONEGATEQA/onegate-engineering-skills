# Release candidate review

Before a public release:

- [ ] Inspect every tracked file for secrets, private infrastructure and personal data
- [ ] Confirm license and third-party provenance
- [ ] Run `python3 tests/validate.py`
- [ ] Test discovery and behavior in Claude Code; record exact version and results
- [ ] Test discovery and behavior in Codex; record exact version and results
- [ ] Confirm Git author and committer email in the actual publishing mechanism
- [ ] Confirm branch protections and review requirements

Do not label this release as production-ready until compatibility and behavior tests are recorded.
