"""Fill side combinations placed by production's saved layouts (side-pairs.html / reference_parts.layout).

Each production part lists element groups of its stroke drawing (`paths`, element numbers) and the
centerline box (x, y, w, h) on the 64 canvas each group was put in. A part without `paths` records only
where the automatic placement put the whole drawing. combination_layout_svg.component maps each group
from its source box onto its box with its own sx, sy; the same maps move the fill.

- Every group moved by one map (`rigid`): the whole fill moves by it.
- Groups moved apart (`split`): the fill is divided between the groups by the nearest group centerline
  (Voronoi cells of points along them), and each piece moves with its group.
- A scaled group keeps the stroke weight at 4, as the stroke engine does. A fill kept as stroked
  lines is outlined again from its moved lines; a filled shape's outside moves in by 2 (s - 1),
  its slits narrow back to 4 and its counters widen.
The cut and clean-up are combine_fill_side.combine's.

Usage from the workspace root:
    python3 -m side_combinations.combine_fill_side_layouts build [--ids ID …] [--out PATH]
"""
from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
import hashlib
from functools import lru_cache
import json
import xml.etree.ElementTree as ET
from pathlib import Path


from shapely.affinity import affine_transform
from shapely.geometry import LineString, Polygon
from shapely.ops import substring, unary_union
from shapely.prepared import prep
from shapely.validation import make_valid

from .combine_fill_side import (CANVAS, HALF_STROKE, clearance, close_returning, cut_main,
                                geometry_to_svg, load_fill, polygons)
from .graph_overlap import analyze as analyze_overlap
from ...vendor.fill_processing.vendor.fill_utils import parse_all_shapes, stroke_to_polygon

DEFAULT_LAYOUTS = DATA / 'data/production-layouts.json'
SAME_MAP = 0.75             # px: groups whose maps place each other's boxes this close move as one
OWNER_SHARE = 0.9           # a fill part goes whole to a group holding this share of its ink overlap
SAMPLE_STEP = 0.5           # px between centerline points for the Voronoi split
MAX_GROUP_SCALE = 2.0       # a group scaled beyond this either way does not fit the drawing
MAX_GROUP_STRETCH = 1.5     # nor one whose axes scale this differently


def repo_layout_svg():
    from . import combination_layout_svg as cls
    return cls


def element_segments(cls, document):
    """Engine segments of each drawable element, in element order (the numbers a layout uses)."""
    root = ET.fromstring(document)
    attrs = {k: v for k, v in root.attrib.items() if k in cls.INHERITED}
    return [cls.segments_of(element, {**attrs, **own}) for element, own in cls.elements(root)]


def group_map(source, box):
    """(sx, sy, dx, dy) taking a source centerline box onto a layout box, as component() bakes it."""
    x0, y0, x1, y1 = source
    sx = box['w'] / (x1 - x0) if x1 - x0 > 1e-9 else None
    sy = box['h'] / (y1 - y0) if y1 - y0 > 1e-9 else None
    sx = sx if sx is not None else (sy if sy is not None else 1.0)
    sy = sy if sy is not None else sx
    return sx, sy, box['x'] - x0 * sx, box['y'] - y0 * sy


REVERSE_FILL_MANIFESTS = (WORK / 'main48-region-fill-review-stroke-fill/manifest.json',
                          WORK / 'sub32-region-fill-review-stroke-fill/manifest.json')


def reverse_fill_hashes():
    """SHA-256 of every fill the stroke-fill rework kept flat as a reverse fill.

    The user's rule: reverse fills stay exactly as they are. Their white strokes are cut-outs of a
    solid shape, so rebuilding them as 4px strokes on moved centerlines pushes round white caps out
    past the shape's edge; they are placed as the plain fill instead.
    """
    stamp = tuple(path.stat().st_mtime_ns if path.exists() else 0 for path in REVERSE_FILL_MANIFESTS)
    return _reverse_fill_hashes(stamp)


@lru_cache(maxsize=2)
def _reverse_fill_hashes(_stamp):
    hashes = set()
    for manifest in REVERSE_FILL_MANIFESTS:
        if not manifest.exists():
            continue
        for record in json.loads(manifest.read_text())['records']:
            if record.get('kind') == 'kept (reverse fill)':
                output = manifest.parent / record['output']
                if output.is_file():
                    hashes.add(hashlib.sha256(output.read_bytes()).hexdigest())
    return frozenset(hashes)


def is_reverse_fill(fill_path):
    """A reverse fill: listed by the rework, or an uploaded icon marked so (fill_icons.portable: id="reverse-fill")."""
    if not fill_path or not Path(fill_path).is_file():
        return False
    data = Path(fill_path).read_bytes()
    return b'id="reverse-fill"' in data[:600] or hashlib.sha256(data).hexdigest() in reverse_fill_hashes()


def apply_map(geometry, m):
    sx, sy, dx, dy = m
    return affine_transform(geometry, [sx, 0, 0, sy, dx, dy])


def keep_stroke_weight(geometry, m):
    """A scaled fill painted as a 4px stroke drawing: undo the scaling of its half stroke.

    Outer edges are a stroke's outside, so they move in by the extra half stroke. A thin hole is a
    negative stroke (a slit) and narrows back to 4; a wider hole is a counter inside a stroke ring and
    widens, as the ring's inner edge moves out.
    """
    s = (m[0] + m[1]) / 2
    grown = HALF_STROKE * (s - 1)
    if abs(grown) < 1e-3:
        return geometry
    out = []
    for part in polygons(geometry):
        body = Polygon(part.exterior).buffer(-grown, join_style='round')
        holes = []
        for ring in part.interiors:
            hole = Polygon(ring)
            slit = hole.buffer(-HALF_STROKE * s * 1.1).is_empty
            holes.append(hole.buffer(-grown if slit else grown, join_style='round'))
        out.append(body.difference(unary_union(holes)) if holes else body)
    return unary_union(out)


CLASSIFY_STEP = 0.5            # px of centerline per black/white sample
SLIVER = 0.4                   # px: paint thinner than twice this between strokes is not a region


def rebuild_strokes(fill, segments, groups, pieces):
    """A flat fill moved by its layout, with its strokes redrawn 4px wide on the moved centerlines.

    Each piece of centerline is black where the unmoved fill covers it (a stroke) and white where it
    does not (a cut-out detail). Strokes and cut-outs are redrawn as 4px strokes around their moved
    centerlines; only the paint between strokes (filled regions) scales, grown back to meet its strokes.
    `pieces` is [(fill part, map)] as placed (one piece for a rigid move). None when nothing is stroked.
    """
    covered = prep(fill)
    black, white, black_here, white_here = [], [], [], []
    for elements, _source, m in groups:
        for i in elements:
            for seg in segments[i]:
                if len(seg) < 2:
                    continue
                line = LineString(seg)
                n = max(1, int(line.length / CLASSIFY_STEP))
                for k in range(n):
                    part = substring(line, k / n, (k + 1) / n, normalized=True)
                    if part.length <= 0:
                        continue
                    inked = covered.contains(line.interpolate((k + .5) / n, normalized=True))
                    (black_here if inked else white_here).append(part)
                    (black if inked else white).append(apply_map(part, m))
    if not black and not white:
        return None
    strokes_here = unary_union(black_here).buffer(HALF_STROKE) if black_here else Polygon()
    cuts_here = unary_union(white_here).buffer(HALF_STROKE + .05) if white_here else Polygon()
    regions = []
    for piece, m in pieces:
        # Cut-outs fill back into their region (inside the drawing only), so moved cut-outs leave no trace.
        # Holes count whole (wide stroke junctions too); closing covers notches open to the outline.
        reach = HALF_STROKE + .3
        closed = piece.buffer(reach, join_style='round').buffer(-reach, join_style='round')
        inside = closed.union(unary_union([Polygon(p.exterior) for p in polygons(piece)]))
        whole = make_valid(piece.union(cuts_here.intersection(inside)))
        region = whole.difference(strokes_here)
        # Slivers where the fill's outline and the stroke outline differ slightly are not regions.
        region = region.buffer(-SLIVER, join_style='round').buffer(SLIVER, join_style='round')
        if region.is_empty:
            continue
        s = (m[0] + m[1]) / 2
        grown = max(0.0, HALF_STROKE * (s - 1))
        # Grown back to meet its strokes, never past the drawing's moved outline.
        outline = unary_union([Polygon(p.exterior) for p in polygons(whole)])
        bound = apply_map(outline, m).buffer(-HALF_STROKE * (s - 1), join_style='round')
        # White counters keep their own (scaled) extent: a region growing back to its strokes must not
        # close a counter that sits against a cut-out stroke (the dot inside a white head ring).
        counters = unary_union([Polygon(r) for p in polygons(whole) for r in p.interiors])
        if not counters.is_empty:
            bound = bound.difference(apply_map(counters, m).buffer(grown, join_style='round'))
        regions.append(apply_map(region, m).buffer(grown + .05, join_style='round').intersection(bound))
    painted = unary_union(regions + ([unary_union(black).buffer(HALF_STROKE)] if black else []))
    return make_valid(painted.difference(unary_union(white).buffer(HALF_STROKE)) if white else painted)


def layout_groups(cls, segments, layout):
    """[(element numbers, source box, map)] for a part's saved layout."""
    boxes = [cls.bbox(s) if s else None for s in segments]
    if all('paths' in g for g in layout):
        groups = [[i for i in g['paths'] if i < len(boxes) and boxes[i]] for g in layout]
        if sorted(i for g in groups for i in g) != [i for i, b in enumerate(boxes) if b]:
            raise ValueError('layout elements do not match the drawing')
    elif len(layout) == 1:
        groups = [[i for i, b in enumerate(boxes) if b]]
    else:
        raise ValueError('several boxes without element numbers')
    return [(g, cls.union(boxes[i] for i in g), group_map(cls.union(boxes[i] for i in g), box))
            for g, box in zip(groups, layout)]


def moves_as_one(groups):
    _g, _s, first = groups[0]
    for _elements, (x0, y0, x1, y1), m in groups[1:]:
        mine = (x0 * m[0] + m[2], y0 * m[1] + m[3], x1 * m[0] + m[2], y1 * m[1] + m[3])
        theirs = (x0 * first[0] + first[2], y0 * first[1] + first[3], x1 * first[0] + first[2], y1 * first[1] + first[3])
        if max(abs(a - b) for a, b in zip(mine, theirs)) > SAME_MAP:
            return False
    return True


def _half_plane(cell, p, q):
    """The part of a convex polygon (a list of points) nearer p than q."""
    mx, my, nx, ny = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2, q[0] - p[0], q[1] - p[1]
    out = []
    for i, a in enumerate(cell):
        b = cell[(i + 1) % len(cell)]
        sa, sb = (a[0] - mx) * nx + (a[1] - my) * ny, (b[0] - mx) * nx + (b[1] - my) * ny
        if sa <= 0:
            out.append(a)
        if (sa < 0 < sb) or (sb < 0 < sa):
            t = sa / (sa - sb)
            out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    return out


def nearest_region(points, owner, n, extent):
    """Where the nearest centerline point is one of group n's: each of its points' cells cut from the extent by the
    bisectors with the other groups' points (side-fill-combine.js voronoiRegion). GEOS's Voronoi diagram breaks on
    the many collinear points of straight strokes (overlapping cells, cells without their point)."""
    import math
    x0, y0, x1, y1 = extent
    mine = [(pt.x, pt.y) for pt, o in zip(points, owner) if o == n]
    others = [(pt.x, pt.y) for pt, o in zip(points, owner) if o != n]
    cells = []
    for p in mine:
        cell = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        reach = max(math.hypot(c[0] - p[0], c[1] - p[1]) for c in cell)
        for d, q in sorted((math.hypot(q[0] - p[0], q[1] - p[1]), q) for q in others):
            if d > 2 * reach:
                break
            cell = _half_plane(cell, p, q)
            if len(cell) < 3:
                break
            reach = max(math.hypot(c[0] - p[0], c[1] - p[1]) for c in cell)
        if len(cell) >= 3:
            cells.append(Polygon(cell).buffer(0))
    return unary_union(cells) if cells else Polygon()


def split_fill(fill, segments, groups):
    """[(piece, map)]: each fill part to the group whose strokes it was drawn from."""
    lines = [[LineString(seg) for i in g for seg in segments[i] if len(seg) > 1] for g, _s, _m in groups]
    ink = [make_valid(unary_union([line.buffer(HALF_STROKE) for line in ls])) for ls in lines]
    points, owner, seen = [], [], set()
    for n, ls in enumerate(lines):
        for line in ls:
            steps = max(1, int(line.length / SAMPLE_STEP))
            for k in range(steps + 1):
                point = line.interpolate(k / steps, normalized=True)
                # Shared endpoints (touching elements) would give one cell two owners: the first keeps it.
                key = (round(point.x, 6), round(point.y, 6))
                if key not in seen:
                    seen.add(key)
                    points.append(point)
                    owner.append(n)
    x0, y0, x1, y1 = fill.bounds
    regions = [nearest_region(points, owner, n, (x0 - 64, y0 - 64, x1 + 64, y1 + 64)) for n in range(len(groups))]
    pieces = [[] for _ in groups]
    divided = False
    for part in polygons(make_valid(fill)):
        overlap = [part.intersection(i).area for i in ink]
        total = sum(overlap)
        best = max(range(len(groups)), key=overlap.__getitem__)
        if total <= 0 or overlap[best] >= OWNER_SHARE * total:
            pieces[best].append(part)
            continue
        divided = True
        # The group with most of the part's ink keeps it whole (a region divided between groups that move apart
        # would open white seams along the cut); each other group also draws its own share where it goes.
        pieces[best].append(part)
        for n, region in enumerate(regions):
            piece = part.intersection(region) if n != best else None
            if piece is not None and not piece.is_empty:
                pieces[n].append(piece)
    return [(unary_union(p), m) for p, (_g, _s, m) in zip(pieces, groups) if p], divided


def restroke(fill_path, m):
    """A fill kept as stroked lines (keep_original), outlined after its lines move: exact at any scale.

    None when the file has filled shapes, which have no lines to move.
    """
    _root, _viewbox, shapes = parse_all_shapes(str(fill_path), include_fills=True)
    close_returning(shapes)
    if not shapes or any(shape.get('kind') == 'fill' for shape in shapes):
        return None
    sx, sy, dx, dy = m
    moved = []
    for shape in shapes:
        shape = dict(shape)
        shape['coords'] = [(x * sx + dx, y * sy + dy) for x, y in shape['coords']]
        if shape.get('native_path') is not None:
            # stroke_to_polygon prefers native_path over sampled coords. Move the
            # original path itself before outlining it at the target stroke width.
            original = shape.get('transform', (1, 0, 0, 1, 0, 0))
            shape['native_path'] = shape['native_path'].transform(*original).transform(sx, 0, 0, sy, dx, dy)
            shape['transform'] = (1, 0, 0, 1, 0, 0)
            shape['non_scaling_stroke'] = False
        shape.pop('source_coords', None)
        if shape.get('clip_geometry') is not None:
            shape['clip_geometry'] = apply_map(shape['clip_geometry'], m)
        moved.append(shape)
    return stroke_to_polygon(moved, (0, 0, CANVAS, CANVAS))


def plausible(groups):
    """Whether every group keeps roughly its size and proportions: element numbers that do not fit the
    drawing (a layout saved for another drawing) squeeze a ring into a dash."""
    for _elements, (x0, y0, x1, y1), (sx, sy, _dx, _dy) in groups:
        flat = x1 - x0 <= 1e-9 or y1 - y0 <= 1e-9
        if not 1 / MAX_GROUP_SCALE <= sx <= MAX_GROUP_SCALE or not 1 / MAX_GROUP_SCALE <= sy <= MAX_GROUP_SCALE:
            return False
        if not flat and max(sx, sy) / min(sx, sy) > MAX_GROUP_STRETCH:
            return False
    return True


def whole_box(fill, layout, fill_path=None, *, scale_stroke_weight=False):
    """The whole fill placed in the box all the layout's groups cover, measured from the fill itself
    (its ink less the half stroke is the drawing's centerline box)."""
    x0, y0, x1, y1 = fill.bounds
    source = (x0 + HALF_STROKE, y0 + HALF_STROKE, x1 - HALF_STROKE, y1 - HALF_STROKE)
    bx0, by0 = min(g['x'] for g in layout), min(g['y'] for g in layout)
    bx1, by1 = max(g['x'] + g['w'] for g in layout), max(g['y'] + g['h'] for g in layout)
    m = group_map(source, {'x': bx0, 'y': by0, 'w': bx1 - bx0, 'h': by1 - by0})
    if scale_stroke_weight:
        return apply_map(fill, m), 'whole_box', m
    lines = restroke(fill_path, m) if fill_path and not is_reverse_fill(fill_path) else None
    return (lines if lines is not None else keep_stroke_weight(apply_map(fill, m), m)), 'whole_box', m


def place_stroke_fill(cls, fill, document, layout, fill_path):
    """A stroke-fill icon moved by the part's layout: centerlines and regions move with their
    element's group map, and every stroke is drawn afterwards at its own width (never scaled)."""
    from .stroke_fill_format import regions_of, render
    regions = regions_of(fill_path)
    try:
        segments = element_segments(cls, document)
        groups = layout_groups(cls, segments, layout)
    except ValueError:
        _placed, how, m = whole_box(fill, layout)
        return render(fill_path, lambda index: m, [(regions, m)]), 'whole_box', m
    how = 'rigid'
    if not plausible(groups):
        everything = [i for g, _s, _m in groups for i in g]
        source = cls.union(cls.bbox(segments[i]) for i in everything)
        x0, y0 = min(g['x'] for g in layout), min(g['y'] for g in layout)
        x1, y1 = max(g['x'] + g['w'] for g in layout), max(g['y'] + g['h'] for g in layout)
        groups = [(everything, source, group_map(source, {'x': x0, 'y': y0, 'w': x1 - x0, 'h': y1 - y0}))]
        how = 'layout_mismatch'
    maps = {i: m for members, _s, m in groups for i in members}
    first = groups[0][2]
    if len(groups) == 1 or moves_as_one(groups):
        return render(fill_path, lambda index: first, [(regions, first)]), how, first
    pieces, divided = split_fill(regions, segments, groups) if not regions.is_empty else ([], False)
    return (render(fill_path, lambda index: maps.get(index, first), pieces),
            'split_divided' if divided else 'split', None)


def place_part(cls, fill, document, layout, fill_path=None, *, scale_stroke_weight=False):
    """The fill moved by the part's layout, and how ('rigid' | 'split' | 'split_divided' |
    'layout_mismatch' | 'whole_box')."""
    from .stroke_fill_format import is_stroke_fill
    if fill_path and is_stroke_fill(fill_path):
        # Strokes keep their weight at any size, small subs included (no scale_stroke_weight).
        return place_stroke_fill(cls, fill, document, layout, fill_path)
    try:
        segments = element_segments(cls, document)
        groups = layout_groups(cls, segments, layout)
    except ValueError:
        # Elements the layout cannot number (drawings with transforms, element lists that no longer
        # match): the layout's boxes still say where the part went.
        return whole_box(fill, layout, fill_path,
                         scale_stroke_weight=scale_stroke_weight)
    how = 'rigid'
    if not plausible(groups):
        # The layout's boxes still say where the part went: place the whole drawing in their union.
        everything = [i for g, _s, _m in groups for i in g]
        source = cls.union(cls.bbox(segments[i]) for i in everything)
        x0, y0 = min(g['x'] for g in layout), min(g['y'] for g in layout)
        x1, y1 = max(g['x'] + g['w'] for g in layout), max(g['y'] + g['h'] for g in layout)
        groups = [(everything, source, group_map(source, {'x': x0, 'y': y0, 'w': x1 - x0, 'h': y1 - y0}))]
        how = 'layout_mismatch'
    if len(groups) == 1 or moves_as_one(groups):
        m = groups[0][2]
        if scale_stroke_weight:
            return apply_map(fill, m), how, m
        reverse = is_reverse_fill(fill_path)
        lines = restroke(fill_path, m) if fill_path and not reverse else None
        if lines is None and not reverse and abs(m[0] - 1) + abs(m[1] - 1) > 1e-3:
            lines = rebuild_strokes(fill, segments, groups, [(fill, m)])
        return (lines if lines is not None else keep_stroke_weight(apply_map(fill, m), m)), how, m
    moved, divided = split_fill(fill, segments, groups)
    if not scale_stroke_weight and not is_reverse_fill(fill_path):
        rebuilt = rebuild_strokes(fill, segments, groups, moved)
        if rebuilt is not None:
            return rebuilt, 'split_divided' if divided else 'split', None
    placed = unary_union([apply_map(piece, m) if scale_stroke_weight else
                          keep_stroke_weight(apply_map(piece, m), m)
                          for piece, m in moved])
    return placed, 'split_divided' if divided else 'split', None


def outline_boxes(cls, document, layout):
    """The boxes component() bakes the outline into, as place_part moves the fill, or None.

    Implausible groups go into the union of the boxes, as place_part places the whole drawing there.
    None when the layout cannot number the drawing's elements (place_part's whole_box).
    """
    try:
        segments = element_segments(cls, document)
        groups = layout_groups(cls, segments, layout)
    except ValueError:
        return None
    if plausible(groups):
        return [{**box, 'paths': elements} for box, (elements, _s, _m) in zip(layout, groups)]
    x0, y0 = min(g['x'] for g in layout), min(g['y'] for g in layout)
    x1, y1 = max(g['x'] + g['w'] for g in layout), max(g['y'] + g['h'] for g in layout)
    return [{'paths': sorted(i for g, _s, _m in groups for i in g),
             'x': x0, 'y': y0, 'w': x1 - x0, 'h': y1 - y0}]


def build(layouts, out, ids=None):
    from .adaptive_overlap import fill_path   # imports this module
    cls = repo_layout_svg()
    items = json.loads(layouts.read_text())['items']
    if ids:
        wanted = set(ids)
        items = [i for i in items if i['reference_id'] in wanted]
    (out / 'svg').mkdir(parents=True, exist_ok=True)
    records = []
    graph_records = {}
    for item in items:
        record = {'id': item['reference_id'], 'concept': item['concept'], 'state': item['state']}
        records.append(record)
        parts = {p['role']: p for p in item['parts']}
        placed, flags = {}, []
        for role in ('main', 'sub'):
            part = parts.get(role) or {}
            if not part.get('icon'):
                record['status'] = f'{role}_not_a_drawing'      # native text and empty parts
                break
            name = part['icon'].split('/', 1)[1]
            sha = part.get('current_sha') or part['built_sha']
            record[role] = part['icon']
            if part.get('built_sha') != sha:
                flags.append(f'{role}_changed_since_layout')
            drawing = (DATA / 'normal' / f'{name}.svg') if role == 'main' else (DATA / 'archive/side-sub-32' / f'{name}.svg')
            if role == 'sub' and not drawing.exists():
                drawing = DATA / 'archive/sub-32-revisions' / name / f'{sha}.svg'
            fill = fill_path(part, role)
            if not drawing.exists():
                record['status'] = f'missing_{role}_drawing'
                break
            actual_sha = hashlib.sha256(drawing.read_bytes()).hexdigest()
            if actual_sha != sha:
                record.update(status=f'{role}_source_hash_mismatch', expected_sha256=sha, actual_sha256=actual_sha)
                break
            if not fill.exists():
                record['status'] = f'missing_{role}_fill'
                break
            record[role + '_source_sha256'] = sha
            record[role + '_fill_sha256'] = hashlib.sha256(fill.read_bytes()).hexdigest()
            try:
                geometry, stroked = load_fill(fill)
                placed[role], how, m = place_part(cls, geometry, drawing.read_text(), part['layout'] or [], fill)
            except Exception as error:
                record.update(status='error', error=f'{role}: {error}')
                break
            record[role + '_layout'] = how
            if how != 'rigid':
                flags.append(f'{role}_{how}')
            if m and max(abs(m[0] - 1), abs(m[1] - 1)) > 0.01:
                flags.append(f'{role}_scaled')
            if stroked:
                flags.append(f'{role}_kept_stroke')
        else:
            main, sub = placed['main'], placed['sub']
            if any(v < -1e-6 or v > CANVAS + 1e-6 for v in (*main.bounds, *sub.bounds)):
                record['status'] = 'outside_canvas'
                continue
            cut, details = cut_main(main, sub)
            if details['split_parts']:
                flags.append('fragmented')
            combined = unary_union([cut, sub])
            try:
                graph = analyze_overlap(main, sub, cut, combined, clearance(sub))
            except Exception as error:
                record.update(status='graph_error', error=str(error))
                continue
            graph_records[item['reference_id']] = graph
            record.update(status='proposal', flags=flags, gap=details['gap'], closed_holes=details['closed_holes'],
                          graph_status=graph['status'], graph_issues=graph['issues'])
            (out / 'svg' / f"{item['reference_id']}.svg").write_text(geometry_to_svg(combined, f'0 0 {CANVAS} {CANVAS}'))
    counts = {}
    for r in records:
        counts[r['status']] = counts.get(r['status'], 0) + 1
    (out / 'report.json').write_text(json.dumps({'counts': counts, 'rows': records}, indent=1))
    (out / 'graph-report.json').write_text(json.dumps(graph_records, indent=2) + '\n')
    output_files = sorted(out / 'svg' / f"{row['id']}.svg" for row in records if row['status'] == 'proposal')
    manifest = {
        'layout_sha256': hashlib.sha256(layouts.read_bytes()).hexdigest(),
        'report_sha256': hashlib.sha256((out / 'report.json').read_bytes()).hexdigest(),
        'graph_report_sha256': hashlib.sha256((out / 'graph-report.json').read_bytes()).hexdigest(),
        'outputs': {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in output_files},
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('command', choices=['build'])
    parser.add_argument('--layouts', type=Path, default=DEFAULT_LAYOUTS)
    parser.add_argument('--ids', nargs='*')
    parser.add_argument('--out', type=Path, default=WORK / 'normal-fill-proposals')
    args = parser.parse_args(argv)
    print(json.dumps(build(args.layouts, args.out, args.ids), indent=1))


if __name__ == '__main__':
    main()
