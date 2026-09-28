#!/usr/bin/env python3
"""Give every pictoicon record a type token in its ``categories``.

python3 -m icon_set.scripts.fix_pictoicon_categories [--input pictoicons.json]
    [--output pictoicons.fixed.json] [--report pictoicons-category-changes.csv]

A record's type is one of ``primitives``, ``primitives-generate``, ``side-combination``,
``container-combination`` or the role types ``symbol``, ``state``, ``container`` and ``text``
(which are not primitives). Rules, in order:

1. A combination type is left alone (combination + ``other`` is reported as skipped).
2. ``other`` is treated as generated: ``primitives-generate`` is added and ``other`` is kept.
3. A record with no type at all gets ``primitives``.

Topic and position tokens are never touched. The
input is left as is; the fixed records and a CSV of every change are written beside it.
The report also names the local profiles (SOLO48, SUB32 ...) built from each source.
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

PRIMITIVES = 'primitives'
GENERATED = 'primitives-generate'
COMBINATIONS = ('side-combination', 'container-combination')
ROLES = ('symbol', 'state', 'container', 'text')
TYPES = {PRIMITIVES, GENERATED, *COMBINATIONS, *ROLES}
OTHER = 'other'
UUID = re.compile(r'[0-9a-f]{8}[-_][0-9a-f]{4}[-_][0-9a-f]{4}[-_][0-9a-f]{4}[-_][0-9a-f]{12}')


def fix_categories(categories: str) -> tuple[str, str]:
    """Return (new categories, reason) for one record's categories string."""
    tokens = list(dict.fromkeys(str(categories or '').split()))
    present = set(tokens)
    if present & set(COMBINATIONS):
        return categories, 'skipped-combination-other' if OTHER in present else 'unchanged'
    if OTHER in present:
        wanted, reason = [GENERATED], 'other-generate'
    elif not present & TYPES:
        wanted, reason = [PRIMITIVES], 'added-primitives'
    else:
        return categories, 'unchanged'
    added = [t for t in wanted if t not in present]
    if not added:
        return categories, 'unchanged'
    return ' '.join(tokens + added), reason


def link_profiles(repo_root: Path = REPO_ROOT) -> dict[str, set[str]]:
    """Source uuid -> profiles of the published icons drawn from it."""
    catalog = repo_root / 'published' / 'gallery' / 'icons.json'
    if not catalog.exists():
        return {}
    data = json.loads(catalog.read_text(encoding='utf-8'))
    links = collections.defaultdict(set)
    for icon in data.get('icons', []) + data.get('failed_icons', []):
        text = f"{(icon.get('python_source') or {}).get('path', '')} {icon.get('original_sources', '')}"
        for uid in UUID.findall(text):
            links[uid.replace('_', '-')].add(icon.get('profile') or '?')
    return links


def run(input_path: Path, output_path: Path, report_path: Path, links: dict[str, set[str]]) -> collections.Counter:
    records = json.loads(input_path.read_text(encoding='utf-8'))
    counts, profiles, rows = collections.Counter(), collections.Counter(), []
    for record in records:
        old = record.get('categories') or ''
        new, reason = fix_categories(old)
        counts[reason] += 1
        if reason == 'unchanged':
            continue
        record['categories'] = new
        linked = sorted(links.get(str(record.get('id')).lower(), ()))
        for profile in linked:
            profiles[(reason, profile)] += 1
        rows.append({'id': record.get('id'), 'concept': record.get('concept'), 'old_categories': old,
                     'new_categories': new, 'reason': reason, 'linked_profiles': ' '.join(linked)})
    output_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with report_path.open('w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=['id', 'concept', 'old_categories', 'new_categories', 'reason',
                                                'linked_profiles'])
        writer.writeheader()
        writer.writerows(rows)
    untyped = [r.get('id') for r in records if not set(str(r.get('categories') or '').split()) & TYPES]
    print(f'{len(records)} records -> {output_path}')
    for reason, n in counts.most_common():
        print(f'  {n:6d}  {reason}')
    print('changed records by linked profile:')
    for (reason, profile), n in sorted(profiles.items()):
        print(f'  {n:6d}  {reason:26s} {profile}')
    print(f'{len(rows)} rows -> {report_path}')
    print(f'records still without a type: {len(untyped)}')
    for uid in untyped[:20]:
        print(f'  {uid}')
    counts['untyped'] = len(untyped)
    return counts


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--input', type=Path, default=REPO_ROOT / 'pictoicons.json')
    parser.add_argument('--output', type=Path, default=REPO_ROOT / 'pictoicons.fixed.json')
    parser.add_argument('--report', type=Path, default=REPO_ROOT / 'pictoicons-category-changes.csv')
    args = parser.parse_args(argv)
    if args.output.resolve() == args.input.resolve():
        parser.error('--output must differ from --input')
    counts = run(args.input, args.output, args.report, link_profiles())
    return 1 if counts['untyped'] else 0


if __name__ == '__main__':
    sys.exit(main())
