"""Mark region/group main variants that draw the same picture as the pair's current fill.

The current fill comes from the stroke-keeping main, so when a region or group variant renders
within --max-change px² of it (or differs only by hairlines under 0.6px wide), only the current one is shown (the user's rule, 2026-10-26). The
variant stays in the report with `duplicate_of: "current"`; the gallery hides it. A decision that
picked such a duplicate moves to the current variant, logged like rebind_ai_decisions.py.
A current fill the main-variant policy rejects never hides its alternatives.
"""

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from .adaptive_overlap import ROOT
from .combine_fill_side import load_fill

REPORT = WORK / 'recombined-all/report.json'
DECISIONS = DATA / 'data/ai-variant-decisions.json'
HISTORY = DATA / 'data/side-variant-selection-history.jsonl'
HAIRLINE = 0.3     # px: differences thinner than twice this everywhere are the same picture


def mark_row(row, folder, max_change=10.0):
    """Annotate one report row's duplicates in place; {variant: px²} of what was marked."""
    current = next((c for c in row['candidates'] if c['variant'] == 'current'), None)
    geometry, marked = None, {}
    for candidate in row['candidates']:
        candidate.pop('duplicate_of', None)
        candidate.pop('duplicate_px2', None)
        if (not current or current['semantic_status'] == 'rejected'
                or not candidate['variant'].startswith(('region-', 'group-'))):
            continue
        if geometry is None:
            geometry = load_fill(folder / current['svg'])[0]
        difference = geometry.symmetric_difference(load_fill(folder / candidate['svg'])[0])
        area = round(difference.area, 2)
        # A long hairline along an edge (stroke-fill vs flat-fill rounding) can add up past
        # max_change while drawing the same picture: nothing survives a 0.3px erosion.
        if area <= max_change or difference.buffer(-HAIRLINE).area <= .5:
            candidate.update(duplicate_of='current', duplicate_px2=area)
            marked[candidate['variant']] = area
    return marked


def mark(report_path=REPORT, max_change=10.0):
    """Annotate duplicates in the report in place; {pair: {variant: px²}} of what was marked."""
    report = json.loads(report_path.read_text())
    marked = {}
    for row in report['rows']:
        found = mark_row(row, report_path.parent, max_change)
        if found:
            marked[row['id']] = found
    temporary = report_path.with_name(report_path.name + '.tmp')
    temporary.write_text(json.dumps(report, indent=2) + '\n')
    os.replace(temporary, report_path)
    return report, marked


def move_decisions(report, marked, apply=False):
    """Point decisions that picked a hidden duplicate at the current variant instead."""
    current = {row['id']: next(c for c in row['candidates'] if c['variant'] == 'current')
               for row in report['rows'] if row['id'] in marked}
    data = json.loads(DECISIONS.read_text())
    now = datetime.now(timezone.utc).isoformat()
    history = []
    for pair, variants in marked.items():
        decision = data['decisions'].get(pair)
        if not decision:
            continue
        before = json.loads(json.dumps(decision))
        target = current[pair]
        note = {'at': now, 'to_variant': 'current', 'to': target['candidate_sha256'],
                'why': 'picked variant draws the same picture as the stroke-keeping current fill'}
        if decision.get('variant') in variants:
            decision.setdefault('rebound', []).append({**note, 'variant': decision['variant'],
                                                       'changed_px2': variants[decision['variant']]})
            decision['variant'], decision['candidate_sha256'] = 'current', target['candidate_sha256']
        acceptable = decision.get('acceptable_candidate_sha256', {})
        if any(acceptable.pop(variant, None) for variant in list(variants)) and decision.get('variant') != 'current':
            acceptable['current'] = target['candidate_sha256']
        for variant in variants:        # a hidden duplicate needs no rejection of its own
            decision.get('rejected_candidate_sha256', {}).pop(variant, None)
        if decision != before:
            history.append({'at': now, 'id': pair, 'previous': before, 'selected': decision,
                            'note': 'duplicate of current hidden (mark_duplicate_variants.py)'})
    if apply and history:
        with HISTORY.open('a') as stream:
            for entry in history:
                stream.write(json.dumps(entry) + '\n')
        temporary = DECISIONS.with_name(DECISIONS.name + '.tmp')
        temporary.write_text(json.dumps(data, indent=2) + '\n')
        os.replace(temporary, DECISIONS)
    return len(history)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, default=REPORT)
    parser.add_argument('--max-change', type=float, default=10.0)
    parser.add_argument('--apply', action='store_true', help='also move decisions (default: report only)')
    args = parser.parse_args()
    report, marked = mark(args.report, args.max_change)
    moved = move_decisions(report, marked, args.apply)
    print(json.dumps({'pairs_with_duplicates': len(marked),
                      'hidden_variants': sum(len(v) for v in marked.values()),
                      'decisions_moved': moved, 'applied': args.apply}, indent=2))


if __name__ == '__main__':
    main()
