#!/usr/bin/env python3
"""Find sub/symbol icons whose canvas is not 32x32 and discard them.

    python3 icon_set/scripts/remove_non32_subs.py                     # dry run: list only
    python3 icon_set/scripts/remove_non32_subs.py --family symbol     # one family
    python3 icon_set/scripts/remove_non32_subs.py --keep-text         # spare natural-width text icons
    python3 icon_set/scripts/remove_non32_subs.py --resize-only       # only ResizeSymbol copies (e.g. 24x24)
    python3 icon_set/scripts/remove_non32_subs.py --apply --user jakes

The size is the model's own canvas (`canvas_dimensions`), which is what the
published SVG's width/height come from; e.g. a 24x24 `*-symbol-resize` icon or
a 68x20 natural-width text icon. Removal goes through `discard_icon.discard_many`,
the gallery's Discard action: the Python model is archived in the gallery
database's discarded_icons table, and its published SVG/PNG, manifest and catalog rows
and review rows are removed. A model that another kept icon depends on (as its
`variant_of` parent or by import) is reported and left in place.
"""
from __future__ import annotations

import argparse
import inspect
import json
from pathlib import Path
import sqlite3
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model.icons.registry import create, factories  # noqa: E402
from icon_set.model.icons.sub._text_base import Text32Mixin, canvas_dimensions  # noqa: E402
from icon_set.scripts.workspace import DEFAULT_DATABASE, DEFAULT_DIST  # noqa: E402


def find_non32(families, keep_text=False, resize_only=False) -> list[dict]:
    from icon_set.model.icons.symbol._resize_base import ResizeSymbol

    rows = []
    for icon_id, factory in sorted(factories().items()):
        if factory.family not in families:
            continue
        try:
            icon = create(icon_id)
            width, height = canvas_dimensions(icon)
        except Exception as error:  # an unbuildable model is reported, never guessed at
            rows.append({'icon_id': icon_id, 'family': factory.family, 'error': f'{type(error).__name__}: {error}'})
            continue
        if (width, height) == (32, 32) or (keep_text and isinstance(icon, Text32Mixin)):
            continue
        if resize_only and not isinstance(icon, ResizeSymbol):
            continue
        path = Path(inspect.getsourcefile(factory)).resolve()
        rows.append({
            'key': f'{factory.family}/{icon_id}', 'icon_id': icon_id, 'family': factory.family,
            'name': icon_id, 'size': f'{width}x{height}', 'text': isinstance(icon, Text32Mixin),
            'python_source': {'path': str(path.relative_to(REPO_ROOT)), 'family': factory.family,
                              'class_name': factory.__name__},
        })
    return rows


def apply(rows, user) -> dict:
    """Discard in passes so a variant goes before the parent it names."""
    from icon_set.scripts.discard_icon import discard_many

    pending, discarded, failed = [r for r in rows if 'error' not in r], [], []
    with sqlite3.connect(DEFAULT_DATABASE) as connection:
        while pending:
            result = discard_many(pending, source_root=REPO_ROOT, dist=DEFAULT_DIST,
                                  connection=connection, user=user)
            connection.commit()
            discarded += result['discarded']
            if not result['discarded']:
                failed = result['failed']
                break
            blocked = {f['icon'] for f in result['failed']}
            pending = [r for r in pending if r['key'] in blocked]
    return {'discarded': discarded, 'failed': failed}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--family', action='append', choices=('sub', 'symbol'),
                        help='family to scan (repeatable; default: sub and symbol)')
    parser.add_argument('--keep-text', action='store_true', help='do not remove natural-width text icons')
    parser.add_argument('--resize-only', action='store_true',
                        help='only resized symbol copies (ResizeSymbol), e.g. 24x24 *-symbol-resize icons')
    parser.add_argument('--apply', action='store_true', help='actually discard (default is a dry run)')
    parser.add_argument('--user', default='remove-non32-subs', help='name recorded in the discard archive')
    parser.add_argument('--report', type=Path, default=REPO_ROOT / 'icon_set/work/remove-non32-subs/report.json')
    args = parser.parse_args(argv)
    families = tuple(args.family or ('sub', 'symbol'))

    rows = find_non32(families, keep_text=args.keep_text, resize_only=args.resize_only)
    for row in rows:
        print(f"{row['family']:7} {row.get('size', 'ERROR'):>8}  {row['icon_id']}"
              + (f"  ({row['error']})" if 'error' in row else ''))
    by_family = {f: sum(r['family'] == f and 'error' not in r for r in rows) for f in families}
    print(f"\n{sum(by_family.values())} non-32x32 icons {by_family}; "
          f"{sum('error' in r for r in rows)} could not be measured")
    report = {'families': families, 'keep_text': args.keep_text, 'resize_only': args.resize_only, 'icons': rows}
    if args.apply:
        result = apply(rows, args.user)
        report.update(result)
        print(f"discarded {len(result['discarded'])}; left in place {len(result['failed'])}")
        for failure in result['failed']:
            print(f"  kept {failure['icon']}: {failure['error']}")
        print('Rebuild the affected families, e.g. python3 icon_set/scripts/build.py --family sub')
    else:
        print('Dry run; nothing removed. Add --apply to discard.')
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(f'report -> {args.report.relative_to(REPO_ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
