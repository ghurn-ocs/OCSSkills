"""Dependency-free lint for this skill's simple frontmatter and local links.
Not a general YAML parser or a confidentiality certification.
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote


def validate(root):
    root = Path(root).resolve()
    entry = root / 'SKILL.md'
    if not entry.is_file():
        return ['missing SKILL.md']
    errors = []
    content = entry.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
    if not match:
        errors.append('missing YAML frontmatter')
    else:
        fields = dict(re.findall(r'^([a-z-]+):\s*(.*)$', match[1], re.M))
        name = fields.get('name', '')
        if name != root.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append('invalid or mismatched name')
        if not 1 <= len(fields.get('description', '')) <= 1024:
            errors.append('invalid description')
    for path in root.rglob('*'):
        if path.is_symlink():
            errors.append(f'symlink forbidden: {path.relative_to(root)}')
            continue
        if path.suffix != '.md' or not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[a-z]+:', target) or target.startswith('#'):
                continue
            resolved = (path.parent / unquote(target.split('#')[0])).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f'broken link: {path.relative_to(root)} -> {target}')
    return errors


if __name__ == '__main__':
    findings = validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
    print('\n'.join(findings) if findings else 'PASS: metadata, local links, and symlinks')
    sys.exit(bool(findings))
