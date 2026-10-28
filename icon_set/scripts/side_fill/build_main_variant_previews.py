"""Render each side-pair main's fill variants on their own (48px) for the gallery's main icon tab.

For every main used by a saved side pair: the current fill (fill_path, stroke-keeping when
published) plus each source-bound region/group variant from its Normal region recipe, labelled
with the main-variant policy status. A variant within 10 px² of the current fill (or differing only by hairlines) is the same
picture and is left out, matching mark_duplicate_variants.py. Writes
output/main-variants/<name>/<variant>.svg and output/main-variants/index.json.
"""

import argparse
import json
from concurrent.futures import ProcessPoolExecutor

from ...vendor.fill_processing.vendor.fill_utils import geometry_to_svg

from .adaptive_overlap import (DEFAULT_LAYOUTS, ROOT, fill_path, main_variant_policy, region_variants,
                               source_path, variant_rejected)
from .combine_fill_side import load_fill
from .mark_duplicate_variants import HAIRLINE
from .paths import WORK

OUT = WORK / 'main-variants'
SAME_PICTURE_PX2 = 10.0


def render(job):
    name, part = job
    source, fill = source_path(part, 'main'), fill_path(part, 'main')
    if not source.is_file() or not fill.is_file():
        return name, {'error': 'missing source or fill'}
    policy = main_variant_policy(name)
    approved, rejected = set(policy.get('approved', [])), set(policy.get('rejected', []))
    current = load_fill(fill)[0]
    try:
        choices = region_variants(name, source, policy.get('groups', {}))[0]
    except Exception as error:            # no usable recipe: the current fill is the only variant
        choices, note = [], repr(error)[:200]
    else:
        note = None
    folder = OUT / name
    folder.mkdir(parents=True, exist_ok=True)
    for stale in folder.glob('*.svg'):
        stale.unlink()
    variants = []
    for label, geometry in choices:
        delta = geometry.symmetric_difference(current)
        difference = round(delta.area, 2)
        # Same rule as the pairs (mark_duplicate_variants.py): within 10 px², or only hairlines.
        if difference <= SAME_PICTURE_PX2 or delta.buffer(-HAIRLINE).area <= .5:
            continue
        path = folder / f'{label}.svg'
        path.write_text(geometry_to_svg(geometry, '0 0 48 48'))
        variants.append({'variant': label, 'svg': str(path.relative_to(WORK)),
                         'status': 'rejected' if variant_rejected(policy, label) else 'approved' if label in approved else 'unreviewed',
                         'differs_from_current_px2': difference})
    return name, {'variants': variants, 'note': note,
                  'exclude_current': bool(policy.get('exclude_current'))}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers', type=int, default=6)
    args = parser.parse_args(argv)
    mains = {}
    for item in json.loads(DEFAULT_LAYOUTS.read_text())['items']:
        for part in item['parts']:
            if part['role'] == 'main' and part.get('icon'):
                mains.setdefault(part['icon'].split('/', 1)[1], part)
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        index = dict(pool.map(render, sorted(mains.items()), chunksize=8))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'index.json').write_text(json.dumps(index, indent=1) + '\n')
    counts = [len(v.get('variants', [])) for v in index.values()]
    print(json.dumps({'mains': len(index), 'with_variants': sum(c > 0 for c in counts),
                      'variants': sum(counts), 'most': max(counts, default=0),
                      'errors': sum('error' in v for v in index.values())}))


if __name__ == '__main__':
    main()
