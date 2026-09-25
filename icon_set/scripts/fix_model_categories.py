#!/usr/bin/env python3
"""Set every Python icon model's categories from its source pictoicon record.

python3 -m icon_set.scripts.fix_model_categories --check    # detect only; exit 1 if anything needs work
python3 -m icon_set.scripts.fix_model_categories            # dry run, writes the report
python3 -m icon_set.scripts.fix_model_categories --apply    # rewrites models and metadata
python3 -m icon_set.scripts.fix_model_categories --set <uuid>=<category> [--set ...] --apply

Run it after new models are authored or pictoicons.json is refreshed, then rebuild
(icon_set/scripts/build.py) so the gallery shows the new categories. Icons whose record
has no topic are listed as "needs a concept category": pick one from the concept name and
record it with --set (stored in data/concept-categories.json, which rebuilds keep).

An icon can belong to several categories. ``categories`` holds every token of the
``SOURCE_ICON_ID`` pictoicon record (``('health', 'state', 'primitives')``); ``category``
stays the single primary one pages group by:

* the record's first topic token (``food``), else its type: ``other`` /
  ``primitives-generate`` -> ``primitives-generate``, else the first of ``symbol``,
  ``state``, ``container``, ``text``, ``typeface``, ``combination``; a record with only
  ``primitive``/``primitives`` takes its concept-name category from
  data/concept-categories.json (put first in ``categories``), else keeps a valid category
  or becomes ``Uncategorized``;
* a model with no pictoicon record keeps a valid catalog category or gets its
  gallery.CATEGORY_ALIASES spelling, and ``categories`` is just that one.

Anything left unresolved is reported and left as it is. In a model only ``category`` and
``categories`` lines change (every class in the file, keeping the quote style); a model
with no ``category`` line gets both after its first ``icon_id`` line. The editable
metadata sidecar (icon_set/metadata/<family>/<icon_id>.json), which the build publishes
over the model, gets the same two fields; the registry says which model file owns each
icon_id, because a helper class can reuse another model's id.
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
METADATA = REPO_ROOT / 'icon_set' / 'metadata'
CATALOG = REPO_ROOT / 'published' / 'gallery' / 'primitives.json'
CONCEPT_CATEGORIES = REPO_ROOT / 'icon_set' / 'data' / 'concept-categories.json'
PICTOICONS = next((p for p in (REPO_ROOT / 'pictoicons.fixed.json', REPO_ROOT / 'pictoicons.json') if p.exists()),
                  REPO_ROOT / 'pictoicons.json')
FAMILIES = ('solo', 'sub', 'symbol', 'container', 'combination_main')
GENERATED = 'primitives-generate'
UNCATEGORIZED = 'Uncategorized'
TYPE_TOKENS = {'primitive', 'primitives', GENERATED, 'other', 'combination', 'side-combination',
               'container-combination'}
POSITION_TOKENS = {'top', 'bottom', 'left', 'right', 'top-left', 'top-right', 'bottom-left', 'bottom-right'}
ROLE_TOKENS = ('symbol', 'state', 'container', 'text', 'typeface', 'combination')
CATEGORY_LINE = re.compile(r'''^(?P<indent>[ \t]+)category\s*=\s*(?P<q>['"])(?P<value>.*?)(?P=q)[ \t]*$''', re.M)
CATEGORIES_LINE = re.compile(r'''^[ \t]+categories\s*=\s*\(.*?\)[ \t]*\n''', re.M)
ICON_ID_LINE = re.compile(r'''^(?P<indent>[ \t]+)icon_id\s*=\s*['"](?P<value>[^'"]*)['"].*$''', re.M)
SOURCE_ID = re.compile(r'''^SOURCE_ICON_ID\s*=\s*['"]([^'"]*)['"]''', re.M)


def pictoicon_categories(path: Path) -> dict[str, list[str]]:
    return {str(r['id']).lower(): list(dict.fromkeys(str(r.get('categories') or '').split()))
            for r in json.loads(path.read_text(encoding='utf-8'))}


def category_from_tokens(tokens: list[str]) -> str | None:
    """The primary model category a pictoicon categories string stands for."""
    topics = [t for t in tokens if t not in TYPE_TOKENS | POSITION_TOKENS and t not in ROLE_TOKENS]
    if topics:
        return topics[0]
    present = set(tokens)
    if present & {'other', GENERATED}:
        return GENERATED
    return next((t for t in ROLE_TOKENS if t in present), None)


def concept_categories(path: Path = CONCEPT_CATEGORIES) -> dict[str, str]:
    """uuid -> category chosen by concept name for records with no topic."""
    if not path.is_file():
        return {}
    entries = json.loads(path.read_text(encoding='utf-8'))['categories']
    return {uid.lower(): entry['category'] for uid, entry in entries.items()}


def set_concept_categories(assignments: list[str], path: Path, records: dict[str, dict],
                           valid: set[str]) -> list[str]:
    """Record ``uuid=category`` choices in data/concept-categories.json; returns the uuids set."""
    data = json.loads(path.read_text(encoding='utf-8')) if path.is_file() else {
        'source': 'chosen by concept name for primitives whose pictoicon record has no topic', 'categories': {}}
    done = []
    for assignment in assignments:
        uid, _, category = assignment.partition('=')
        uid, category = uid.strip().lower(), category.strip()
        if category not in valid:
            raise SystemExit(f'--set {assignment}: {category!r} is not a catalog category')
        if uid not in records:
            raise SystemExit(f'--set {assignment}: {uid} is not a pictoicon id')
        record = records[uid]
        data['categories'][uid] = {'category': category, 'concept': record.get('concept', ''),
                                   'old_concept': record.get('old_concept', '')}
        done.append(uid)
    data['categories'] = dict(sorted(data['categories'].items()))
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return done


def valid_categories(catalog: Path = CATALOG) -> set[str]:
    return set(json.loads(catalog.read_text(encoding='utf-8'))['categories'])


def resolve(uuid: str, current: str | None, records: dict[str, list[str]], valid: set[str],
            by_concept: dict[str, str] | None = None) -> tuple[str | None, tuple[str, ...], str]:
    """(category, categories, how) for a model; category None means leave it alone."""
    if uuid and uuid in records:
        tokens = tuple(records[uuid])
        category = category_from_tokens(records[uuid])
        if category:
            return category, tokens, 'pictoicon'
        if uuid in (by_concept or {}):
            chosen = by_concept[uuid]
            return chosen, (chosen, *(t for t in tokens if t != chosen)), 'concept name'
        if current in valid:
            return current, tokens, 'kept'
        return UNCATEGORIZED, tokens, 'pictoicon has no topic or type'
    if current in valid:
        return current, (current,), 'kept'
    alias = CATEGORY_ALIASES.get(current or '') or {'containers': 'container'}.get(current or '')
    if alias:
        return alias, (alias,), 'alias'
    return None, (), 'no pictoicon record' if uuid else 'no SOURCE_ICON_ID'


def tuple_literal(values: tuple[str, ...], quote: str) -> str:
    items = ', '.join(f'{quote}{v}{quote}' for v in values)
    return f'({items},)' if len(values) == 1 else f'({items})'


def rewrite(text: str, category: str, categories: tuple[str, ...]) -> str:
    text = CATEGORIES_LINE.sub('', text)
    if CATEGORY_LINE.search(text):
        return CATEGORY_LINE.sub(
            lambda m: (f"{m['indent']}category = {m['q']}{category}{m['q']}\n"
                       f"{m['indent']}categories = {tuple_literal(categories, m['q'])}"), text)
    match = ICON_ID_LINE.search(text)
    if not match:
        return text
    return (text[:match.end()] + f"\n{match['indent']}category = '{category}'"
            f"\n{match['indent']}categories = {tuple_literal(categories, chr(39))}" + text[match.end():])


def update_metadata(path: Path, category: str, categories: tuple[str, ...], apply: bool) -> bool:
    """Give an existing metadata sidecar the model's categories; True when it changes."""
    if not path.exists():
        return False
    document = json.loads(path.read_text(encoding='utf-8'))
    if document.get('category') == category and document.get('categories') == list(categories):
        return False
    updated = {}
    for key, value in document.items():
        if key == 'categories':
            continue
        updated[key] = category if key == 'category' else value
        if key == 'category':
            updated['categories'] = list(categories)
    updated.setdefault('category', category)
    updated.setdefault('categories', list(categories))
    if apply:
        path.write_text(json.dumps(updated, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return True


def model_files(root: Path):
    for family in FAMILIES:
        for path in sorted((root / family).glob('*.py')):
            if path.name == '__init__.py' or (path.name.startswith('_') and not path.name.startswith('_draft')):
                continue
            yield family, path


def registered_files() -> dict[str, tuple[str, Path]]:
    """icon_id -> (family, model file) for every icon the registry builds."""
    from icon_set.model.icons import registry
    return {icon_id: (factory.family, Path(sys.modules[factory.__module__].__file__).resolve())
            for icon_id, factory in registry.factories().items()}


def run(root: Path, records: dict[str, list[str]], valid: set[str], report: Path, apply: bool,
        metadata: Path | None = None, registered: dict[str, tuple[str, Path]] | None = None,
        by_concept: dict[str, str] | None = None, needs_concept: list | None = None) -> collections.Counter:
    counts, rows, resolved = collections.Counter(), {}, {}
    for family, path in model_files(root):
        text = path.read_text(encoding='utf-8')
        source = SOURCE_ID.search(text)
        uuid = source.group(1).lower() if source else ''
        currents = [m['value'] for m in CATEGORY_LINE.finditer(text)]
        category, categories, how = resolve(uuid, currents[0] if currents else None, records, valid, by_concept)
        # A model with no source and no category line inherits its family default.
        status, metadata_changed = ('unresolved' if currents else 'inherits family default'), False
        if category is not None:
            new_text = rewrite(text, category, categories)
            if new_text == text:
                status = 'unchanged' if currents else 'unresolved'
                how = how if currents else 'no category or icon_id line'
            else:
                status = 'changed'
                if apply:
                    path.write_text(new_text, encoding='utf-8')
            if status != 'unresolved':
                resolved[path.resolve()] = (category, categories)
        counts[status] += 1
        if category == UNCATEGORIZED:
            counts['needs a concept category'] += 1
            if needs_concept is not None:
                needs_concept.append((uuid, str(path.relative_to(root))))
        rows[path.resolve()] = {'file': str(path.relative_to(root)), 'family': family, 'source_icon_id': uuid,
                                'old_category': ' | '.join(currents), 'new_category': category or '',
                                'categories': ' '.join(categories), 'status': status, 'how': how,
                                'metadata_changed': False}
    if metadata is not None:
        for icon_id, (family, path) in (registered_files() if registered is None else registered).items():
            sidecar = metadata / family / f'{icon_id}.json'
            target = resolved.get(path.resolve())
            if target is None and sidecar.exists():
                # No source record: only fix a misspelled category the sidecar was seeded with.
                current = json.loads(sidecar.read_text(encoding='utf-8')).get('category')
                category, categories, _ = resolve('', current, {}, valid)
                target = (category, categories) if category else None
            if target and update_metadata(sidecar, *target, apply):
                counts['metadata changed'] += 1
                if path.resolve() in rows:
                    rows[path.resolve()]['metadata_changed'] = True
    rows = [row for row in rows.values() if row['status'] != 'unchanged' or row['metadata_changed']]
    with report.open('w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=['file', 'family', 'source_icon_id', 'old_category', 'new_category',
                                                'categories', 'status', 'how', 'metadata_changed'])
        writer.writeheader()
        writer.writerows(rows)
    return counts


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--pictoicons', type=Path, default=PICTOICONS)
    parser.add_argument('--models', type=Path, default=MODELS)
    parser.add_argument('--metadata', type=Path, default=METADATA)
    parser.add_argument('--concept-categories', type=Path, default=CONCEPT_CATEGORIES)
    parser.add_argument('--catalog', type=Path, default=CATALOG, help='primitives.json with the valid categories')
    parser.add_argument('--report', type=Path, default=REPO_ROOT / 'model-category-changes.csv')
    parser.add_argument('--set', action='append', default=[], metavar='UUID=CATEGORY',
                        help='record a concept-name category for a record with no topic (repeatable)')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true', help='rewrite models and metadata (default: dry run)')
    mode.add_argument('--check', action='store_true', help='detect only; exit 1 when anything needs fixing')
    args = parser.parse_args(argv)
    rows = {str(r['id']).lower(): r for r in json.loads(args.pictoicons.read_text(encoding='utf-8'))}
    records = {uid: list(dict.fromkeys(str(r.get('categories') or '').split())) for uid, r in rows.items()}
    valid = valid_categories(args.catalog)
    if args.set:
        print(f'recorded {len(set_concept_categories(args.set, args.concept_categories, rows, valid))} '
              f'concept categories -> {args.concept_categories}')
    needs = []
    counts = run(args.models, records, valid, args.report, args.apply, args.metadata,
                 by_concept=concept_categories(args.concept_categories), needs_concept=needs)
    print(('applied' if args.apply else 'check' if args.check else 'dry run') + f' ({args.pictoicons.name}) -> {args.report}')
    for status, n in counts.most_common():
        print(f'  {n:6d}  {status}')
    if needs:
        print('needs a concept category (then run again with --set <uuid>=<category> --apply):')
        for uid, file in needs:
            record = rows.get(uid, {})
            print(f"  {uid}  {record.get('concept', '')!r} (was {record.get('old_concept', '')!r})  {file}")
    pending = counts['changed'] + counts['metadata changed'] + counts['needs a concept category']
    if args.check:
        print('categories are up to date' if not pending else f'{pending} fixes pending')
        return 1 if pending else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
