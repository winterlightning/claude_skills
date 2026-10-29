"""Render AI-authored, pair-local Normal layout proposals one pair at a time.

The saved production layouts and source SVGs are read only. A proposal changes
the target layout boxes, then replays the original 4px stroke placement code.
It is evidence for visual review, never an automatic approval.
"""

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import copy
import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path

from shapely.geometry import Point, box as geometry_box
from shapely.ops import unary_union

from .adaptive_overlap import (DEFAULT_LAYOUTS, checked_source, fill_path,
                               main_variant_policy, place, region_variants)
from .combine_fill_side import (GAP, ROOT, clearance, cut_main,
                                cut_outline_strokes, geometry_to_svg, load_fill)
from .combine_fill_side_layouts import outline_boxes, place_part, repo_layout_svg
from .graph_overlap import analyze as analyze_overlap, region_graph

DEFAULT_SPECS = DATA / 'data/ai-layout-proposals.json'
DEFAULT_OUT = WORK / 'ai-layout-proposals'
KEYSHAPES = DATA / 'data/side-keyshapes.json'
ID = re.compile(r'[a-z0-9][a-z0-9-]*\Z')
ANCHORS = {'br': (1, 1), 'bl': (0, 1), 'tr': (1, 0), 'tl': (0, 0),
           'ri': (1, .5), 'le': (0, .5), 'bo': (.5, 1), 'to': (.5, 0)}
PAIR_PAINTED_PADDING = 4


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


@lru_cache(maxsize=1)
def keyshape_tables():
    return json.loads(KEYSHAPES.read_text())


def source_keyshape_name(role, source_bounds):
    shapes = keyshape_tables()[role]
    return next((name for name, bounds in sorted(shapes.items(),
                 key=lambda item: item[0] != 'SQUARE')
                 if all(abs(a-b) < .05 for a, b in zip(bounds, source_bounds))), 'custom')


def source_centerline_bounds(cls, source, role):
    part = cls.component({'role': role, 'document': source.read_text(),
                          'scale': 1, 'tx': 0, 'ty': 0}, 64)
    bounds = [box for box in part['sources'] if box]
    return [min(b[0] for b in bounds), min(b[1] for b in bounds),
            max(b[2] for b in bounds), max(b[3] for b in bounds)]


def placed_outline_svg(cls, source, layout):
    """Bake one source's saved boxes, including legacy single boxes without paths."""
    document = source.read_text()
    boxes = outline_boxes(cls, document, layout) or copy.deepcopy(layout)
    if len(boxes) == 1 and 'paths' not in boxes[0]:
        source_part = cls.component({'role': 'main', 'document': document,
                                     'scale': 1, 'tx': 0, 'ty': 0}, 64)
        boxes[0]['paths'] = [index for index, bounds in
                             enumerate(source_part['sources']) if bounds]
    return cls.component({'role': 'main', 'document': document,
                          'scale': 1, 'tx': 0, 'ty': 0, 'layout': boxes}, 64)['document']


def layout_with_paths(cls, source, layout, role):
    boxes = copy.deepcopy(layout)
    if len(boxes) == 1 and 'paths' not in boxes[0]:
        raw = cls.component({'role': role, 'document': source.read_text(),
                             'scale': 1, 'tx': 0, 'ty': 0}, 64)
        boxes[0]['paths'] = [i for i, bounds in enumerate(raw['sources']) if bounds]
    return boxes


def keyshape_preset_box(role, position, source_bounds, size, shape, *, custom=False):
    """Port of the 64px presetBox in web/side-pairs/src/lib/editor.svelte.js."""
    presets = {'main': (48, range(32, 65, 4), 48),
               'sub': (32, range(12, 45, 4), 32)}
    if role not in presets:
        raise ValueError('unknown part role')
    base, sizes, canvas = presets[role]
    if isinstance(size, bool) or not isinstance(size, int):
        raise ValueError(f'{role} size must be an integer grid unit')
    if custom:
        if not min(sizes) <= size <= max(sizes):
            raise ValueError(f'{role} custom size must be between {min(sizes)} and {max(sizes)}')
        if shape != 'own':
            raise ValueError('custom size must keep the source keyshape proportions')
    elif size not in sizes:
        raise ValueError(f'{role} preset size must be one of {list(sizes)}')
    shapes = keyshape_tables()[role]
    if shape == 'own':
        k = size / canvas
        w = round((source_bounds[2] - source_bounds[0]) * k)
        h = round((source_bounds[3] - source_bounds[1]) * k)
    elif shape in shapes:
        bounds = shapes[shape]
        w = bounds[2] - bounds[0] + size - base
        h = bounds[3] - bounds[1] + size - base
    else:
        raise ValueError(f'unknown {role} keyshape: {shape}')
    # Production side layouts reserve 4px from the painted edge of the canvas.
    # The source editor uses PADDING=2; applying that here incorrectly marks the
    # approved 4px production placements as outside their keyshapes.
    inner = 64 - 2 * PAIR_PAINTED_PADDING
    if w < 4 or h < 4 or w + 4 > inner or h + 4 > inner:
        raise ValueError(f'{role} keyshape preset is too large for the 64px canvas')
    px, py = ANCHORS[position]
    ax, ay = (1-px, 1-py) if role == 'main' else (px, py)
    x = round(PAIR_PAINTED_PADDING + (inner - w - 4) * ax) + 2
    y = round(PAIR_PAINTED_PADDING + (inner - h - 4) * ay) + 2
    return [x, y, x+w, y+h]


def adjusted_layout(boxes, change, *, role=None, position=None, source_bounds=None):
    """Move/resize role boxes using the source editor's keyshape preset mapping."""
    if any(key in change for key in ('scale', 'scale_x', 'scale_y')):
        raise ValueError('percentage scales are disabled; choose a preset or custom grid size')
    dx, dy = change.get('dx', 0), change.get('dy', 0)
    if any(isinstance(v, bool) or not isinstance(v, int) for v in (dx, dy)):
        raise ValueError('layout moves must snap to integer grid units')
    if not boxes:
        raise ValueError('part has no saved layout boxes')
    if 'units' in change:
        return copy.deepcopy(change['units'])
    left = min(box['x'] for box in boxes)
    top = min(box['y'] for box in boxes)
    right = max(box['x'] + box['w'] for box in boxes)
    bottom = max(box['y'] + box['h'] for box in boxes)
    if role is None or position is None or source_bounds is None:
        raise ValueError('keyshape resize needs role, position, and source bounds')
    custom = change.get('mode') == 'custom'
    target = keyshape_preset_box(role, position, source_bounds,
                                change['size'],
                                'own' if custom else change['shape'],
                                custom=custom)
    fw, fh = right-left, bottom-top
    if fw <= 0 or fh <= 0:
        raise ValueError('keyshape resize needs a nonempty part box')
    result = copy.deepcopy(boxes)
    for box in result:
        x0 = round(target[0] + (box['x'] - left) * (target[2]-target[0]) / fw)
        y0 = round(target[1] + (box['y'] - top) * (target[3]-target[1]) / fh)
        x1 = round(target[0] + (box['x'] + box['w'] - left) * (target[2]-target[0]) / fw)
        y1 = round(target[1] + (box['y'] + box['h'] - top) * (target[3]-target[1]) / fh)
        box.update(x=x0+dx, y=y0+dy, w=max(1, x1-x0) if box['w'] else 0,
                   h=max(1, y1-y0) if box['h'] else 0)
    return result


def within_canvas(geometry):
    return not geometry.is_empty and all(-0.01 <= v <= 64.01 for v in geometry.bounds)


def keyshape_validation(role, position, source_bounds, boxes, change):
    source_shape = source_keyshape_name(role, source_bounds)
    current = [min(box['x'] for box in boxes), min(box['y'] for box in boxes),
               max(box['x']+box['w'] for box in boxes), max(box['y']+box['h'] for box in boxes)]
    result = {'source_shape': source_shape, 'centerline_box': current,
              'stroke_envelope_inside_canvas': all((current[0] >= 2, current[1] >= 2,
                                                     current[2] <= 62, current[3] <= 62))}
    preset_mode = 'size' in change or 'shape' in change
    mode = change.get('mode', 'preset') if preset_mode else 'baseline'
    custom = mode == 'custom'
    guide_shape = ('own' if custom else change.get('shape', 'own') if preset_mode
                   else source_shape if source_shape != 'custom' else 'own')
    icon_size = change.get('size', 48 if role == 'main' else 32)
    size = change.get('guide_size', icon_size) if preset_mode else \
        change.get('guide_size', 48 if role == 'main' else 32)
    target = keyshape_preset_box(role, position, source_bounds, size, guide_shape,
                                 custom=custom)
    overflow = max(0, target[0]-current[0], target[1]-current[1],
                   current[2]-target[2], current[3]-target[3])
    original_w = source_bounds[2]-source_bounds[0]
    original_h = source_bounds[3]-source_bounds[1]
    actual_w = current[2]-current[0]
    actual_h = current[3]-current[1]
    aspect_error = abs(actual_w/original_w - actual_h/original_h) if original_w and original_h else 0
    result.update({'preset': source_shape if custom else guide_shape,
                   'size': icon_size, 'guide_size': size, 'mode': mode,
                   'keyshape_overflow_px': round(overflow, 3),
                   'aspect_error': round(aspect_error, 3),
                   'target_centerline_box': target,
                   'fits_keyshape': overflow <= .05 and
                   (mode == 'preset' or 'units' in change or aspect_error <= .05)})
    target = result['target_centerline_box']
    result['guide_painted_box'] = [target[0]-2, target[1]-2, target[2]+2, target[3]+2]
    result['guide_kind'] = 'circle' if result['preset'] == 'CIRCLE' else 'rect'
    return result


def keyshape_ink_outside(geometry, check):
    painted = check['guide_painted_box']
    if check['guide_kind'] == 'circle':
        cx, cy = (painted[0]+painted[2])/2, (painted[1]+painted[3])/2
        radius = (painted[2]-painted[0])/2
        guide = Point(cx, cy).buffer(radius, quad_segs=96)
    else:
        guide = geometry_box(*painted)
    return geometry.difference(guide.buffer(.25)).area


def validate_locked_change(role, position, source_bounds, change, source_layout=None):
    """Accept only grid-snapped preset or custom sizes with a locked source shape."""
    if not isinstance(change, dict):
        raise ValueError(f'{role} layout change must be an object')
    if any(key in change for key in ('scale', 'scale_x', 'scale_y')):
        raise ValueError(f'{role} percentage scales are disabled; choose a preset or custom grid size')
    mode = change.get('mode', 'preset')
    if mode not in ('preset', 'custom'):
        raise ValueError(f'{role} resize mode must be preset or custom')
    source_shape = source_keyshape_name(role, source_bounds)
    expected_shape = source_shape if source_shape != 'custom' else 'own'
    if change.get('shape') != expected_shape:
        raise ValueError(f'{role} keyshape is locked to {expected_shape}')
    if 'size' not in change:
        raise ValueError(f'{role} icon size is required')
    size = change['size']
    guide_size = change.get('guide_size', size)
    keyshape_preset_box(role, position, source_bounds, size,
                        'own' if mode == 'custom' else expected_shape,
                        custom=mode == 'custom')
    keyshape_preset_box(role, position, source_bounds, guide_size,
                        'own' if mode == 'custom' else expected_shape,
                        custom=mode == 'custom')
    for axis in ('dx', 'dy'):
        value = change.get(axis, 0)
        if isinstance(value, bool) or not isinstance(value, int) or not -64 <= value <= 64:
            raise ValueError(f'{role} {axis} must snap to an integer grid unit')
    if 'units' in change:
        units = change['units']
        if not isinstance(units, list) or not units or source_layout is None:
            raise ValueError(f'{role} element layout must be a nonempty list')
        expected = sorted(path for box in source_layout for path in box.get('paths', []))
        actual = []
        for unit in units:
            if not isinstance(unit, dict) or not isinstance(unit.get('paths'), list) or not unit['paths']:
                raise ValueError(f'{role} element paths are required')
            if any(isinstance(path, bool) or not isinstance(path, int) for path in unit['paths']):
                raise ValueError(f'{role} element paths must be integers')
            actual.extend(unit['paths'])
            for axis in ('x', 'y', 'w', 'h'):
                value = unit.get(axis)
                if isinstance(value, bool) or not isinstance(value, int) or not -64 <= value <= 128:
                    raise ValueError(f'{role} element {axis} must be an integer grid unit')
            if unit['w'] < 0 or unit['h'] < 0:
                raise ValueError(f'{role} element size cannot be negative')
        if sorted(actual) != expected:
            raise ValueError(f'{role} element layout must place each original path exactly once')


def main_geometries(name, source, fill):
    choices = {'current': (load_fill(fill)[0], fill),
               'outline': (load_fill(source)[0], source)}
    policy = main_variant_policy(name)
    # Policy-rejected variants are still shown in the gallery, so the editor can compose them too;
    # a saved layout is only a candidate awaiting visual review either way.
    for variant, geometry in region_variants(name, source, policy.get('groups', {}))[0]:
        choices[variant] = (geometry, None)
    return choices


def render_baseline_stress(pair_id, variant, out, layouts_path=DEFAULT_LAYOUTS):
    """Render the actual 8px cut for one existing filled Normal main variant."""
    if variant == 'outline':
        return None
    item = next((row for row in json.loads(layouts_path.read_text())['items']
                 if row['reference_id'] == pair_id), None)
    if item is None:
        raise ValueError(f'unknown side pair: {pair_id}')
    parts = {part['role']: part for part in item['parts']}
    main_part, sub_part = parts['main'], parts['sub']
    main_source, sub_source = checked_source(main_part, 'main'), checked_source(sub_part, 'sub')
    main_fill, sub_fill = fill_path(main_part, 'main'), fill_path(sub_part, 'sub')
    choices = main_geometries(main_part['icon'].split('/', 1)[1], main_source, main_fill)
    if variant not in choices:
        return None
    cls = repo_layout_svg()
    geometry, fill_file = choices[variant]
    main = place(cls, geometry, main_source, main_part['layout'], fill_file)
    sub = place(cls, load_fill(sub_fill)[0], sub_source, sub_part['layout'], sub_fill)
    cut, details = cut_main(main, sub, 8)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(geometry_to_svg(unary_union([cut, sub]), '0 0 64 64'))
    border_losses = [
        {'region': node['id'], 'lost_black_border_px2': round(
            main.intersection(node['geometry'].buffer(4)).difference(cut).area, 2)}
        for node in region_graph(main)[0] if node['kind'] == 'white']
    return {'svg': str(out), 'sha256': digest(out), 'gap_px': details['gap'],
            'white_border_loss_at_8px': border_losses}


DRAWABLE = ('path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon')


def omitted_main(out, pair_id, label, source, fill, omit, base):
    """Copies of the main source and stroke-fill with the listed drawing elements left out.

    Elements are numbered in document order as the layout's `paths` are. The source keeps every
    element (so the numbering holds) with the omitted ones unstroked; the stroke-fill loses their
    black or white stroke, so a white digit cut becomes solid fill. Only `current` and `outline`.
    """
    import xml.etree.ElementTree as ET
    from .stroke_fill_format import element_index, is_stroke_fill
    if base not in ('current', 'outline'):
        raise ValueError(f'{label}: omit_main_elements supports the current fill or the outline only')
    if not all(isinstance(index, int) and index >= 0 for index in omit):
        raise ValueError(f'{label}: omit_main_elements must list element numbers')
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    folder = out / 'omit' / f'{pair_id}--{label}'
    folder.mkdir(parents=True, exist_ok=True)
    root = ET.fromstring(source.read_text())
    drawn = [el for el in root.iter() if el.tag.split('}')[-1] in DRAWABLE]
    if max(omit) >= len(drawn):
        raise ValueError(f'{label}: the main has only {len(drawn)} elements')
    for index in omit:
        drawn[index].set('stroke', 'none')
        drawn[index].set('fill', 'none')
    source_copy = folder / 'source.svg'
    source_copy.write_text(ET.tostring(root, encoding='unicode'))
    choices = {'outline': (load_fill(source_copy)[0], source_copy)}
    if base == 'current':
        if not is_stroke_fill(fill):
            raise ValueError(f'{label}: omitting elements needs a stroke-fill main fill')
        fill_root = ET.fromstring(fill.read_text())
        for group in fill_root.iter():
            for child in list(group):
                if element_index(child) in omit:
                    group.remove(child)
        fill_copy = folder / 'fill.svg'
        fill_copy.write_text(ET.tostring(fill_root, encoding='unicode'))
        choices['current'] = (load_fill(fill_copy)[0], fill_copy)
    return source_copy, choices, choices['outline'][0]


def render_one(pair_id, *, layouts_path=DEFAULT_LAYOUTS, specs_path=DEFAULT_SPECS,
               out=DEFAULT_OUT, allow_keyshape_mismatch=False):
    layout_items = json.loads(layouts_path.read_text())['items']
    item = next((item for item in layout_items if item['reference_id'] == pair_id), None)
    if item is None:
        raise ValueError(f'unknown side pair: {pair_id}')
    specs = json.loads(specs_path.read_text())
    if specs.get('schema') != 'side-ai-layout-proposals/v1':
        raise ValueError('invalid layout proposal schema')
    proposals = specs.get('pairs', {}).get(pair_id, [])
    if not proposals:
        raise ValueError(f'no layout proposals for {pair_id}')
    parts = {part['role']: part for part in item['parts']}
    main_part, sub_part = parts['main'], parts['sub']
    main_source, sub_source = checked_source(main_part, 'main'), checked_source(sub_part, 'sub')
    main_fill, sub_fill = fill_path(main_part, 'main'), fill_path(sub_part, 'sub')
    if not main_fill.is_file() or not sub_fill.is_file():
        raise ValueError('main or sub fill is missing')
    cls = repo_layout_svg()
    main_saved_layout = layout_with_paths(cls, main_source, main_part['layout'], 'main')
    sub_saved_layout = layout_with_paths(cls, sub_source, sub_part['layout'], 'sub')
    main_name = main_part['icon'].split('/', 1)[1]
    choices = main_geometries(main_name, main_source, main_fill)
    sub_choices = {'fill': (load_fill(sub_fill)[0], sub_fill),
                   'outline': (load_fill(sub_source)[0], None)}
    main_outline_geometry = load_fill(main_source)[0]
    sub_has_fill = sub_choices['fill'][0].symmetric_difference(sub_choices['outline'][0]).area > 1
    source_position = sub_part['position']
    main_bounds = source_centerline_bounds(cls, main_source, 'main')
    sub_bounds = source_centerline_bounds(cls, sub_source, 'sub')
    seen = set()
    entries = []
    (out / 'svg').mkdir(parents=True, exist_ok=True)
    for proposal in proposals:
        label = proposal.get('id')
        if not isinstance(label, str) or not ID.fullmatch(label) or label in seen:
            raise ValueError(f'invalid or duplicate proposal id: {label!r}')
        seen.add(label)
        base = proposal.get('base_variant')
        # User-authorised, pair-local deletion of main source elements (e.g. one digit under the sub).
        omit = proposal.get('omit_main_elements') or []
        src_p, choices_p, outline_p = main_source, choices, main_outline_geometry
        if omit:
            src_p, choices_p, outline_p = omitted_main(out, pair_id, label, main_source, main_fill, omit, base)
        sub_variant = proposal.get('sub_variant', 'fill')
        overlap_mode = proposal.get('overlap_mode', 'clear')
        position = proposal.get('position', source_position)
        if position not in ANCHORS:
            raise ValueError(f'{label}: unknown pair position {position!r}')
        if base not in choices_p:
            raise ValueError(f'unknown Normal main variant: {base}')
        if sub_variant not in sub_choices:
            raise ValueError(f'unknown Normal sub variant: {sub_variant}')
        if overlap_mode not in ('clear', 'join'):
            raise ValueError(f'{label}: unknown overlap mode {overlap_mode!r}')
        if overlap_mode == 'join' and (base == 'outline' or sub_variant != 'outline'):
            raise ValueError(f'{label}: joined overlap needs a filled main and original outline sub')
        main_has_fill = (base != 'outline' and
                         choices_p[base][0].symmetric_difference(outline_p).area > 1)
        if not main_has_fill and not (sub_variant == 'fill' and sub_has_fill):
            raise ValueError('a fill side combination needs a filled main or sub')
        if not proposal.get('reason'):
            raise ValueError(f'proposal {label} needs a visual reason')
        # A user's manual edit may be forced past its keyshape guide; the 64px canvas limits still apply.
        override = proposal.get('keyshape_override', False)
        if not isinstance(override, bool):
            raise ValueError(f'{label}: keyshape_override must be true or false')
        allow_mismatch = allow_keyshape_mismatch or override
        validate_locked_change('main', position, main_bounds, proposal.get('main', {}), main_saved_layout)
        validate_locked_change('sub', position, sub_bounds, proposal.get('sub', {}), sub_saved_layout)
        main_layout = adjusted_layout(main_saved_layout, proposal.get('main', {}),
                                      role='main', position=position, source_bounds=main_bounds)
        sub_layout = adjusted_layout(sub_saved_layout, proposal.get('sub', {}),
                                     role='sub', position=position, source_bounds=sub_bounds)
        keyshape_checks = {'main': keyshape_validation('main', position, main_bounds, main_layout,
                                                       proposal.get('main', {})),
                           'sub': keyshape_validation('sub', position, sub_bounds, sub_layout,
                                                      proposal.get('sub', {}))}
        if not allow_mismatch and any(check['fits_keyshape'] is False for check in keyshape_checks.values()):
            raise ValueError(f'{label}: layout does not fit the selected keyshape')
        for role, boxes in (('main', main_layout), ('sub', sub_layout)):
            if any(box['x'] < 2 or box['y'] < 2 or box['x']+box['w'] > 62 or
                   box['y']+box['h'] > 62 for box in boxes):
                raise ValueError(f'{label}: {role} 4px stroke envelope is outside 64x64')
        main_geometry, main_file = choices_p[base]
        main = place(cls, main_geometry, src_p, main_layout, main_file)
        sub_geometry, sub_file = sub_choices[sub_variant]
        # Very small filled subs need their source detail widths scaled with the
        # icon. Keeping a 4px stroke here closes tiny white marks such as cubes.
        small_sub = sub_variant == 'fill' and proposal['sub']['size'] < 20
        sub = (place_part(cls, sub_geometry, sub_source.read_text(), sub_layout,
                          sub_file, scale_stroke_weight=True)[0] if small_sub else
               place(cls, sub_geometry, sub_source, sub_layout, sub_file))
        for role, geometry in (('main', main), ('sub', sub)):
            check = keyshape_checks[role]
            check['ink_outside_guide_px2'] = round(keyshape_ink_outside(geometry, check), 3)
            if check['ink_outside_guide_px2'] > .5:
                check['fits_keyshape'] = False
        if not allow_mismatch and any(check['fits_keyshape'] is False for check in keyshape_checks.values()):
            raise ValueError(f'{label}: painted icon exceeds its keyshape guide')
        if not within_canvas(main) or not within_canvas(sub):
            raise ValueError(f'{label}: main or sub ink is outside 64x64')
        if overlap_mode == 'join':
            if main.intersection(sub).area <= .05:
                raise ValueError(f'{label}: joined parts must touch')
            cut, details = main, {'gap': 0.0}
        elif base == 'outline':
            placed_outline = placed_outline_svg(cls, src_p, main_layout)
            cut, details = cut_outline_strokes(placed_outline, sub, GAP)
        else:
            cut, details = cut_main(main, sub, GAP)
        combined = unary_union([cut, sub])
        if not within_canvas(combined):
            raise ValueError(f'{label}: combined ink is outside 64x64')
        validation = clearance(sub, 8)
        white_nodes = [] if base == 'outline' else [
            node for node in region_graph(main)[0] if node['kind'] == 'white']
        stress_file = None
        stress_details = None
        white_boundary_losses = []
        if base != 'outline':
            stress_cut, stress_details = ((main, {'gap': 0.0}) if overlap_mode == 'join'
                                          else cut_main(main, sub, 8))
            stress_combined = unary_union([stress_cut, sub])
            stress_file = out / 'stress' / f'{pair_id}--layout-{label}--8px.svg'
            stress_file.parent.mkdir(parents=True, exist_ok=True)
            stress_file.write_text(geometry_to_svg(stress_combined, '0 0 64 64'))
            white_boundary_losses = [
                {'region': node['id'], 'lost_black_border_px2': round(
                    main.intersection(node['geometry'].buffer(4)).difference(stress_cut).area, 2)}
                for node in white_nodes]
        white_overlaps = [
            {'region': node['id'], 'area_px2': round(node['geometry'].area, 2),
             'overlap_px2': round(node['geometry'].intersection(validation).area, 2)}
            for node in white_nodes if node['geometry'].intersection(validation).area > 0.05]
        graph = analyze_overlap(main, sub, cut, combined, clearance(sub, GAP))
        path = out / 'svg' / f'{pair_id}--layout-{label}.svg'
        path.write_text(geometry_to_svg(combined, '0 0 64 64'))
        entries.append({'id': label, 'variant': f'layout-{label}', 'base_variant': base,
                        'sub_variant': sub_variant, 'overlap_mode': overlap_mode,
                        'position': position,
                        'svg': str(path.relative_to(out)), 'candidate_sha256': digest(path),
                        'main': proposal.get('main', {}), 'sub': proposal.get('sub', {}),
                        'layout_boxes': {'main': main_layout, 'sub': sub_layout},
                        'sub_stroke_mode': 'scaled' if small_sub else
                        'source_outline' if sub_variant == 'outline' else 'fixed_4px',
                        'keyshape_validation': keyshape_checks,
                        'keyshape_override': override,
                        'reason': proposal['reason'], 'main_bounds': [round(v, 2) for v in main.bounds],
                        'sub_bounds': [round(v, 2) for v in sub.bounds],
                        'render_gap_px': details['gap'],
                        'white_regions_inside_8px': white_overlaps,
                        'white_border_loss_at_8px': white_boundary_losses,
                        'stress_svg': str(stress_file.relative_to(out)) if stress_file else None,
                        'stress_sha256': digest(stress_file) if stress_file else None,
                        'stress_gap_px': stress_details['gap'] if stress_details else None,
                        'graph_status': graph['status'], 'graph_issues': graph['issues'],
                        'status': 'awaiting_visual_review'})
    report_path = out / 'report.json'
    report = json.loads(report_path.read_text()) if report_path.exists() else {
        'schema': 'side-ai-layout-renderings/v1', 'pairs': {}}
    if report.get('schema') != 'side-ai-layout-renderings/v1':
        raise ValueError('invalid existing layout report schema')
    report['pairs'][pair_id] = {'concept': item['concept'], 'main': main_part['icon'],
                                'sub': sub_part['icon'], 'layout_sha256': digest(layouts_path),
                                'specs_sha256': digest(specs_path),
                                'pair_specs_sha256': hashlib.sha256(json.dumps(
                                    proposals, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                                'main_source_sha256': digest(main_source),
                                'sub_source_sha256': digest(sub_source),
                                'main_fill_sha256': digest(main_fill),
                                'sub_fill_sha256': digest(sub_fill),
                                'candidates': entries}
    report_path.write_text(json.dumps(report, indent=2) + '\n')
    current_files = {out / candidate['svg'] for candidate in entries}
    current_stress = {out / candidate['stress_svg'] for candidate in entries if candidate['stress_svg']}
    for old_file in (out / 'svg').glob(f'{pair_id}--layout-*.svg'):
        if old_file not in current_files:
            old_file.unlink()
    for old_file in (out / 'stress').glob(f'{pair_id}--layout-*--8px.svg') if (out / 'stress').exists() else ():
        if old_file not in current_stress:
            old_file.unlink()
    return report['pairs'][pair_id]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--id', required=True, help='Review exactly one side pair')
    parser.add_argument('--layouts', type=Path, default=DEFAULT_LAYOUTS)
    parser.add_argument('--specs', type=Path, default=DEFAULT_SPECS)
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
    print(json.dumps(render_one(args.id, layouts_path=args.layouts,
                                specs_path=args.specs, out=args.out), indent=2))


if __name__ == '__main__':
    main()
