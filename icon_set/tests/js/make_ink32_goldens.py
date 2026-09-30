#!/usr/bin/env python3
"""Golden cases for normalize-ink32.js: every sub drawing of a D1 snapshot normalized by sub_ink32.normalize_ink32.

    python3 icon_set/tests/js/make_ink32_goldens.py --db snapshot.sqlite [--sample 150] [--out ink32-goldens.json]

The drawing goes through build_combination_previews._inline_class_styles first, as side_recombine does.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.build_combination_previews import _inline_class_styles  # noqa: E402
from icon_set.scripts.sub_ink32 import normalize_ink32  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--db', required=True, type=Path)
    parser.add_argument('--sample', type=int, default=0, help='keep this many cases (0: all)')
    parser.add_argument('--out', type=Path, default=Path(__file__).with_name('ink32-goldens.json'))
    args = parser.parse_args()
    db = sqlite3.connect(f'file:{args.db}?mode=ro', uri=True)
    rows = db.execute("""SELECT DISTINCT i.key, CASE WHEN i.uploaded THEN (SELECT svg FROM uploaded_icons u WHERE u.icon = i.key)
        ELSE (SELECT svg FROM revisions r WHERE r.svg_sha256 = i.svg_sha256) END FROM icons i
        WHERE i.family = 'sub' AND i.svg_sha256 != ''""").fetchall()
    cases = []
    for key, svg in rows:
        if not svg:
            continue
        svg = _inline_class_styles(svg)
        case = {'key': key, 'svg': svg, 'text': False}
        try:
            case['document'], case['ink'] = normalize_ink32(svg, text=False)
        except Exception as error:  # noqa: BLE001 - the JS must refuse the same drawings
            case['error'] = f'{type(error).__name__}: {error}'
        cases.append(case)
    if args.sample:
        cases = random.Random(5).sample(cases, min(args.sample, len(cases)))
    args.out.write_text(json.dumps(cases, separators=(',', ':')) + '\n')
    print(f'{len(cases)} cases → {args.out}')


if __name__ == '__main__':
    main()
