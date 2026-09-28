#!/usr/bin/env python3
"""Copy the artwork, stroke-edit and reference-image stores of a gallery into the cloud (read-only on the source).

    python3 cloud/migrate/push_stores.py --state /srv/pictographic/state --base-url https://pictographic.<account>.workers.dev

* ``icon-artwork/<hash>/artwork.json``      → store ``icon-artwork``, key = the icon key
* ``stroke-edits/<hash>/<hash>.json``       → store ``stroke-edits``, key = ``<icon>@<source svg sha256>``
* ``reference-images/<sha>.<png|svg>`` + meta → POST /api/reference-images (R2 file + D1 row)

Newer servers keep the first two as rows of ``feedback.sqlite3`` (tables ``icon_artwork`` and
``stroke_edits``) and reference image metadata in ``reference_images`` (the bytes stay in the
folder); those are read too, opened read-only. Documents are written as they are (their revision
numbers carry over). Reference images keep their ids because ids are content hashes.
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


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--state', type=Path, required=True, help='folder that holds feedback.sqlite3 and the store folders')
    parser.add_argument('--base-url', required=True)
    args = parser.parse_args(argv)
    token = cloudapi.push_token(args.base_url)
    counts = {'icon-artwork': 0, 'stroke-edits': 0, 'reference-images': 0}
    artwork = [json.loads(path.read_text(encoding='utf-8')) for path in sorted((args.state / 'icon-artwork').glob('*/artwork.json'))]
    edits = [json.loads(path.read_text(encoding='utf-8')) for path in sorted((args.state / 'stroke-edits').glob('*/*.json'))]
    metas = {path.stem: json.loads(path.read_text()) for path in sorted((args.state / 'reference-images').glob('*.json'))}
    database = args.state / 'feedback.sqlite3'
    if database.is_file():
        with closing(sqlite3.connect(f'file:{database}?mode=ro', uri=True)) as connection:
            tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            if 'icon_artwork' in tables:
                artwork += [json.loads(text) for (text,) in connection.execute('SELECT document FROM icon_artwork ORDER BY icon')]
            if 'stroke_edits' in tables:
                edits += [json.loads(text) for (text,) in connection.execute(
                    'SELECT document FROM stroke_edits ORDER BY icon, source_svg_sha256')]
            if 'reference_images' in tables:
                for image_id, kind, name in connection.execute('SELECT id, kind, name FROM reference_images ORDER BY id'):
                    metas[image_id] = {'id': image_id, 'kind': kind, 'name': name}
    for document in artwork:
        cloudapi.post_json(args.base_url, '/api/store/icon-artwork',
                           {'key': document['icon'], 'document': document, 'user': document.get('updated_by') or 'migration'}, token)
        counts['icon-artwork'] += 1
    for document in edits:
        key = f"{document['icon']}@{document['source_svg_sha256']}"
        cloudapi.post_json(args.base_url, '/api/store/stroke-edits',
                           {'key': key, 'document': document, 'user': document.get('updated_by') or 'migration'}, token)
        counts['stroke-edits'] += 1
    for meta in metas.values():
        image = args.state / 'reference-images' / f"{meta['id']}.{meta['kind']}"
        if not image.is_file():
            print(f'skipped {meta["id"]}: image file missing', file=sys.stderr)
            continue
        saved = cloudapi.post_json(args.base_url, '/api/reference-images',
                                   {'name': meta.get('name'), 'data': base64.b64encode(image.read_bytes()).decode()})
        if saved['id'] != meta['id']:
            raise SystemExit(f'error: {image.name} came back as {saved["id"]}')
        counts['reference-images'] += 1
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
