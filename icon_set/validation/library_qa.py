"""Library QA: existing vector spacing plus vendored rendered negative space.

Artifact switches never switch off validation. Evidence describes the exact
rendered SVG and resolved rules, including failed icons that cannot be released.
"""
from __future__ import annotations

import base64
from dataclasses import asdict
import hashlib
import html
import json
from pathlib import Path
import tempfile

from ..model import contracts
from ..model.profiles import STROKE_WIDTH
from ..renderers.svg import build_paths
from .path_commands import commands_for_path
from .internal_spacing import analyze_internal_spacing, internal_overlay, RULES as INTERNAL_RULES
from .spacing_reviews import apply_spacing_reviews
from .parallel_straight import RULES as PARALLEL_STRAIGHT_RULES
from .circle_exceptions import circle_candidates, apply_circle_exceptions
from .stroke_distance import analyze_paths
from .symmetry import analyze as analyze_symmetry, failure_messages as symmetry_failures, RULES as SYMMETRY_RULES
from .validator import _declared_connections, _pair_elements

PALETTE = ('#2563eb', '#9333ea', '#087f5b', '#c2410c', '#be185d', '#0e7490')
# Icons per results/report shard; keeps every tracked file well under GitHub's 50 MB warning.
SHARD_SIZE = 500


def _hash(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def negative_space_rules() -> dict:
    rules = contracts.load('negative-space.v1')
    for field in ('minimum_enclosed_radius', 'minimum_solid_fill_depth', 'measurement_stroke_width'):
        import math
        value = rules[field]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(f'{field} must be finite and positive')
    samples = rules['samples_per_unit']
    if type(samples) is not int or not 4 <= samples <= 64:
        raise ValueError('samples_per_unit must be an integer between 4 and 64')
    if rules['measurement_stroke_width'] > STROKE_WIDTH:
        raise ValueError('measurement stroke cannot exceed authored stroke')
    return rules


def measure_negative_space(document: str, canvas: int, *, overlay: Path | None = None, drawing=None) -> dict:
    # A missing rendering dependency is a checker error, never an empty-hole pass.
    from . import hole_geometry as engine

    rules = negative_space_rules()
    samples = rules['samples_per_unit']
    retreat = (STROKE_WIDTH - rules['measurement_stroke_width']) / 2
    radius = rules['minimum_enclosed_radius'] + retreat
    # Closure depth belongs to the authored paint, not the thinned hole mask.
    # Subtracting the 1.5-unit hole retreat disabled the 1-unit pinch rule.
    fill = rules['minimum_solid_fill_depth']
    view = (0.0, 0.0, float(canvas), float(canvas))
    with tempfile.TemporaryDirectory(prefix='icon-hole-measure-') as temporary:
        path = Path(temporary) / 'icon.svg'
        path.write_text(document, encoding='utf-8')
        ink = engine.render_ink_mask(path, canvas, canvas, samples, retreat)
        labels, region_ids = engine.enclosed_components(ink)
        holes = engine.measure_holes(labels, region_ids, view, samples, radius, canvas, canvas)
        for hole in holes:
            authored_radius = hole['inscribed_radius_design_u'] - retreat
            hole['equivalent_radius_at_authored_stroke_design_u'] = round(authored_radius, 4)
            hole['equivalent_diameter_at_authored_stroke_design_u'] = round(2 * authored_radius, 4)
        apply_circle_exceptions(holes, labels, region_ids, circle_candidates(document, drawing),
                                rule=rules['circle_hole_exception'], samples=samples,
                                measuring_stroke=rules['measurement_stroke_width'])
        # Thinning can merge a tiny painted-stroke pocket into a larger hole.
        # Check the actual exported ink too; a size correction alone cannot
        # preserve that topology. Keep the same threshold and circle exceptions.
        authored_ink = engine.render_ink_mask(path, canvas, canvas, samples, 0)
        pinches = engine.find_pinches(path, authored_ink, view, samples, fill, 0, canvas,
                                      circle_closures=circle_candidates(document, drawing),
                                      circle_rule=rules['circle_hole_exception'], authored_stroke=STROKE_WIDTH)
        authored_labels, authored_ids = engine.enclosed_components(authored_ink)
        authored_holes = engine.measure_holes(
            authored_labels, authored_ids, view, samples,
            rules['minimum_enclosed_radius'], canvas, canvas)
        apply_circle_exceptions(
            authored_holes, authored_labels, authored_ids, circle_candidates(document, drawing),
            rule=rules['circle_hole_exception'], samples=samples, measuring_stroke=STROKE_WIDTH)
        # A single background sample can be a raster-edge artifact at a
        # tangency. Discard it only when a finer render confirms there is no
        # undersized region in that neighborhood; retain all persistent pockets.
        raster_artifacts = []
        finer_labels = finer_ids = finer_holes = None
        for hole in authored_holes:
            if hole['status'] != 'fail' or hole['inscribed_radius_design_u'] > 1.01 / samples:
                continue
            if finer_labels is None:
                finer_ink = engine.render_ink_mask(path, canvas, canvas, samples * 2, 0)
                finer_labels, finer_ids = engine.enclosed_components(finer_ink)
                finer_holes = engine.measure_holes(
                    finer_labels, finer_ids, view, samples * 2,
                    rules['minimum_enclosed_radius'], canvas, canvas)
            x, y, width, height = hole['bbox_viewbox']
            scale = samples * 2
            left, top = max(0, int(x * scale) - 2), max(0, int(y * scale) - 2)
            right = min(finer_labels.shape[1], int((x + width) * scale) + 3)
            bottom = min(finer_labels.shape[0], int((y + height) * scale) + 3)
            neighborhood = finer_labels[top:bottom, left:right]
            if not any(refined['status'] == 'fail' and (neighborhood == region).any()
                       for region, refined in zip(finer_ids, finer_holes)):
                hole['status'] = 'raster-artifact'
                hole['confirmation_samples_per_unit'] = samples * 2
                raster_artifacts.append(hole)
        measured_by_region = dict(zip(region_ids, holes))
        additional_failures = []
        for hole in authored_holes:
            if hole['status'] != 'fail':
                continue
            x, y = hole['center_viewbox']
            measured = measured_by_region.get(int(labels[int(y * samples), int(x * samples)]))
            if measured is not None and measured['status'] == 'fail':
                continue  # This pocket is already reported by the thin-stroke check.
            additional_failures.append({
                **hole, 'hole': len(holes) + len(additional_failures) + 1,
                'measuring_stroke_width': STROKE_WIDTH,
                'equivalent_radius_at_authored_stroke_design_u': hole['inscribed_radius_design_u'],
                'equivalent_diameter_at_authored_stroke_design_u': hole['inscribed_diameter_design_u'],
            })
        if overlay is not None:
            overlay.parent.mkdir(parents=True, exist_ok=True)
            engine.save_overlay(ink, labels, region_ids, holes, pinches, overlay, view, samples)
            engine.save_overlay(authored_ink, authored_labels, authored_ids, authored_holes, pinches,
                                overlay.with_name('authored-' + overlay.name), view, samples)
        holes.extend(additional_failures)
    return {
        'status': 'fail' if any(h['status'] == 'fail' for h in holes) or pinches else 'pass',
        'authored_holes': authored_holes, 'authored_hole_count': len(authored_holes) - len(raster_artifacts),
        'raster_artifact_count': len(raster_artifacts),
        'hole_count': len(holes), 'failed_hole_count': sum(h['status'] == 'fail' for h in holes),
        'pinch_count': len(pinches), 'holes': holes, 'pinches': pinches,
        'exception_count': sum('exception' in h for h in holes),
        'minimum_authored_diameter': rules['minimum_enclosed_radius'] * 2,
        'minimum_measured_diameter': radius * 2,
        'configured_fill_depth': rules['minimum_solid_fill_depth'],
        'effective_fill_depth': fill, 'measuring_stroke_width': rules['measurement_stroke_width'],
        'pinch_measuring_stroke_width': STROKE_WIDTH,
        'samples_per_unit': samples,
    }


def measure_spacing(icon, drawing, validation) -> dict:
    paths = build_paths(drawing)
    result = analyze_paths(
        [{'elementId': p['id'], 'commands': commands_for_path(p['primitives'], p['closed'])} for p in paths],
        minimum_distance=float(icon.profile.spec.equal_stroke_centerline_min),
        stroke_width=float(STROKE_WIDTH),
    )
    owners = dict(drawing.owners)
    declared = _declared_connections(drawing)
    for pair in result.get('pairs', []):
        first, second = _pair_elements(pair)
        if first in owners and owners[first] == owners.get(second):
            pair['exemption'] = 'internal to a child validated at its own profile'
        elif frozenset((first, second)) in declared:
            pair['exemption'] = 'declared connect relationship'
    result['raw_status'] = result['status']
    result['status'] = ('fail' if any(e.startswith('mic') for e in validation.errors)
                        else 'review' if any(e.startswith('mic') for e in validation.warnings) else 'pass')
    result['canvas'] = icon.profile.spec.canvas_size
    result['strokeWidth'] = STROKE_WIDTH
    return result


def spacing_overlay(result: dict) -> str:
    canvas = result['canvas']
    colors = {c['id']: PALETTE[i % len(PALETTE)] for i, c in enumerate(result.get('components', []))}
    pieces = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" viewBox="0 0 {canvas} {canvas}">',
              '<rect width="100%" height="100%" fill="white"/>']
    for contour in result.get('contours', []):
        color = colors.get(contour.get('componentId'), '#64748b')
        pieces.append(f'<path d="{html.escape(contour["pathData"], quote=True)}" fill="none" '
                      f'stroke="{color}" stroke-width="{result["strokeWidth"]}" stroke-linecap="round" stroke-linejoin="round"/>')
    for pair in result.get('pairs', []):
        points = pair.get('nearestPoints')
        if not points or len(points) != 2 or not all(p is not None for p in points):
            continue
        (x1, y1), (x2, y2) = points
        color = '#64748b' if pair.get('exemption') else '#087f5b' if pair['status'] == 'pass' else '#dc2626'
        pieces.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="0.5" stroke-dasharray="1 1"/>')
        for x, y in points:
            pieces.append(f'<circle cx="{x}" cy="{y}" r="0.65" fill="white" stroke="{color}" stroke-width="0.35"/>')
    return '\n'.join(pieces + ['</svg>'])


def inspect_icon(icon, *, validation=None, debug_dir: Path | None = None, selected=True) -> dict:
    """Return serializable measurements plus a private exact SVG for publication."""
    row = {'icon_id': str(icon.icon_id), 'family': str(icon.family),
           'profile': getattr(icon.profile, 'name', str(icon.profile)),
           'selected_for_build': selected, 'status': 'error', 'errors': [], 'warnings': [],
           'spacing': {'status': 'error'}, 'negative_space': {'status': 'error'},
           'symmetry': {'status': 'error'},
           'artifacts': {}}
    try:
        validation = validation if validation is not None else icon.validate_icon()
        row['errors'] = list(validation.errors)
        row['warnings'] = list(validation.warnings)
        row['checks_run'] = list(validation.checks_run)
        row['status'] = {'valid': 'pass', 'invalid': 'fail'}.get(validation.status, validation.status)
        # Schema failures cannot safely enter either geometry engine or filenames.
        if any(e.startswith('schema/profile') for e in validation.errors):
            row['spacing'] = {'status': 'not_run'}
            row['negative_space'] = {'status': 'not_run'}
            row['symmetry'] = {'status': 'not_run'}
            return row
        drawing = icon.draw()
        document = icon.to_svg()
        row['_svg'] = document
        row['svg_sha256'] = _hash(document.encode('utf-8'))
        rules = {'profile': asdict(icon.profile.spec), 'stroke_width': STROKE_WIDTH,
                 'negative_space': negative_space_rules(), 'internal_spacing': INTERNAL_RULES,
                 'pinch_measurement': 'authored-stroke-v1',
                 'internal_parallel_straight': PARALLEL_STRAIGHT_RULES,
                 'symmetry': SYMMETRY_RULES}
        row['rules'] = rules
        row['rules_sha256'] = _hash(json.dumps(rules, sort_keys=True, separators=(',', ':')).encode('utf-8'))
        row['checks_run'].append('symmetry')
        row['symmetry'] = analyze_symmetry(icon, drawing=drawing, document=document)
        if row['symmetry']['status'] == 'fail':
            row['status'] = 'fail'
            row['errors'].extend(symmetry_failures(row['symmetry']))
        row['spacing'] = measure_spacing(icon, drawing, validation)
        row['internal_spacing'] = apply_spacing_reviews(
            icon, analyze_internal_spacing(icon, drawing), row['svg_sha256'], row['rules_sha256'])
        row['needs_review'] = row['internal_spacing']['status'] == 'review'
        if row['needs_review']:
            # A sampled finding is not a certified failure, but it must not be
            # published as a pass while the geometry still needs review.
            if row['status'] == 'pass':
                row['status'] = 'review'
            for finding in row['internal_spacing']['findings']:
                if 'visual_review' in finding:
                    continue
                first, second = finding['elements']
                row['warnings'].append(
                    f"internal-spacing [{finding['contour']}]: {first} and {second} "
                    f"have {finding['ink_gap']:g} units of ink clearance over "
                    f"{finding['sustained_length']:g} units; requires "
                    f"{row['internal_spacing']['required_ink_gap']:g}; review required")
        overlay = debug_dir / 'holes.png' if debug_dir is not None else None
        row['negative_space'] = measure_negative_space(document, icon.profile.spec.canvas_size, overlay=overlay, drawing=drawing)
        if row['negative_space']['status'] != 'pass':
            row['status'] = 'fail'
            row['errors'].append(f"holes/pinches: {row['negative_space']['failed_hole_count']} undersized holes; "
                                 f"{row['negative_space']['pinch_count']} pinches")
        if debug_dir is not None:
            import cairosvg
            debug_dir.mkdir(parents=True, exist_ok=True)
            internal_svg = internal_overlay(icon, drawing, row['internal_spacing'])
            (debug_dir / 'internal-spacing.svg').write_text(internal_svg, encoding='utf-8')
            (debug_dir / 'internal-spacing.png').write_bytes(cairosvg.svg2png(
                bytestring=internal_svg.encode('utf-8'), output_width=512, output_height=512))
            overlay_svg = spacing_overlay(row['spacing'])
            (debug_dir / 'spacing.svg').write_text(overlay_svg, encoding='utf-8')
            (debug_dir / 'spacing.png').write_bytes(cairosvg.svg2png(
                bytestring=overlay_svg.encode('utf-8'), output_width=512, output_height=512))
        if icon.to_svg() != document:
            raise ValueError('drawing changed during QA; regenerate and rerun validation')
    except Exception as error:
        row['status'] = 'error'
        row['errors'].append(f'{type(error).__name__}: {error}')
    return row


def artifact_key(icon) -> str:
    """Fixed directory names; never trust an invalid icon ID as a path."""
    identity = f'{icon.family}:{icon.icon_id}'
    import re
    if isinstance(icon.icon_id, str) and re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', icon.icon_id):
        family = getattr(icon.profile, 'family', None)
        if family in contracts.families():
            return f'{family}/{icon.icon_id}'
    return 'invalid/' + _hash(identity.encode('utf-8'))[:16]


def public_row(row):
    return {k: v for k, v in row.items() if not k.startswith('_')}


def _shards(items: list) -> list[list]:
    return [items[start:start + SHARD_SIZE] for start in range(0, len(items), SHARD_SIZE)]


def load_results(directory: Path) -> dict:
    """Reassemble a sharded QA snapshot into one aggregate with every icon row."""
    aggregate = json.loads((directory / 'results.json').read_text(encoding='utf-8'))
    icons = []
    for part in aggregate.pop('parts'):
        icons += json.loads((directory / part).read_text(encoding='utf-8'))['icons']
    return {**aggregate, 'icons': icons}


def save_evidence(rows: list[dict], directory: Path, *, debug: bool, report: bool) -> None:
    """Write a fresh QA snapshot, including complete failed/error rows."""
    directory.mkdir(parents=True, exist_ok=True)
    for index, row in enumerate(rows):
        key = row.get('_key', f'invalid/{index}')
        folder = directory / key
        folder.mkdir(parents=True, exist_ok=True)
        document = row.get('_svg')
        if document is not None:
            (folder / 'icon.svg').write_text(document, encoding='utf-8')
            row['artifacts']['svg'] = f'{key}/icon.svg'
        if debug and (folder / 'holes.png').exists():
            row['artifacts']['holes'] = f'{key}/holes.png'
        if debug and (folder / 'spacing.png').exists():
            row['artifacts']['spacing'] = f'{key}/spacing.png'
            row['artifacts']['spacing_svg'] = f'{key}/spacing.svg'
        if debug and (folder / 'internal-spacing.png').exists():
            row['artifacts']['internal-spacing'] = f'{key}/internal-spacing.png'
            row['artifacts']['internal_spacing_svg'] = f'{key}/internal-spacing.svg'
        row['artifacts']['metrics'] = f'{key}/metrics.json'
        (folder / 'metrics.json').write_text(json.dumps(public_row(row), indent=2, allow_nan=False) + '\n', encoding='utf-8')
    aggregate = {'schema_version': 1, 'scope': 'current library validation snapshot',
                 'debug': debug, 'report': report, 'count': len(rows),
                 'counts': {status: sum(r['status'] == status for r in rows) for status in ('pass', 'fail', 'review', 'error')},
                 'advisory_review_count': sum(r.get('needs_review', False) for r in rows),
                 'shard_size': SHARD_SIZE, 'parts': []}
    (directory / 'results').mkdir()
    for number, shard in enumerate(_shards(rows), 1):
        part = f'results/{number:03}.json'
        document = {'schema_version': 1, 'part': number, 'icons': [public_row(r) for r in shard]}
        (directory / part).write_text(json.dumps(document, indent=2, allow_nan=False) + '\n', encoding='utf-8')
        aggregate['parts'].append(part)
    (directory / 'results.json').write_text(json.dumps(aggregate, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    if report:
        (directory / 'report').mkdir()
        page, shards = html_report(rows, aggregate)
        for number, cards in enumerate(shards, 1):
            script = "document.querySelector('main').insertAdjacentHTML('beforeend'," + json.dumps(cards) + ');\n'
            (directory / f'report/{number:03}.js').write_text(script, encoding='utf-8')
        (directory / 'index.html').write_text(page, encoding='utf-8')


def html_report(rows, aggregate) -> tuple[str, list[str]]:
    """Return the report page and its card shards, loaded as report/NNN.js scripts."""
    cards = []
    for row in sorted(rows, key=lambda r: (r['status'] == 'pass', not r.get('needs_review', False), r['family'], r['icon_id'])):
        esc = html.escape
        document = row.get('_svg')
        preview = ('data:image/svg+xml;base64,' + base64.b64encode(document.encode()).decode()) if document else ''
        images = f'<img class="preview" src="{preview}" alt="{esc(row["icon_id"])}">' if preview else '<div class="missing">No render</div>'
        for label in ('spacing', 'holes', 'internal-spacing'):
            path = row['artifacts'].get(label)
            if path:
                images += f'<a href="{esc(path)}"><img src="{esc(path)}" alt="{label} debug"><span>{label.title()} debug</span></a>'
        holes = row['negative_space']
        spacing = row['spacing']
        gap = spacing.get('minimumInkClearance')
        gap_text = f'{gap:.3g}u' if isinstance(gap, (int, float)) else 'No disconnected pair' if spacing.get('status') == 'pass' else 'Not measured'
        diameter_rows = ''.join(f'<tr><td>{h["hole"]}</td><td>{h["equivalent_diameter_at_authored_stroke_design_u"]:g}u</td>'
                                f'<td>{h["inscribed_diameter_design_u"]:g}u</td><td>{h["status"]}{" (circle exception)" if "exception" in h else ""}</td></tr>' for h in holes.get('holes', []))
        findings = ''.join(f'<li>{esc(message)}</li>' for message in row['errors'] + row['warnings'])
        internal = row.get('internal_spacing', {'status': 'not_run', 'findings': []})
        internal_items = ''.join(f'<li>#{i}: {esc(" ↔ ".join(f["elements"]))}: '
                                 f'{f["ink_gap"]:g}u gap over ≈{f["sustained_length"]:g}u'
                                 + (f' · Reviewed: {esc(f["visual_review"]["reason"])}'
                                    if 'visual_review' in f else '') + '</li>'
                                 for i, f in enumerate(internal['findings'], 1))
        review_label = ('Visual review recorded for this exact drawing' if internal['status'] == 'reviewed'
                        else 'Review required before release' if row.get('needs_review')
                        else 'No unresolved spacing reviews')
        display_status = 'needs-review' if row['status'] == 'pass' and row.get('needs_review') else row['status']
        badge = 'review' if display_status == 'needs-review' else row['status']
        metadata = esc(json.dumps(public_row(row), indent=2))
        cards.append(f'''<article data-status="{display_status}" data-family="{esc(row['family'])}">
<div class="heading"><h2>{esc(row['icon_id'])}</h2><b class="badge {badge}">{display_status.replace("-", " ")}</b></div>
<p class="muted">{esc(row['family'])} · {esc(row['profile'])} · {'Included in build' if row['selected_for_build'] else 'Library context — not selected for build'}</p>
<div class="images">{images}</div><div class="measurements">
<p><strong>Spacing: {esc(spacing['status'])}</strong><br>Minimum ink gap: {gap_text}<br>Required ink gap: {spacing.get('requiredInkClearance', '—')}u</p>
<p><strong>Holes/pinches: {esc(holes['status'])}</strong><br>{holes.get('hole_count', '—')} holes · {holes.get('failed_hole_count', '—')} undersized · {holes.get('pinch_count', '—')} pinches<br>Required authored diameter: {holes.get('minimum_authored_diameter', '—')}u</p></div>
<ul class="findings">{findings}</ul>
<div class="internal"><strong>Connected-edge spacing: {internal['status']}</strong>
<p>{review_label} · release checks: {esc(row['status'])}. Required gap: {internal.get('required_ink_gap', '—')}u. Negative gaps mean overlapping ink.</p><ul>{internal_items}</ul></div>
{'<table><thead><tr><th>Hole</th><th>Authored Ø</th><th>Measuring Ø</th><th>Status</th></tr></thead><tbody>' + diameter_rows + '</tbody></table>' if diameter_rows else ''}
<details><summary>Measurements, thresholds and source hashes</summary><pre>{metadata}</pre></details>
<a class="metrics" href="{esc(row['artifacts']['metrics'])}">Download metrics JSON</a></article>''')
    counts = aggregate['counts']
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Icon library · Validation</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f5f7;color:#18202f;font:15px/1.5 system-ui,sans-serif}header,main{max-width:1500px;margin:auto;padding:32px}header{padding-bottom:12px}h1{font-size:32px;margin:4px 0}h2{font-size:17px;margin:0;overflow-wrap:anywhere}.eyebrow{color:#53657a;font-weight:650;letter-spacing:.1em;text-transform:uppercase;font-size:12px}.intro{max-width:920px;color:#53657a}.summary{display:flex;gap:12px;flex-wrap:wrap}.summary div{background:white;padding:12px 20px;border-radius:10px;min-width:120px}.summary strong{display:block;font-size:26px}.toolbar{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}input,select{border:1px solid #cbd1dc;border-radius:8px;padding:11px;font:inherit;background:white}input{flex:1;min-width:200px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,390px),1fr));gap:20px}article{background:white;border:1px solid #e1e5eb;border-radius:14px;padding:20px;min-width:0}.heading{display:flex;gap:10px;align-items:start;justify-content:space-between}.badge{font-size:12px;border-radius:20px;padding:3px 10px;text-transform:uppercase}.pass{background:#e2f4ea;color:#146c43}.fail,.error{background:#ffe5e5;color:#a32222}.review{background:#fff0c9;color:#725000}.muted{color:#6d7686;font-size:12px}.images{display:flex;flex-wrap:wrap;gap:10px;align-items:center;min-height:148px}.images>a{text-align:center;font-size:11px;color:#53657a}.images img{width:110px;height:110px;max-width:100%;object-fit:contain}.images .preview{width:110px;height:110px;padding:10px;background:#f7f8fa;border-radius:10px}.measurements{display:flex;gap:16px;font-size:13px}.measurements p{flex:1}.findings{padding-left:20px;color:#a32222;font-size:13px}.internal{font-size:12px;color:#92400e;background:#fffbeb;padding:10px;border-radius:8px;margin:10px 0}.internal ul{padding-left:18px}pre{max-height:350px;overflow:auto;font-size:11px;background:#f6f7f9;padding:10px}summary{cursor:pointer;font-size:12px;color:#53657a}table{border-collapse:collapse;width:100%;font-size:12px;margin-bottom:14px}th,td{text-align:left;padding:7px;border-bottom:1px solid #e8ebef}.metrics{display:inline-block;margin-top:12px;font-size:12px;color:#2457a7}[hidden]{display:none!important}
</style><header><div class="eyebrow">Pictographic · Quality assurance</div><h1>Icon library validation</h1>
<p class="intro">Current source drawings, including failures. This is a validation snapshot, not proof of a published release. Spacing measures disconnected centerline components; declared contacts and child ownership exemptions are recorded. Hole diameters are raster measurements translated back to the authored stroke. Numeric checks do not replace visual review.</p>
<div class="summary">''' + ''.join(f'<div><strong>{value}</strong>{label}</div>' for label, value in [('Icons', len(rows)), ('Unresolved spacing reviews', aggregate['advisory_review_count'])] + list(counts.items())) + '''</div>
<div class="toolbar"><input id="search" type="search" placeholder="Find an icon…" aria-label="Find an icon"><select id="family" aria-label="Family"><option value="">All families</option><option>sub</option><option>solo</option><option>container</option></select><select id="status" aria-label="Status"><option value="">All statuses</option><option value="needs-review">Unresolved legacy review</option><option>pass</option><option>fail</option><option>review</option><option>error</option></select><a href="results.json">All measurements</a></div></header><main></main>''' + ''.join(f'<script src="report/{number:03}.js"></script>' for number in range(1, len(_shards(cards)) + 1)) + '''<script>
const search=document.querySelector('#search'),family=document.querySelector('#family'),status=document.querySelector('#status');
function filter(){for(const card of document.querySelectorAll('article'))card.hidden=!(card.querySelector('h2').textContent.toLowerCase().includes(search.value.toLowerCase())&&(!family.value||card.dataset.family===family.value)&&(!status.value||card.dataset.status===status.value));}
for(const control of [search,family,status])control.addEventListener('input',filter);
</script></html>''', [''.join(shard) for shard in _shards(cards)]
