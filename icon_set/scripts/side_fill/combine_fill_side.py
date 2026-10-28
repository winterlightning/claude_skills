"""Copied 64px side-pair clearance and cut geometry for local Normal proposals.

The stroke engine (claude_skills icon_set/scripts/combination_experiment.render + vendor/combination)
places both drawings with `placement` and erases the main's centerlines inside
    hull(sub centerlines)  ∪  sub centerlines ⊕ 8
then paints them with 4px round caps. The fill cut reserves one clean convex
envelope around the placed sub ink, including disconnected parts and counters:
    convex_hull(sub fill) ⊕ 4
This prevents small concave pockets between sub parts from leaving noisy main-ink
tips beside the sub. The 8px validation clearance uses the same hull.

The local builder is ``python3 -m side_combinations.combine_fill_side_layouts build``.
"""
from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import os
import re
import tempfile
from io import BytesIO
from pathlib import Path

from shapely.affinity import affine_transform
from shapely.geometry import LineString, Polygon
from shapely.ops import unary_union

from ...vendor.fill_processing.vendor.fill_utils import (_drop_tiny_holes, geometry_to_svg,
                                               load_one, parse_all_shapes,
                                               stroke_to_polygon)

ROOT = WORK          # build output; source data lives under DATA (paths.py)
CANVAS = 64
HALF_STROKE = 2.0           # 4px strokes at 64
GAP = 4.0                   # main ink to sub ink, as the stroke engine's buffer_px=8 leaves it
MIN_PART_AREA = 4.0         # px² at 64: smaller main fragments are dropped
MIN_HOLE_AREA = 2.0         # px² at 64: smaller holes are filled
MIN_PART_WIDTH = 2.0        # parts that vanish under an opening of half this width are dropped
STUB_SHARE = 0.5           # a hole the notch would leave less than this share of is filled
DETAIL_AREA = 48.0          # px²: smaller holes are details a notch may fill
SCRAP_AREA = 64.0           # px²: smaller pieces a cut breaks off a part are dropped
FRAGMENT_AREA = 24.0        # main parts at least this big count when a cut splits the main
EPS = 0.05


def polygons(geometry):
    """Every polygon in a geometry, including those inside a collection a boolean returned."""
    if isinstance(geometry, Polygon):
        return [] if geometry.is_empty else [geometry]
    return [p for g in getattr(geometry, 'geoms', []) for p in polygons(g)]


def close_returning(shapes):
    """Mark a stroked line that ends where it starts as closed, as a final Z would.

    The vendor stroker drops nearly all ink of such a ring when it is left open (a bank roof
    drawn M2 13 L16 2 L30 13 L2 13 keeps 0.2 px² of 154); with round joins and caps the closed
    ring paints the same strokes.
    """
    for shape in shapes:
        coords = shape.get('coords')
        if (shape.get('kind') != 'fill' and shape.get('closed') is False and coords and len(coords) > 3
                and max(abs(a - b) for a, b in zip(coords[0], coords[-1])) < 1e-6):
            shape['closed'] = True
    return shapes


def closed_returning_source(text):
    """The SVG with Z written after each path's subpaths that end where they start (see close_returning)."""
    from .combination_layout_svg import IDENTITY, NUMBER, matrix_path

    def close_d(match):
        d = match.group(2)
        try:
            absolute = re.split(r'(?=M)', matrix_path(d, IDENTITY))
        except (ValueError, KeyError):
            return match.group(0)
        original = re.split(r'(?=[Mm])', d)
        absolute = [part for part in absolute if part.strip()]
        lead = [part for part in original if not part.strip()]
        original = [part for part in original if part.strip()]
        if len(original) != len(absolute):
            return match.group(0)
        out = []
        for raw, flat in zip(original, absolute):
            points = [float(n) for n in NUMBER.findall(flat)]
            if (not re.search(r'[Zz]\s*$', raw) and len(points) >= 6
                    and abs(points[0] - points[-2]) < 1e-6 and abs(points[1] - points[-1]) < 1e-6):
                raw = raw.rstrip() + 'Z'
            out.append(raw)
        return match.group(1) + ''.join(lead + out) + match.group(3)
    return re.sub(r'(<path\b[^>]*?\sd=")([^"]*)(")', close_d, text)


def load_fill(path):
    """(filled geometry in its own viewBox units, whether it kept stroked lines).

    A fill approved as keep_original (bare arrows, glyphs) is still stroked; its ink is outlined.
    A stroke-fill file (regions plus black and white original strokes) is painted in its own order.
    """
    from .stroke_fill_format import is_stroke_fill, native
    if is_stroke_fill(path):
        geometry = native(path)
        if geometry.is_empty:
            raise ValueError(f'{path} has no ink')
        return geometry, True
    text = Path(path).read_text()
    closed = closed_returning_source(text)
    if closed == text:
        loaded = load_one(str(path))
    else:
        with tempfile.NamedTemporaryFile('w', suffix='.svg', delete=False) as handle:
            handle.write(closed)
        try:
            loaded = load_one(handle.name)
        finally:
            os.unlink(handle.name)
    geometry = loaded['polygon']
    if geometry is None or geometry.is_empty:
        raise ValueError(f'{path} has no ink')
    stroked = loaded['stroke_polygon'] is not None and not loaded['stroke_polygon'].is_empty
    return (geometry if geometry.is_valid else geometry.buffer(0)), stroked


def matches_drawing(geometry, item, tolerance=0.6):
    """Whether a fill's ink spans the drawing's centerline bounds plus the half stroke."""
    x0, y0, x1, y1 = item['bounds']
    expected = (x0 - HALF_STROKE, y0 - HALF_STROKE, x1 + HALF_STROKE, y1 + HALF_STROKE)
    return max(abs(a - b) for a, b in zip(geometry.bounds, expected)) < tolerance


def place(geometry, scale, tx, ty):
    return affine_transform(geometry, [scale, 0, 0, scale, tx, ty])


def clearance(sub, gap=GAP):
    """Where main ink may not go: the placed sub's convex hull plus the gap."""
    return sub.convex_hull.buffer(gap, join_style='round')


def round_cut_ends(main_cut, clear):
    """Round the corners a cut leaves, as the stroke ends there have round caps.

    Only the band along the clearance is opened; the rest of the main keeps its drawn corners.
    """
    r = HALF_STROKE - EPS
    opened = main_cut.buffer(-r).buffer(r)
    band = clear.buffer(2 * HALF_STROKE).difference(clear)
    return main_cut.difference(band.difference(opened))


def clean_main(main):
    """Drop slivers, crumbs and pinholes a cut left; report what remains."""
    kept = []
    for part in polygons(main):
        if part.area < MIN_PART_AREA or part.buffer(-MIN_PART_WIDTH / 2).is_empty:
            continue
        kept.append(_drop_tiny_holes(part, MIN_HOLE_AREA))
    cleaned = unary_union(kept) if kept else Polygon()
    big = [p for p in polygons(cleaned) if p.area >= FRAGMENT_AREA]
    return cleaned, len(big)


def holes_near(main, clear):
    """The main's holes where they meet the notch: (main, holes to cut last, filled).

    Nothing is drawn that the artwork does not have. A hole the notch reaches opens into it, as the
    stroke engine cuts a line through. Two exceptions:
    - a small detail (a slit or a small hole) the notch takes most of is filled (a highlight): the
      stroke engine erases such a line outright, and its stub would dent the notch edge;
    - a hole clear of the notch but near it keeps the wall it is drawn with: it is cut after the notch
      is rounded, so the rounding cannot break that wall open.
    """
    zone = clear.buffer(2 * HALF_STROKE)
    out, later, closed = [], [], 0
    for part in polygons(main):
        keep = []
        for ring in part.interiors:
            hole = Polygon(ring)
            if not hole.intersects(zone):
                keep.append(ring)
                continue
            detail = hole.area < DETAIL_AREA or hole.buffer(-HALF_STROKE * 1.1).is_empty
            if detail and hole.difference(zone).area < STUB_SHARE * hole.area:
                closed += 1
            elif hole.intersects(clear):
                keep.append(ring)
            else:
                later.append(hole)
        out.append(Polygon(part.exterior, keep))
    return (unary_union(out) if out else main), later, closed


def drop_cut_scraps(drawn, cut):
    """Drop the small pieces a cut breaks off a drawn part (a door frame's corner, a ruler tick).

    Each drawn part keeps its largest piece; other pieces it was cut into go when under SCRAP_AREA.
    Parts drawn apart (cart wheels) are never compared with each other.
    """
    pieces = polygons(cut)
    parts = polygons(drawn)
    # A piece belongs to the drawn part it overlaps most. (Its representative point can fall in a
    # white opening the cut temporarily filled, outside every part, which dropped whole mains.)
    owner = {}
    for index, piece in enumerate(pieces):
        overlaps = [(piece.intersection(part).area, k) for k, part in enumerate(parts)]
        best = max(overlaps, default=(0, None))
        if best[0] > EPS:
            owner[index] = best[1]
    keep, dropped = [], 0
    for k, part in enumerate(parts):
        mine = [p for i, p in enumerate(pieces) if owner.get(i) == k]
        if not mine:
            continue
        largest = max(mine, key=lambda p: p.area)
        for p in mine:
            if p is largest or p.area >= SCRAP_AREA:
                keep.append(p)
            else:
                dropped += 1
    return (unary_union(keep) if keep else Polygon()), dropped


def cut_main(main, sub, gap=GAP):
    """The main cut clear of the sub: (cut main, details)."""
    clear = clearance(sub, gap)
    solid, later, closed = holes_near(main, clear)
    cut = solid.difference(clear)
    erased = solid.area - cut.area
    if erased > EPS:
        cut = round_cut_ends(cut, clear)
    if later:
        cut = cut.difference(unary_union(later))
        # Delaying a white opening temporarily fills it in `solid`. Its black
        # islands are separate original objects; restore only their source ink
        # after reopening the white region, respecting the same sub clearance.
        islands = [part for part in polygons(main)
                   if any(hole.contains(part.representative_point()) for hole in later)]
        if islands:
            cut = unary_union([cut, *[part.difference(clear) for part in islands]])
    cut, dropped = drop_cut_scraps(main, cut)
    cut, big_parts = clean_main(cut)
    _same, drawn_parts = clean_main(main)
    gap = cut.distance(sub) if not cut.is_empty else None
    return cut, {'erased_area': round(erased, 3), 'main_parts': big_parts, 'closed_holes': closed,
                 'dropped_scraps': dropped,
                 'split_parts': max(0, big_parts - drawn_parts),
                 'gap': None if gap is None else round(gap, 3)}


def _line_parts(geometry):
    if isinstance(geometry, LineString):
        return [] if geometry.is_empty else [geometry]
    return [line for part in getattr(geometry, 'geoms', [])
            for line in _line_parts(part)]


def cut_outline_strokes(placed_svg, sub, gap=GAP):
    """Clear the source outline's centerlines around actual sub ink, then restroke.

    A polygon subtraction from already painted outline ink leaves tapered hairlines
    at the cut. Clipping the native centerlines and repainting their original stroke
    widths gives full-width, round-ended surviving strokes. The sub's actual paint,
    including concave gaps, supplies the clearance; its convex hull is not used.
    Filled marks already in the original drawing are cut as paint.
    """
    _root, viewbox, shapes = parse_all_shapes(BytesIO(placed_svg.encode()),
                                              include_fills=True)
    close_returning(shapes)
    original_strokes = stroke_to_polygon(shapes, viewbox)
    filled = [shape['geometry'] for shape in shapes if shape.get('kind') == 'fill']
    original = unary_union([part for part in [original_strokes, *filled]
                            if part is not None and not part.is_empty])
    clipped = []
    for shape in shapes:
        if shape.get('kind') == 'fill':
            continue
        line = LineString(shape['coords'])
        centerline_clearance = sub.buffer(gap + shape['stroke_width'] / 2,
                                         join_style='round')
        if line.length <= EPS:
            # A dot is a zero-length stroke painted by its round cap: kept
            # whole when clear of the sub, erased whole otherwise.
            if not line.intersects(centerline_clearance):
                clipped.append({key: value for key, value in shape.items()
                                if key not in ('native_path', 'source_coords', 'transform',
                                               'clip_geometry')})
            continue
        remaining = line.difference(centerline_clearance)
        was_cut = remaining.length < line.length - EPS
        for part in _line_parts(remaining):
            # A cut can isolate a few units of a once-continuous outline. Its
            # round caps read as a stray dot or hairline, not source detail.
            if part.length <= EPS or (was_cut and
                                      part.length < 1.5 * shape['stroke_width']):
                continue
            piece = {key: value for key, value in shape.items()
                     if key not in ('native_path', 'source_coords', 'transform',
                                    'clip_geometry')}
            piece.update(coords=list(part.coords), closed=False)
            clipped.append(piece)
    remaining_strokes = stroke_to_polygon(clipped, viewbox) if clipped else None
    painted_clearance = sub.buffer(gap, join_style='round')
    remaining_fills = [part.difference(painted_clearance) for part in filled]
    cut = unary_union([part for part in [remaining_strokes, *remaining_fills]
                       if part is not None and not part.is_empty])
    _cleaned, parts = clean_main(cut)
    actual_gap = cut.distance(sub) if not cut.is_empty else None
    return cut, {'erased_area': round(original.area - cut.area, 3),
                 'main_parts': parts, 'closed_holes': 0,
                 'dropped_scraps': 0, 'split_parts': 0,
                 'gap': None if actual_gap is None else round(actual_gap, 3)}


def combine(main_fill, sub_fill, main_transform, sub_transform):
    """→ (combined geometry, placed main after cut, placed sub, details)."""
    main = place(main_fill, *main_transform)
    sub = place(sub_fill, *sub_transform)
    cut, details = cut_main(main, sub)
    return unary_union([cut, sub]), cut, sub, details


