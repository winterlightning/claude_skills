#!/usr/bin/env python3
"""Copy the folders kept beside a feedback database into the cloud (read-only on the source).

    python3 cloud/migrate/push_stores.py --state /srv/pictographic/state --base-url https://pictographic.<account>.workers.dev

* ``icon-artwork/<hash>/artwork.json``      → store ``icon-artwork``, key = the icon key
* ``stroke-edits/<hash>/<hash>.json``       → store ``stroke-edits``, key = ``<icon>@<source svg sha256>``
* ``reference-images/<sha>.<png|svg>`` + meta → POST /api/reference-images (R2 file + D1 row)

Documents are written as they are (their revision numbers carry over). Reference images keep
their ids because ids are content hashes.
"""
from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path
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
    for path in sorted((args.state / 'icon-artwork').glob('*/artwork.json')):
        document = json.loads(path.read_text(encoding='utf-8'))
        cloudapi.post_json(args.base_url, '/api/store/icon-artwork',
                           {'key': document['icon'], 'document': document, 'user': document.get('updated_by') or 'migration'}, token)
        counts['icon-artwork'] += 1
    for path in sorted((args.state / 'stroke-edits').glob('*/*.json')):
        document = json.loads(path.read_text(encoding='utf-8'))
        key = f"{document['icon']}@{document['source_svg_sha256']}"
        cloudapi.post_json(args.base_url, '/api/store/stroke-edits',
                           {'key': key, 'document': document, 'user': document.get('updated_by') or 'migration'}, token)
        counts['stroke-edits'] += 1
    for meta_path in sorted((args.state / 'reference-images').glob('*.json')):
        meta = json.loads(meta_path.read_text())
        image = meta_path.with_name(f"{meta['id']}.{meta['kind']}")
        if not image.is_file():
            print(f'skipped {meta_path.name}: image file missing', file=sys.stderr)
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
