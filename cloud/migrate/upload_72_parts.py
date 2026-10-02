#!/usr/bin/env python3
"""Upload the 72 side-pair parts drawn in tracer (main-54, sub-36) and pick the twin drawings, read-only on tracer.

    python3 cloud/migrate/upload_72_parts.py --tracer ~/Documents/gitlab/tracer --base-url https://pictographic-review-next.pictographic.workers.dev
    python3 cloud/migrate/upload_72_parts.py … --send                       # dry run without it
    python3 cloud/migrate/upload_72_parts.py … --send --twins cloud/exports/sync-next/twin-picks-72.json

tracer's work/subs-72/main54 and sub36 flows (flow.db, state cleaned or authored) hold each part's drawing, its id
being the part's reference id. Each goes to POST /api/icons/upload with family main-54 / sub-36 and reference_id, which
links it to the reference and fills that part's 72 pick in every side pair using it. A part already on the site with
the same drawing (same family and reference, same SVG apart from the width / height the upload adds) is skipped, so a
rerun sends only what is new or redrawn.

--twins: picks of another reference's drawing (an API duplicate part drawn once), saved from the site as
{reference_id, role, family, drawing_reference_id}; each is set with POST /api/combinations/parts (size 72) to the
uploaded drawing of `drawing_reference_id`.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402

FLOWS = {'main-54': 'work/subs-72/main54', 'sub-36': 'work/subs-72/sub36'}
STATES = ('cleaned', 'authored')


def drawings(tracer: Path) -> list[dict]:
    """Every finished part of the two flows: family, reference id, name, SVG."""
    out = []
    for family, folder in FLOWS.items():
        con = sqlite3.connect(f'file:{tracer / folder / "flow.db"}?mode=ro', uri=True)
        for reference_id, name, svg in con.execute(f"SELECT id, name, out_svg FROM icons WHERE state IN {STATES} ORDER BY idx"):
            if not svg:
                raise SystemExit(f'error: {family} {reference_id} is finished but has no out_svg')
            out.append({'family': family, 'reference_id': reference_id, 'name': name, 'svg': (tracer / svg).read_text()})
    return out


def same_drawing(a: str, b: str) -> bool:
    """Equal SVG text apart from the width / height an upload adds to the root."""
    strip = lambda s: re.sub(r'\s+(width|height)="[^"]*"', '', s.split('>', 1)[0]) + '>' + s.split('>', 1)[1] if '>' in s else s
    return strip(a).strip() == strip(b).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--tracer', required=True, type=Path)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--limit', type=int)
    parser.add_argument('--twins', type=Path)
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()

    parts = drawings(args.tracer)
    print(f'{len(parts)} finished parts in tracer: ' + ', '.join(f'{f} {sum(p["family"] == f for p in parts)}' for f in FLOWS))
    existing = uploaded(args.base_url)
    todo = [p for p in parts if not same_drawing(existing.get((p['family'], p['reference_id']), ('', ''))[1] or '', p['svg'])]
    todo = todo[:args.limit] if args.limit else todo
    print(f'{len(existing)} on the site already; {len(todo)} to upload')
    if not args.send:
        for p in todo[:5]:
            print(f'  would upload {p["family"]} {p["reference_id"]} {p["name"]}')
        return 0

    picked, failed = 0, []

    def send(part: dict):
        try:
            answer = cloudapi.post_json(args.base_url, '/api/icons/upload', {
                'name': part['name'], 'family': part['family'], 'reference_id': part['reference_id'],
                'bypass_validation': True, 'svg': part['svg']})
            return part, answer, None
        except RuntimeError as error:
            return part, None, str(error)

    with ThreadPoolExecutor(args.workers) as pool:
        for n, (part, answer, error) in enumerate(pool.map(send, todo), 1):
            if error:
                failed.append(f'{part["family"]} {part["reference_id"]}: {error}')
            else:
                picked += len(answer.get('combination_parts', []))
            if n % 100 == 0 or n == len(todo):
                print(f'uploaded {n}/{len(todo)} ({picked} pair parts picked, {len(failed)} failed)', flush=True)
    for line in failed[:10]:
        print('  failed', line)

    if args.twins:
        existing = uploaded(args.base_url)
        twins = json.loads(args.twins.read_text())
        missing, set_ = [], 0
        for twin in twins:
            drawing = existing.get((twin['family'], twin['drawing_reference_id']))
            if not drawing:
                missing.append(twin)
                continue
            cloudapi.post_json(args.base_url, '/api/combinations/parts', {
                'reference_id': twin['reference_id'], 'role': twin['role'], 'icon': drawing[0], 'size': 72})
            set_ += 1
        print(f'{set_} twin picks set; {len(missing)} without an uploaded drawing')
    return 1 if failed else 0


def uploaded(base_url: str, workers: int = 8) -> dict[tuple[str, str], tuple[str, str]]:
    """(family, reference id) → (key, svg) of the main-54 / sub-36 uploads on the site: their keys from the paged list
    (GET /api/icons), each one's reference from its record (GET /api/icon) and drawing (GET /api/combinations/drawings)."""
    keys = []
    for family in FLOWS:
        offset = 0
        while True:
            status, content = cloudapi.request(base_url, 'GET', f'/api/icons?family={family}&limit=192&offset={offset}')
            if status >= 400:
                raise SystemExit(f'error: GET /api/icons -> {status}')
            page = json.loads(content)
            keys += [item['key'] for item in page['items']]
            offset += len(page['items'])
            if not page['items'] or offset >= page['total']:
                break

    def record(key: str) -> dict:
        status, content = cloudapi.request(base_url, 'GET', '/api/icon?key=' + urllib.parse.quote(key))
        if status >= 400:
            raise SystemExit(f'error: GET /api/icon {key} -> {status}')
        return json.loads(content)

    with ThreadPoolExecutor(workers) as pool:
        records = list(pool.map(record, keys))
    svgs = {}
    for start in range(0, len(keys), 100):
        status, content = cloudapi.request(base_url, 'GET', '/api/combinations/drawings?keys=' + ','.join(keys[start:start + 100]))
        if status >= 400:
            raise SystemExit(f'error: GET /api/combinations/drawings -> {status}')
        svgs.update({k: d.get('svg') or '' for k, d in json.loads(content).items()})
    out = {}
    for item in records:
        reference = reference_of(item)
        if reference:
            out[(item['family'], reference)] = (item['key'], svgs.get(item['key'], ''))
    return out


def reference_of(record: dict) -> str | None:
    """The reference an upload was drawn from: its original's file is named `<concept>_<reference id>.svg`."""
    for source in record.get('original_sources') or []:
        name = (source.get('source_path') or '').rsplit('/', 1)[-1]
        if '_' in name and name.endswith('.svg'):
            return name[:-4].rsplit('_', 1)[1].lower()
    return None


if __name__ == '__main__':
    raise SystemExit(main())
