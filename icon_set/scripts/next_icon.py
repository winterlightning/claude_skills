#!/usr/bin/env python3
"""Write one TODO solo reference as a short text input, without the gallery server.

Reads the tracked catalog (published/gallery/primitives.json) and, when present,
a local copy of the review database (icon_set/state/feedback.sqlite3) read-only,
using the same functions the server calls. Standalone Ray attempts with a saved
result are also excluded, regardless of validation, without changing the catalog
or review database.

    python3 icon_set/scripts/next_icon.py                                 # print the first TODO
    python3 icon_set/scripts/next_icon.py --offset 1 --out primitive-input-2.txt
    python3 icon_set/scripts/next_icon.py --uuid <uuid>
"""
import argparse
from contextlib import closing
import json
from pathlib import Path
import re
import sqlite3
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
from icon_set.scripts.workspace import DEFAULT_DIST, DEFAULT_DATABASE, primitive_results_dir  # noqa: E402
from icon_set.scripts.primitive_status import load_status, merge, filter_rows  # noqa: E402
from icon_set.scripts.primitive_briefs import load_primitive_briefs  # noqa: E402
from icon_set.scripts.primitives_catalog import primitives_root  # noqa: E402

ICONS = REPO_ROOT / 'icon_set' / 'model' / 'icons'
UUID_IN_NAME = re.compile(r'[0-9a-f]{8}(?:_[0-9a-f]{4}){3}_[0-9a-f]{12}')


def load_decisions(database):
    """SKIP decisions and saved briefs from a read-only database; empty when absent."""
    if not database.is_file():
        return {}, {}, False
    with closing(sqlite3.connect(database.resolve().as_uri() + '?mode=ro', uri=True, timeout=10)) as connection:
        return load_status(connection), load_primitive_briefs(connection), True


def originals_by_source():
    """Source UUID -> Python originals carrying it (the catalog can lag the source tree)."""
    found = {}
    for path in ICONS.glob('*/*.py'):
        for match in UUID_IN_NAME.findall(path.name):
            found.setdefault(match.replace('_', '-'), []).append(str(path.relative_to(REPO_ROOT)))
    return found


def completed_result_sources(root=None):
    """Skip recorded attempts, including failures; unfinished attempts may retry."""
    root = Path(root) if root is not None else primitive_results_dir()
    completed = set()
    for path in root.glob('*/*/result.json'):
        try:
            result = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(result, dict):
                continue
            uid = result.get('source_uuid')
            if not isinstance(uid, str) or uid != path.parent.parent.name:
                continue
            if not any(p.is_file() for p in path.parent.glob('*.py')):
                continue
            completed.add(uid)
        except (OSError, ValueError):
            continue
    return completed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--offset', type=int, default=0, help='skip this many TODO items')
    parser.add_argument('--uuid', help='use this reference instead of the next TODO')
    parser.add_argument('--category')
    parser.add_argument('--database', type=Path, default=DEFAULT_DATABASE)
    parser.add_argument('--out', type=Path, help='write the text here instead of printing it')
    args = parser.parse_args(argv)
    if args.offset < 0:
        parser.error('--offset must be nonnegative')

    catalog = json.loads((DEFAULT_DIST / 'gallery' / 'primitives.json').read_text(encoding='utf-8'))
    statuses, briefs, has_database = load_decisions(args.database)
    if not has_database:
        print(f'warning: no database at {args.database}; SKIP decisions and saved briefs not applied', file=sys.stderr)
    merged = merge(catalog['rows'], statuses)
    originals = originals_by_source()
    completed = completed_result_sources()
    if args.uuid:
        rows = [r for r in merged if r['uuid'] == args.uuid.lower()]
        if not rows:
            sys.exit(f'error: unknown uuid {args.uuid}')
        if rows[0]['uuid'] in completed:
            sys.exit(f'error: {args.uuid} already has a saved standalone attempt and result')
        if rows[0]['status'] != 'todo' or rows[0]['uuid'] in originals:
            sys.exit(f"error: {args.uuid} is {rows[0]['status']}, not TODO")
        row = rows[0]
    else:
        rows = [r for r in sorted(filter_rows(merged, args.category, 'todo'), key=lambda r: (r['path'], r['uuid']))
                if r['uuid'] not in originals and r['uuid'] not in completed]
        if args.offset >= len(rows):
            sys.exit(f'error: only {len(rows)} TODO references')
        row = rows[args.offset]

    reference = primitives_root() / row['path']
    if not reference.is_file():
        sys.exit(f'error: reference SVG missing: {reference}')
    lines = [f"concept: {row.get('concept') or row.get('old_concept')}",
             f"source UUID: {row['uuid']}",
             f"reference: {reference.relative_to(REPO_ROOT) if reference.is_relative_to(REPO_ROOT) else reference}",
             f"category: {row['category']}"]
    saved = briefs.get(row['uuid'])
    if saved:
        lines.append(f"brief:\n{saved['brief']}")
    text = '\n'.join(lines) + '\n'
    if args.out:
        args.out.write_text(text, encoding='utf-8')
        print(f'wrote {args.out}')
    else:
        print(text, end='')
    return 0


if __name__ == '__main__':
    sys.exit(main())
