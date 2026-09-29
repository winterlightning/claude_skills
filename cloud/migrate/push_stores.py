#!/usr/bin/env python3
"""Copy the stores kept beside a feedback database into the cloud (read-only on the source).

    python3 cloud/migrate/push_stores.py --state /srv/pictographic/state --base-url https://pictographic.<account>.workers.dev
    python3 cloud/migrate/push_stores.py --state icon_set/state --base-url <worker> --dry-run    # count only

Artwork choices and stroke edits are read from the ``icon_artwork`` / ``stroke_edits`` tables of
``<state>/feedback.sqlite3`` when that database has them (deploy.py moved the folders into the
database with the ``legacy-json-stores-v1`` migration); otherwise from the old folders. Reference
image metadata comes from the ``reference_images`` table too when it exists (the bytes stay in
the folder), on top of the folder's ``<sha>.json`` files:

* ``icon-artwork/<hash>/artwork.json``      → store ``icon-artwork``, key = the icon key
* ``stroke-edits/<hash>/<hash>.json``       → store ``stroke-edits``, key = ``<icon>@<source svg sha256>``
* ``reference-images/<sha>.<png|svg>`` + meta → POST /api/reference-images (R2 file + D1 row)

Documents are written as they are (their revision numbers carry over). Reference images keep
their ids because ids are content hashes. ``--database`` names another database than
``<state>/feedback.sqlite3`` (a snapshot, for example).
"""
from __future__ import annotations

import argparse
import base64
from contextlib import closing
import json
from pathlib import Path
import sqlite3
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402


def documents_from_database(database: Path) -> dict[str, list[dict]] | None:
    """The artwork and stroke-edit documents stored in the database, or None when it has no store tables."""
    with closing(sqlite3.connect(database.resolve().as_uri() + '?mode=ro', uri=True)) as source:
        tables = {row[0] for row in source.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if not {'icon_artwork', 'stroke_edits'} <= tables:
            return None
        artwork = [json.loads(row[0]) for row in source.execute('SELECT document FROM icon_artwork ORDER BY icon')]
        strokes = [json.loads(row[0]) for row in
                   source.execute('SELECT document FROM stroke_edits ORDER BY icon, source_svg_sha256')]
        images = ([{'id': image_id, 'kind': kind, 'name': name} for image_id, kind, name in
                   source.execute('SELECT id, kind, name FROM reference_images ORDER BY id')]
                  if 'reference_images' in tables else [])
    return {'icon-artwork': artwork, 'stroke-edits': strokes, 'reference-images': images}


def documents_from_folders(state: Path) -> dict[str, list[dict]]:
    artwork = [json.loads(path.read_text(encoding='utf-8'))
               for path in sorted((state / 'icon-artwork').glob('*/artwork.json'))]
    strokes = [json.loads(path.read_text(encoding='utf-8'))
               for path in sorted((state / 'stroke-edits').glob('*/*.json'))]
    return {'icon-artwork': artwork, 'stroke-edits': strokes, 'reference-images': []}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--state', type=Path, required=True, help='folder that holds feedback.sqlite3 and the store folders')
    parser.add_argument('--database', type=Path, help='database to read the store tables from (default <state>/feedback.sqlite3)')
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--dry-run', action='store_true', help='count what would be sent; write nothing')
    args = parser.parse_args(argv)
    database = args.database or args.state / 'feedback.sqlite3'
    documents = documents_from_database(database) if database.is_file() else None
    origin = 'database' if documents is not None else 'folders'
    if documents is None:
        documents = documents_from_folders(args.state)
    token = None if args.dry_run else cloudapi.push_token(args.base_url)
    counts = {'icon-artwork': 0, 'stroke-edits': 0, 'reference-images': 0}
    for document in documents['icon-artwork']:
        if not args.dry_run:
            cloudapi.post_json(args.base_url, '/api/store/icon-artwork',
                               {'key': document['icon'], 'document': document, 'user': document.get('updated_by') or 'migration'}, token)
        counts['icon-artwork'] += 1
    for document in documents['stroke-edits']:
        key = f"{document['icon']}@{document['source_svg_sha256']}"
        if not args.dry_run:
            cloudapi.post_json(args.base_url, '/api/store/stroke-edits',
                               {'key': key, 'document': document, 'user': document.get('updated_by') or 'migration'}, token)
        counts['stroke-edits'] += 1
    metas = {path.stem: json.loads(path.read_text()) for path in sorted((args.state / 'reference-images').glob('*.json'))}
    metas.update((meta['id'], meta) for meta in documents['reference-images'])
    for meta in metas.values():
        image = args.state / 'reference-images' / f"{meta['id']}.{meta['kind']}"
        if not image.is_file():
            print(f'skipped {meta["id"]}: image file missing', file=sys.stderr)
            continue
        if not args.dry_run:
            saved = cloudapi.post_json(args.base_url, '/api/reference-images',
                                       {'name': meta.get('name'), 'data': base64.b64encode(image.read_bytes()).decode()})
            if saved['id'] != meta['id']:
                raise SystemExit(f'error: {image.name} came back as {saved["id"]}')
        counts['reference-images'] += 1
    print(json.dumps({'source': origin, 'dry_run': args.dry_run, 'counts': counts}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
