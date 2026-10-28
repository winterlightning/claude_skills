"""Read and place stroke-fill/v1 icons (stroke_fill_rework.py): black fill regions plus original strokes.

A layout moves and scales centerlines and regions; strokes are drawn afterwards at their own width
(4px, or a detail width), so a resized icon keeps its stroke weight. Painting order follows the file:
regions, white strokes under the black ones, black strokes, white strokes over everything.
"""

import re
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

from shapely.affinity import affine_transform
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import substring, unary_union
from shapely.validation import make_valid

FORMAT = 'stroke-fill/v1'
SVG = '{http://www.w3.org/2000/svg}'
TUCK = 1.0          # stroke_fill_rework.TUCK: region edges sit this far from their stroke centerline
DEFAULT_WIDTH = 4.0


# The upload route keeps ids but drops data- attributes, so an uploaded icon carries the format as the root's id and
# each element's number as its id (fill_icons.portable).
FORMAT_ID = 'stroke-fill-v1'
ELEMENT_ID = re.compile(r'element-(\d+)\Z')


def is_stroke_fill(path):
    try:
        with open(path, 'rb') as handle:
            head = handle.read(600)
        return f'data-format="{FORMAT}"'.encode() in head or f'id="{FORMAT_ID}"'.encode() in head
    except OSError:
        return False


def element_index(element):
    """The element's number in its source drawing: data-element, or an uploaded icon's id element-N."""
    if element.get('data-element') is not None:
        return int(element.get('data-element'))
    match = ELEMENT_ID.match(element.get('id') or '')
    return int(match.group(1)) if match else -1


def _map(geometry, m):
    sx, sy, dx, dy = m
    return affine_transform(geometry, [sx, 0, 0, sy, dx, dy])


def _dashed(line, length, pattern, offset):
    """The dash pieces of one centerline: SVG dashing in path-length units, offset into the pattern."""
    if len(pattern) % 2:
        pattern = pattern * 2
    total = sum(pattern)
    if total <= 0 or line.length <= 0:
        return line
    ratio = line.length / length
    # The path starts `offset` into the pattern (a negative offset lands in the long final gap).
    into, index = offset % total, 0
    while into >= pattern[index]:
        into -= pattern[index]
        index = (index + 1) % len(pattern)
    pieces, position = [], 0.0
    while position < length:
        end = min(position + pattern[index] - into, length)
        if index % 2 == 0 and end > position:
            pieces.append(substring(line, position * ratio, end * ratio))
        position, into, index = end, 0.0, (index + 1) % len(pattern)
    return unary_union(pieces) if pieces else LineString()


@lru_cache(maxsize=4096)
def _parts(path, modified):
    from .combination_layout_svg import elements as walk_elements, segments_of
    from .stroke_fill_rework import filled_area, svg_length
    root = ET.parse(path).getroot()
    regions = Polygon()
    entries = []
    parent = {child: node for node in root.iter() for child in node}
    for element, own in walk_elements(root):
        if element.get('id') == 'fill-regions':
            regions = filled_area(element, root)
            continue
        group = parent.get(element)
        group_id = group.get('id', '') if group is not None else ''
        index = element_index(element)
        stroked = (element.get('stroke') or own.get('stroke', 'none')).lower() not in ('none', 'transparent')
        filled = (element.get('fill') or own.get('fill', 'none')).lower() not in ('none', 'transparent')
        width = float(str(element.get('stroke-width') or own.get('stroke-width') or DEFAULT_WIDTH).rstrip('px'))
        segments, seen = [], set()
        if stroked:
            for seg in segments_of(element, {k: v for k, v in own.items() if k.startswith('stroke')}):
                key = tuple((round(x, 6), round(y, 6)) for x, y in seg)
                if seg and key not in seen:
                    seen.add(key)
                    segments.append(seg)
        lines = [LineString(seg) if len(seg) > 1 and LineString(seg).length > 1e-9 else Point(seg[0])
                 for seg in segments]
        centerline = unary_union(lines) if lines else Polygon()
        dash = None
        if element.get('stroke-dasharray') and stroked:
            pattern = [float(v) for v in element.get('stroke-dasharray').replace(',', ' ').split()]
            run = [line for line in lines if isinstance(line, LineString)]
            if len(run) == 1 or (run and unary_union(run).geom_type == 'LineString'):
                from shapely.ops import linemerge
                merged = linemerge(run) if len(run) > 1 else run[0]
                if merged.geom_type == 'LineString':
                    length = svg_length(element) or merged.length
                    dash = _dashed(merged, length, pattern, float(element.get('stroke-dashoffset', '0')))
        entries.append({'index': index, 'paint': 'white' if 'white' in group_id else 'black',
                        'under': group_id == 'white-strokes-under', 'width': width,
                        'centerline': dash if dash is not None else centerline, 'stroked': stroked,
                        'area': filled_area(element, root) if filled else Polygon()})
    return regions, tuple(entries)


def parts(path):
    path = str(path)
    return _parts(path, Path(path).stat().st_mtime_ns)


def _ink(entry, m):
    stroke = (_map(entry['centerline'], m).buffer(entry['width'] / 2)
              if entry['stroked'] and not entry['centerline'].is_empty else Polygon())
    area = _map(entry['area'], m) if not entry['area'].is_empty else Polygon()
    return unary_union([stroke, area])


IDENTITY = (1.0, 1.0, 0.0, 0.0)


def render(path, map_of=None, region_pieces=None):
    """The icon painted with each element moved by map_of(element index) and regions placed.

    region_pieces: [(region geometry, map)]; by default the whole region set unmoved.
    """
    map_of = map_of or (lambda index: IDENTITY)
    regions, entries = parts(path)
    if region_pieces is None:
        region_pieces = [(regions, IDENTITY)]
    placed = []
    for piece, m in region_pieces:
        if piece.is_empty:
            continue
        grow = max(0.0, max(m[0], m[1]) * TUCK - (DEFAULT_WIDTH / 2 - .2))
        moved = _map(piece, m)
        placed.append(moved.buffer(grow, join_style='round') if grow > 0 else moved)
    painted = unary_union(placed) if placed else Polygon()
    for layer in ('under', 'black', 'over'):
        for entry in entries:
            if layer == 'under' and not (entry['paint'] == 'white' and entry['under']):
                continue
            if layer == 'black' and entry['paint'] != 'black':
                continue
            if layer == 'over' and not (entry['paint'] == 'white' and not entry['under']):
                continue
            ink = _ink(entry, map_of(entry['index']))
            painted = painted.union(ink) if layer == 'black' else painted.difference(ink)
    return make_valid(painted)


def native(path):
    """The icon at its own size (what load_fill returns for a flat fill)."""
    return render(path)


def regions_of(path):
    return parts(path)[0]
