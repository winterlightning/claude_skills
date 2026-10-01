#!/usr/bin/env python3
"""Golden cases for rebuilding stale side pairs in the browser: pairs recombined from current drawings.

    python3 icon_set/tests/js/make_stale_goldens.py --pairs experiment-combination.json --db snapshot.sqlite \\
        [--limit 700] [--out /tmp/stale-goldens.json]

For every side pair whose main or sub was redrawn since it was built (reference_parts.built_sha is not the
icon's drawing, migration 0009), recombine it the way the side pages do: side_recombine.pair_with_documents
measures the changed drawings (a sub is normalized to SUB32), then combination_experiment.render combines.
Each case keeps the published row's chosen items, the current documents and the Python SVG.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.combination_experiment import render  # noqa: E402
from icon_set.scripts.side_recombine import pair_with_documents  # noqa: E402


def one(job):
    ref, docs, row = job
    main, sub = row['mains'][0]['icon'], row['subs'][0]['icon']
    main = next((m['icon'] for m in row['mains'] if m.get('family') in ('solo', 'combination_main')), main)
    case = {'row_id': ref, 'main': main, 'sub': sub, 'documents': docs,
            'row': {**{k: v for k, v in row.items() if k not in ('mains', 'subs')},
                    'mains': [m for m in row['mains'] if m['icon'] == main][:1],
                    'subs': [s for s in row['subs'] if s['icon'] == sub][:1]}}
    try:
        current, chosen = pair_with_documents(row, main, sub, docs)
        case['measured'] = {'main': next(m for m in current['mains'] if m['icon'] == chosen['main']),
                            'sub': next(s for s in current['subs'] if s['icon'] == chosen['sub'])}
        result = render({'id': ref, **chosen}, row=current)
        case['python'] = {'svg': result['svg']}
    except ValueError as error:
        case['error'] = str(error)
    return case


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--pairs', required=True, type=Path)
    parser.add_argument('--db', required=True, type=Path)
    parser.add_argument('--limit', type=int, default=700)
    parser.add_argument('--out', type=Path, default=Path('/tmp/stale-goldens.json'))
    parser.add_argument('--jobs', type=int, default=8)
    args = parser.parse_args()
    rows = {r['id']: r for r in json.loads(args.pairs.read_text())['rows']}
    db = sqlite3.connect(f'file:{args.db}?mode=ro', uri=True)
    stale = db.execute("""
        SELECT p.reference_id, p.role, p.icon,
            CASE WHEN i.uploaded THEN (SELECT svg FROM uploaded_icons u WHERE u.icon = i.key)
                 ELSE (SELECT svg FROM revisions r WHERE r.svg_sha256 = i.svg_sha256) END AS svg
        FROM reference_parts p JOIN icons i ON i.key = p.icon
        WHERE p.role IN ('main', 'sub') AND p.built_sha IS NOT NULL AND p.built_sha != i.svg_sha256""").fetchall()
    documents = {}
    for ref, role, icon, svg in stale:
        if ref in rows and svg:
            documents.setdefault(ref, {})[role] = svg
    jobs = [(ref, docs, rows[ref]) for ref, docs in sorted(documents.items())[:args.limit]]
    with ProcessPoolExecutor(args.jobs) as pool:
        cases = list(pool.map(one, jobs, chunksize=4))
    args.out.write_text(json.dumps(cases, separators=(',', ':')) + '\n')
    print(f'{len(cases)} cases ({sum("error" in c for c in cases)} errors) → {args.out}')


if __name__ == '__main__':
    main()
