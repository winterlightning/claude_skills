#!/usr/bin/env python3
"""Strict 32x32 gate, fix scaffolding and blocker records for /fix-icon-sub.

    python3 icon_set/scripts/fix_icon_sub.py check --icon airplane-horizontal-sub32
    python3 icon_set/scripts/fix_icon_sub.py scaffold --icon airplane-horizontal-sub32 \
        --label "SUB32 fix: wing clearance" --author claude-opus-5-5
    python3 icon_set/scripts/fix_icon_sub.py record --icon airplane-horizontal-sub32 \
        --status cannot-fix --author claude-opus-5-5 --blocker "mic: ..." --attempt "..." --attempt "..."
    python3 icon_set/scripts/fix_icon_sub.py check --source 952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9
    python3 icon_set/scripts/fix_icon_sub.py backlog --jobs 6
    python3 icon_set/scripts/fix_icon_sub.py list --status cannot-fix

`check` passes only a plain SUB32 drawing: the library QA row is `pass`
(validate_icon with no warnings, symmetry, spacing, internal spacing and
negative space), the canvas is exactly 32x32 and every stroke is 4. Larger
canvases, compact 2px strokes and FREE keyshapes are reported as failures here
even when an approved exception lets them publish elsewhere.

`record` writes the outcome into the icon's own Python module as
``SUB32_FIX_RECORDS[<icon-id>]``; it never touches geometry.
"""
from __future__ import annotations

import argparse
import ast
from datetime import date
import inspect
import json
from pathlib import Path
import pprint
import re
import sys
import xml.etree.ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from functools import lru_cache  # noqa: E402

from icon_set.model.icons.registry import create, factories as _factories  # noqa: E402


@lru_cache(maxsize=None)
def factories():
    return _factories()

RECORDS = 'SUB32_FIX_RECORDS'
STATUSES = ('fixed', 'cannot-fix')
SUB_DIR = REPO_ROOT / 'icon_set' / 'model' / 'icons' / 'sub'


def module_path(icon_id: str) -> Path:
    factory = factories()[icon_id]
    return Path(inspect.getsourcefile(factory)).resolve()


def module_value(path: Path, name: str):
    for node in ast.parse(path.read_text(encoding='utf-8')).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            try:
                return ast.literal_eval(node.value)
            except ValueError:
                return None
    return None


def sub_models_by_source() -> dict[str, list[str]]:
    """Source UUID -> every registered sub icon drawn from it."""
    groups: dict[str, list[str]] = {}
    for icon_id, factory in factories().items():
        if factory.family == 'sub':
            source = module_value(module_path(icon_id), 'SOURCE_ICON_ID')
            if source:
                groups.setdefault(str(source), []).append(icon_id)
    return {source: sorted(ids) for source, ids in groups.items()}


def expand_icons(icons, sources) -> list[str]:
    ids = list(icons or [])
    if sources:
        groups = sub_models_by_source()
        for source in sources:
            if source not in groups:
                raise SystemExit(f'error: no sub icon has SOURCE_ICON_ID {source}')
            ids.extend(i for i in groups[source] if i not in ids)
    if not ids:
        raise SystemExit('error: give --icon and/or --source')
    return ids


def strict_check(icon_id: str) -> dict:
    """Return the full library QA row plus the plain-SUB32 conditions."""
    from icon_set.validation.library_qa import inspect_icon
    from icon_set.model.icons.sub._text_base import canvas_dimensions

    icon = create(icon_id)
    row = inspect_icon(icon)
    problems = []
    if str(icon.family) != 'sub' or getattr(icon.profile, 'name', '') != 'SUB32':
        problems.append(f'family/profile is {icon.family}/{getattr(icon.profile, "name", icon.profile)}, not sub/SUB32')
    try:
        width, height = canvas_dimensions(icon)
    except Exception as error:  # a broken text canvas is a failure, not a crash
        width = height = None
        problems.append(f'canvas: {error}')
    if (width, height) != (32, 32):
        problems.append(f'canvas: {width}x{height}; the fix must fit a 32x32 canvas')
    if getattr(icon.keyshape, 'name', '') == 'FREE':
        problems.append('keyshape: FREE; choose a real SUB32 keyshape')
    document = row.pop('_svg', None) or icon.to_svg()
    root = ET.fromstring(document)
    if (root.get('width'), root.get('height'), root.get('viewBox')) != ('32', '32', '0 0 32 32'):
        problems.append(f"svg root: width={root.get('width')} height={root.get('height')} viewBox={root.get('viewBox')}")
    widths = {element.get('stroke-width') for element in root.iter() if element.get('stroke-width') is not None}
    if widths - {'4'}:
        problems.append(f'stroke: widths {sorted(widths)}; every stroke must be 4')
    if row.get('warnings') and row['status'] == 'pass':
        problems.append('warnings present; a warning is not a pass')
    errors = list(row.get('errors', [])) + list(row.get('warnings', [])) + problems
    return {
        'icon_id': icon_id,
        'module': str(module_path(icon_id).relative_to(REPO_ROOT)),
        'source_icon_id': module_value(module_path(icon_id), 'SOURCE_ICON_ID'),
        'source_path': module_value(module_path(icon_id), 'SOURCE_PATH'),
        'keyshape': getattr(icon.keyshape, 'name', str(icon.keyshape)),
        'qa_status': row.get('automatic_status', row['status']),
        'strict_32': 'pass' if row.get('automatic_status', row['status']) == 'pass' and not problems else 'fail',
        'failures': errors,
    }


def cmd_check(args) -> int:
    results = [strict_check(icon_id) for icon_id in expand_icons(args.icon, args.source)]
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            print(f"{result['icon_id']}: strict-32 {result['strict_32']} (qa {result['qa_status']}, "
                  f"keyshape {result['keyshape']})")
            print(f"  module: {result['module']}")
            print(f"  source: {result['source_icon_id']}  {result['source_path']}")
            for message in result['failures']:
                print(f'  - {message}')
    return 0 if all(r['strict_32'] == 'pass' for r in results) else 1


def cmd_scaffold(args) -> int:
    """create_variant.py, plus the source-UUID filename and your AUTHOR."""
    from icon_set.scripts.create_variant import prepare_variant

    _, new_id, text = prepare_variant(args.icon, 'sub', args.label)
    source_id = module_value(module_path(args.icon), 'SOURCE_ICON_ID')
    stem = new_id.replace('-', '_')
    if source_id:
        stem += '_' + re.sub(r'[^0-9A-Za-z]+', '_', str(source_id)).strip('_').lower()
    destination = SUB_DIR / f'{stem}.py'
    text, count = re.subn(r"(?m)^AUTHOR = .*$", f'AUTHOR = {args.author!r}', text)
    if not count:
        raise SystemExit(f'error: {args.icon} has no module-level AUTHOR to update')
    # The parent's fix records describe the parent, not this new drawing.
    tree = ast.parse(text)
    tree.body = [node for node in tree.body if not (
        isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == RECORDS for t in node.targets))]
    header = text.split('\n', 1)[0] + '\n'
    text = header + ast.unparse(tree) + '\n'
    compile(text, str(destination), 'exec')
    with destination.open('x', encoding='utf-8') as file:
        file.write(text)
    print(f'New variant: {new_id}\nPython file: {destination.relative_to(REPO_ROOT)}\nParent preserved: {args.icon}')
    return 0


def write_record(path: Path, icon_id: str, record: dict) -> None:
    text = path.read_text(encoding='utf-8')
    tree = ast.parse(text)
    records, node = {}, None
    for candidate in tree.body:
        if isinstance(candidate, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == RECORDS for t in candidate.targets):
            node, records = candidate, ast.literal_eval(candidate.value)
    records[icon_id] = record
    block = f'{RECORDS} = ' + pprint.pformat(records, width=100, sort_dicts=False) + '\n'
    lines = text.splitlines(keepends=True)
    if node is None:
        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'
        lines.append('\n# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.\n' + block)
    else:
        lines[node.lineno - 1:node.end_lineno] = [block]
    updated = ''.join(lines)
    compile(updated, str(path), 'exec')
    path.write_text(updated, encoding='utf-8')


def cmd_record(args) -> int:
    path = module_path(args.icon)
    result = strict_check(args.icon)
    if args.status == 'fixed':
        if not args.variant:
            raise SystemExit('error: --status fixed needs --variant <passing-icon-id>')
        if strict_check(args.variant)['strict_32'] != 'pass':
            raise SystemExit(f'error: {args.variant} does not pass the strict 32x32 gate; record cannot-fix instead')
    elif not args.blocker or len(args.attempt) < 2:
        raise SystemExit('error: cannot-fix needs --blocker and at least two --attempt descriptions')
    record = {
        'status': args.status,
        'date': date.today().isoformat(),
        'author': args.author,
        'source_icon_id': result['source_icon_id'],
        'failures_at_review': result['failures'],
    }
    if args.variant:
        record['variant'] = args.variant
    if args.blocker:
        record['blocker'] = args.blocker
    if args.attempt:
        record['attempts'] = list(args.attempt)
    if args.evidence:
        record['evidence'] = args.evidence
    write_record(path, args.icon, record)
    print(f'{args.icon}: recorded {args.status} in {path.relative_to(REPO_ROOT)}')
    return 0


def _safe_check(icon_id):
    try:
        return strict_check(icon_id)
    except Exception as error:  # one broken module must not stop the audit
        return {'icon_id': icon_id, 'strict_32': 'fail', 'qa_status': 'error',
                'failures': [f'{type(error).__name__}: {error}']}


def cmd_backlog(args) -> int:
    """Group failing sub icons by original and strict-check every sub model of each."""
    from concurrent.futures import ProcessPoolExecutor

    groups = sub_models_by_source()
    failed_path = REPO_ROOT / 'published' / 'failed' / 'sub32' / 'manifest.json'
    failed = {row['icon_id'] for row in json.loads(failed_path.read_text())['icons']}
    selected = {s: ids for s, ids in groups.items() if args.all or failed & set(ids)}
    icon_ids = sorted({i for ids in selected.values() for i in ids})
    print(f'{len(selected)} originals, {len(icon_ids)} sub models to check', file=sys.stderr)
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        results = {r['icon_id']: r for r in pool.map(_safe_check, icon_ids, chunksize=4)}
    originals = []
    for source, ids in sorted(selected.items()):
        passing = [i for i in ids if results[i]['strict_32'] == 'pass']
        originals.append({
            'source_icon_id': source,
            'source_path': next((results[i].get('source_path') for i in ids if results[i].get('source_path')), None),
            'state': 'has-strict-pass' if passing else 'needs-fix',
            'passing': passing,
            'failing': {i: results[i]['failures'] for i in ids if i not in passing},
        })
    summary = {state: sum(o['state'] == state for o in originals) for state in ('has-strict-pass', 'needs-fix')}
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({'date': date.today().isoformat(), 'summary': summary,
                               'originals': originals}, indent=2), encoding='utf-8')
    print(json.dumps(summary))
    print(f'backlog -> {out}')
    return 0


def cmd_list(args) -> int:
    for path in sorted(SUB_DIR.glob('*.py')):
        if RECORDS not in path.read_text(encoding='utf-8'):
            continue
        for icon_id, record in (module_value(path, RECORDS) or {}).items():
            if args.status and record.get('status') != args.status:
                continue
            detail = record.get('variant') or record.get('blocker', '')
            print(f"{record.get('status'):10} {icon_id}  {detail}")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    check = sub.add_parser('check', help='run the strict 32x32 gate on one or more icons')
    check.add_argument('--icon', action='append')
    check.add_argument('--source', action='append', help='source UUID; checks every sub model drawn from it')
    check.add_argument('--json', action='store_true')
    scaffold = sub.add_parser('scaffold', help='create the fix variant file')
    scaffold.add_argument('--icon', required=True)
    scaffold.add_argument('--label', required=True)
    scaffold.add_argument('--author', required=True)
    record = sub.add_parser('record', help='write the fix outcome into the icon module')
    record.add_argument('--icon', required=True, help='the reviewed (failing) icon')
    record.add_argument('--status', choices=STATUSES, required=True)
    record.add_argument('--author', required=True)
    record.add_argument('--variant', help='the passing fix variant (status fixed)')
    record.add_argument('--blocker', help='check, element and why no meaning-preserving redraw passes')
    record.add_argument('--attempt', action='append', default=[], help='one tried redesign and the failure it hit')
    record.add_argument('--evidence', help='repo-relative folder holding the review evidence')
    backlog = sub.add_parser('backlog', help='strict-check every sub model of each failing original')
    backlog.add_argument('--out', default='icon_set/work/fix-icon-sub/backlog.json')
    backlog.add_argument('--jobs', type=int, default=6)
    backlog.add_argument('--all', action='store_true', help='include originals with no failing sub model')
    listing = sub.add_parser('list', help='list recorded outcomes')
    listing.add_argument('--status', choices=STATUSES)
    args = parser.parse_args(argv)
    return {'check': cmd_check, 'scaffold': cmd_scaffold, 'record': cmd_record, 'backlog': cmd_backlog, 'list': cmd_list}[args.command](args)


if __name__ == '__main__':
    raise SystemExit(main())
