"""Editable stroke geometry (the Browser Edit graph) read back from a flat SVG drawing.

Uploaded icons are an SVG, not a Python model, so no build pushes a graph for them. `graph_from_svg`
turns the drawing's paths into the graph the geometry editor and stroke_edits use (the graphics service's
POST /svg-graph): `line`, `arc` and `bezier` primitives, one contour per subpath. Each top-level group with
an id prefixes its element ids, so its strokes can be told apart and selected on their own.
"""
from __future__ import annotations

import xml.etree.ElementTree as ET

from svgpathtools import Arc, CubicBezier, Line, QuadraticBezier, parse_path

SUB_FAMILIES = ('sub', 'symbol', 'sub-36', 'symbol24')
SHAPES = ('path', 'line', 'polyline', 'polygon', 'rect', 'circle', 'ellipse')


def local(tag):
    return tag.rsplit('}', 1)[-1]


def num(v):
    v = round(float(v), 4)
    return int(v) if v == int(v) else v


def pt(z):
    return [num(z.real), num(z.imag)]


def shape_d(el):
    """Path data for a basic shape (attributes as drawn; transforms must already be flattened)."""
    tag, f = local(el.tag), lambda name: float(el.get(name) or 0)
    if tag == 'path':
        return el.get('d') or ''
    if tag == 'line':
        return f'M{f("x1")} {f("y1")}L{f("x2")} {f("y2")}'
    if tag in ('polyline', 'polygon'):
        values = [float(v) for v in (el.get('points') or '').replace(',', ' ').split()]
        pairs = [f'{values[i]} {values[i + 1]}' for i in range(0, len(values) - 1, 2)]
        return ('M' + 'L'.join(pairs) + ('Z' if tag == 'polygon' else '')) if pairs else ''
    if tag in ('circle', 'ellipse'):
        cx, cy = f('cx'), f('cy')
        rx, ry = (f('r'), f('r')) if tag == 'circle' else (f('rx'), f('ry'))
        return f'M{cx - rx} {cy}A{rx} {ry} 0 0 1 {cx + rx} {cy}A{rx} {ry} 0 0 1 {cx - rx} {cy}Z'
    if tag == 'rect':
        x, y, w, h = f('x'), f('y'), f('width'), f('height')
        rx = min(f('rx') or f('ry'), w / 2); ry = min(f('ry') or rx, h / 2)
        if not rx:
            return f'M{x} {y}H{x + w}V{y + h}H{x}Z'
        return (f'M{x + rx} {y}H{x + w - rx}A{rx} {ry} 0 0 1 {x + w} {y + ry}V{y + h - ry}A{rx} {ry} 0 0 1 {x + w - rx} {y + h}'
                f'H{x + rx}A{rx} {ry} 0 0 1 {x} {y + h - ry}V{y + ry}A{rx} {ry} 0 0 1 {x + rx} {y}Z')
    return ''


def cubic(seg):
    """A quadratic as its exact cubic."""
    c1 = seg.start + 2 / 3 * (seg.control - seg.start)
    c2 = seg.end + 2 / 3 * (seg.control - seg.end)
    return CubicBezier(seg.start, c1, c2, seg.end)


def primitives_of(subpath, prefix, counter):
    """Primitives of one continuous subpath; consecutive cubics join into one bezier primitive."""
    out = []
    for seg in subpath:
        if isinstance(seg, QuadraticBezier):
            seg = cubic(seg)
        if isinstance(seg, Arc) and abs(seg.rotation) > 1e-9:
            # The editor's arcs are axis-aligned; a rotated arc is kept as its cubic approximation.
            for c in seg.as_cubic_curves():
                out.append(('bezier', c))
            continue
        out.append(('bezier' if isinstance(seg, CubicBezier) else 'arc' if isinstance(seg, Arc) else 'line', seg))
    result = []
    for kind, seg in out:
        if kind == 'bezier' and result and result[-1]['kind'] == 'bezier':
            result[-1]['segments'].append([pt(seg.control1), pt(seg.control2), pt(seg.end)])
            result[-1]['end'] = pt(seg.end)
            continue
        counter[0] += 1
        p = {'kind': kind, 'element_id': f'{prefix}-{counter[0]}', 'start': pt(seg.start), 'end': pt(seg.end)}
        if kind == 'bezier':
            p['segments'] = [[pt(seg.control1), pt(seg.control2), pt(seg.end)]]
        elif kind == 'arc':
            p.update(radius_x=num(seg.radius.real), radius_y=num(seg.radius.imag), large_arc=bool(seg.large_arc), sweep=bool(seg.sweep))
        result.append(p)
    return result


def graph_from_svg(svg: str, *, canvas: int, family: str, icon_id: str = '', name: str = '', profile: str = '') -> dict:
    root = ET.fromstring(svg)
    if any(el.get('transform') for el in root.iter()):
        raise ValueError('This SVG uses transforms; Browser Edit needs flat paths. Upload it again without transforms.')
    primitives, contours = [], []

    def walk(node, role, counters):
        for child in node:
            tag = local(child.tag)
            if tag in ('title', 'desc', 'metadata', 'defs', 'style'):
                continue
            if tag == 'g':
                walk(child, role, counters)
                continue
            if tag not in SHAPES or (child.get('stroke') == 'none'):
                continue
            d = shape_d(child)
            if not d.strip():
                continue
            for sub in parse_path(d).continuous_subpaths():
                if not len(sub):
                    continue
                members = primitives_of(sub, role, counters['p'])
                if not members:
                    continue
                counters['c'][0] += 1
                primitives.extend(members)
                contours.append({'contour_id': f'{role}-{counters["c"][0]}', 'members': [m['element_id'] for m in members],
                                 'closed': bool(sub.isclosed())})

    groups = [c for c in root if local(c.tag) == 'g' and c.get('id')]
    loose = [c for c in root if not (local(c.tag) == 'g' and c.get('id'))]
    for g in groups:
        walk(g, g.get('id'), {'p': [0], 'c': [0]})
    if loose:
        holder = ET.Element('g')
        holder.extend(loose)
        walk(holder, 'stroke', {'p': [0], 'c': [0]})
    graph = {'icon_id': icon_id, 'name': name, 'family': family, 'profile': profile, 'canvas_size': canvas,
             'semantic_role': 'SUB' if family in SUB_FAMILIES else 'MAIN',
             'style': {'stroke_width': 4, 'line_cap': 'round', 'line_join': 'round', 'grid': 1},
             'primitives': primitives, 'contours': contours, 'anchors': {}, 'relationships': []}
    return {**graph, **fitted_keyshape(graph)}


def fitted_keyshape(graph: dict) -> dict:
    """The family keyshape whose bounds are the drawing's visible ink, as an authored icon declares it; FREE
    around the ink when none is (Browser Edit can pick another)."""
    from icon_set.model.keyshapes import Keyshape
    from icon_set.model.primitives import primitive_from_dict
    from icon_set.model.profiles import Profile
    from icon_set.validation.envelope import visible_bounds

    ink = [num(v) for v in visible_bounds([primitive_from_dict(p) for p in graph['primitives']])]
    if graph['profile'] in Profile.__members__:
        for keyshape in Keyshape:
            if keyshape is Keyshape.FREE:
                continue
            try:
                bounds = list(keyshape.bounds_for(Profile[graph['profile']]))
            except ValueError:
                continue
            if bounds == ink:
                return {'keyshape': keyshape.name, 'keyshape_bounds': bounds}
    return {'keyshape': 'FREE', 'keyshape_bounds': ink,
            'free_keyshape': {'bounds': ink, 'approval_id': None, 'rationale': 'Uploaded drawing: its strokes were read back from the SVG.'}}
