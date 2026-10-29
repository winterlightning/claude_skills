"""Compile explicit, source-bound object recipes into isolated draft outputs."""
import copy
import hashlib
import importlib.metadata
import json
import math
import re
import shutil
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from shapely.geometry import Point, box
from shapely.ops import unary_union

from . import geometry as g
from .corners import round_export
from .spacing import fit_regions_with_gaps, measure_pairs

STYLES = ('normal', 'round', 'sharp')
TREATMENTS = {'keep_strokes', 'keep_solid', 'fill_regions', 'reverse_regions', 'subtract_strokes'}


def dump(path, data):
    path.write_text(json.dumps(data, indent=2, allow_nan=False)+'\n')


def engine_hash():
    files = sorted(Path(__file__).parent.glob('*.py')) + [Path(g.fu.__file__)]
    return hashlib.sha256(b''.join(p.name.encode()+p.read_bytes() for p in files)).hexdigest()


def select_regions(paint, definitions, style):
    available = g.faces(paint)
    chosen, used, ids = [], set(), set()
    for definition in definitions:
        name = definition['id']
        if name in ids:
            raise ValueError('Duplicate region ID: '+name)
        ids.add(name)
        grouped = definition.get('anchors_by_style')
        if grouped is not None:
            if set(definition) != {'id', 'anchors_by_style', 'expected_counts_by_style'} or not isinstance(grouped, dict) or set(grouped) != set(STYLES):
                raise ValueError('A semantic region group needs exact anchors for every style')
            if any(not isinstance(points, list) or not points for points in grouped.values()):
                raise ValueError('A semantic region group cannot be empty')
            counts = definition['expected_counts_by_style']
            if not isinstance(counts, dict) or set(counts) != set(STYLES) or any(type(counts[s]) is not int or counts[s] != len(grouped[s]) for s in STYLES):
                raise ValueError('Semantic region group counts must match the recorded style anchors')
            for points in grouped.values():
                for point in points:
                    if not isinstance(point, list) or len(point) != 2 or any(type(x) not in (int, float) or not math.isfinite(x) for x in point):
                        raise ValueError('Semantic region group needs finite source anchors')
            anchors = grouped[style]
        else:
            anchors = [definition.get('anchors', {}).get(style, definition.get('anchor'))]
        selected = []
        for anchor in anchors:
            if (not isinstance(anchor, list) or len(anchor) != 2 or
                    any(type(x) not in (int, float) or not math.isfinite(x) for x in anchor)):
                raise ValueError('Region needs a finite two-coordinate anchor: '+name)
            matches = [i for i, face in enumerate(available) if face.contains(Point(anchor))]
            if len(matches) != 1 or matches[0] in used:
                raise ValueError('Ambiguous, missing or duplicate region anchor: '+name)
            used.add(matches[0]); selected.append(available[matches[0]])
        chosen.append(unary_union(selected))
    if not chosen:
        raise ValueError('A region treatment requires explicitly selected regions')
    return chosen


def validate_recipe(recipe):
    if recipe.get('schema') != 'source-object-treatments/v1':
        raise ValueError('Unsupported recipe schema')
    if not recipe.get('objects'):
        raise ValueError('No object decisions supplied')
    ids = set()
    for obj in recipe['objects']:
        name = obj['id']
        if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]*', name) or name in ids:
            raise ValueError('Invalid or duplicate object ID')
        ids.add(name)
        if obj['treatment'] not in TREATMENTS:
            raise ValueError('Unsupported treatment: '+obj['treatment'])
        if obj['treatment'] not in {'fill_regions', 'reverse_regions'} and obj.get('regions'):
            raise ValueError('Only region treatments accept region decisions')
        if any('anchors_by_style' in region for region in obj.get('regions', [])) and obj['treatment'] != 'fill_regions':
            raise ValueError('Semantic region groups currently support fill selection only')
        if 'include_detail_boundaries' in obj:
            if obj['include_detail_boundaries'] is not True or obj['treatment'] != 'fill_regions':
                raise ValueError('Native detail boundaries require an explicit fill_regions object')
        if obj.get('normalization') and obj['treatment'] != 'reverse_regions':
            raise ValueError('Only reversed regions may be enlarged')
        if obj.get('extension') and obj['treatment'] != 'subtract_strokes':
            raise ValueError('Only subtraction may extend a source endpoint')
    positive = {o['id'] for o in recipe['objects'] if o['treatment'] != 'subtract_strokes'}
    for obj in recipe['objects']:
        if obj['treatment'] == 'subtract_strokes' and obj.get('target') not in positive:
            raise ValueError('Subtraction requires an explicit positive target object')
        if obj.get('include_detail_boundaries') and not any(detail['treatment'] == 'subtract_strokes' and detail.get('target') == obj['id'] for detail in recipe['objects']):
            raise ValueError('Native detail boundaries require subtract_strokes owned by this fill target')
    if not positive:
        raise ValueError('Recipe has no positive objects')


def compile_recipe(recipe_path, source_dir, output_dir, styles=STYLES):
    recipe_path, source_dir, output_dir = map(Path, (recipe_path, source_dir, output_dir))
    recipe = json.loads(recipe_path.read_text())
    validate_recipe(recipe)
    if any(s not in STYLES for s in styles):
        raise ValueError('Unsupported source style')
    styles = tuple(s for s in STYLES if s in styles)
    if not styles:
        raise ValueError('No supported styles requested')
    # Normal is the reference even when the caller requests only Round or Sharp.
    needs_reference = any(o.get('normalization') for o in recipe['objects'])
    processing = tuple(s for s in STYLES if s in styles or s == 'normal' and needs_reference)
    output_dir = output_dir.resolve()
    source_dir = source_dir.resolve()
    for protected in [source_dir/s for s in STYLES] + [source_dir/'fill_processing/fill-output', source_dir/'fill_processing/imported-fixes']:
        if output_dir == protected or protected in output_dir.parents or output_dir in protected.parents:
            raise ValueError('Output must be separate from source SVGs and published fills')
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError('Use a new output directory; existing runs are preserved')
    output_dir.mkdir(parents=True, exist_ok=True)
    receipt = {'schema': 'object-treatment-run/v1', 'name': recipe['name'],
               'recipe_sha256': g.sha(recipe_path), 'engine_sha256': engine_hash(),
               'status': 'generated_review_pending', 'visual_review': 'pending',
               'source_geometry_only': True, 'white_representation': 'transparent_cutout', 'styles': {}}
    receipt['dependencies'] = {name: importlib.metadata.version(name)
                               for name in ('shapely', 'scipy', 'numpy', 'svgpathtools', 'skia-pathops', 'fonttools')}
    normal_bounds, normal_regions = {}, {}
    for style in processing:
        work = Path(tempfile.mkdtemp(prefix='.'+style+'-', dir=output_dir))
        try:
            src = recipe['sources'].get(style)
            if not src:
                raise ValueError('Missing style source record: '+style)
            path = (source_dir/src['file']).resolve()
            if source_dir not in path.parents or not path.is_file():
                raise ValueError('Missing or out-of-root style source: '+style)
            if g.sha(path) != src['sha256']:
                raise ValueError('Source hash mismatch: '+style)
            raw = path.read_bytes()
            root = ET.fromstring(raw)
            closure_audit = None
            if 'native_closures' in recipe:
                from .native_closures import apply
                root, closure_audit = apply(root, recipe, source_dir, style)
            g.validate_source(root)
            items = g.leaves(root)
            assigned = set()
            for obj in recipe['objects']:
                selectors = obj['source_elements'].get(style, [])
                g.subset(root, selectors)
                if assigned.intersection(selectors):
                    raise ValueError('Source element ownership overlaps: '+obj['id'])
                assigned.update(selectors)
            if assigned != {'leaf:'+str(i) for i in range(len(items))}:
                raise ValueError('Unassigned source elements')
            (work/'source.svg').write_bytes(raw)
            objects, audits, region_sets, source_paints = {}, {}, {}, {}
            for obj in recipe['objects']:
                oid, treatment = obj['id'], obj['treatment']
                if treatment == 'subtract_strokes':
                    continue
                paint = g.paint(g.subset(root, obj['source_elements'][style]), work/(oid+'-source.svg'))
                source_paints[oid] = paint
                if style == 'normal':
                    normal_bounds[oid] = paint.bounds
                audit = {'id': oid, 'treatment': treatment, 'source_elements': obj['source_elements'][style],
                         'source_bounds': paint.bounds, 'reason': obj.get('reason', '')}
                result = paint
                if treatment in {'fill_regions', 'reverse_regions'}:
                    detection_paint = paint
                    if obj.get('include_detail_boundaries'):
                        # Details still define native face boundaries even when
                        # their final treatment is transparent subtraction. Use
                        # only this target's original, unextended detail paint;
                        # ownership and final paint/cut operations stay unchanged.
                        details = [detail for detail in recipe['objects'] if detail['treatment'] == 'subtract_strokes' and detail.get('target') == oid]
                        detail_paints = [g.paint(g.subset(root, detail['source_elements'][style]), work/(oid+'-boundary-'+detail['id']+'.svg')) for detail in details]
                        detection_paint = unary_union([paint, *detail_paints])
                        audit['detail_boundaries'] = [detail['id'] for detail in details]
                    regions = select_regions(detection_paint, obj.get('regions', []), style)
                    if style == 'normal':
                        normal_regions[oid] = list(regions)
                    if obj.get('normalization'):
                        policy = obj['normalization']
                        if policy.get('target') != 'normal_object_painted_bounds':
                            raise ValueError('Unsupported normalization target')
                        if oid not in normal_bounds:
                            raise ValueError('Normal reference is unavailable')
                        ids = [r['id'] for r in obj['regions']]
                        gap, tolerance = policy.get('gap', 4), policy.get('tolerance', .001)
                        pairs = [(ids.index(a), ids.index(b), gap) for a, b in policy['neighbors']]
                        regions, fit = fit_regions_with_gaps(regions, normal_bounds[oid], pairs,
                            ids=ids, reference_regions=normal_regions[oid], tolerance=tolerance, minimum_clearance=gap)
                        audit['normalization'] = fit
                    combined = unary_union(regions)
                    result = paint.union(combined) if treatment == 'fill_regions' else combined
                    region_sets[oid] = regions
                    audit['regions'] = [{'id': d['id'], 'area': r.area, 'bounds': r.bounds}
                                        for d, r in zip(obj['regions'], regions)]
                    for definition, region in zip(obj['regions'], regions):
                        # Filenames use numeric slots; external region IDs remain in the receipt.
                        n = obj['regions'].index(definition)
                        (work/f'{oid}-region-{n}.svg').write_text(g.serialize(region))
                objects[oid] = result
                audits[oid] = audit
            for obj in recipe['objects']:
                if obj['treatment'] != 'subtract_strokes':
                    continue
                oid, target = obj['id'], obj['target']
                tree = g.subset(root, obj['source_elements'][style])
                audit = {'id': oid, 'treatment': obj['treatment'], 'target': target,
                         'source_elements': obj['source_elements'][style], 'reason': obj.get('reason', '')}
                if obj.get('extension'):
                    ext = obj['extension']
                    if ext.get('mode') != 'through_target_exterior':
                        raise ValueError('Unsupported extension mode')
                    audit['extension'] = g.extend_straight(tree, obj['source_elements'][style], ext['endpoint'], objects[target].bounds)
                cut = g.paint(tree, work/(oid+'-source.svg'))
                objects[target] = objects[target].difference(cut)
                (work/(oid+'-cut.svg')).write_text(g.serialize(cut))
                audits[oid] = audit
            for oid, result in objects.items():
                if result.is_empty or not result.is_valid:
                    raise ValueError('Empty or invalid object result: '+oid)
                (work/(oid+'-result.svg')).write_text(g.serialize(result))
            combined = g.clean(unary_union(list(objects.values())))
            if combined.is_empty or not combined.is_valid:
                raise ValueError('Invalid assembled fill')
            (work/'before-corners.svg').write_text(g.serialize(combined))
            output = work/'fill.svg'
            corners = None
            policy = recipe.get('corner_policy', {}).get(style, {})
            if policy:
                if style != 'round' or policy.get('operation') != 'round_convex_black':
                    raise ValueError('Unsupported corner policy')
                final, corners = round_export(combined, output, radius=policy.get('radius', 2))
            else:
                output.write_text(g.serialize(combined))
                final = g.read_export(output)
            if final.is_empty or not final.is_valid or not box(-.001, -.001, 48.001, 48.001).covers(final):
                raise ValueError('Invalid final geometry or output outside canvas')
            if g.topology(final) != g.topology(combined):
                raise ValueError('Serialization changed topology')
            for obj in recipe['objects']:
                oid = obj['id']
                if obj.get('normalization'):
                    policy = obj['normalization']; ids = [r['id'] for r in obj['regions']]
                    regions = [r.intersection(final) for r in region_sets[oid]]
                    pairs = [(ids.index(a), ids.index(b), policy.get('gap', 4)) for a, b in policy['neighbors']]
                    measurements = measure_pairs(regions, pairs, ids)
                    if any(r.is_empty for r in regions) or any(abs(m['measured_gap']-m['required_gap']) > policy.get('tolerance', .001) for m in measurements):
                        raise ValueError('Final SVG violates neighboring region gaps')
                    final_bounds = unary_union(regions).bounds
                    if max(abs(a-b) for a, b in zip(final_bounds, normal_bounds[oid])) > .001:
                        raise ValueError('Final rounded regions no longer fit the requested object bounds')
                    audits[oid]['final_spacing'] = measurements
                    audits[oid]['final_bounds'] = final_bounds
                if obj['treatment'] in {'keep_solid', 'keep_strokes'}:
                    loss = source_paints[oid].difference(final).area
                    audits[oid]['retained_paint_loss_area'] = loss
                    # Protect explicitly retained marks from automatic dot conversion/rounding.
                    if loss > .02:
                        raise ValueError('Retained source paint changed: '+oid)
            if g.sha(path) != src['sha256']:
                raise ValueError('Source changed during execution')
            result = {'status': 'generated_review_pending', 'source_sha256': src['sha256'],
                      'source_unchanged': True, 'output_sha256': g.sha(output), 'bounds': final.bounds,
                      'topology': g.topology(final), 'objects': list(audits.values()), 'corner_pass': corners,
                      'native_closures': closure_audit}
            dump(work/'receipt.json', result)
            if style in styles:
                work.rename(output_dir/style)
                result['output'] = style+'/fill.svg'
            receipt['styles'][style] = result
        except Exception as exc:
            receipt['styles'][style] = {'status': 'held', 'error': f'{type(exc).__name__}: {exc}'}
            receipt['status'] = 'held'
        finally:
            if work.exists():
                shutil.rmtree(work)
    dump(output_dir/'recipe.json', recipe)
    dump(output_dir/'receipt.json', receipt)
    return receipt
