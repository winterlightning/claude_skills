#!/usr/bin/env python3
"""Give Uncategorized icons stored in a gallery database their catalog category.

python3 icon_set/scripts/fix_uncategorized_artwork.py                     # dry run on the local database
python3 icon_set/scripts/fix_uncategorized_artwork.py --apply
python3 icon_set/scripts/fix_uncategorized_artwork.py --apply \\
    --database /srv/pictographic/state/feedback.sqlite3 --gallery <active release>/gallery   # production

Two kinds of record live in the database rather than icons.json, so a rebuilt catalog
cannot recategorize them:

* accepted gallery edits (icon_artwork): the server overlays the saved edited_graph on
  the icon, including the category it had when it was edited. The category becomes the
  one icons.json now gives the icon. validation / validation_override graph_sha256 are
  recomputed so the edit stays accepted; the geometry is untouched.
* uploaded icons (uploaded_icons): the category of the primitive whose uuid appears in
  the icon id, else of the primitive with the same concept name (the most common one
  when several share it).

Only records whose category is Uncategorized in the requested families are changed.
--apply writes a backup next to the database first.
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path
import re
import sqlite3
import sys
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.stroke_edits import effective_validation_status, graph_sha256  # noqa: E402
from icon_set.scripts.workspace import DEFAULT_DIST  # noqa: E402

UNCATEGORIZED = 'Uncategorized'
DEFAULT_DATABASE = REPO_ROOT / 'icon_set' / 'state' / 'feedback.sqlite3'
_UUID = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')


def load_gallery(gallery: Path) -> tuple[dict, dict, dict]:
    """icon key -> build category; primitive uuid -> category; concept name -> Counter of categories."""
    icons = json.loads((gallery / 'icons.json').read_text(encoding='utf-8'))
    built = {r['key']: r.get('category') for r in icons.get('icons', []) + icons.get('failed_icons', [])}
    primitives = json.loads((gallery / 'primitives.json').read_text(encoding='utf-8'))
    by_uuid, by_name = {}, collections.defaultdict(collections.Counter)
    for row in primitives['rows']:
        for uid in [row.get('uuid')] + [alias['uuid'] for alias in row.get('aliases', [])]:
            if uid:
                by_uuid[uid] = row['category']
        by_name[row['concept'].lower()][row['category']] += 1
    return built, by_uuid, by_name


def upload_category(record: dict, by_uuid: dict, by_name: dict) -> str | None:
    for uid in _UUID.findall(f"{record.get('icon_id', '')} {record.get('name', '')}"):
        if by_uuid.get(uid, UNCATEGORIZED) != UNCATEGORIZED:
            return by_uuid[uid]
    names = by_name.get(str(record.get('name', '')).lower())
    for category, _ in (names or collections.Counter()).most_common():
        if category != UNCATEGORIZED:
            return category
    return None


def recategorize_edit(document: dict, category: str) -> None:
    """Change edited_graph.category and keep the edit's acceptance exactly as it was."""
    edit = document['edited']
    before, old = effective_validation_status(edit), graph_sha256(edit['edited_graph'])
    edit['edited_graph']['category'] = category
    digest = graph_sha256(edit['edited_graph'])
    for field in ('validation', 'validation_override'):
        if (edit.get(field) or {}).get('graph_sha256') == old:
            edit[field]['graph_sha256'] = digest
    if effective_validation_status(edit) != before:
        raise ValueError(f"{document.get('icon')}: acceptance changed from {before}")


def plan(connection, built: dict, by_uuid: dict, by_name: dict, families: set[str]) -> list[dict]:
    changes = []
    for icon, text in connection.execute(
            "SELECT icon, document FROM icon_artwork WHERE json_extract(document, '$.edited.edited_graph.category') = ?",
            (UNCATEGORIZED,)).fetchall():
        family = icon.split('/', 1)[0]
        category = built.get(icon)
        if family in families:
            changes.append(dict(kind='edit', key=icon, table='icon_artwork', id=icon, text=text,
                                category=category if category and category != UNCATEGORIZED else None))
    for rowid, text in connection.execute(
            "SELECT rowid, record FROM uploaded_icons WHERE json_extract(record, '$.category') = ?",
            (UNCATEGORIZED,)).fetchall():
        record = json.loads(text)
        if record.get('family') in families:
            changes.append(dict(kind='upload', key=record.get('key') or record.get('icon_id'), table='uploaded_icons',
                                id=rowid, text=text, category=upload_category(record, by_uuid, by_name)))
    return changes


def apply(connection, changes: list[dict]) -> int:
    applied = 0
    with connection:
        for change in changes:
            if not change['category']:
                continue
            data = json.loads(change['text'])
            if change['kind'] == 'edit':
                recategorize_edit(data, change['category'])
                connection.execute('UPDATE icon_artwork SET document = ? WHERE icon = ?', (json.dumps(data), change['id']))
            else:
                data['category'] = change['category']
                connection.execute('UPDATE uploaded_icons SET record = ? WHERE rowid = ?', (json.dumps(data), change['id']))
            applied += 1
    return applied


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--database', type=Path, default=DEFAULT_DATABASE)
    parser.add_argument('--gallery', type=Path, default=DEFAULT_DIST / 'gallery',
                        help='the built gallery this database is served with (icons.json + primitives.json)')
    parser.add_argument('--family', action='append', dest='families', help='family to fix (repeatable; default solo)')
    parser.add_argument('--apply', action='store_true', help='write the changes (default: dry run)')
    args = parser.parse_args(argv)
    families = set(args.families or ['solo'])
    if not args.database.is_file():
        parser.exit(1, f'error: database not found: {args.database}\n')
    built, by_uuid, by_name = load_gallery(args.gallery)
    connection = sqlite3.connect(args.database, timeout=30)
    try:
        changes = plan(connection, built, by_uuid, by_name, families)
        for change in changes:
            print(f"{change['kind']:6} {change['key']} -> {change['category'] or 'SKIP (no category found)'}")
        counts = collections.Counter((c['kind'], bool(c['category'])) for c in changes)
        print(f"{counts[('edit', True)]} edits, {counts[('upload', True)]} uploads to fix; "
              f"{counts[('edit', False)] + counts[('upload', False)]} without a category")
        if not args.apply:
            print('dry run; pass --apply to write')
            return 0
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        backup = args.database.with_name(f'{args.database.stem}.before-categories-{stamp}{args.database.suffix}')
        with sqlite3.connect(backup) as target:
            connection.backup(target)
        print(f'backup -> {backup}')
        print(f'{apply(connection, changes)} records updated in {args.database}')
    finally:
        connection.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
