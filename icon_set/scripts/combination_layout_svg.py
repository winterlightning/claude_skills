"""Connected elements and baked layouts for a side pair, in an isolated combination-engine process.

Reads one JSON request on stdin and prints one JSON line:

    {"components": [{"role": "main", "document": "<svg…>", "scale": 1, "tx": 0, "ty": 0,
                     "layout": [{"paths": [0, 1, 2], "x": 2, "y": 22, "w": 36, "h": 36}, …] | null}]}

`scale`, `tx` and `ty` map the component's own coordinates onto the combination canvas
(its default placement). Every component comes back with its connected element groups
as canvas centerline boxes; one with a layout also comes back baked: every group
scaled on each axis and moved so its centerline box is exactly (x, y, w, h), written
as a canvas-sized document with the stroke kept at 4.

The engine ignores `transform`, so coordinates are rewritten rather than wrapped.
"""
import copy
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'vendor/combination'))

NS = 'http://www.w3.org/2000/svg'
SHAPES = ('path', 'circle', 'ellipse', 'rect', 'line', 'polyline', 'polygon')
SKIP = ('defs', 'clipPath', 'mask', 'title', 'desc', 'metadata', 'style')
# Presentation attributes a flattened element inherits from its dropped parent groups.
INHERITED = ('fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin',
             'stroke-miterlimit', 'fill-rule', 'opacity', 'stroke-opacity', 'fill-opacity')
STROKE = 4
NUMBER = re.compile(r'[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?')
ARGS = {'M': 2, 'L': 2, 'T': 2, 'H': 1, 'V': 1, 'C': 6, 'S': 4, 'Q': 4, 'A': 7, 'Z': 0}


def local(tag):
    return tag.rsplit('}', 1)[-1]


def elements(root):
    """Drawable elements in document order, each with the attributes inherited from its groups."""
    found = []

    def walk(node, inherited):
        for child in node:
            name = local(child.tag)
            if name in SKIP:
                continue
            if child.get('transform'):
                raise ValueError('Artwork with transforms cannot be adjusted.')
            own = {**inherited, **{k: v for k, v in child.attrib.items() if k in INHERITED}}
            if name in SHAPES:
                found.append((child, own))
            elif name == 'g':
                walk(child, own)
    walk(root, {})
    return found


def fmt(n):
    n = round(n, 6)
    return ('%.6f' % n).rstrip('0').rstrip('.') if n else '0'


def transform_path(d, sx, sy, tx, ty):
    """Scale each axis and translate a path, keeping every command and control point."""
    out, tokens = [], re.findall(r'[MmLlHhVvCcSsQqTtAaZz]|' + NUMBER.pattern, d)
    i, command = 0, None
    while i < len(tokens):
        if tokens[i].isalpha():
            command = tokens[i]
            i += 1
            out.append(command)
            if command in 'Zz':
                continue
        elif command is None:
            raise ValueError('Path data must start with a command.')
        upper, relative = command.upper(), command.islower()
        count = ARGS[upper]
        values = [float(v) for v in tokens[i:i + count]]
        if len(values) != count:
            raise ValueError('Incomplete path data.')
        i += count
        if upper == 'A':
            rx, ry, rotation, large, sweep, x, y = values
            x, y = (x * sx, y * sy) if relative else (x * sx + tx, y * sy + ty)
            turn = rotation % 180
            if abs(sx - sy) > 1e-9 and min(turn, 180 - turn) > 1e-9 and abs(turn - 90) > 1e-9:
                raise ValueError('A rotated arc can only be scaled evenly; keep the proportions.')
            if abs(turn - 90) <= 1e-9:
                rx, ry = rx * sy, ry * sx
            else:
                rx, ry = rx * sx, ry * sy
            values = [rx, ry, rotation, large, sweep, x, y]
            out.append(' '.join(fmt(v) for v in values))
        elif upper == 'H':
            out.append(fmt(values[0] * sx + (0 if relative else tx)))
        elif upper == 'V':
            out.append(fmt(values[0] * sy + (0 if relative else ty)))
        else:
            moved = []
            for n in range(0, count, 2):
                x, y = values[n] * sx, values[n + 1] * sy
                moved += [x, y] if relative else [x + tx, y + ty]
            out.append(' '.join(fmt(v) for v in moved))
        # Extra coordinate pairs after M are implicit line-tos.
        if upper == 'M':
            command = 'l' if relative else 'L'
    return ''.join(part if part.isalpha() else ' ' + part + ' ' for part in out).strip()


def transform_element(element, sx, sy, tx, ty):
    name, a = local(element.tag), element.attrib

    def point(xk, yk):
        if xk in a:
            a[xk] = fmt(float(a[xk]) * sx + tx)
        if yk in a:
            a[yk] = fmt(float(a[yk]) * sy + ty)

    def length(scale, *keys):
        for key in keys:
            if key in a:
                a[key] = fmt(float(a[key]) * scale)
    if name == 'path':
        a['d'] = transform_path(a.get('d', ''), sx, sy, tx, ty)
    elif name in ('circle', 'ellipse'):
        a.setdefault('cx', '0')
        a.setdefault('cy', '0')
        point('cx', 'cy')
        if name == 'circle' and abs(sx - sy) > 1e-9:
            # A stretched circle is an ellipse.
            element.tag = element.tag[:-len('circle')] + 'ellipse'
            a['rx'] = a['ry'] = a.pop('r', '0')
        if 'r' in a:
            length(sx, 'r')
        length(sx, 'rx')
        length(sy, 'ry')
    elif name == 'rect':
        a.setdefault('x', '0')
        a.setdefault('y', '0')
        point('x', 'y')
        length(sx, 'width', 'rx')
        length(sy, 'height', 'ry')
    elif name == 'line':
        point('x1', 'y1')
        point('x2', 'y2')
    else:
        values = [float(v) for v in NUMBER.findall(a.get('points', ''))]
        a['points'] = ' '.join(fmt(v * sx + tx if n % 2 == 0 else v * sy + ty) for n, v in enumerate(values))


def markup(element, own):
    """One element on its own with its inherited attributes, for drawing it in the editor."""
    copy_ = copy.deepcopy(element)
    copy_.tail = None
    for key, value in own.items():
        copy_.set(key, value)
    copy_.attrib.pop('id', None)
    ET.register_namespace('', NS)
    return ET.tostring(copy_, encoding='unicode')


def segments_of(element, stroke_attrs):
    """Engine segments of one element on its own, exactly as the engine flattens it."""
    from icon_combination.utils import parse_svg_geometric_elements
    root = ET.Element('{%s}svg' % NS, {'stroke': 'currentColor', **stroke_attrs})
    root.append(copy.deepcopy(element))
    segments, _points = parse_svg_geometric_elements(root, 1)
    return segments


def bbox(segments):
    xs = [p[0] for s in segments for p in s]
    ys = [p[1] for s in segments for p in s]
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None


def union(boxes):
    boxes = [b for b in boxes if b]
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes)) if boxes else None


def connected(segment_lists, reach):
    """Groups of element indexes whose centerlines come within `reach`: their strokes touch."""
    from shapely.geometry import LineString, MultiLineString
    shapes = [MultiLineString([LineString(s) for s in segs if len(s) > 1]) if segs else None
              for segs in segment_lists]
    parent = list(range(len(shapes)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i, a in enumerate(shapes):
        for j in range(i + 1, len(shapes)):
            b = shapes[j]
            if a is not None and b is not None and not a.is_empty and not b.is_empty \
                    and a.distance(b) <= reach + 1e-6:
                parent[find(j)] = find(i)
    groups = {}
    for i in range(len(shapes)):
        groups.setdefault(find(i), []).append(i)
    return sorted(groups.values(), key=lambda g: g[0])


def component(request, canvas):
    root = ET.fromstring(request['document'])
    base = float(root.get('stroke-width') or STROKE)
    found = elements(root)
    if not found:
        raise ValueError('The artwork has no drawable elements.')
    stroke_attrs = {k: v for k, v in root.attrib.items() if k in INHERITED}
    segment_lists = [segments_of(e, {**stroke_attrs, **own}) for e, own in found]
    source = [bbox(s) for s in segment_lists]
    scale, tx, ty = float(request['scale']), float(request['tx']), float(request['ty'])
    if scale <= 0:
        raise ValueError('Placement scale must be positive.')

    def to_canvas(b):
        return [b[0] * scale + tx, b[1] * scale + ty, b[2] * scale + tx, b[3] * scale + ty]
    layout = request.get('layout')
    groups = [g for g in connected(segment_lists, STROKE / scale) if union(source[i] for i in g)]
    result = {'role': request['role'], 'markup': [markup(e, own) for e, own in found],
              'names': [e.get('id') or local(e.tag) for e, _own in found],
              'sources': [list(b) if b else None for b in source], 'elements': [
        {'paths': g, 'source': list(union(source[i] for i in g)), 'box': to_canvas(union(source[i] for i in g))}
        for g in groups]}
    if layout is None:
        return result

    # Bake: every listed group lands on its own integer box on the canvas.
    drawable = [i for i, b in enumerate(source) if b]
    seen = sorted(i for g in layout for i in g['paths'])
    if seen != drawable:
        raise ValueError('Each element of the %s must be placed exactly once.' % request['role'])
    out = ET.Element('{%s}svg' % NS, {
        'width': str(canvas), 'height': str(canvas), 'viewBox': '0 0 %s %s' % (canvas, canvas),
        'fill': root.get('fill', 'none'), 'stroke': root.get('stroke', 'currentColor'),
        'stroke-width': str(STROKE), 'stroke-linecap': root.get('stroke-linecap', 'round'),
        'stroke-linejoin': root.get('stroke-linejoin', 'round')})
    placed = {}
    for group in layout:
        x0, y0, x1, y1 = union(source[i] for i in group['paths'])
        scales = []
        for extent, target in ((x1 - x0, group['w']), (y1 - y0, group['h'])):
            # An axis without extent (a straight rule) has nothing to scale and stays flat.
            if extent <= 1e-9:
                if target != 0:
                    raise ValueError('A flat element keeps zero size along its flat axis.')
                scales.append(1.0)
            elif target < 1:
                raise ValueError('An element must stay at least one unit on each axis.')
            else:
                scales.append(target / extent)
        sx, sy = scales
        if x1 - x0 <= 1e-9 and y1 - y0 > 1e-9:
            sx = sy
        if y1 - y0 <= 1e-9 and x1 - x0 > 1e-9:
            sy = sx
        for i in group['paths']:
            placed[i] = (sx, sy, group['x'] - x0 * sx, group['y'] - y0 * sy)
    boxes = {}
    for i, (element, own) in enumerate(found):
        if i not in placed:
            continue
        sx, sy, dx, dy = placed[i]
        copy_ = copy.deepcopy(element)
        copy_.tail = None
        for key, value in own.items():
            copy_.set(key, value)
        # The stroke never scales: a width other than the drawing's own keeps its ratio to it.
        if copy_.get('stroke-width') is not None:
            copy_.set('stroke-width', fmt(float(copy_.get('stroke-width')) / base * STROKE))
        copy_.attrib.pop('id', None)
        transform_element(copy_, sx, sy, dx, dy)
        out.append(copy_)
        boxes[i] = bbox(segments_of(copy_, {'stroke-width': str(STROKE)}))
    ET.register_namespace('', NS)
    result['document'] = ET.tostring(out, encoding='unicode')
    result['bounds'] = list(union(boxes.values()))
    result['elements'] = [{'paths': g['paths'], 'source': list(union(source[i] for i in g['paths'])),
                           'box': list(union(boxes[i] for i in g['paths']))} for g in layout]
    return result


if __name__ == '__main__':
    try:
        request = json.loads(sys.stdin.read())
        print(json.dumps({'components': [component(c, request.get('canvas', 64))
                                         for c in request['components']]}))
    except (ValueError, KeyError, TypeError, ET.ParseError) as error:
        print(json.dumps({'error': str(error) or 'Could not read the layout.'}))
        sys.exit(1)
