#!/usr/bin/env python3
"""Fill the icon list columns of a database whose icons were pushed before migration 0015, from its own catalog.

    python3 cloud/migrate/backfill_records.py --base-url https://pictographic-review-next.pictographic.workers.dev

Reads the site's /gallery/icons.json and review-facets.json once, stores each pushed icon's full record with its
list columns and symmetry (POST /api/icons/records: nothing else changes, so a drawing picked since the push keeps
its svg_sha256), then POST /api/icons/reindex for uploads and combinations built in the browser and every icon's
review state. Uploads are skipped here: their records are already in D1.
"""
from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
import sys
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402

CHUNK = 200


def fetch(base_url: str, path: str):
    request = urllib.request.Request(base_url.rstrip('/') + path, headers={'Accept-Encoding': 'gzip', 'User-Agent': 'pictographic-migrate/1.0'})
    with urllib.request.urlopen(request, timeout=900) as response:
        body = response.read()
        return json.loads(gzip.decompress(body) if response.headers.get('Content-Encoding') == 'gzip' else body)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--base-url', required=True)
    args = parser.parse_args()
    token = cloudapi.push_token(args.base_url)
    catalog = fetch(args.base_url, '/gallery/icons.json')
    try:
        facets = fetch(args.base_url, '/gallery/review-facets.json')
    except OSError:
        facets = {}
    records = [r for field in ('icons', 'failed_icons') for r in catalog.get(field, []) if not r.get('uploaded_icon')]
    print(f'{len(records)} pushed records, {len(facets)} facets', flush=True)
    stored = 0
    for start in range(0, len(records), CHUNK):
        chunk = records[start:start + CHUNK]
        result = cloudapi.post_json(args.base_url, '/api/icons/records', {'records': chunk,
                                    'facets': {r['key']: facets[r['key']] for r in chunk if r['key'] in facets}}, token)
        stored += result['stored']
        print(f'records {start + len(chunk)}/{len(records)} (stored {stored})', flush=True)
    # Uploads' symmetry (their rows are not pushed).
    pushed = {r['key'] for r in records}
    uploads = sorted((k, v) for k, v in facets.items() if k not in pushed)
    for start in range(0, len(uploads), 500):
        cloudapi.post_json(args.base_url, '/api/catalog/push', {'push_id': 'backfill', 'icons': [], 'final': False,
                                                                'upload_facets': dict(uploads[start:start + 500])}, token)
    offset, indexed = 0, 0
    while offset is not None:
        result = cloudapi.post_json(args.base_url, '/api/icons/reindex', {'offset': offset, 'limit': 500}, token)
        indexed += result['indexed']
        offset = result['next_offset']
        print(f'reindexed up to row {offset} ({indexed} with records)', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
