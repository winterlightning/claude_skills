#!/usr/bin/env python3
"""Golden cases for the browser side engine (combine.js `side`): pairs rendered by the Python engine.

    python3 icon_set/tests/js/make_side_goldens.py --pairs experiment-combination.json --db snapshot.sqlite \\
        [--limit 200] [--out /tmp/side-goldens.json]

Renders published side pairs with combination_experiment.render (the engine the side pages use), spread
over every sizing mode, plus every hand-adjusted layout saved in the `side-layouts` store. Each case keeps
only the pair row's chosen main and sub, the request and the Python SVG, so the JS port can be checked
stroke for stroke (side.test.mjs).
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from collections import defaultdict
import json
from pathlib import Path
import random
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.combination_experiment import render  # noqa: E402


def slim(row, main, sub):
    pick = lambda items, icon: [i for i in items if i['icon'] == icon][:1]
    keep = {k: v for k, v in row.items() if k not in ('mains', 'subs')}
    return {**keep, 'mains': pick(row['mains'], main), 'subs': pick(row['subs'], sub)}


def one(job):
    data, row = job
    main_icon = data.get('main') or row['mains'][0]['icon']
    sub_icon = data.get('sub') or row['subs'][0]['icon']
    case = {'request': data, 'row': slim(row, main_icon, sub_icon)}
    try:
        result = render(dict(data), row)
        case['python'] = {'svg': result['svg'], 'placements': result['placements'], 'canvas': result['canvas']}
    except ValueError as error:
        case['error'] = str(error)
    return case


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--pairs', required=True, type=Path)
    parser.add_argument('--db', type=Path)
    parser.add_argument('--limit', type=int, default=200)
    parser.add_argument('--out', type=Path, default=Path('/tmp/side-goldens.json'))
    parser.add_argument('--jobs', type=int, default=8)
    args = parser.parse_args()
    rows = {r['id']: r for r in json.loads(args.pairs.read_text())['rows']}

    # Spread over sizing modes and positions: every kind gets its share of the sample.
    kinds = defaultdict(list)
    for row in rows.values():
        sub = row['subs'][0] if row['subs'] else {}
        kinds[(sub.get('sizing_mode') or 'default', row.get('position'), bool(row.get('native_text')))].append(row['id'])
    rng = random.Random(64)
    picked = []
    while len(picked) < args.limit and any(kinds.values()):
        for key in sorted(kinds, key=str):
            if kinds[key] and len(picked) < args.limit:
                picked.append(kinds[key].pop(rng.randrange(len(kinds[key]))))

    requests = [{'id': pid} for pid in picked]
    if args.db:
        db = sqlite3.connect(f'file:{args.db}?mode=ro', uri=True)
        for key, text in db.execute("SELECT key, document FROM store_documents WHERE store = 'side-layouts' "
                                    "AND json_extract(document, '$.layout') IS NOT NULL"):
            entry = json.loads(text)
            if key in rows:
                requests.append({'id': key, 'main': entry['main']['icon'], 'sub': entry['sub']['icon'], 'layout': entry['layout']})

    with ProcessPoolExecutor(args.jobs) as pool:
        cases = list(pool.map(one, [(data, rows[data['id']]) for data in requests], chunksize=4))
    args.out.write_text(json.dumps(cases, separators=(',', ':')) + '\n')
    print(f'{len(cases)} cases ({sum("error" in c for c in cases)} errors) → {args.out}')


if __name__ == '__main__':
    main()
