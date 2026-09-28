#!/usr/bin/env python3
"""Give Uncategorized primitives the category the pictoicon data records for them.

python3 icon_set/scripts/primitive_categories.py build --rows .../pg_d1_app_search_worker/sql/rows.json
python3 icon_set/scripts/primitive_categories.py summary

The ``_uncategorized_NN`` folders hold primitives whose D1 ``categories`` carry no topic
folder. Only rows with style ``pictoicon`` are read. A primitive tagged
``primitives-generate`` there is shown in the ``primitives-generate`` category; one with
only the generic ``primitive``/``primitives`` tags has no category and stays
Uncategorized. ``build`` rewrites data/primitive-categories.json from scratch:

    {"categories": {uuid: {"category", "pictoicon_categories", "concept"}}}

primitives_catalog.py moves each listed row into ``category``.
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.primitives_catalog import (CATEGORIES_PATH, UNCATEGORIZED, primitives_root,  # noqa: E402
                                                 scan)

STYLE = 'pictoicon'
GENERATED = 'primitives-generate'
GENERIC = {'primitive', 'primitives'}


def pictoicon_rows(path: Path) -> dict[str, dict]:
    """id -> D1 row for the pictoicon style (rows.json, or an extract of only pictoicon rows)."""
    rows = json.loads(path.read_text(encoding='utf-8'))
    return {str(r['id']).lower(): r for r in rows if r.get('style') == STYLE}


def category_for(categories: str) -> str | None:
    tokens = set(str(categories or '').split())
    return GENERATED if GENERATED in tokens else None


def build(rows_json: Path, root: Path, target: Path) -> collections.Counter:
    rows = pictoicon_rows(rows_json)
    entries, counts = {}, collections.Counter()
    for row in scan(root):
        uid = row['uuid']
        if row['category'] != UNCATEGORIZED or not uid:
            continue
        record = rows.get(uid)
        if record is None:
            counts['not in pictoicon'] += 1
            continue
        category = category_for(record.get('categories'))
        counts[category or 'no category (stays Uncategorized)'] += 1
        if category:
            entries[uid] = {'category': category, 'pictoicon_categories': record.get('categories'),
                            'concept': row['concept']}
    target.write_text(json.dumps({'source': f'D1 rows, style {STYLE}', 'categories': dict(sorted(entries.items()))},
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return counts


def summary(target: Path) -> None:
    entries = json.loads(target.read_text(encoding='utf-8'))['categories']
    print(f'{len(entries)} entries in {target}')
    for category, n in collections.Counter(e['category'] for e in entries.values()).most_common():
        print(f'  {n:5d}  {category}')


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--primitives', type=Path)
    parser.add_argument('--target', type=Path, default=CATEGORIES_PATH)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('build', help='rewrite the categories from the pictoicon rows')
    p.add_argument('--rows', type=Path, required=True, help='D1 rows.json from pg_d1_app_search_worker/sql')
    sub.add_parser('summary', help='count entries by category')
    args = parser.parse_args(argv)
    if args.command == 'build':
        counts = build(args.rows, primitives_root(args.primitives), args.target)
        print(' '.join(f'{k}={v}' for k, v in counts.items()), '->', args.target)
    else:
        summary(args.target)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
