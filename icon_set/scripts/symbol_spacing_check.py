"""Check every SYMBOL32 icon (container symbols) against a stricter spacing rule.

The SYMBOL32 contract allows 2 units of ink clearance (centerline 6 with
stroke 4). This audit raises the requirement in-process only -- the contract
is not changed -- and lists every symbol that does not keep the gap:

    /opt/homebrew/bin/python3 icon_set/scripts/symbol_spacing_check.py
    /opt/homebrew/bin/python3 icon_set/scripts/symbol_spacing_check.py --gap 4 --out DIR --overlays

Text symbols are skipped: sources marked text_number in
icon_set/data/container-text-v2.json and source-native text modules.
Two checks are run at the raised minimum: the validator's MIC check (certified
centerline distance between separate strokes, plus parallel straight runs) and
the sampled internal-spacing review (opposing edges of one connected shape).
Earlier spacing reviews are ignored on purpose; they were judged at 2 units.

Writes report.json and report.csv to --out; exits 1 when any symbol fails.
"""
from __future__ import annotations

import argparse
import csv
import dataclasses
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

TEXT_LIST = REPO_ROOT / 'icon_set/data/container-text-v2.json'
AT_LIMIT = 0.01  # a gap this close to the minimum is the minimum (curve sampling error)
UUID = re.compile(r'[0-9a-f]{8}[_-][0-9a-f]{4}[_-][0-9a-f]{4}[_-][0-9a-f]{4}[_-][0-9a-f]{12}')


def raise_symbol_minimum(gap: int) -> None:
    """Make SYMBOL32 require `gap` units of ink clearance for this process."""
    from icon_set.model.profiles import Profile, STROKE_WIDTH
    spec = Profile.SYMBOL32.value
    object.__setattr__(spec, 'mic', gap)
    object.__setattr__(spec, 'equal_stroke_centerline_min', gap + STROKE_WIDTH)
    from icon_set.validation import parallel_straight
    parallel_straight.RULES['profile_overrides']['SYMBOL32'] = {
        'required_centerline_distance': gap + STROKE_WIDTH, 'required_ink_clearance': gap}


def text_source_ids() -> set[str]:
    data = json.loads(TEXT_LIST.read_text())
    return {item['source_id'] for item in data['icons']}


def source_id(icon) -> str | None:
    match = UUID.search(type(icon).__module__)
    return match.group(0).replace('_', '-') if match else None


def check(icon, gap: int, overlay_dir: Path | None) -> dict:
    from icon_set.model.profiles import STROKE_WIDTH
    from icon_set.validation.validator import IconValidator
    from icon_set.validation.internal_spacing import analyze_internal_spacing, internal_overlay

    row = {'icon_id': icon.icon_id, 'source_id': source_id(icon),
           'module': type(icon).__module__.rsplit('.', 1)[-1],
           'spacing': [], 'other_errors': []}
    report = IconValidator(require_free_approval=False).validate(icon)
    errors = set(report.errors)
    for finding in report.findings:
        if finding.check != 'mic':
            if str(finding) in errors:
                row['other_errors'].append(str(finding))
            continue
        detail = finding.detail or {}
        distance = detail.get('centerlineDistance', detail.get('centerline_distance'))
        ink = detail.get('ink_gap')
        if ink is None and isinstance(distance, (int, float)):
            ink = distance - STROKE_WIDTH
        points = detail.get('nearestPoints') or (
            [detail['start'], detail['end']] if 'start' in detail and 'end' in detail else None)
        if isinstance(ink, (int, float)) and ink >= gap - AT_LIMIT:
            continue  # exactly at the minimum; the engine reports that as review
        row['spacing'].append({'check': 'mic', 'ink_gap': _round(ink), 'points': _points(points),
                               'message': finding.message})

    try:
        drawing = icon.draw()
        internal = analyze_internal_spacing(icon, drawing)
    except (ValueError, TypeError, AttributeError, KeyError) as error:
        internal = {'findings': []}
        row['other_errors'].append(f'internal-spacing could not run: {error}')
    for finding in internal['findings']:
        if finding.get('ink_gap', -1) >= gap - AT_LIMIT:
            continue
        first, second = finding['elements']
        row['spacing'].append({
            'check': 'internal-spacing', 'ink_gap': _round(finding.get('ink_gap')),
            'points': _points(finding.get('nearest_points')),
            'message': f"[{finding['contour']}] {first} and {second}: "
                       f"{finding['ink_gap']:g} ink over {finding['sustained_length']:g} units"})
        if overlay_dir is not None:
            overlay_dir.mkdir(parents=True, exist_ok=True)
            (overlay_dir / f'{icon.icon_id}.svg').write_text(internal_overlay(icon, drawing, internal))

    gaps = [s['ink_gap'] for s in row['spacing'] if isinstance(s['ink_gap'], (int, float))]
    row['min_ink_gap'] = min(gaps) if gaps else None
    # "new" = met the old 2-unit rule but not the raised one.
    row['status'] = 'pass' if not row['spacing'] else (
        'fail-new' if len(gaps) == len(row['spacing']) and min(gaps) >= 2 - 0.01 else 'fail')
    return row


def _points(points):
    """Two (x, y) points where the strokes come too close, or None."""
    try:
        return [[round(float(p[0]), 3), round(float(p[1]), 3)] for p in points][:2] if points else None
    except (TypeError, ValueError, IndexError, KeyError):
        try:
            return [[round(float(p.x), 3), round(float(p.y), 3)] for p in points][:2]
        except AttributeError:
            return None


def _round(value):
    return round(value, 3) if isinstance(value, (int, float)) else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--gap', type=int, default=4, help='required ink clearance in units (default 4)')
    parser.add_argument('--out', type=Path, default=REPO_ROOT / 'icon_set/work/symbol-spacing-check')
    parser.add_argument('--overlays', action='store_true', help='write internal-spacing overlay SVGs')
    parser.add_argument('--include-text', action='store_true', help='also check text symbols')
    parser.add_argument('ids', nargs='*', help='only these icon ids')
    args = parser.parse_args()

    raise_symbol_minimum(args.gap)
    from icon_set.model.icons import registry

    text_ids = set() if args.include_text else text_source_ids()
    rows, skipped = [], []
    for icon_id, factory in sorted(registry.factories().items()):
        if args.ids and icon_id not in args.ids:
            continue
        icon = factory()
        if icon.family != 'symbol':
            continue
        if not args.include_text and (
                source_id(icon) in text_ids
                or getattr(icon, 'sizing_mode', None) == 'text-source-native-v2'):
            skipped.append(icon_id)
            continue
        rows.append(check(icon, args.gap, args.out / 'overlays' if args.overlays else None))

    failed = [r for r in rows if r['status'] != 'pass']
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / 'report.json').write_text(json.dumps({
        'required_ink_gap': args.gap, 'checked': len(rows), 'failed': len(failed),
        'skipped_text': skipped, 'icons': rows}, indent=1))
    with (args.out / 'report.csv').open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(['icon_id', 'source_id', 'status', 'min_ink_gap', 'findings', 'other_errors', 'module'])
        for r in rows:
            writer.writerow([r['icon_id'], r['source_id'], r['status'], r['min_ink_gap'],
                             ' | '.join(s['message'] for s in r['spacing']),
                             ' | '.join(r['other_errors']), r['module']])

    for r in failed:
        print(f"FAIL {r['icon_id']}  min gap {r['min_ink_gap']}  ({len(r['spacing'])} finding(s))")
    new = sum(r['status'] == 'fail-new' for r in rows)
    print(f"\n{len(rows)} symbols checked at {args.gap}-unit clearance, {len(skipped)} text symbols skipped")
    print(f"{len(rows) - len(failed)} pass, {len(failed)} fail ({new} passed the 2-unit rule but fail {args.gap})")
    print(f"report: {args.out / 'report.json'}  {args.out / 'report.csv'}")
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
