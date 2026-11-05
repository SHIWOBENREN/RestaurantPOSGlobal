#!/usr/bin/env python3
"""Strict allowlist for the marketing/docs repository (not a source audit)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    '.gitignore', 'README.md', 'README.zh-CN.md', 'CHANGELOG.md',
    'LICENSE_NOTICE.md', 'SECURITY.md', 'SUPPORT.md',
    'docs/FEATURES.md', 'docs/RELEASE_STATUS.md',
    'docs/INSTALL_WINDOWS.md', 'docs/INSTALL_MAC.md',
    'docs/LAN_SECURITY.md', 'docs/DATA_AND_PRIVACY.md', 'docs/FAQ.md',
    'releases/RELEASE_NOTES_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/bug_report.yml',
    '.github/ISSUE_TEMPLATE/config.yml',
    '.github/workflows/public-docs-safety.yml',
    'scripts/audit_public_repo.py',
}
BAD_TEXT_PATTERNS = [
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    r'gh[pousr]_[A-Za-z0-9_]{25,}',
    r'github_pat_[A-Za-z0-9_]{25,}',
    r'AKIA[0-9A-Z]{16}',
    r'(?i)password\s*[:=]\s*["\'][^"\']{6,}["\']',
]

def audit():
    problems=[]
    found=set()
    for p in ROOT.rglob('*'):
        if '.git' in p.relative_to(ROOT).parts:
            continue
        rel=p.relative_to(ROOT).as_posix()
        if p.is_symlink():
            problems.append('Symlink forbidden: '+rel)
            continue
        if not p.is_file():
            continue
        found.add(rel)
        if rel not in ALLOWED:
            problems.append('Unexpected file: '+rel)
            continue
        if p.stat().st_size > 400_000:
            problems.append('File too large: '+rel)
        if rel.endswith(('.md', '.yml', '.yaml')):
            try: txt=p.read_text('utf-8')
            except UnicodeDecodeError:
                problems.append('Non-UTF8 docs: '+rel)
                continue
            for pat in BAD_TEXT_PATTERNS:
                if re.search(pat,txt):
                    problems.append('Potential secret in '+rel+' matched '+pat[:24])
    for missing in sorted(ALLOWED-found):
        problems.append('Expected file absent: '+missing)
    if problems:
        print('PUBLIC SAFETY AUDIT FAILED:')
        for e in problems: print(' - '+e)
        return 1
    print('PASS: public documentation allowlist, no extra files or detected secrets; '+str(len(found))+' files')
    return 0

if __name__=='__main__':
    sys.exit(audit())
