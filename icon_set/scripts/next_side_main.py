#!/usr/bin/env python3
"""Write the next missing side-combination main as a short text input, without the gallery server.

Reads the staged side-components.json (the data behind gallery/side-mains.html and
side-subs.html) and takes components whose status is "missing", in the pages' default
order (most pair uses first). Subs marked text/number in the review database are left
out, as the side-subs page shows them in its own Text bucket. Standalone attempts with a
saved result are also excluded, regardless of validation, without changing the catalog
or review database. next_side_sub.py runs the same retrieval for subs.

    python3 icon_set/scripts/next_side_main.py                                 # print the next missing main
    python3 icon_set/scripts/next_side_main.py --offset 1 --out side-main-input-2.txt
    python3 icon_set/scripts/next_side_main.py --uuid <uuid>
"""
import argparse
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))
from icon_set.scripts.workspace import (  # noqa: E402
    DEFAULT_DATABASE, DEFAULT_DIST, side_main_results_dir, side_sub_results_dir)
from icon_set.scripts.next_icon import completed_result_sources, load_decisions  # noqa: E402

# Two combinations are enough to show which part is the component; more only costs tokens.
CONTEXT_LIMIT = 2
ROLES = {'main': ('mains', side_main_results_dir), 'sub': ('subs', side_sub_results_dir)}


def _ids(item):
    return {item['id'].lower(), *(uid.lower() for uid in item.get('source_ids') or [])}


def text_marked(item, statuses):
    return any(statuses.get(uid, {}).get('reason') == 'text_number'
               for uid in [item['id'], *(item.get('source_ids') or [])])


def missing_components(items, completed, statuses=None):
    """Missing items in file order, minus text marks and any whose id or alias has a saved attempt."""
    statuses = statuses or {}
    return [item for item in items
            if item.get('status') == 'missing' and not text_marked(item, statuses)
            and not _ids(item) & completed]


def missing_mains(components, completed):
    return missing_components(components['mains'], completed)


def reference_for(item, root=REPO_ROOT, dist=DEFAULT_DIST):
    """The component's primitive SVG, falling back to its combination-original render."""
    candidates = []
    if item.get('source_path'):
        candidates.append(Path(root) / item['source_path'])
    if item.get('reference_url'):
        candidates.append(Path(dist) / 'gallery' / item['reference_url'])
    return next((path for path in candidates if path.is_file()), None)


def describe(item, reference, root=REPO_ROOT, dist=DEFAULT_DIST):
    def shown(path):
        path = Path(path)
        return path.relative_to(root) if path.is_relative_to(root) else path
    source_path = item.get('source_path') or ''
    category = Path(source_path).parent.name if source_path else ''
    aliases = sorted(uid for uid in item.get('source_ids') or [] if uid != item['id'])
    originals = Path(dist) / 'gallery' / 'combination-originals'
    lines = [f"concept: {item['concept']}",
             f"source UUID: {item['id']}",
             f"reference: {shown(reference)}",
             f"category: {category}",
             f"aliases: {', '.join(aliases) if aliases else 'none'}",
             f"uses: {item.get('uses', 0)}",
             'combination context:']
    lines += [f"- {shown(originals / (pair['id'] + '.svg'))} — {pair['concept']}"
              for pair in (item.get('pairs') or [])[:CONTEXT_LIMIT]]
    return '\n'.join(lines) + '\n'


def main(argv=None, *, role='main', root=REPO_ROOT, dist=DEFAULT_DIST, results=None,
         database=DEFAULT_DATABASE):
    key, results_dir = ROLES[role]
    parser = argparse.ArgumentParser(description=f'Write the next missing side-combination {role}.')
    parser.add_argument('--offset', type=int, default=0, help=f'skip this many missing {key}')
    parser.add_argument('--uuid', help=f'use this {role} instead of the next missing one')
    parser.add_argument('--out', type=Path, help='write the text here instead of printing it')
    args = parser.parse_args(argv)
    if args.offset < 0:
        parser.error('--offset must be nonnegative')

    staged = Path(dist) / 'gallery' / 'side-components.json'
    if not staged.is_file():
        sys.exit(f'error: {staged} missing; rebuild it with python3 -m icon_set.scripts.side_components')
    items = json.loads(staged.read_text(encoding='utf-8'))[key]
    statuses = {}
    if role == 'sub':
        statuses, _, has_database = load_decisions(Path(database))
        if not has_database:
            print(f'warning: no database at {database}; text/number marks not applied', file=sys.stderr)
    completed = completed_result_sources(results if results is not None else results_dir(root))
    if args.uuid:
        uid = args.uuid.lower()
        rows = [item for item in items if uid in _ids(item)]
        if not rows:
            sys.exit(f'error: unknown side {role} {args.uuid}')
        item = rows[0]
        if _ids(item) & completed:
            sys.exit(f'error: {args.uuid} already has a saved standalone attempt and result')
        if item.get('status') != 'missing':
            sys.exit(f"error: {args.uuid} is {item.get('status')}, not missing")
        if text_marked(item, statuses):
            sys.exit(f'error: {args.uuid} is marked text/number')
    else:
        rows = missing_components(items, completed, statuses)
        if not rows:
            sys.exit(f'error: no missing side {key} remain')
        if args.offset >= len(rows):
            sys.exit(f'error: only {len(rows)} missing side {key}')
        item = rows[args.offset]

    reference = reference_for(item, root, dist)
    if reference is None:
        sys.exit(f"error: reference SVG missing for {item['id']}")
    text = describe(item, reference, root, dist)
    if args.out:
        args.out.write_text(text, encoding='utf-8')
        print(f'wrote {args.out}')
    else:
        print(text, end='')
    return 0


if __name__ == '__main__':
    sys.exit(main())
