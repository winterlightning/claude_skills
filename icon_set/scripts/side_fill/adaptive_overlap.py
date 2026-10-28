"""Validate main fill variants at a wider clearance; render with the standard gap.

Run from the workspace root:
    python3 -m side_combinations.adaptive_overlap --ids ID [ID ...]

The original source and saved layouts are never changed. Candidate fills are
assembled with the existing region engine and rendered as separate evidence.
"""
from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import ast
import hashlib
import html
import json
from functools import lru_cache
from pathlib import Path

from shapely.affinity import affine_transform
from shapely.geometry import LineString
from shapely.ops import unary_union

from ...vendor.fill_processing.vendor.fill_utils import assemble_polygon, build_region_dataframe, load_one, stroke_to_polygon
from ...vendor.fill_processing.workflow.recipes import transfer

from .combine_fill_side import (GAP, ROOT, clearance, cut_main,
                                cut_outline_strokes, geometry_to_svg, load_fill)
from .combine_fill_side_layouts import (DEFAULT_LAYOUTS, element_segments, layout_groups,
                                        outline_boxes, place_part, repo_layout_svg)
from .graph_overlap import analyze as analyze_overlap

EXTRA_GAP = 4.0
MAX_ADDED_FILL_IN_VALIDATION = 4.0  # px² at 64px; small boundary differences
MAIN_VARIANT_POLICY = DATA / 'data/main-region-variant-policy.json'


MAIN48_USER_MARKS = DATA / 'data/main48-user-review-marks.json'
MAIN48_SOURCES = DATA / 'data/latest-side-main-48'


def main48_user_mark(name):
    """The user's main48 review mark for this main, when it was made on the current source."""
    if not MAIN48_USER_MARKS.exists():
        return {}
    mark = json.loads(MAIN48_USER_MARKS.read_text()).get('marks', {}).get(name, {})
    source = MAIN48_SOURCES / f'{name}.svg'
    if not mark or not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != mark.get('source_sha256'):
        return {}
    return mark


def main_variant_policy(name):
    """The side policy for a main, with the user's main48 review choices applied on top.

    A variant the user removed on the main48 review page (`approved:<variant>`) is rejected here
    too; "Retain original" rejects every region/group variant (`reject_all`).
    """
    policy = {'approved': [], 'rejected': [], 'groups': {}}
    if MAIN_VARIANT_POLICY.exists():
        data = json.loads(MAIN_VARIANT_POLICY.read_text())
        if data.get('schema') != 'side-main-region-variant-policy/v1':
            raise ValueError('invalid main region variant policy schema')
        policy = json.loads(json.dumps(data.get('mains', {}).get(name, policy)))
    mark = main48_user_mark(name)
    removed = [item.split(':', 1)[1] for item in mark.get('removed_variants', []) if item.startswith('approved:')]
    policy['rejected'] = list(dict.fromkeys(policy.get('rejected', []) + removed))
    policy['approved'] = [v for v in policy.get('approved', []) if v not in removed]
    if mark.get('action') == 'retain':
        policy['reject_all'] = True
    return policy


def variant_rejected(policy, label):
    return policy.get('reject_all', False) or label in policy.get('rejected', [])


def source_path(part, role):
    name = part['icon'].split('/', 1)[1]
    if role == 'main':
        return DATA / 'normal' / f'{name}.svg'
    path = DATA / 'archive/side-sub-32' / f'{name}.svg'
    if path.exists():
        return path
    return DATA / 'archive/sub-32-revisions' / name / f"{part.get('current_sha') or part['built_sha']}.svg"


def fill_path(part, role):
    name = part['icon'].split('/', 1)[1]
    revision = part.get('current_sha') or part['built_sha']
    if role == 'main':
        # Reviewed stroke-fill mains (publish_stroke_fills.py), else the shared 48px collection.
        current = DATA / 'data/current-normal-fill-48' / name / f'{revision}.svg'
        return current if current.is_file() else DATA / 'normal-fill' / f'{name}.svg'
    current = DATA / 'data/current-normal-fill-32' / name / f'{revision}.svg'
    if current.is_file():
        return current
    return DATA / 'data/legacy-normal-fill-32' / name / f'{revision}.svg'


def checked_source(part, role):
    path = source_path(part, role)
    expected = part.get('current_sha') or part['built_sha']
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f'{role} saved source is missing or differs from its layout hash')
    return path


def place(cls, geometry, source, layout, fill_file=None):
    return place_part(cls, geometry, source.read_text(), layout, fill_file)[0]


def source_detail_losses(cls, source, layout, clear):
    """Measure cut exposure of each original stroke element after saved placement."""
    try:
        segments = element_segments(cls, source.read_text())
        groups = layout_groups(cls, segments, layout)
    except (ValueError, IndexError):
        return []
    maps = {index: transform for members, _, transform in groups for index in members}
    elements = []
    for index, paths in enumerate(segments):
        if index not in maps:
            continue
        sx, sy, dx, dy = maps[index]
        ink = unary_union([affine_transform(LineString(points), [sx, 0, 0, sy, dx, dy]).buffer(2)
                           for points in paths if len(points) > 1])
        if ink.is_empty or ink.area < 1:
            continue
        elements.append((index, ink))
    if not elements:
        return []
    primary = max(elements, key=lambda pair: pair[1].area)[0]
    return [{'element': index, 'role': 'primary' if index == primary else 'detail',
             'ink_px2': round(ink.area, 2),
             'cut_px2': round(ink.intersection(clear).area, 2),
             'cut_fraction': round(ink.intersection(clear).area / ink.area, 3)}
            for index, ink in elements]


def region_recipe(name, source):
    home = DATA / 'recipes'
    paths = [home / 'overrides' / f'{name}.json']
    paths += sorted((home / 'icons' / name).glob('attempt-*/recipe.json'), reverse=True)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    for path in paths:
        if not path.exists():
            continue
        recipe = json.loads(path.read_text())
        if (recipe.get('schema') == 'normal-region-decisions/v1'
                and recipe.get('mode') == 'regions'
                and recipe.get('sources', {}).get('normal', {}).get('sha256') == digest
                and not recipe.get('closures') and not recipe.get('native_closures')):
            return recipe, path
    return None, None


def region_variants(name, source, groups=None):
    """Source-bound single-region and named grouped-region fill choices."""
    recipe, path = region_recipe(name, source)
    if recipe is None:
        return [], None
    row = load_one(str(source), edge_close=recipe['closure_requested'])
    df = build_region_dataframe(row['stroke_polygon'], recipe['adjacency_distance'])
    if df.empty:
        return [], str(path)
    df['fill'] = 'keep'
    transfer(recipe['regions'], df)
    original = {int(r.region_id): r.fill for _, r in df.iterrows()}
    regions = df.set_index('region_id')
    root_holes = {int(r.region_id) for _, r in df.iterrows()
                  if r.ring == 'hole' and r.parent_id is not None and r.parent_id == r.parent_id
                  and regions.loc[int(r.parent_id)].ring == 'exterior'
                  and regions.loc[int(r.parent_id)].level == 1}
    parents = {int(r.region_id): int(r.parent_id) if r.parent_id is not None and r.parent_id == r.parent_id else None
               for _, r in df.iterrows()}

    def owning_hole(region_id):
        while region_id is not None:
            if region_id in root_holes:
                return region_id
            region_id = parents.get(region_id)
        return None

    nested_holes = {int(r.region_id) for _, r in df.iterrows()
                    if r.ring == 'hole' and r.level > 2
                    and owning_hole(int(r.region_id)) is not None}

    selections = [(f'region-{region_id}', {region_id}, (), (), False, ())
                  for region_id in sorted(root_holes)]
    for group_name, spec in (groups or {}).items():
        ids = spec if isinstance(spec, list) else spec.get('fill', [])
        white_regions = () if isinstance(spec, list) else tuple(spec.get('white_regions', []))
        white_strokes = () if isinstance(spec, list) else tuple(spec.get('white_strokes', []))
        white_native_fills = False if isinstance(spec, list) else spec.get('white_native_fills', False)
        black_strokes_over = () if isinstance(spec, list) else tuple(spec.get('black_strokes_over', []))
        selected = set(ids)
        if (not selected or not selected <= root_holes | nested_holes
                or (len(selected) == 1 and selected <= root_holes
                    and not (white_regions or white_strokes or white_native_fills))
                or not isinstance(white_native_fills, bool)
                or any(region_id not in regions.index or regions.loc[region_id].ring != 'exterior'
                       for region_id in white_regions)):
            raise ValueError(f'invalid source region group {group_name}: {spec}')
        selections.append((f'group-{group_name}', selected, white_regions, white_strokes,
                           white_native_fills, black_strokes_over))
    if len(root_holes) >= 3:
        largest = max(root_holes, key=lambda region_id: regions.loc[region_id].geometry.area)
        small_regions = root_holes - {largest}
        if not any(selected == small_regions and not white_regions and not white_strokes
                   and not white_native_fills and not black_strokes_over
                   for _, selected, white_regions, white_strokes, white_native_fills,
                   black_strokes_over in selections):
            selections.append(('group-all-small', small_regions, (), (), False, ()))
    choices = []
    for (label, selected, white_regions, white_strokes, white_native_fills,
         black_strokes_over) in selections:
        selected_roots = selected & root_holes
        selected_nested = selected & nested_holes
        choice = df.copy()
        for idx, other in choice.iterrows():
            owner = owning_hole(int(other.region_id))
            if owner is None:
                continue
            if int(other.region_id) == owner:
                choice.at[idx, 'fill'] = 'fill' if owner in selected_roots else 'keep'
            elif owner not in selected_roots:
                # A source detail inside an unfilled region must remain its
                # original black stroke, not a cutout intended for a solid fill.
                choice.at[idx, 'fill'] = 'keep'
            else:
                choice.at[idx, 'fill'] = original[int(other.region_id)]
        geometry = assemble_polygon(choice)
        # assemble_polygon omits nested black islands when their enclosing
        # hole stays white. Reinsert those exact source stroke polygons.
        native_details = [other.geometry for _, other in df.iterrows()
                          if other.ring == 'exterior' and other.level > 1
                          and (owner := owning_hole(int(other.region_id))) is not None
                          and owner not in selected_roots]
        geometry = unary_union([g for g in (geometry, row['filled_polygon'], *native_details,
                                           *(regions.loc[region_id].geometry for region_id in selected_nested))
                                if g is not None])
        selected_region = unary_union([regions.loc[region_id].geometry for region_id in selected])
        for cut in recipe.get('native_cuts', []):
            # Native black dots become white only inside the newly filled
            # region. Else they stay as original black marks.
            from shapely import wkt
            native_cut = wkt.loads(cut['geometry_wkt'])
            if selected_region.intersection(native_cut).area >= native_cut.area * 0.5:
                geometry = geometry.difference(native_cut)
        if white_regions:
            geometry = geometry.difference(unary_union([regions.loc[region_id].geometry
                                                        for region_id in white_regions]))
        if white_strokes or black_strokes_over:
            by_source_id = {shape['source_id']: shape for shape in row['shapes']}
            missing = (set(white_strokes) | set(black_strokes_over)) - by_source_id.keys()
            if missing:
                raise ValueError(f'unknown source stroke in {label}: {sorted(missing)}')
        if white_strokes:
            white_ink = stroke_to_polygon([by_source_id[source_id] for source_id in white_strokes],
                                          ast.literal_eval(row['viewbox']))
            geometry = geometry.difference(white_ink)
        if white_native_fills:
            # The original SVG's solid marks (for example a wallet's button)
            # are exact source geometry, not inferred holes in the region mesh.
            # The selected group may reverse their polarity to white.
            geometry = geometry.difference(row['filled_polygon'])
        if black_strokes_over:
            # Source strokes drawn above the new white strokes keep the native
            # exterior and boundary lines continuous at their junctions.
            black_ink = stroke_to_polygon([by_source_id[source_id] for source_id in black_strokes_over],
                                          ast.literal_eval(row['viewbox']))
            geometry = geometry.union(black_ink)
        choices.append((label, geometry))
    return choices, str(path)


@lru_cache(maxsize=1024)
def cached_region_variants(name, source, groups_json):
    """Reuse source-bound geometry when one main appears in many side pairs."""
    return region_variants(name, source, json.loads(groups_json))


def analyze_item(item, out, cls, validation_gap):
    parts = {part['role']: part for part in item['parts']}
    main_part, sub_part = parts['main'], parts['sub']
    main_source = checked_source(main_part, 'main')
    sub_source = checked_source(sub_part, 'sub')
    main_fill = fill_path(main_part, 'main')
    sub_fill = fill_path(sub_part, 'sub')
    if not main_fill.exists() or not sub_fill.exists():
        raise ValueError('main or sub fill is missing')
    sub = place(cls, load_fill(sub_fill)[0], sub_source, sub_part['layout'], sub_fill)
    original = place(cls, load_fill(main_source)[0], main_source, main_part['layout'], main_source)
    current = place(cls, load_fill(main_fill)[0], main_source, main_part['layout'], main_fill)
    if any(value < -1e-6 or value > 64 + 1e-6 for geometry in (sub, current)
           for value in geometry.bounds):
        raise ValueError('outside_canvas')
    validation_clear = clearance(sub, validation_gap)
    render_clear = clearance(sub, GAP)
    source_losses = source_detail_losses(cls, main_source, main_part['layout'], validation_clear)
    name = main_part['icon'].split('/', 1)[1]
    policy = main_variant_policy(name)
    approved = set(policy.get('approved', []))
    rejected = set(policy.get('rejected', []))
    groups_json = json.dumps(policy.get('groups', {}), sort_keys=True)
    alternatives, recipe_path = cached_region_variants(name, main_source, groups_json)
    candidates = [('current', current, original, 'normal', 'base')]
    for label, geometry in alternatives:
        candidate = place(cls, geometry, main_source, main_part['layout'])
        if all(candidate.symmetric_difference(existing).area > 0.5 for _, existing, _, _, _ in candidates):
            status = 'rejected' if variant_rejected(policy, label) else 'approved' if label in approved else 'unreviewed'
            candidates.append((label, candidate, original, 'normal', status))
    candidates.append(('outline', original, original, 'normal', 'base'))
    rows = []
    for label, main, source_main, style, semantic_status in candidates:
        if label == 'outline':
            boxes = outline_boxes(cls, main_source.read_text(), main_part['layout'])
            if boxes is None:
                # Elements the layout cannot number cannot be rebaked as
                # strokes; cut the placed outline as paint instead.
                cut, details = cut_main(main, sub, GAP)
            else:
                placed = cls.component({'role': 'main', 'document': main_source.read_text(),
                                        'scale': 1, 'tx': 0, 'ty': 0, 'layout': boxes}, 64)['document']
                cut, details = cut_outline_strokes(placed, sub, GAP)
        else:
            cut, details = cut_main(main, sub, GAP)
        combined = unary_union([cut, sub])
        graph = analyze_overlap(main, sub, cut, combined, render_clear)
        added = main.difference(source_main)
        added_in_validation = added.intersection(validation_clear).area
        added_outside_validation = added.difference(validation_clear).area
        # The graph check compares a candidate against itself and can mark a
        # source counter as lost when the intentional notch opens it. Keep that
        # diagnostic, but choose by source-relative added-fill loss.
        safe = added_in_validation <= MAX_ADDED_FILL_IN_VALIDATION
        if label == 'current' and policy.get('exclude_current'):
            semantic_status = 'rejected'
        file = f"{item['reference_id']}--{label}.svg"
        svg = geometry_to_svg(combined, '0 0 64 64')
        (out / 'variants' / file).write_text(svg)
        rows.append({'variant': label, 'svg': f'variants/{file}', 'safe': safe,
                     'semantic_status': semantic_status, 'main_style': style, 'sub_style': 'normal',
                     'candidate_sha256': hashlib.sha256(svg.encode()).hexdigest(),
                     'added_fill_inside_validation_px2': round(added_in_validation, 2),
                     'added_fill_outside_validation_px2': round(added_outside_validation, 2),
                     'original_ink_inside_validation_px2': round(source_main.intersection(validation_clear).area, 2),
                     'render_gap_px': details['gap'], 'graph_status': graph['status'],
                     'graph_issues': graph['issues']})
    eligible = [r for r in rows if r['safe'] and r['semantic_status'] in ('base', 'approved')]
    if policy.get('prefer_current') and not policy.get('exclude_current') and rows[0]['safe']:
        chosen = rows[0]
    else:
        chosen = max(eligible, key=lambda r: (r['added_fill_outside_validation_px2'], r['variant'] == 'current')) if eligible else rows[-1]
    (out / 'svg' / f"{item['reference_id']}.svg").write_text((out / chosen['svg']).read_text())
    return {'id': item['reference_id'], 'concept': item['concept'], 'main': main_part['icon'],
            'sub': sub_part['icon'], 'render_gap_px': GAP,
            'extra_validation_px': validation_gap - GAP,
            'validation_gap_px': validation_gap, 'recipe': recipe_path, 'chosen': chosen['variant'],
            'source_element_losses': source_losses,
            'source_detail_needs_review': any(e['role'] == 'detail' and e['cut_fraction'] > 0.3
                                              for e in source_losses),
            'candidates': rows}


def gallery(rows):
    cards = []
    for item in rows:
        cards.append(f"<section><h2>{html.escape(item['concept'])}</h2><p>{html.escape(item['id'])} · chosen: <b>{html.escape(item['chosen'])}</b></p><div class='variants'>")
        for candidate in item['candidates']:
            label = html.escape(candidate['variant'])
            cards.append(f"<figure><img src='{html.escape(candidate['svg'])}'><figcaption>{label} · {candidate['semantic_status']}<br>fill inside {item['validation_gap_px']:g}px check: {candidate['added_fill_inside_validation_px2']} px²<br>fill outside check: {candidate['added_fill_outside_validation_px2']} px²<br>rendered gap: {candidate['render_gap_px']} px<br>{'safe' if candidate['safe'] else 'collision'}</figcaption></figure>")
        cards.append('</div></section>')
    return "<!doctype html><meta charset='utf-8'><title>Adaptive side overlap</title><style>body{font:15px system-ui;background:#f5f5f5;color:#222;max-width:1100px;margin:32px auto}section{background:white;padding:20px;margin:20px 0;border-radius:12px}.variants{display:flex;gap:14px;flex-wrap:wrap}figure{margin:0;padding:12px;border:1px solid #ddd;border-radius:8px}img{width:160px;height:160px;image-rendering:auto}figcaption{line-height:1.5}</style>" + ''.join(cards)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--layouts', type=Path, default=DEFAULT_LAYOUTS)
    parser.add_argument('--ids', nargs='*')
    parser.add_argument('--out', type=Path, default=WORK / 'adaptive-8px')
    parser.add_argument('--extra-gap', type=float, default=EXTRA_GAP)
    parser.add_argument('--summary-only', action='store_true')
    args = parser.parse_args(argv)
    if args.extra_gap < 0:
        parser.error('--extra-gap must be nonnegative')
    gap = GAP + args.extra_gap
    items = json.loads(args.layouts.read_text())['items']
    if args.ids:
        wanted = set(args.ids)
        items = [item for item in items if item['reference_id'] in wanted]
        missing = wanted - {item['reference_id'] for item in items}
        if missing:
            parser.error('unknown IDs: ' + ', '.join(sorted(missing)))
    for dirname in ('svg', 'variants'):
        (args.out / dirname).mkdir(parents=True, exist_ok=True)
    cls = repo_layout_svg()
    rows, errors = [], []
    for item in items:
        try:
            rows.append(analyze_item(item, args.out, cls, gap))
        except Exception as error:
            errors.append({'id': item['reference_id'], 'error': str(error)})
    used = {'svg': {f"{row['id']}.svg" for row in rows},
            'variants': {Path(candidate['svg']).name for row in rows for candidate in row['candidates']}}
    for dirname, names in used.items():
        for stale in (args.out / dirname).glob('*.svg'):
            if stale.name not in names:
                stale.unlink()
    (args.out / 'report.json').write_text(json.dumps({'rows': rows, 'errors': errors}, indent=2) + '\n')
    (args.out / 'index.html').write_text(gallery(rows))
    summary = {'generated': len(rows), 'errors': errors}
    if not args.summary_only:
        summary['chosen'] = {r['id']: r['chosen'] for r in rows}
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
