"""Remove rejected icons from the set: their Python models, published files and review rows.

Used by deploy.py's Discard action, for one icon or a batch. Stdlib only, so the
server never imports the icon registry. The removed source and records are
archived beside the database.
"""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import tempfile

SIBLING_IMPORT = re.compile(r'^\s*from\s+\.(\w+)\s+import\s+\(?([\w\s,]+)\)?', re.MULTILINE)
VARIANT_OF = re.compile(r"variant_of\s*=\s*['\"]([^'\"]+)['\"]")


def remove_class(text: str, class_name: str) -> str:
    """Drop one top-level class (with its decorators and trailing blank lines) by line span."""
    node = next(n for n in ast.parse(text).body if isinstance(n, ast.ClassDef) and n.name == class_name)
    lines = text.splitlines(keepends=True)
    start = min([node.lineno] + [d.lineno for d in node.decorator_list]) - 1
    end = node.end_lineno
    while end < len(lines) and not lines[end].strip():
        end += 1
    return ''.join(lines[:start] + lines[end:])


def _icon_classes(text: str) -> list[str]:
    return [node.name for node in ast.parse(text).body if isinstance(node, ast.ClassDef) and any(
        isinstance(statement, (ast.Assign, ast.AnnAssign)) and any(
            isinstance(target, ast.Name) and target.id == 'icon_id'
            for target in (statement.targets if isinstance(statement, ast.Assign) else [statement.target]))
        for statement in node.body)]


def _write_atomic(path: Path, text: str) -> None:
    handle, temporary = tempfile.mkstemp(dir=path.parent, prefix='.' + path.name)
    with os.fdopen(handle, 'w', encoding='utf-8') as file:
        file.write(text)
    os.replace(temporary, path)


class _FamilyIndex:
    """Who imports which sibling class and who is a variant of what, read once per family folder."""

    def __init__(self, folder: Path):
        self.imports: dict[tuple[str, str], list[str]] = {}
        self.variants: dict[str, list[str]] = {}
        for path in folder.glob('*.py'):
            text = path.read_text(encoding='utf-8')
            for module, names in SIBLING_IMPORT.findall(text):
                for name in re.split(r'[\s,]+', names.strip()):
                    if name:
                        self.imports.setdefault((module, name), []).append(path.name)
            for parent in VARIANT_OF.findall(text):
                self.variants.setdefault(parent, []).append(path.name)


def plan_source_removal(source_root: Path, icon: dict, indexes: dict | None = None, *, detach_variants: bool = False) -> dict:
    """Check the model can be removed without breaking another icon; raise ValueError if not.

    With detach_variants, variants of the icon are allowed: discard_many re-points them first.
    """
    source_root = Path(source_root).resolve()
    indexes = {} if indexes is None else indexes
    source = icon.get('python_source') or {}
    family, icon_id, class_name = icon['family'], icon['icon_id'], source.get('class_name')
    folder = (source_root / 'icon_set' / 'model' / 'icons' / family).resolve()
    path = (source_root / str(source.get('path', ''))).resolve()
    if not class_name or path.suffix != '.py' or path.parent != folder or not path.is_file():
        raise ValueError('The Python model for this icon is not available on this server.')
    text = path.read_text(encoding='utf-8')
    if class_name not in _icon_classes(text):
        raise ValueError(f'{path.name} no longer defines {class_name}. Rebuild before discarding.')
    exceptions = source_root / 'icon_set' / 'model' / 'contracts' / 'exceptions.v1.json'
    if exceptions.is_file() and f'"{icon_id}"' in exceptions.read_text(encoding='utf-8'):
        raise ValueError(f'{icon_id} has an approved keyshape exception; remove it from exceptions.v1.json first.')
    if folder not in indexes:
        indexes[folder] = _FamilyIndex(folder)
    index = indexes[folder]
    children = [name for name in index.variants.get(icon_id, []) if name != path.name]
    if children and not detach_variants:
        raise ValueError(f'{children[0]} is a variant of {icon_id}; discard or detach it first.')
    importers = [name for name in index.imports.get((path.stem, class_name), []) if name != path.name]
    if importers:
        raise ValueError(f'{importers[0]} imports {class_name}; update it before discarding.')
    parent = VARIANT_OF.search(text)
    return {'path': path, 'text': text, 'class_name': class_name, 'children': [folder / name for name in children],
            'parent': parent[1] if parent else None}


def detach_variant(path: Path, icon_id: str, parent: str | None) -> None:
    """Point a variant of a discarded icon at that icon's own parent, or make it standalone."""
    text = path.read_text(encoding='utf-8')
    line = re.compile(r"^([ \t]*)variant_of\s*=\s*['\"]" + re.escape(icon_id) + r"['\"][ \t]*\n", re.MULTILINE)
    _write_atomic(path, line.sub((lambda m: f"{m[1]}variant_of = '{parent}'\n") if parent else '', text))


def discard_many(icons: list[dict], *, source_root: Path, dist: Path, archive: Path, connection, user: str,
                 detach_variants: bool = False) -> dict:
    """Discard every icon that passes its checks; the rest are reported, not touched (caller commits).

    The large catalog and manifest files are rewritten once for the whole batch.
    """
    source_root = Path(source_root).resolve()
    indexes: dict = {}
    plans, failed = [], []
    for icon in icons:
        try:
            plans.append((icon, plan_source_removal(source_root, icon, indexes, detach_variants=detach_variants)))
        except (ValueError, SyntaxError) as error:
            failed.append({'icon': icon['key'], 'name': icon.get('name', icon['icon_id']), 'error': str(error)})
    if not plans:
        return {'discarded': [], 'failed': failed}

    now = datetime.now(timezone.utc)
    archive.mkdir(parents=True, exist_ok=True)
    current: dict[Path, str] = {}
    discarded, removed_ids, removed_keys = [], {}, set()
    for icon, plan in plans:
        key, icon_id, path = icon['key'], icon['icon_id'], plan['path']
        folder = {'solo': 'solo48', 'sub': 'sub32', 'symbol': 'symbol32', 'container': 'container64'}[icon['family']]
        text = current.get(path, plan['text'])
        stem = f"{now.strftime('%Y%m%dT%H%M%SZ')}-{icon['family']}-{icon_id}"
        feedback = [dict(zip(('id', 'feedback', 'svg_sha256', 'created_at', 'author'), row)) for row in connection.execute(
            'SELECT id, feedback, svg_sha256, created_at, author FROM feedback WHERE icon=?', (key,))]
        # A module holding other icons loses only this class; earlier removals in the batch are kept.
        shared = len(_icon_classes(text)) > 1
        (archive / f'{stem}.py').write_text(text, encoding='utf-8')
        (archive / f'{stem}.json').write_text(json.dumps({
            'discarded_by': user, 'discarded_at': now.isoformat(), 'source_path': str(path.relative_to(source_root)),
            'shared_module': shared, 'record': icon, 'feedback': feedback}, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8')
        discarding = {p['path'] for _, p in plans}
        for child in plan.get('children', []):
            if child not in discarding:
                detach_variant(child, icon_id, plan['parent'])
        if shared:
            current[path] = remove_class(text, plan['class_name'])
            _write_atomic(path, current[path])
        else:
            path.unlink()
        for artifact in (dist / folder / f'{icon_id}.svg',
                         dist / 'failed' / folder / f'{icon_id}.svg',
                         source_root / 'published' / 'previews-png' / folder / f'{icon_id}.png'):
            artifact.unlink(missing_ok=True)
        removed_ids.setdefault(folder, set()).add(icon_id)
        removed_keys.add(key)
        rows = {table: connection.execute(f'DELETE FROM {table} WHERE icon=?', (key,)).rowcount
                for table in ('reviews', 'icon_flags', 'icon_types', 'feedback')}
        discarded.append({'icon': key, 'name': icon.get('name', icon_id), 'source': str(path.relative_to(source_root)),
                          'shared_module': shared, 'archive': f'{stem}.py', 'removed_rows': rows})

    targets = [(dist / folder / 'manifest.json', 'icon_id', ids) for folder, ids in removed_ids.items()]
    targets += [(dist / 'failed' / folder / 'manifest.json', 'icon_id', ids) for folder, ids in removed_ids.items()]
    targets.append((dist / 'gallery' / 'icons.json', 'key', removed_keys))
    for path, field, values in targets:
        if path.is_file():
            data = json.loads(path.read_text(encoding='utf-8'))
            if 'failed_icons' in data:
                data['failed_icons'] = [row for row in data['failed_icons'] if row.get(field) not in values]
                _write_atomic(path, json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n')
            kept = [row for row in data['icons'] if row.get(field) not in values]
            if len(kept) != len(data['icons']):
                data['icons'] = kept
                if 'count' in data:
                    data['count'] = len(kept)
                _write_atomic(path, json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n')
    if discarded:
        from icon_set.scripts.gallery import stage_failures
        catalog = json.loads((dist / 'gallery' / 'icons.json').read_text())
        stage_failures(dist, dist, ['solo48', 'sub32', 'container64'], dist / 'gallery', passed=len(catalog['icons']))
    return {'discarded': discarded, 'failed': failed}
