"""Prepare semantic side-fill review and apply explicit AI decisions.

Run after adaptive_overlap. Geometry scores prioritize visual inspection; only
explicit visual decisions are copied into the reviewed output directory.
"""
from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import hashlib
import io
import json
from functools import lru_cache
from pathlib import Path

from .adaptive_overlap import DEFAULT_LAYOUTS, ROOT, fill_path, source_path
from .combine_fill_side import load_fill

DEFAULT_INPUT = (WORK / 'recombined-all' if (WORK / 'recombined-all/report.json').exists()
                 else WORK / 'adaptive-8px-all')
DEFAULT_DECISIONS = DATA / 'data/ai-variant-decisions.json'
DEFAULT_LAYOUT_OUTPUT = WORK / 'ai-layout-proposals'
DEFAULT_LAYOUT_SPECS = DATA / 'data/ai-layout-proposals.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normal_candidates(item):
    return [candidate for candidate in item['candidates']
            if candidate.get('main_style', 'normal') == 'normal'
            and candidate.get('sub_style', 'normal') == 'normal']


def candidate_has_genuine_fill(pair_id, variant, candidate, layouts_path=DEFAULT_LAYOUTS):
    """A retained original in a fill file does not make an outline pair a fill pair."""
    main_variant = candidate.get('base_variant', variant)
    sub_variant = candidate.get('sub_variant', 'fill')
    if main_variant not in ('current', 'outline'):
        return True  # Source-region and group variants contain a selected fill.
    if main_variant == 'outline' and sub_variant == 'outline':
        return False
    item = next((row for row in read_current_json(layouts_path)['items']
                 if row['reference_id'] == pair_id), None)
    if item is None:
        return False
    parts = {part['role']: part for part in item['parts']}

    def changed(role):
        original = load_fill(source_path(parts[role], role))[0]
        filled = load_fill(fill_path(parts[role], role))[0]
        return original.symmetric_difference(filled).area > 1

    return ((main_variant == 'current' and changed('main')) or
            (sub_variant == 'fill' and changed('sub')))


@lru_cache(maxsize=12)
def _read_json_version(path, modified_ns):
    return json.loads(Path(path).read_text())


def read_current_json(path):
    return _read_json_version(str(path), path.stat().st_mtime_ns)


def candidate_sources(item, input_dir, layout_dir=DEFAULT_LAYOUT_OUTPUT):
    def fitting(candidate):
        checks = candidate.get('keyshape_validation', {})
        if candidate.get('keyshape_override'):
            return all(check.get('stroke_envelope_inside_canvas') for check in checks.values())
        return not checks or all(check.get('fits_keyshape') and
                                 check.get('stroke_envelope_inside_canvas') and
                                 check.get('ink_outside_guide_px2', 0) <= .5
                                 for check in checks.values())

    sources = {c['variant']: (c, input_dir / c['svg']) for c in normal_candidates(item)}
    report_path = layout_dir / 'report.json'
    if report_path.exists():
        layout_row = read_current_json(report_path).get('pairs', {}).get(item['id'])
        if layout_row and layout_dir.resolve() != DEFAULT_LAYOUT_OUTPUT.resolve():
            for candidate in layout_row.get('candidates', []):
                if fitting(candidate):
                    sources[candidate['variant']] = (candidate, layout_dir / candidate['svg'])
        elif layout_row and DEFAULT_LAYOUT_SPECS.exists():
            layouts = read_current_json(DEFAULT_LAYOUTS)['items']
            saved = next((row for row in layouts if row['reference_id'] == item['id']), None)
            pair_specs = read_current_json(DEFAULT_LAYOUT_SPECS).get('pairs', {}).get(item['id'], [])
            specs_hash = hashlib.sha256(json.dumps(pair_specs, sort_keys=True,
                            separators=(',', ':')).encode()).hexdigest()
            parts = {part['role']: part for part in saved['parts']} if saved else {}
            current = (layout_row.get('layout_sha256') == sha(DEFAULT_LAYOUTS)
                       and layout_row.get('pair_specs_sha256') == specs_hash
                       and all(path.is_file() and layout_row.get(field) == sha(path)
                               for field, path in (
                                   ('main_source_sha256', source_path(parts['main'], 'main')),
                                   ('sub_source_sha256', source_path(parts['sub'], 'sub')),
                                   ('main_fill_sha256', fill_path(parts['main'], 'main')),
                                   ('sub_fill_sha256', fill_path(parts['sub'], 'sub')),
                               ))) if saved and 'main' in parts and 'sub' in parts else False
            if current:
                for candidate in layout_row.get('candidates', []):
                    if fitting(candidate):
                        sources[candidate['variant']] = (candidate, layout_dir / candidate['svg'])
    return sources


def stress_current(variant, candidate, decision, layout_dir):
    """Filled layout proposals require the reviewed, exact 8px stress SVG."""
    if not variant.startswith('layout-') or candidate.get('base_variant') == 'outline':
        return True
    relative = candidate.get('stress_svg')
    expected = decision.get('stress_candidate_sha256', {}).get(variant)
    if not relative or not expected:
        return False
    path = layout_dir / relative
    return path.is_file() and sha(path) == expected == candidate.get('stress_sha256')


def load(input_dir, decisions_path):
    report = json.loads((input_dir / 'report.json').read_text())
    decisions = json.loads(decisions_path.read_text()) if decisions_path.exists() else {'decisions': {}}
    if decisions.get('schema') != 'side-ai-variant-decisions/v1':
        raise ValueError('decision file needs side-ai-variant-decisions/v1 schema')
    return report, decisions


REVIEW_PROTOCOL = 'native48-composition-v1'


def queue(input_dir, decisions_path, out):
    report, decisions = load(input_dir, decisions_path)
    rows = []
    for item in report['rows']:
        candidates = normal_candidates(item)
        sources = candidate_sources(item, input_dir)
        current = next(c for c in candidates if c['variant'] == 'current')
        reasons = []
        if not current['safe']:
            reasons.append('current_fill_enters_validation_mask')
        if item['source_detail_needs_review']:
            reasons.append('source_detail_cut')
        if current['graph_status'] == 'review':
            reasons.append('graph_review')
        if not reasons:
            reasons.append('routine_semantic_review')
        decision = decisions['decisions'].get(item['id'])
        status = decision['status'] if decision else 'pending'
        if decision and status == 'accepted':
            approved = dict(decision.get('acceptable_candidate_sha256', {}))
            if decision.get('variant'):
                approved[decision['variant']] = decision.get('candidate_sha256')
            if not approved or any(variant not in sources or not sources[variant][1].is_file()
                                   or sha(sources[variant][1]) != digest
                                   or not stress_current(variant, sources[variant][0], decision, DEFAULT_LAYOUT_OUTPUT)
                                   for variant, digest in approved.items()):
                status = 'stale_decision'
                reasons.append('accepted_candidate_changed')
            elif decision.get('review_protocol') != REVIEW_PROTOCOL:
                status = 'stale_decision'
                reasons.append('native48_composition_review_required')
        priority = (2 if not current['safe'] or item['source_detail_needs_review']
                    else 1 if current['graph_status'] == 'review' else 0)
        rows.append({'id': item['id'], 'concept': item['concept'], 'main': item['main'],
                     'sub': item['sub'], 'reasons': reasons,
                     'priority': priority,
                     'current_validation_overlap_px2': current['added_fill_inside_validation_px2'],
                     'options': list(sources),
                     'review_status': status})
    rows.sort(key=lambda row: (row['review_status'] not in ('pending', 'stale_decision'),
                               -row['priority'], -row['current_validation_overlap_px2'], row['id']))
    result = {'schema': 'side-ai-variant-review-queue/v1',
              'source_report_sha256': sha(input_dir / 'report.json'),
              'counts': {'input_pairs': len(report['rows']), 'input_errors': len(report['errors']),
                         'review_pairs': len(rows),
                         'pending': sum(r['review_status'] in ('pending', 'stale_decision') for r in rows),
                         'accepted': sum(r['review_status'] == 'accepted' for r in rows),
                         'pending_human': sum(r['review_status'] == 'pending_human' for r in rows),
                         'needs_repair': sum(r['review_status'] == 'needs_repair' for r in rows)},
              'rows': rows}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    return result


def preview_sheet(input_dir, queue_path, layouts_path, out, offset, limit):
    import cairosvg
    from PIL import Image, ImageDraw

    review = json.loads(queue_path.read_text())
    report_rows = {row['id']: row for row in json.loads((input_dir / 'report.json').read_text())['rows']}
    items = {x['reference_id']: x for x in json.loads(layouts_path.read_text())['items']}
    rows = review['rows'][offset:offset + limit]
    if not rows:
        raise ValueError('no queue rows at this offset')
    cell, label, row_height = 126, 34, 192
    sheet = Image.new('RGB', (cell * 7 + 16, row_height * len(rows)), 'white')
    draw = ImageDraw.Draw(sheet)

    def render(path):
        png = cairosvg.svg2png(url=str(path), output_width=104, output_height=104)
        return Image.open(io.BytesIO(png)).convert('RGBA')

    for j, review_row in enumerate(rows):
        item = items[review_row['id']]
        parts = {p['role']: p for p in item['parts']}
        original = source_path(parts['main'], 'main')
        sub_fill = fill_path(parts['sub'], 'sub')
        candidates = {variant: path for variant, (_candidate, path) in
                      candidate_sources(report_rows[review_row['id']], input_dir).items()}
        variants = ['current']
        variants += [v for v in review_row['options'] if v not in variants and v != 'outline'][:3]
        variants.append('outline')
        cells = [('main source', original), ('filled sub', sub_fill)]
        cells += [(variant, candidates[variant]) for variant in variants if variant in candidates]
        y = j * row_height
        draw.text((8, y + 3), f"{offset + j + 1}. {review_row['concept']} · {review_row['id']}", fill='black')
        draw.text((8, y + 19), ', '.join(review_row['reasons']), fill='#555555')
        for k, (title, path) in enumerate(cells[:7]):
            x = k * cell + 8
            try:
                image = render(path)
                sheet.paste(image, (x, y + label), image)
            except Exception:
                draw.text((x, y + label + 35), 'render error', fill='#a00')
            draw.text((x, y + label + 108), title, fill='black')
        draw.line((0, y + row_height - 1, sheet.width, y + row_height - 1), fill='#cccccc')
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    return {'rows': len(rows), 'first': offset, 'last': offset + len(rows) - 1, 'output': str(out)}


def preview_one(pair_id, input_dir, decisions_path, layouts_path, out,
                layout_dir=DEFAULT_LAYOUT_OUTPUT):
    """Show every Normal and pair-local layout candidate for exactly one pair."""
    import cairosvg
    from PIL import Image, ImageDraw
    from .pair_layout_review import render_baseline_stress

    report, decisions = load(input_dir, decisions_path)
    item = next((row for row in report['rows'] if row['id'] == pair_id), None)
    if item is None:
        raise ValueError(f'pair not found in complete report: {pair_id}')
    layout_item = next(row for row in json.loads(layouts_path.read_text())['items']
                       if row['reference_id'] == pair_id)
    parts = {part['role']: part for part in layout_item['parts']}
    sources = candidate_sources(item, input_dir, layout_dir)
    cells = [('original main', source_path(parts['main'], 'main'), None, False),
             ('Normal main fill', fill_path(parts['main'], 'main'), None, False),
             ('original sub', source_path(parts['sub'], 'sub'), None, False),
             ('sub fill', fill_path(parts['sub'], 'sub'), None, False)]
    stress_meta = {}
    for variant, (candidate, path) in sources.items():
        cells.append((variant, path, variant, False))
        if variant == 'outline' or candidate.get('base_variant') == 'outline':
            continue
        if variant.startswith('layout-'):
            stress = layout_dir / candidate['stress_svg'] if candidate.get('stress_svg') else None
            stress_meta[variant] = candidate
        else:
            stress = out.parent / 'stress' / f'{pair_id}--{variant}--8px.svg'
            stress_meta[variant] = render_baseline_stress(pair_id, variant, stress, layouts_path)
        if stress and stress.is_file():
            cells.append((f'{variant} · actual 8px cut', stress, variant, True))
    sheet = Image.new('RGB', (650, 224 * len(cells) + 32), 'white')
    draw = ImageDraw.Draw(sheet)
    draw.text((10, 8), f"{item['concept']} · {pair_id}", fill='black')
    decision = decisions['decisions'].get(pair_id, {})
    proposed = dict(decision.get('acceptable_candidate_sha256', {}))
    if decision.get('variant'):
        proposed[decision['variant']] = decision.get('candidate_sha256')
    for index, (label, path, variant, is_stress) in enumerate(cells):
        y = 32 + index * 224
        digest = sha(path) if path.is_file() else None
        state = ('AI proposed' if proposed.get(variant) == digest else
                 'AI rejected' if decision.get('rejected_candidate_sha256', {}).get(variant) == digest
                 else 'awaiting visual review')
        draw.text((10, y + 8), label, fill='black')
        if is_stress:
            draw.text((10, y + 28), 'Validation render only', fill='#444444')
            meta = stress_meta.get(variant) or {}
            losses = meta.get('white_border_loss_at_8px', [])
            draw.text((10, y + 48), f'white border loss: {losses}', fill='#444444')
        elif variant:
            draw.text((10, y + 28), state, fill='black')
            candidate = sources[variant][0]
            if variant.startswith('layout-'):
                draw.text((10, y + 48), f"based on {candidate['base_variant']}", fill='#444444')
                draw.text((10, y + 68), f"main {candidate['main']}", fill='#444444')
                draw.text((10, y + 88), f"sub {candidate['sub']}", fill='#444444')
                draw.text((10, y + 108), f"white/8px {candidate['white_regions_inside_8px']}", fill='#444444')
            else:
                draw.text((10, y + 48), f"fill/8px {candidate['added_fill_inside_validation_px2']} px²", fill='#444444')
        try:
            for label, size, x in (('native 48', 48, 320),
                                   ('native 64', 64, 382),
                                   ('enlarged', 192, 456)):
                draw.text((x, y + 4), label, fill='#444444')
                png = cairosvg.svg2png(url=str(path), output_width=size, output_height=size)
                art = Image.open(io.BytesIO(png)).convert('RGBA')
                sheet.paste(art, (x, y + 24), art)
        except Exception as error:
            draw.text((326, y + 90), f'render error: {error}', fill='#a00')
        draw.line((0, y + 223, 650, y + 223), fill='#dddddd')
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    return {'id': pair_id, 'candidates': len(sources), 'output': str(out)}


def apply(input_dir, decisions_path, out, layout_dir=DEFAULT_LAYOUT_OUTPUT):
    report, decisions = load(input_dir, decisions_path)
    by_id = {row['id']: row for row in report['rows']}
    (out / 'svg').mkdir(parents=True, exist_ok=True)
    (out / 'variants').mkdir(parents=True, exist_ok=True)
    applied, errors, skipped_absent = [], [], []
    for pair_id, decision in decisions['decisions'].items():
        if decision.get('status') != 'accepted':
            continue
        item = by_id.get(pair_id)
        if item is None:
            skipped_absent.append(pair_id)
            continue
        proposed = {}
        if decision.get('variant'):
            proposed[decision['variant']] = decision.get('candidate_sha256')
        for variant, digest in decision.get('acceptable_candidate_sha256', {}).items():
            proposed.setdefault(variant, digest)
        if not proposed or not decision.get('reason'):
            errors.append({'id': pair_id, 'error': 'missing reviewed proposal or reason'})
            continue
        sources = candidate_sources(item, input_dir, layout_dir)
        invalid = [variant for variant, digest in proposed.items()
                   if variant not in sources or not sources[variant][1].is_file()
                   or sha(sources[variant][1]) != digest
                   or not stress_current(variant, sources[variant][0], decision, layout_dir)]
        if invalid:
            errors.append({'id': pair_id, 'error': 'reviewed candidate changed or missing',
                           'variants': invalid})
            continue
        variants = []
        for variant in proposed:
            candidate, source = sources[variant]
            target = out / 'variants' / f'{pair_id}--{variant}.svg'
            target.write_bytes(source.read_bytes())
            variants.append({'variant': variant, 'svg': str(target.relative_to(out)),
                             'sha256': sha(target),
                             'base_variant': candidate.get('base_variant', variant)})
        primary = decision.get('variant') if decision.get('variant') in proposed else next(iter(proposed))
        target = out / 'svg' / f'{pair_id}.svg'
        target.write_bytes(sources[primary][1].read_bytes())
        applied.append({'id': pair_id, 'concept': item['concept'], 'variant': primary,
                        'variants': variants,
                        'reason': decision['reason'], 'reviewer': decision.get('reviewer'),
                        'render_gap_px': item['render_gap_px'],
                        'validation_gap_px': item['validation_gap_px'],
                        'svg_sha256': sha(target)})
    approved_ids = {entry['id'] for entry in applied}
    for stale in (out / 'svg').glob('*.svg'):
        if stale.stem not in approved_ids:
            stale.unlink()
    approved_variants = {entry['svg'] for pair in applied for entry in pair['variants']}
    for stale in (out / 'variants').glob('*.svg'):
        if str(stale.relative_to(out)) not in approved_variants:
            stale.unlink()
    result = {'schema': 'side-ai-reviewed-outputs/v1', 'source_report_sha256': sha(input_dir / 'report.json'),
              'applied': applied, 'skipped_absent': skipped_absent, 'errors': errors}
    (out / 'report.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('command', choices=['queue', 'sheet', 'one', 'apply'])
    parser.add_argument('--input', type=Path, default=DEFAULT_INPUT)
    parser.add_argument('--decisions', type=Path, default=DEFAULT_DECISIONS)
    parser.add_argument('--queue', type=Path, default=WORK / 'ai-review-queue.json')
    parser.add_argument('--layouts', type=Path, default=DEFAULT_LAYOUTS)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--limit', type=int, default=8)
    parser.add_argument('--id', help='Pair ID for a one-by-one visual review sheet')
    parser.add_argument('--layout-output', type=Path, default=DEFAULT_LAYOUT_OUTPUT)
    args = parser.parse_args(argv)
    if args.command == 'queue':
        result = queue(args.input, args.decisions, args.out or args.queue)
        print(json.dumps(result['counts'], indent=2))
    elif args.command == 'sheet':
        out = args.out or WORK / f'review-sheets/sheet-{args.offset:04d}.png'
        print(json.dumps(preview_sheet(args.input, args.queue, args.layouts, out,
                                       args.offset, args.limit), indent=2))
    elif args.command == 'one':
        if not args.id:
            parser.error('one requires --id')
        out = args.out or WORK / 'review-sheets' / f'one-{args.id}.png'
        print(json.dumps(preview_one(args.id, args.input, args.decisions, args.layouts,
                                     out, args.layout_output), indent=2))
    else:
        result = apply(args.input, args.decisions, args.out or WORK / 'ai-reviewed',
                       args.layout_output)
        print(json.dumps({'applied': len(result['applied']), 'errors': result['errors']}, indent=2))


if __name__ == '__main__':
    main()
