"""Fold Claude's pair-local layouts back into the pair's own variants (user request, 2026-10-28).

A `layout-claude-…` pick that only moved/resized the main and sub of a normal variant (current,
outline, region-N, group-…) with the normal fill sub becomes that variant: the pair's saved placement
in data/production-layouts.json is set to the layout's boxes, the pair is recombined, and the pick is
renamed to its base variant. The first such pick sets the placement; later picks of a pair become their
base variant at that same placement. Picks that cannot fold (outline sub, moved position, omitted main
elements, joined overlap) stay as layouts.

Every placement change is recorded in data/pair-placement-overrides.json with the original boxes, so a
re-import of production layouts can re-apply it and any pair can be restored.

  plan     write output/fold-layouts/plan.json (no changes)
  apply    change placements, specs and renders per the plan; prints the new proposal lists file
"""
from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import json
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from .adaptive_overlap import ROOT, DEFAULT_LAYOUTS, main as recombine
from .mark_duplicate_variants import mark as mark_duplicates

OUT = WORK / 'fold-layouts'
GALLERY = WORK / 'gallery-data.js'
SPECS = DATA / 'data/ai-layout-proposals.json'
LAYOUT_REPORT = WORK / 'ai-layout-proposals/report.json'
RECOMBINED = WORK / 'recombined-all'
OVERRIDES = DATA / 'data/pair-placement-overrides.json'
USER_TOUCHED = ('1e909a20', '24fe2386')


def gallery_rows():
    text = GALLERY.read_text()
    return {row['id']: row for row in json.loads(text[text.index('{'):text.rindex('}') + 1])['rows']}


def foldable(pair_id, spec):
    """Why a layout spec cannot become its base variant, or None when it can."""
    if spec is None:
        return 'no spec'
    if spec.get('sub_variant', 'fill') != 'fill':
        return 'outline sub'
    if spec.get('omit_main_elements'):
        return 'omits main elements'
    if spec.get('overlap_mode', 'clear') != 'clear':
        return 'joined overlap'
    if spec.get('position', pair_id[-2:]) != pair_id[-2:]:
        return 'moved position'
    return None


def plan(_args):
    rows = gallery_rows()
    specs = json.loads(SPECS.read_text())['pairs']
    report = json.loads(LAYOUT_REPORT.read_text())['pairs']
    pairs = {}
    for pair_id, row in rows.items():
        if row.get('selection_status') != 'selected' or pair_id.startswith(USER_TOUCHED):
            continue
        picks = row['proposed_variants']
        if not any(v.startswith('layout-claude-') for v in picks):
            continue
        placement, new, kept = None, [], []
        for variant in picks:
            if not variant.startswith('layout-claude-'):
                new.append(variant)
                continue
            spec = next((s for s in specs.get(pair_id, []) if 'layout-' + s['id'] == variant), None)
            why = foldable(pair_id, spec)
            if why:
                new.append(variant); kept.append({'variant': variant, 'why': why})
                continue
            if placement is None:
                rendered = next(c for c in report[pair_id]['candidates'] if c['variant'] == variant)
                placement = {'from': variant, 'boxes': rendered['layout_boxes']}
            new.append(spec['base_variant'])
        if placement:
            pairs[pair_id] = {'old': picks, 'new': list(dict.fromkeys(new)), 'placement': placement, 'kept_layouts': kept}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'plan.json').write_text(json.dumps(pairs, indent=1) + '\n')
    print(f'{len(pairs)} pairs fold; {sum(len(p["kept_layouts"]) for p in pairs.values())} picks stay layouts')


def apply(_args):
    pairs = json.loads((OUT / 'plan.json').read_text())
    stamp = datetime.now(timezone.utc).isoformat(timespec='seconds')
    # 1. placements, with the originals recorded
    layouts = json.loads(DEFAULT_LAYOUTS.read_text())
    overrides = json.loads(OVERRIDES.read_text()) if OVERRIDES.exists() else {'schema': 'pair-placement-overrides/v1', 'pairs': {}}
    for item in layouts['items']:
        entry = pairs.get(item['reference_id'])
        if not entry:
            continue
        boxes = entry['placement']['boxes']
        original = {p['role']: p['layout'] for p in item['parts']}
        for part in item['parts']:
            part['layout'] = boxes[part['role']]
        overrides['pairs'][item['reference_id']] = {
            'at': stamp, 'from_layout': entry['placement']['from'], 'layout': boxes,
            'original': overrides['pairs'].get(item['reference_id'], {}).get('original', original)}
    DEFAULT_LAYOUTS.write_text(json.dumps(layouts, indent=2) + '\n')
    OVERRIDES.write_text(json.dumps(overrides, indent=1) + '\n')
    # 2. recombine those pairs and merge them into recombined-all
    ids = sorted(pairs)
    with tempfile.TemporaryDirectory(prefix='fold-recombine-') as tmp:
        tmp = Path(tmp)
        recombine(['--out', str(tmp), '--summary-only', '--ids', *ids])
        fresh = {row['id']: row for row in json.loads((tmp / 'report.json').read_text())['rows']}
        report = json.loads((RECOMBINED / 'report.json').read_text())
        for i, row in enumerate(report['rows']):
            if row['id'] in fresh:
                report['rows'][i] = fresh[row['id']]
                for candidate in fresh[row['id']]['candidates']:
                    shutil.copy2(tmp / candidate['svg'], RECOMBINED / candidate['svg'])
        (RECOMBINED / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    mark_duplicates(RECOMBINED / 'report.json')
    # 3. drop the Claude layout records of folded pairs (keep picked layouts that could not fold), re-render the rest
    from .main_gallery_server import REVIEW_LOCK, render_layout_one
    with REVIEW_LOCK:
        specs = json.loads(SPECS.read_text())
        for pair_id, entry in pairs.items():
            keep = {k['variant'] for k in entry['kept_layouts']}
            specs['pairs'][pair_id] = [s for s in specs['pairs'].get(pair_id, [])
                                       if not ('layout-' + s['id']).startswith('layout-claude-') or 'layout-' + s['id'] in keep]
            if not specs['pairs'][pair_id]:
                del specs['pairs'][pair_id]
        SPECS.write_text(json.dumps(specs, indent=2) + '\n')
    layout_report = json.loads(LAYOUT_REPORT.read_text())
    for pair_id in ids:
        if pair_id not in specs['pairs']:
            layout_report['pairs'].pop(pair_id, None)
    LAYOUT_REPORT.write_text(json.dumps(layout_report, indent=2) + '\n')
    failed = {}
    for pair_id in ids:
        if pair_id in specs['pairs']:
            try:
                render_layout_one(pair_id)
            except Exception as error:
                failed[pair_id] = str(error)[:200]
    (OUT / 'proposals.json').write_text(json.dumps({p: e['new'] for p, e in pairs.items()}, indent=1) + '\n')
    print(f'folded {len(ids)} pairs; layout re-render failures: {failed}')
    print(f'new proposal lists: {OUT / "proposals.json"} (select them in this order)')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('plan'); sub.add_parser('apply')
    args = parser.parse_args()
    {'plan': plan, 'apply': apply}[args.command](args)


if __name__ == '__main__':
    main()
