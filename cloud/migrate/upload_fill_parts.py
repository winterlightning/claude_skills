#!/usr/bin/env python3
"""Upload the fill variant icons of the fill side pairs (icon_set/state/side-fill/fill-icons/manifest.json, written by
`python3 -m icon_set side-fill icons`): one POST /api/icons/upload per variant, family main-fill-48 / sub-fill-32,
with variant_of (the solo / sub icon it fills) and variant_label (current, region-3, fill…). Each starts Ready in Icon
review. The outline is the solo / sub icon itself and is not uploaded.

    python3 cloud/migrate/upload_fill_parts.py --base-url http://127.0.0.1:8821            # dry run
    python3 cloud/migrate/upload_fill_parts.py --base-url … --send

What is on the site already is read from GET /api/side-fill/parts (keyset pages of 120 parts with their variants'
shas: about one row per part and variant, never a table scan). A variant whose drawing is already there is skipped;
one that changed is uploaded again, which the route stores as a new drawing of the same icon (back to Ready).
Run the import SQL first (fill_parts lists the parts), then this, then the picks SQL.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
WORK = REPO / 'icon_set/state/side-fill'
MANIFEST = WORK / 'fill-icons/manifest.json'
# What was sent and what the site stored (the route cleans the SVG, so its sha is not the file's): a variant is
# skipped when the site still has the drawing sent for the same file.
LEDGER = WORK / 'fill-icons/uploaded.json'


def on_site(base_url: str) -> dict[tuple[str, str], str]:
    """(variant_of, variant_label) → svg_sha256 of the fill variants the site has, from bounded part pages."""
    found = {}
    for role in ('main', 'sub'):
        after = None
        while True:
            query = {'role': role, 'limit': 120, **({'after': after} if after else {})}
            status, content = cloudapi.request(base_url, 'GET', '/api/side-fill/parts?' + urllib.parse.urlencode(query))
            if status >= 400:
                raise SystemExit(f'error: GET /api/side-fill/parts -> {status} {content[:200]!r}')
            page = json.loads(content)
            for part in page['parts']:
                for v in part['variants']:
                    found[(part['key'], v['variant'])] = v['svg_sha256']
            after = page.get('next')
            if not after:
                break
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--limit', type=int)
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    existing = on_site(args.base_url)
    ledger_all = json.loads(LEDGER.read_text()) if LEDGER.is_file() else {}
    ledger = ledger_all.setdefault(args.base_url.rstrip('/'), {})
    todo = []
    for item in manifest:
        svg = (WORK / item['svg']).read_text()
        mine = hashlib.sha256(svg.encode()).hexdigest()
        sent = ledger.get(f'{item["variant_of"]} {item["variant_label"]}', {})
        if sent.get('file_sha256') == mine and existing.get((item['variant_of'], item['variant_label'])) == sent.get('site_sha256'):
            continue
        todo.append((item, svg))
    print(f'{len(manifest)} fill variant icons; {len(manifest) - len(todo)} on the site already; {len(todo)} to upload'
          + (f' (sending the first {args.limit})' if args.limit else ''))
    todo = todo[:args.limit] if args.limit else todo
    if not args.send:
        for item, _ in todo[:5]:
            print(f'  would upload {item["family"]} {item["variant_of"]} {item["variant_label"]}')
        return 0

    def send(job):
        item, svg = job
        try:
            answer = cloudapi.post_json(args.base_url, '/api/icons/upload', {
                'name': item['name'], 'family': item['family'], 'category': 'Fill side pairs',
                'variant_of': item['variant_of'], 'variant_label': item['variant_label'],
                'bypass_validation': True, 'svg': svg})
            return item, answer, None
        except RuntimeError as error:
            return item, None, str(error)

    failed = []
    with ThreadPoolExecutor(args.workers) as pool:
        for n, (item, answer, error) in enumerate(pool.map(send, todo), 1):
            if error:
                failed.append(f'{item["variant_of"]} {item["variant_label"]}: {error}')
            else:
                ledger[f'{item["variant_of"]} {item["variant_label"]}'] = {
                    'file_sha256': item['svg_sha256'], 'site_sha256': answer['record']['svg_sha256'], 'key': answer['record']['key']}
            if n % 100 == 0 or n == len(todo):
                print(f'uploaded {n}/{len(todo)} ({len(failed)} failed)', flush=True)
    LEDGER.write_text(json.dumps(ledger_all, indent=1) + '\n')
    for line in failed[:10]:
        print('  failed', line)
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
