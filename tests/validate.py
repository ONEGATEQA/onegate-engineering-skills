#!/usr/bin/env python3
"""Static checks for the OneGate Engineering Skills package. No third-party dependencies."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]

# Required files — core
required = [
    'README.md',
    'LICENSE',
    'CLAUDE.md',
    'AGENTS.md',
    'TESTED.md',
    # Skills
    'skills/onegate-engineering/SKILL.md',
    'skills/prompt-injection-defense/SKILL.md',
    'skills/session-recovery/SKILL.md',
    'skills/behavioral-verification/SKILL.md',
    # Protocols
    'protocols/authorization.md',
    'protocols/worktrees.md',
    'protocols/security.md',
    'protocols/verification.md',
    # Agents
    'agents/security-auditor.md',
    'agents/code-reviewer.md',
    # Commands
    '.claude/commands/auth.md',
    '.claude/commands/verify.md',
    '.claude/commands/handoff.md',
    '.claude/commands/inject-check.md',
    # Templates
    'templates/task.md',
    'templates/handoff.md',
    # Adapters
    'adapters/claude-code.md',
    'adapters/codex.md',
    'adapters/cursor.md',
    'adapters/gemini-cli.md',
    'adapters/windsurf.md',
    # Tests
    'tests/BEHAVIOR.md',
]

errors = []

for rel in required:
    path = root / rel
    if not path.is_file():
        errors.append(f'Missing: {rel}')
    elif path.stat().st_size == 0:
        errors.append(f'Empty: {rel}')
    elif path.is_symlink():
        errors.append(f'Unexpected symlink: {rel}')

# Check SKILL.md frontmatter for all skills
skill_dirs = list((root / 'skills').glob('*/SKILL.md'))
for skill_path in skill_dirs:
    text = skill_path.read_text()
    rel = str(skill_path.relative_to(root))
    if not text.startswith('---\n'):
        errors.append(f'{rel}: missing frontmatter')
        continue
    if '\nname:' not in text:
        errors.append(f'{rel}: missing name field')
    if '\ndescription:' not in text:
        errors.append(f'{rel}: missing description field')
    if '\ncompatibility:' not in text:
        errors.append(f'{rel}: missing compatibility field')
    if 'Use when' not in text:
        errors.append(f'{rel}: description should include "Use when"')

# Check authorization.md has tier definitions
auth_text = (root / 'protocols/authorization.md').read_text()
for tier in ['Tier 0', 'Tier 1', 'Tier 2', 'Tier 3']:
    if tier not in auth_text:
        errors.append(f'protocols/authorization.md: missing {tier}')

# Check behavioral-verification has all 7 scenarios
bv_text = (root / 'skills/behavioral-verification/SKILL.md').read_text()
for i in range(1, 8):
    if f'Scenario {i}' not in bv_text:
        errors.append(f'skills/behavioral-verification/SKILL.md: missing Scenario {i}')

# Check README references all skills
readme_text = (root / 'README.md').read_text()
for skill_path in skill_dirs:
    skill_name = skill_path.parent.name
    if skill_name not in readme_text:
        errors.append(f'README.md: skill {skill_name} not referenced')

if errors:
    print('FAIL:')
    for e in errors:
        print(f'  {e}')
    sys.exit(1)
else:
    print(f'PASS: {len(required)} required files, {len(skill_dirs)} skills, all checks passed')
