"""A fill side pair pick combined from icon drawings: the reference for side-fill-combine.js, which the pages run.

A pick (reference_part_fills) names, for the main and the sub, an icon (a fill variant, or the solo / sub icon
itself for the outline) and its boxes on the 64 grid; the main row may add options (omit, overlap). This places
both from their SVG texts and cuts the main clear of the sub with the same engine as the build
(combine_fill_side_layouts.place_part, combine_fill_side.cut_main / cut_outline_strokes):

    fill main      its fill placed by the layout, cut_main around the placed sub
    outline main   the source strokes baked into the layout (combination_layout_svg.component), cut_outline_strokes
    sub            its fill, or the outline of the source strokes (moved, not stroked again), placed by the layout
    overlap join   the main is not cut (a joined outline sub)
    sub_scaled     a filled sub under 20px scales its stroke with it (pair_layout_review's small sub)
    omit           main elements left out: unstroked in the source, dropped from a stroke-fill

    python3 -m icon_set side-fill check [--ids ID …] [--workers N]     # every pick against the reviewed gallery SVG
    python3 -m icon_set side-fill goldens [--count N]                  # fixtures for icon_set/tests/js/side-fill.test.mjs
"""
import argparse
import gzip
import json
import os
import tempfile
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from shapely.ops import unary_union

from .combine_fill_side import GAP, cut_main, cut_outline_strokes, geometry_to_svg, load_fill
from .combine_fill_side_layouts import outline_boxes, place_part, repo_layout_svg
from .paths import DATA, WORK

SVG_NS = 'http://www.w3.org/2000/svg'
DRAWABLE = ('path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon')
REPO = Path(__file__).resolve().parents[3]
GOLDENS = REPO / 'icon_set/tests/js/fixtures/side-fill'
# Picks the browser engine once got wrong, kept as goldens: an outline crossing itself (GEOS splits it there), a hole
# only touching the clearance (shapely's intersects), parts moved apart (the split's dominant group).
HARD = {('85a99e1a-5536-45d4-9959-dd04e8c520br', 1), ('51e8bb01-0f35-5ff5-ad90-841c585f54br', 2),
        ('5745d4f1-e28e-45ca-94ab-65d5649059ri', 1), ('f3a40f08-7124-46f5-931a-9f1999e263bl', 1),
        ('991efad5-dac4-455d-8bc1-20ad32b800bl', 2), ('1aef3c2a-6d0d-43a2-9217-7031427f5fbr', 2),
        ('4a9e005b-7ece-42f1-98bb-b90c403098br', 1), ('9be8499b-bfad-4b5b-8424-bca1c4ce8ato', 1)}


def omitted(source, fill, omit):
    """(source, fill) texts with the main elements `omit` left out (pair_layout_review.omitted_main)."""
    from .stroke_fill_format import element_index
    ET.register_namespace('', SVG_NS)
    root = ET.fromstring(source)
    drawn = [el for el in root.iter() if el.tag.split('}')[-1] in DRAWABLE]
    for index in omit:
        if index < len(drawn):
            drawn[index].set('stroke', 'none')
            drawn[index].set('fill', 'none')
    source = ET.tostring(root, encoding='unicode')
    if fill is not None:
        fill_root = ET.fromstring(fill)
        for group in fill_root.iter():
            for child in list(group):
                if element_index(child) in omit:
                    group.remove(child)
        fill = ET.tostring(fill_root, encoding='unicode')
    return source, fill


def combine(pick):
    """{main|sub: {svg, source, layout, outline}, options} → (combined, cut main, placed sub, details)."""
    cls = repo_layout_svg()
    options = pick.get('options') or {}
    with tempfile.TemporaryDirectory() as folder:
        def write(name, text):
            path = Path(folder) / name
            path.write_text(text)
            return path
        placed = {}
        main = pick['main']
        main_source, main_fill = main['source'], None if main['outline'] else main['svg']
        if options.get('omit'):
            main_source, main_fill = omitted(main_source, main_fill, options['omit'])
        for role, source, fill in (('main', main_source, main_fill),
                                   ('sub', pick['sub']['source'], None if pick['sub']['outline'] else pick['sub']['svg'])):
            source_file = write(f'{role}-source.svg', source)
            file = write(f'{role}-fill.svg', fill) if fill is not None else source_file
            # An outline sub is its strokes' outline moved by the layout, not stroked again (as
            # pair_layout_review placed it); an outline main is baked and cut as strokes below.
            fill_file = None if role == 'sub' and fill is None else file
            scaled = role == 'sub' and fill is not None and bool(options.get('sub_scaled'))
            placed[role] = place_part(cls, load_fill(file)[0], source, pick[role]['layout'] or [], fill_file,
                                      scale_stroke_weight=scaled)[0]
    sub = placed['sub']
    if options.get('overlap') == 'join':
        cut, details = placed['main'], {'gap': 0.0}
    elif main['outline']:
        boxes = outline_boxes(cls, main_source, main['layout'] or [])
        if boxes is None:
            cut, details = cut_main(placed['main'], sub, GAP)
        else:
            document = cls.component({'role': 'main', 'document': main_source, 'scale': 1, 'tx': 0, 'ty': 0,
                                      'layout': boxes}, 64)['document']
            cut, details = cut_outline_strokes(document, sub, GAP)
    else:
        cut, details = cut_main(placed['main'], sub, GAP)
    return unary_union([cut, sub]), cut, sub, details


# ---------------------------------------------------------------- the picks as the site holds them

def source_text(part):
    from .adaptive_overlap import source_path
    return source_path(part, part['role']).read_text()


def pick_inputs(ids=None):
    """[(spec, pick)] for every pick (d1_import.pick_specs) with the icon texts it combines."""
    from .d1_import import pick_specs
    manifest = {(m['variant_of'], m['variant_label']): WORK / m['svg']
                for m in json.loads((WORK / 'fill-icons/manifest.json').read_text())}
    items = {i['reference_id']: i for i in json.loads((DATA / 'data/production-layouts.json').read_text())['items']}
    out = []
    for spec in pick_specs():
        if ids and spec['reference_id'] not in ids:
            continue
        parts = {p['role']: p for p in items[spec['reference_id']]['parts']}
        if set(spec['roles']) != {'main', 'sub'}:
            continue
        pick = {'options': spec['options']}
        for role, chosen in spec['roles'].items():
            source = source_text(parts[role])
            outline = chosen['label'] == 'outline'
            svg = source if outline else manifest[(chosen['source'], chosen['label'])].read_text()
            pick[role] = {'svg': svg, 'source': source, 'layout': chosen['layout'], 'outline': outline,
                          'icon': chosen['source'] if outline else f"{chosen['source']} {chosen['label']}"}
        out.append((spec, pick))
    return out


def reviewed_svg(spec):
    """The combined SVG the gallery showed for this pick (what was reviewed), or None."""
    from .d1_import import gallery_rows
    row = gallery_rows().get(spec['reference_id']) or {}
    combo = next((c for c in row.get('variant_combinations', []) if c['variant'] == spec['variant']), None)
    if not combo or not combo.get('combined'):
        return None
    path = WORK / combo['combined'].split('?', 1)[0]
    return path if path.is_file() else None


def _check(job):
    spec, pick = job
    from .combine_fill_side import load_one
    try:
        combined = combine(pick)[0]
    except Exception as error:
        return {'id': spec['reference_id'], 'rank': spec['rank'], 'variant': spec['variant'], 'error': repr(error)[:200]}
    reviewed = reviewed_svg(spec)
    result = {'id': spec['reference_id'], 'rank': spec['rank'], 'variant': spec['variant'], 'area': round(combined.area, 2)}
    if reviewed is not None:
        before = load_one(str(reviewed))['polygon']
        result['differs_px2'] = round(combined.symmetric_difference(before).area, 2)
    return result


def check(ids=None, workers=None):
    jobs = pick_inputs(ids)
    with ProcessPoolExecutor(workers or os.cpu_count()) as pool:
        results = list(pool.map(_check, jobs, chunksize=8))
    differs = sorted((r for r in results if r.get('differs_px2', 0) > 1), key=lambda r: -r['differs_px2'])
    errors = [r for r in results if 'error' in r]
    report = {'picks': len(results), 'compared': sum('differs_px2' in r for r in results),
              'same_within_1px2': sum(r.get('differs_px2', 99) <= 1 for r in results),
              'differs': len(differs), 'errors': len(errors), 'worst': differs[:40], 'error_examples': errors[:10]}
    (WORK / 'pick-check.json').write_text(json.dumps({'report': report, 'results': results}, indent=1) + '\n')
    return report


def goldens(count=240):
    """Fixtures covering every kind of pick: inputs and the combined geometry the reference makes."""
    jobs = pick_inputs()

    def kind(job):
        spec, pick = job
        m, s = pick['main'], pick['sub']
        return ('outline' if m['outline'] else 'stroke-fill' if 'stroke-fill-v1' in m['svg'][:400] else 'flat',
                'outline' if s['outline'] else 'stroke-fill' if 'stroke-fill-v1' in s['svg'][:400] else 'flat',
                spec['variant'].startswith('layout-'), bool(spec['options']),
                len(m['layout'] or []) > 1)
    by_kind = {}
    for job in jobs:
        by_kind.setdefault(kind(job), []).append(job)
    chosen, per = [job for job in jobs if (job[0]['reference_id'], job[0]['rank']) in HARD], max(1, count // max(1, len(by_kind)))
    for k in sorted(by_kind):
        chosen.extend(job for job in by_kind[k][:per] if job not in chosen)
    rest = [j for j in jobs if j not in chosen]
    chosen.extend(rest[::max(1, len(rest) // max(1, count - len(chosen)))][:max(0, count - len(chosen))])
    GOLDENS.mkdir(parents=True, exist_ok=True)
    for old in [*GOLDENS.glob('*.json'), *GOLDENS.glob('*.json.gz')]:
        old.unlink()
    written = 0
    for spec, pick in chosen:
        try:
            combined, cut, sub, details = combine(pick)
        except Exception:
            continue
        name = f"{spec['reference_id']}--{spec['rank']}"
        (GOLDENS / f'{name}.json.gz').write_bytes(gzip.compress(json.dumps({
            'id': spec['reference_id'], 'rank': spec['rank'], 'variant': spec['variant'], 'kind': list(kind((spec, pick))),
            'pick': pick, 'expected': {'svg': geometry_to_svg(combined, '0 0 64 64'), 'area': round(combined.area, 3),
                                       'main_area': round(cut.area, 3), 'sub_area': round(sub.area, 3),
                                       'bounds': [round(v, 3) for v in combined.bounds], 'gap': details.get('gap')}},
            separators=(',', ':')).encode(), mtime=0))
        written += 1
    return {'goldens': written, 'kinds': {' / '.join(map(str, k)): len(v) for k, v in sorted(by_kind.items())}}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=['check', 'goldens'])
    parser.add_argument('--ids', nargs='*')
    parser.add_argument('--workers', type=int)
    parser.add_argument('--count', type=int, default=240)
    args = parser.parse_args(argv)
    result = check(set(args.ids or []) or None, args.workers) if args.command == 'check' else goldens(args.count)
    print(json.dumps(result, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
