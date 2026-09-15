#!/usr/bin/env python3
"""Keep only the latest version of every icon: the highest -vN replaces its base ID.

python3 icon_set/scripts/consolidate_variants.py            # dry run, prints the plan
python3 icon_set/scripts/consolidate_variants.py --apply    # back up, rewrite sources, migrate the feedback DB
Then rebuild: python3 icon_set/scripts/build.py

Older versions' modules are deleted (a shared module loses only that class). The
latest module drops variant_of/variant_label, takes the base icon_id and class
name, and loses its _vN filename token. Review rows move to the base key with the
renamed SVG's hash, so a latest version keeps its own status; rows for deleted
versions are removed.
"""
from __future__ import annotations

import argparse
import ast
from contextlib import closing
from datetime import date
import hashlib
import inspect
import json
from pathlib import Path
import re
import sqlite3
import sys
import tarfile

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from icon_set.model.icons.registry import factories  # noqa: E402
from icon_set.scripts.discard_icon import remove_class  # noqa: E402

PACKAGE_ROOT = REPO_ROOT / 'icon_set'
DEFAULT_DB = PACKAGE_ROOT / 'data' / 'feedback.sqlite3'
EXCEPTIONS = PACKAGE_ROOT / 'model' / 'contracts' / 'exceptions.v1.json'
VERSION = re.compile(r'^(?P<base>.+)-v(?P<number>\d+)$')
HEADER = re.compile(r'^# Variant of [^\n]*; parent file remains unchanged\.\n')


def version_number(factory) -> int:
    match = VERSION.match(factory.icon_id)
    return int(match['number']) if match else 1


def plan_groups(registered: dict) -> tuple[list[dict], list[str]]:
    """Group every version under its root; the highest -vN is the one kept."""
    groups: dict[str, list] = {}
    for icon_id, factory in registered.items():
        root = factory
        while getattr(root, 'variant_of', None):
            root = registered[root.variant_of]
        groups.setdefault(root.icon_id, []).append(factory)
    # A -vN ID without variant_of still supersedes its registered base.
    for icon_id, factory in registered.items():
        match = VERSION.match(icon_id)
        if match and not getattr(factory, 'variant_of', None) and match['base'] in groups \
                and factory not in groups[match['base']]:
            groups[match['base']].extend(groups.pop(icon_id, [factory]))
    blockers, plan = [], []
    for root_id, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        members.sort(key=version_number)
        latest, olds = members[-1], members[:-1]
        root = registered[root_id]
        match = VERSION.match(latest.icon_id)
        if VERSION.match(root_id) or not match or match['base'] != root_id:
            blockers.append(f'{root_id}: latest {latest.icon_id} is not named {root_id}-vN')
            continue
        if version_number(members[-2]) == version_number(latest):
            blockers.append(f'{root_id}: tie for latest version')
            continue
        if any(f.family != root.family for f in members):
            blockers.append(f'{root_id}: versions span families')
            continue
        source = Path(inspect.getsourcefile(latest)).resolve()
        token = f"_v{match['number']}"
        stem = re.sub(rf'{token}(?=_|$)', '', source.stem, count=1)
        if stem == source.stem:
            blockers.append(f'{root_id}: cannot find {token} in {source.name}')
            continue
        plan.append({
            'root': root_id, 'family': root.family, 'latest': latest.icon_id,
            'latest_class': latest.__name__, 'root_class': root.__name__,
            'latest_file': str(source), 'target_file': str(source.with_name(stem + '.py')),
            'olds': [{'icon_id': f.icon_id, 'class': f.__name__, 'file': str(Path(inspect.getsourcefile(f)).resolve())}
                     for f in olds],
        })
    return plan, blockers


def check_plan(plan: list[dict], registered: dict) -> list[str]:
    blockers = []
    modules: dict[str, int] = {}
    for factory in registered.values():
        path = str(Path(inspect.getsourcefile(factory)).resolve())
        modules[path] = modules.get(path, 0) + 1
    deleted_files = {old['file'] for group in plan for old in group['olds'] if modules[old['file']] == 1}
    kept_files = {str(Path(inspect.getsourcefile(f)).resolve()) for f in registered.values()} - deleted_files
    targets = set()
    for group in plan:
        target = group['target_file']
        if target in targets or (Path(target).exists() and target not in deleted_files):
            blockers.append(f"{group['root']}: {Path(target).name} already exists")
        targets.add(target)
    # A kept module must not import a class that disappears or is renamed.
    removed = {(Path(old['file']).parent, old['class']) for group in plan for old in group['olds']}
    removed |= {(Path(group['latest_file']).parent, group['latest_class']) for group in plan}
    for path in kept_files:
        for node in ast.walk(ast.parse(Path(path).read_text(encoding='utf-8'))):
            if isinstance(node, ast.ImportFrom) and node.level == 1:
                for alias in node.names:
                    if (Path(path).parent, alias.name) in removed:
                        blockers.append(f'{Path(path).name} imports {alias.name}, which is removed')
    exceptions = EXCEPTIONS.read_text(encoding='utf-8')
    for group in plan:
        for icon_id in [group['root'], group['latest'], *(old['icon_id'] for old in group['olds'])]:
            if f'"{icon_id}"' in exceptions:
                blockers.append(f'{icon_id} has an exceptions.v1.json entry')
    for group in plan:
        group['shared_olds'] = [old['icon_id'] for old in group['olds'] if modules[old['file']] > 1]
    return blockers


def svg_hashes(plan: list[dict], registered: dict) -> None:
    """Old and renamed SVG hashes of each latest version; only <title> carries the ID."""
    for group in plan:
        try:
            document = registered[group['latest']]().to_svg()
        except Exception as error:  # a broken model still renames; its reviews keep their hash
            group['old_sha'] = group['new_sha'] = None
            group['svg_error'] = str(error)
            continue
        title = f"<title>{group['latest']}</title>"
        if document.count(title) != 1:
            raise ValueError(f"{group['latest']}: expected one {title} in the SVG")
        group['old_sha'] = hashlib.sha256(document.encode('utf-8')).hexdigest()
        renamed = document.replace(title, f"<title>{group['root']}</title>")
        group['new_sha'] = hashlib.sha256(renamed.encode('utf-8')).hexdigest()


def rewrite_latest(text: str, group: dict) -> str:
    node = next(n for n in ast.parse(text).body if isinstance(n, ast.ClassDef) and n.name == group['latest_class'])
    lines = text.splitlines(keepends=True)
    drop = set()
    found_id = False
    for statement in node.body:
        targets = statement.targets if isinstance(statement, ast.Assign) else \
            [statement.target] if isinstance(statement, ast.AnnAssign) else []
        names = {t.id for t in targets if isinstance(t, ast.Name)}
        if names & {'variant_of', 'variant_label'}:
            drop.update(range(statement.lineno - 1, statement.end_lineno))
        elif 'icon_id' in names:
            span = range(statement.lineno - 1, statement.end_lineno)
            chunk = ''.join(lines[i] for i in span)
            new = re.sub(rf"(['\"]){re.escape(group['latest'])}\1", rf"\g<1>{group['root']}\g<1>", chunk, count=1)
            if new == chunk:
                raise ValueError(f"{group['latest']}: icon_id literal not found")
            lines[span.start] = new
            drop.update(span[1:])
            found_id = True
    if not found_id:
        raise ValueError(f"{group['latest']}: icon_id assignment not found")
    text = ''.join(line for i, line in enumerate(lines) if i not in drop)
    text = HEADER.sub('', text, count=1)
    return re.sub(rf"\b{re.escape(group['latest_class'])}\b", group['root_class'], text)


def backup(plan: list[dict], database: Path, directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    files = {group['latest_file'] for group in plan} | {old['file'] for group in plan for old in group['olds']}
    with tarfile.open(directory / 'sources.tar.gz', 'w:gz') as archive:
        for path in sorted(files):
            archive.add(path, arcname=str(Path(path).relative_to(REPO_ROOT)))
    if database.exists():
        with closing(sqlite3.connect(database)) as source, closing(sqlite3.connect(directory / database.name)) as copy:
            source.backup(copy)
    (directory / 'plan.json').write_text(json.dumps(plan, indent=1) + '\n', encoding='utf-8')


def apply_sources(plan: list[dict]) -> None:
    shared: dict[str, list[str]] = {}
    for group in plan:
        for old in group['olds']:
            if old['icon_id'] in group['shared_olds']:
                shared.setdefault(old['file'], []).append(old['class'])
            else:
                Path(old['file']).unlink()
    for path, classes in shared.items():
        text = Path(path).read_text(encoding='utf-8')
        for name in classes:
            text = remove_class(text, name)
        Path(path).write_text(text, encoding='utf-8')
    for group in plan:
        source, target = Path(group['latest_file']), Path(group['target_file'])
        text = rewrite_latest(source.read_text(encoding='utf-8'), group)
        compile(text, str(target), 'exec')
        target.write_text(text, encoding='utf-8')
        if source != target:
            source.unlink()


def migrate_database(plan: list[dict], database: Path) -> dict:
    counts = {}
    with closing(sqlite3.connect(database, timeout=30)) as connection, connection:
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        for group in plan:
            family = group['family']
            root = f"{family}/{group['root']}"
            latest = f"{family}/{group['latest']}"
            olds = [f"{family}/{old['icon_id']}" for old in group['olds']]
            gone = [key for key in olds]  # includes the root key: its drawing is deleted
            for table in ('reviews', 'icon_flags'):
                if table in tables:
                    removed = connection.execute(
                        f"DELETE FROM {table} WHERE icon IN ({','.join('?' * len(gone))})", gone).rowcount
                    counts[f'{table} removed'] = counts.get(f'{table} removed', 0) + removed
            if 'reviews' in tables:
                if group.get('old_sha'):
                    connection.execute('UPDATE reviews SET svg_sha256=? WHERE icon=? AND svg_sha256=?',
                                       (group['new_sha'], latest, group['old_sha']))
                moved = connection.execute('UPDATE reviews SET icon=? WHERE icon=?', (root, latest)).rowcount
                counts['reviews moved'] = counts.get('reviews moved', 0) + moved
            if 'icon_flags' in tables:
                counts['icon_flags moved'] = counts.get('icon_flags moved', 0) + connection.execute(
                    'UPDATE icon_flags SET icon=? WHERE icon=?', (root, latest)).rowcount
            # Feedback and split history stay with the subject under its base key.
            for table, column in (('feedback', 'icon'), ('split_requests', 'icon'), ('pending_briefs', 'generated_icon')):
                if table in tables:
                    keys = [latest, *olds]
                    counts[f'{table} re-keyed'] = counts.get(f'{table} re-keyed', 0) + connection.execute(
                        f"UPDATE {table} SET {column}=? WHERE {column} IN ({','.join('?' * len(keys))})",
                        [root, *keys]).rowcount
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--apply', action='store_true', help='rewrite sources and migrate the database')
    parser.add_argument('--database', type=Path, default=DEFAULT_DB)
    parser.add_argument('--plan-out', type=Path, help='write the planned changes as JSON')
    parser.add_argument('--backup-dir', type=Path,
                        default=PACKAGE_ROOT / 'data' / f'variant-consolidation-{date.today().isoformat()}')
    args = parser.parse_args(argv)

    registered = factories()
    plan, blockers = plan_groups(registered)
    blockers += check_plan(plan, registered)
    svg_hashes(plan, registered)
    deleted = sum(len(group['olds']) for group in plan)
    print(f'{len(registered)} icons · {len(plan)} version groups · {deleted} older versions to delete · '
          f'{len(plan)} latest versions to rename · {len(registered) - deleted} icons after')
    if args.plan_out:
        args.plan_out.write_text(json.dumps(plan, indent=1) + '\n', encoding='utf-8')
    if blockers:
        print('Blocked:\n  ' + '\n  '.join(blockers))
        return 1
    if not args.apply:
        print('Dry run: nothing changed. Re-run with --apply.')
        return 0
    backup(plan, args.database, args.backup_dir)
    apply_sources(plan)
    counts = migrate_database(plan, args.database) if args.database.exists() else {}
    print(f'Backup: {args.backup_dir}')
    for name, value in counts.items():
        print(f'  {name}: {value}')
    print('Now rebuild: python3 icon_set/scripts/build.py')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
