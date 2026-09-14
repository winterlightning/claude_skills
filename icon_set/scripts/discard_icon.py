"""Remove a rejected icon from the set: its Python model, published files and review rows.

Used by deploy.py's Discard action. Stdlib only, so the server never imports the
icon registry. The removed source and records are archived beside the database.
"""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import tempfile


def remove_class(text: str, class_name: str) -> str:
    """Drop one top-level class (with its decorators and trailing blank lines) by line span."""
    node = next(n for n in ast.parse(text).body if isinstance(n, ast.ClassDef) and n.name == class_name)
    lines = text.splitlines(keepends=True)
    start = min([node.lineno] + [d.lineno for d in node.decorator_list]) - 1
    end = node.end_lineno
    while end < len(lines) and not lines[end].strip():
        end += 1
    return ''.join(lines[:start] + lines[end:])


def _icon_classes(tree: ast.Module) -> list[str]:
    return [node.name for node in tree.body if isinstance(node, ast.ClassDef) and any(
        isinstance(statement, (ast.Assign, ast.AnnAssign)) and any(
            isinstance(target, ast.Name) and target.id == 'icon_id'
            for target in (statement.targets if isinstance(statement, ast.Assign) else [statement.target]))
        for statement in node.body)]


def _write_atomic(path: Path, text: str) -> None:
    handle, temporary = tempfile.mkstemp(dir=path.parent, prefix='.' + path.name)
    with os.fdopen(handle, 'w', encoding='utf-8') as file:
        file.write(text)
    os.replace(temporary, path)


def plan_source_removal(source_root: Path, icon: dict) -> dict:
    """Check the model can be removed without breaking another icon; raise ValueError if not."""
    source_root = Path(source_root).resolve()
    source = icon.get('python_source') or {}
    family, icon_id, class_name = icon['family'], icon['icon_id'], source.get('class_name')
    folder = (source_root / 'icon_set' / 'model' / 'icons' / family).resolve()
    path = (source_root / str(source.get('path', ''))).resolve()
    if not class_name or path.suffix != '.py' or path.parent != folder or not path.is_file():
        raise ValueError('The Python model for this icon is not available on this server.')
    text = path.read_text(encoding='utf-8')
    tree = ast.parse(text)
    classes = _icon_classes(tree)
    if class_name not in classes:
        raise ValueError(f'{path.name} no longer defines {class_name}. Rebuild before discarding.')
    exceptions = source_root / 'icon_set' / 'model' / 'contracts' / 'exceptions.v1.json'
    if exceptions.is_file() and f'"{icon_id}"' in exceptions.read_text(encoding='utf-8'):
        raise ValueError(f'{icon_id} has an approved keyshape exception; remove it from exceptions.v1.json first.')
    variant = re.compile(rf"variant_of\s*=\s*['\"]{re.escape(icon_id)}['\"]")
    for other in folder.glob('*.py'):
        if other == path:
            continue
        content = other.read_text(encoding='utf-8')
        if variant.search(content):
            raise ValueError(f'{other.name} is a variant of {icon_id}; discard or detach it first.')
        if class_name in content:
            for node in ast.walk(ast.parse(content)):
                if isinstance(node, ast.ImportFrom) and node.level == 1 and node.module == path.stem \
                        and any(alias.name == class_name for alias in node.names):
                    raise ValueError(f'{other.name} imports {class_name}; update it before discarding.')
    shared = len(classes) > 1
    return {'path': path, 'text': text, 'shared': shared, 'class_name': class_name,
            'removed': remove_class(text, class_name) if shared else None}


def discard(icon: dict, *, source_root: Path, dist: Path, archive: Path, connection, user: str) -> dict:
    """Delete the model and published artifacts, then the icon's review rows (caller commits)."""
    source_root = Path(source_root).resolve()
    plan = plan_source_removal(source_root, icon)
    key, icon_id = icon['key'], icon['icon_id']
    folder = icon['preview_url'].split('/')[1]
    now = datetime.now(timezone.utc)
    archive.mkdir(parents=True, exist_ok=True)
    stem = f"{now.strftime('%Y%m%dT%H%M%SZ')}-{icon['family']}-{icon_id}"
    feedback = [dict(zip(('id', 'feedback', 'svg_sha256', 'created_at', 'author'), row)) for row in connection.execute(
        'SELECT id, feedback, svg_sha256, created_at, author FROM feedback WHERE icon=?', (key,))]
    (archive / f'{stem}.py').write_text(plan['text'], encoding='utf-8')
    (archive / f'{stem}.json').write_text(json.dumps({
        'discarded_by': user, 'discarded_at': now.isoformat(), 'source_path': str(plan['path'].relative_to(source_root)),
        'shared_module': plan['shared'], 'record': icon, 'feedback': feedback}, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8')

    if plan['shared']:
        _write_atomic(plan['path'], plan['removed'])
    else:
        plan['path'].unlink()
    for path in (dist / folder / f'{icon_id}.svg', source_root / 'icon_set' / 'assets' / 'previews-png' / folder / f'{icon_id}.png'):
        path.unlink(missing_ok=True)
    for path, field in ((dist / folder / 'manifest.json', 'icon_id'), (dist / 'gallery' / 'icons.json', 'key')):
        if path.is_file():
            data = json.loads(path.read_text(encoding='utf-8'))
            kept = [row for row in data['icons'] if row.get(field) != (icon_id if field == 'icon_id' else key)]
            if len(kept) != len(data['icons']):
                data['icons'] = kept
                if 'count' in data:
                    data['count'] = len(kept)
                _write_atomic(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')

    removed = {table: connection.execute(f'DELETE FROM {table} WHERE icon=?', (key,)).rowcount
               for table in ('reviews', 'icon_flags', 'feedback')}
    return {'discarded': key, 'source': str(plan['path'].relative_to(source_root)),
            'shared_module': plan['shared'], 'archive': f'{stem}.py', 'removed_rows': removed}
