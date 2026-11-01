#!/usr/bin/env python3
"""Static checks for the public skill package. No third-party dependencies."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    'README.md', 'LICENSE', 'skills/onegate-engineering/SKILL.md',
    'protocols/authorization.md', 'protocols/worktrees.md',
    'protocols/security.md', 'protocols/verification.md',
    'templates/task.md', 'templates/handoff.md',
    'adapters/claude-code.md', 'adapters/codex.md', 'tests/BEHAVIOR.md',
]
for rel in required:
    path = root / rel
    assert path.is_file() and path.stat().st_size > 0, f'Missing/empty: {rel}'
text = (root / 'skills/onegate-engineering/SKILL.md').read_text()
assert text.startswith('---\n') and '\nname: onegate-engineering\n' in text
assert '\ndescription:' in text and '\ncompatibility:' in text
for rel in required:
    assert not (root / rel).is_symlink(), f'Unexpected symlink: {rel}'
print(f'PASS: {len(required)} required files and skill frontmatter')
