#!/usr/bin/env python3
"""Set every Python icon model's ``category`` from its source pictoicon record.

python3 -m icon_set.scripts.fix_model_categories            # dry run, writes the report
python3 -m icon_set.scripts.fix_model_categories --apply    # rewrites the model files

Authored models carry free-form categories (``objects/food``, ``objects/general``,
``nature/batch-01`` ...). The correct one comes from ``SOURCE_ICON_ID``: the pictoicon
record's topic token (``food``). A record with no topic falls back to its type:
``other`` / ``primitives-generate`` -> ``primitives-generate``, else the first of
``symbol``, ``state``, ``container``, ``text``, ``typeface``, ``combination``; one with only
``primitive``/``primitives`` is ``Uncategorized``, as the build shows it. Models with no
pictoicon record keep a valid catalog category and only get gallery.CATEGORY_ALIASES
spellings fixed. Anything left unresolved is reported and left as it is.

Only ``category = ...`` lines are rewritten (every one in the file, keeping the quote
style); a model with none gets one after its first ``icon_id`` line.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.gallery import CATEGORY_ALIASES  # noqa: E402

MODELS = REPO_ROOT / 'icon_set' / 'model' / 'icons'
FAMILIES = ('solo', 'sub', 'symbol', 'container', 'combination_main')
GENERATED = 'primitives-generate'
UNCATEGORIZED = 'Uncategorized'
CATALOG = REPO_ROOT / 'published' / 'gallery' / 'primitives.json'
TYPE_TOKENS = {'primitive', 'primitives', GENERATED, 'other', 'combination', 'side-combination',
               'container-combination'}
POSITION_TOKENS = {'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right'}
ROLE_TOKENS = ('symbol', 'state', 'container', 'text', 'typeface', 'combination')
CATEGORY_LINE = re.compile(r'''^(?P<indent>[ \t]+)category\s*=\s*(?P<q>['"])(?P<value>.*?)(?P=q)[ \t]*$''', re.M)
ICON_ID_LINE = re.compile(r'''^(?P<indent>[ \t]+)icon_id\s*=.*$''', re.M)
SOURCE_ID = re.compile(r'''^SOURCE_ICON_ID\s*=\s*['"]([^'"]*)['"]''', re.M)


def pictoicon_categories(path: Path) -> dict[str, list[str]]:
    return {str(r['id']).lower(): str(r.get('categories') or '').split()
            for r in json.loads(path.read_text(encoding='utf-8'))}


def category_from_tokens(tokens: list[str]) -> str | None:
    """The one model category a pictoicon categories string stands for."""
    topics = [t for t in tokens if t not in TYPE_TOKENS | POSITION_TOKENS and t not in ROLE_TOKENS]
    if topics:
        return topics[0]
    present = set(tokens)
    if present & {'other', GENERATED}:
        return GENERATED
    return next((t for t in ROLE_TOKENS if t in present), None)


def valid_categories(catalog: Path = CATALOG) -> set[str]:
    return set(json.loads(catalog.read_text(encoding='utf-8'))['categories'])


def resolve(uuid: str, current: str | None, records: dict[str, list[str]],
            valid: set[str]) -> tuple[str | None, str]:
    """(category, how) for a model; category None means leave it alone."""
    if uuid and uuid in records:
        category = category_from_tokens(records[uuid])
        if category:
            return category, 'pictoicon'
        return (current, 'kept') if current in valid else (UNCATEGORIZED, 'pictoicon has no topic or type')
    if current in valid:
        return current, 'kept'
    alias = CATEGORY_ALIASES.get(current or '') or {'containers': 'container'}.get(current or '')
    if alias:
        return alias, 'alias'
    return None, 'no pictoicon record' if uuid else 'no SOURCE_ICON_ID'


def rewrite(text: str, category: str) -> str:
    if CATEGORY_LINE.search(text):
        return CATEGORY_LINE.sub(lambda m: f"{m['indent']}category = {m['q']}{category}{m['q']}", text)
    match = ICON_ID_LINE.search(text)
    if not match:
        return text
    return text[:match.end()] + f"\n{match['indent']}category = '{category}'" + text[match.end():]


def model_files(root: Path):
    for family in FAMILIES:
        for path in sorted((root / family).glob('*.py')):
            if path.name == '__init__.py' or (path.name.startswith('_') and not path.name.startswith('_draft')):
                continue
            yield family, path


def run(root: Path, records: dict[str, list[str]], valid: set[str], report: Path,
        apply: bool) -> collections.Counter:
    counts, rows = collections.Counter(), []
    for family, path in model_files(root):
        text = path.read_text(encoding='utf-8')
        source = SOURCE_ID.search(text)
        uuid = source.group(1).lower() if source else ''
        currents = [m['value'] for m in CATEGORY_LINE.finditer(text)]
        current = currents[0] if currents else None
        category, how = resolve(uuid, current, records, valid)
        if category is None:
            status = 'unresolved'
        elif all(c == category for c in currents) and currents:
            status = 'unchanged'
        else:
            status = 'changed'
            new_text = rewrite(text, category)
            if new_text == text:
                status = 'unresolved'
                how = 'no category or icon_id line'
            elif apply:
                path.write_text(new_text, encoding='utf-8')
        counts[status] += 1
        if status != 'unchanged':
            rows.append({'file': str(path.relative_to(root)), 'family': family, 'source_icon_id': uuid,
                         'old_category': ' | '.join(currents), 'new_category': category or '', 'status': status,
                         'how': how})
    with report.open('w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=['file', 'family', 'source_icon_id', 'old_category', 'new_category',
                                                'status', 'how'])
        writer.writeheader()
        writer.writerows(rows)
    return counts


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--pictoicons', type=Path, default=REPO_ROOT / 'pictoicons.json')
    parser.add_argument('--models', type=Path, default=MODELS)
    parser.add_argument('--catalog', type=Path, default=CATALOG, help='primitives.json with the valid categories')
    parser.add_argument('--report', type=Path, default=REPO_ROOT / 'model-category-changes.csv')
    parser.add_argument('--apply', action='store_true', help='rewrite the model files (default: dry run)')
    args = parser.parse_args(argv)
    counts = run(args.models, pictoicon_categories(args.pictoicons), valid_categories(args.catalog), args.report,
                 args.apply)
    print(('applied' if args.apply else 'dry run') + f' -> {args.report}')
    for status, n in counts.most_common():
        print(f'  {n:6d}  {status}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
