#!/usr/bin/env python3
"""Export every combination part (main, sub, container, symbol) with its SVGs, read-only on D1.

    python3 cloud/migrate/export_parts.py                       # → cloud/exports/reference-parts/
    python3 cloud/migrate/export_parts.py --role symbol --no-drawn

For each role in ``reference_parts`` it writes, under ``<out>/<role>/``:

* ``<old concept>_<reference id>.svg``   the original reference the part is drawn from, named like the
                                         source files so the reference id can be read back from the name
* ``drawn/<family>__<icon id>.svg``      the current drawing of every icon linked to that reference
                                         (``icon_references``), unless --no-drawn

and ``<out>/manifest.csv`` + ``manifest.json``: one row per (role, part) with the reference id and
sha256, the combinations that use it, the drawn icons (key and svg_sha256), and ``original_sources``,
the exact JSON to store on an icon re-uploaded for this part so it links back to the reference (the
same value built icons carry). Parts whose reference id is not in ``references`` are listed with
status ``missing-reference`` and no SVG.

Reference SVGs are read from the local pictographic-primitives / pictographic-combinations folders and
fetched from the Worker (``/gallery/originals/<sha256>``) when a file is not there. D1 is queried
through the Cloudflare API with CLOUDFLARE_API_TOKEN from cloud/.env.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import csv
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cloudapi  # noqa: E402

ROOT = cloudapi.ROOT
ROLES = ('main', 'sub', 'container', 'symbol')
WORKER = 'https://pictographic-review.pictographic.workers.dev'
LOCAL_ROOTS = {'references/primitives/': 'pictographic-primitives/', 'references/combinations/': 'pictographic-combinations/'}


def wrangler_ids() -> tuple[str, str]:
    text = (ROOT / 'cloud' / 'worker' / 'wrangler.toml').read_text()
    account = re.search(r'^account_id\s*=\s*"([^"]+)"', text, re.M).group(1)
    database = re.search(r'^database_id\s*=\s*"([^"]+)"', text, re.M).group(1)
    return account, database


def d1_query(sql: str, params: list | None = None) -> list[dict]:
    token = cloudapi.settings().get('CLOUDFLARE_API_TOKEN')
    if not token:
        raise SystemExit('error: set CLOUDFLARE_API_TOKEN in cloud/.env')
    account, database = wrangler_ids()
    status, content = cloudapi.request('https://api.cloudflare.com', 'POST',
                                       f'/client/v4/accounts/{account}/d1/database/{database}/query',
                                       body=json.dumps({'sql': sql, 'params': params or []}).encode(), token=token)
    data = json.loads(content or b'{}')
    if status >= 400 or not data.get('success'):
        raise RuntimeError(f'D1 query failed (HTTP {status}): {data.get("errors", data)}')
    return data['result'][0]['results']


def safe(text: str) -> str:
    return re.sub(r'[\\/:*?"<>|\x00-\x1f]+', ' ', text or '').strip() or 'untitled'


def reference_svg(row: dict) -> bytes | None:
    key = row.get('r2_key') or ''
    for prefix, folder in LOCAL_ROOTS.items():
        if key.startswith(prefix) and (path := ROOT / (folder + key[len(prefix):])).is_file():
            return path.read_bytes()
    if row.get('sha256'):
        status, content = cloudapi.request(WORKER, 'GET', '/gallery/originals/' + row['sha256'])
        if status == 200:
            return content
    return None


def original_sources(row: dict) -> list[dict]:
    """The original_sources value built icons carry for this reference."""
    folder = 'pictographic-combinations' if (row.get('r2_key') or '').startswith('references/combinations/') else 'pictographic-primitives'
    return [{'url': f'originals/{row["sha256"]}', 'format': 'SVG', 'source_path': f'{folder}/{row["folder"]}/{row["file"]}'}]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, default=ROOT / 'cloud' / 'exports' / 'reference-parts')
    parser.add_argument('--role', choices=ROLES, action='append', help='only these roles (repeatable; default all)')
    parser.add_argument('--no-drawn', action='store_true', help='skip the drawn icon SVGs')
    args = parser.parse_args(argv)
    roles = args.role or list(ROLES)

    marks = ','.join('?' * len(roles))
    parts = d1_query(f"""
        SELECT p.role, p.part_reference_id AS reference_id, count(*) AS used_in,
               group_concat(p.reference_id, ' ') AS combinations,
               group_concat(DISTINCT coalesce(p.position, '')) AS positions,
               r.concept, r.old_concept, r.folder, r.file, r.r2_key, r.sha256
        FROM reference_parts p LEFT JOIN "references" r ON r.reference_id = p.part_reference_id
        WHERE p.role IN ({marks})
        GROUP BY p.role, p.part_reference_id
        ORDER BY p.role, used_in DESC""", roles)

    drawn = defaultdict(list)
    for row in d1_query(f"""
        SELECT ir.reference_id, i.key, i.family, i.icon_id, i.svg_sha256, i.uploaded,
               {'NULL' if args.no_drawn else 'v.svg'} AS svg
        FROM icon_references ir JOIN icons i ON i.key = ir.icon
        LEFT JOIN revisions v ON v.svg_sha256 = i.svg_sha256
        WHERE ir.reference_id IN (SELECT part_reference_id FROM reference_parts WHERE role IN ({marks}))""", roles):
        drawn[row['reference_id']].append(row)

    manifest, counts = [], defaultdict(lambda: defaultdict(int))
    for part in parts:
        role, rid = part['role'], part['reference_id']
        folder = args.out / role
        entry = {'role': role, 'reference_id': rid, 'reference_sha256': part['sha256'], 'concept': part['concept'],
                 'old_concept': part['old_concept'], 'used_in_combinations': part['used_in'],
                 'combination_ids': part['combinations'].split(), 'positions': [p for p in part['positions'].split(',') if p],
                 'reference_svg': None, 'original_sources': None, 'drawn_icons': [], 'status': 'ok'}
        if part['sha256'] is None:
            entry['status'] = 'missing-reference'
            counts[role]['missing reference'] += 1
            manifest.append(entry)
            continue
        entry['original_sources'] = original_sources(part)
        svg = reference_svg(part)
        if svg is None:
            entry['status'] = 'reference-svg-unavailable'
            counts[role]['reference svg unavailable'] += 1
        else:
            path = folder / f'{safe(part["old_concept"] or part["concept"])}_{rid}.svg'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(svg)
            entry['reference_svg'] = str(path.relative_to(args.out))
            counts[role]['reference svgs'] += 1
        for icon in drawn.get(rid, []):
            item = {'key': icon['key'], 'family': icon['family'], 'svg_sha256': icon['svg_sha256'], 'uploaded': bool(icon['uploaded']), 'svg': None}
            if icon['svg']:
                path = folder / 'drawn' / f'{icon["family"]}__{icon["icon_id"]}.svg'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(icon['svg'], encoding='utf-8')
                item['svg'] = str(path.relative_to(args.out))
                counts[role]['drawn svgs'] += 1
            entry['drawn_icons'].append(item)
        counts[role]['parts'] += 1
        counts[role]['parts with a drawn icon'] += bool(entry['drawn_icons'])
        manifest.append(entry)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
    with (args.out / 'manifest.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['role', 'reference_id', 'reference_sha256', 'concept', 'old_concept', 'used_in_combinations',
                         'positions', 'status', 'reference_svg', 'drawn_icons', 'original_sources'])
        for e in manifest:
            writer.writerow([e['role'], e['reference_id'], e['reference_sha256'], e['concept'], e['old_concept'],
                             e['used_in_combinations'], ' '.join(e['positions']), e['status'], e['reference_svg'],
                             ' '.join(f'{d["key"]}@{d["svg_sha256"]}' for d in e['drawn_icons']),
                             json.dumps(e['original_sources'], separators=(',', ':')) if e['original_sources'] else ''])
    for role in roles:
        print(role, dict(counts[role]))
    print('wrote', args.out)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
