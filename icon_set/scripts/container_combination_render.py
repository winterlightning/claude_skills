"""A container pair's combined 64x64 icon: the container as drawn, with its symbol placed on the grid.

The symbol sits around `center`. With no `ink` size it keeps its natural size in the standard 32x32
box (its viewBox fitted like an <img>); with `ink` = [W, H] (even) its painted ink box is exactly W x H,
each axis scaled on its own. Either way the symbol is baked by the side combination engine helper
(combination_layout_svg.py): coordinates are rewritten onto whole grid units and the stroke stays 4,
the same way a saved side layout is.
"""
from __future__ import annotations

import math
import re
import xml.etree.ElementTree as ET

from icon_set.scripts.combination_experiment import layout_components
from icon_set.scripts.combination_layout_svg import SHAPES, local, transform_element

NS = 'http://www.w3.org/2000/svg'
CANVAS, BOX, STROKE = 64, 32, 4
PRESENTATION = ('fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin')


def fit(root, size=BOX):
    """(scale, tx, ty) fitting the drawing's viewBox into a size x size box, centered (preserveAspectRatio meet)."""
    try:
        vx, vy, vw, vh = (float(v) for v in root.get('viewBox', '').replace(',', ' ').split())
        if vw <= 0 or vh <= 0:
            raise ValueError
    except ValueError:
        vx, vy = 0.0, 0.0
        vw, vh = float(root.get('width') or size), float(root.get('height') or size)
    k = min(size / vw, size / vh)
    return k, (size - vw * k) / 2 - vx * k, (size - vh * k) / 2 - vy * k


TRANSFORM = re.compile(r'(translate|scale|matrix)\s*\(([^)]*)\)')


def affine(text):
    """(sx, sy, tx, ty) of a transform list made of translate / scale / axis-aligned matrix steps."""
    sx, sy, tx, ty = 1.0, 1.0, 0.0, 0.0
    steps = TRANSFORM.findall(text)
    if TRANSFORM.sub('', text).strip(' ,'):
        raise ValueError('Rotated or skewed artwork cannot be combined; redraw it without transforms.')
    for name, args in steps:
        v = [float(n) for n in re.split(r'[\s,]+', args.strip()) if n]
        if name == 'translate':
            a, b, c, d, e, f = 1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0
        elif name == 'scale':
            a, b, c, d, e, f = v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0
        else:
            a, b, c, d, e, f = v
        if abs(b) > 1e-9 or abs(c) > 1e-9:
            raise ValueError('Rotated or skewed artwork cannot be combined; redraw it without transforms.')
        # Steps apply right to left: the running transform maps after this step.
        tx, ty = tx + sx * e, ty + sy * f
        sx, sy = sx * a, sy * d
    return sx, sy, tx, ty


def flatten(svg):
    """The drawing with group and element transforms written into its coordinates (the engine refuses transforms)."""
    root = ET.fromstring(svg)

    def walk(node, t):
        for child in node:
            own = affine(child.attrib.pop('transform', ''))
            sx, sy, tx, ty = t
            here = (sx * own[0], sy * own[1], tx + sx * own[2], ty + sy * own[3])
            if local(child.tag) in SHAPES:
                if here != (1.0, 1.0, 0.0, 0.0):
                    transform_element(child, *here)
            else:
                walk(child, here)
    walk(root, (1.0, 1.0, 0.0, 0.0))
    ET.register_namespace('', NS)
    return ET.tostring(root, encoding='unicode')


def union(boxes):
    boxes = [b for b in boxes if b]
    return [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]


def check(center, ink):
    if not (isinstance(center, list) and len(center) == 2 and all(isinstance(v, (int, float)) for v in center)
            and all(0 <= v <= CANVAS for v in center)):
        raise ValueError('The symbol center must be [x, y] inside the 64x64 canvas.')
    if ink is not None and not (isinstance(ink, list) and len(ink) == 2
                                and all(isinstance(v, (int, float)) and v == int(v) and 4 <= v <= CANVAS for v in ink)):
        # Whole units (odd too): a symbol whose elements were placed one by one keeps its exact size; with an
        # odd size the center sits on a half unit, so both edges are still on grid lines.
        raise ValueError('The symbol size must be [width, height], each a whole number from 4 to 64.')


def render(main_svg: str, symbol_svg: str, center: list, ink: list | None = None) -> dict:
    check(center, ink)
    main_svg, symbol_svg = flatten(main_svg), flatten(symbol_svg)
    symbol = ET.fromstring(symbol_svg)
    k, tx, ty = fit(symbol)
    placed = {'role': 'sub', 'document': symbol_svg, 'scale': k, 'tx': center[0] - BOX / 2 + tx,
              'ty': center[1] - BOX / 2 + ty, 'layout': None}
    measured = layout_components([placed, {'role': 'main', 'document': main_svg, 'scale': 1, 'tx': 0, 'ty': 0, 'layout': None}],
                                 CANVAS)
    sources = measured['sub']['sources']
    drawable = [i for i, b in enumerate(sources) if b]
    x0, y0, x1, y1 = union(sources)
    natural = union(g['box'] for g in measured['sub']['elements'])

    def half_up(v):  # Math.round, as the page rounds
        return math.floor(v + 0.5)

    def axis(start, end, extent, c, size):
        # A flat axis (a straight rule) keeps zero extent at the placed position.
        if extent <= 1e-9:
            return half_up(start), 0
        if size is None:
            # Natural size, snapped like a resize: the ink edge on a grid line and the ink size even.
            return half_up(start), max(2, 2 * half_up((end - start) / 2))
        return int(c - size / 2 + STROKE / 2), int(size - STROKE)
    x, w = axis(natural[0], natural[2], x1 - x0, center[0], ink[0] if ink else None)
    y, h = axis(natural[1], natural[3], y1 - y0, center[1], ink[1] if ink else None)
    baked = layout_components([{**placed, 'layout': [{'paths': drawable, 'x': x, 'y': y, 'w': w, 'h': h}]}], CANVAS)['sub']
    b = baked['bounds']
    if b[0] - STROKE / 2 < -1e-6 or b[1] - STROKE / 2 < -1e-6 or b[2] + STROKE / 2 > CANVAS + 1e-6 or b[3] + STROKE / 2 > CANVAS + 1e-6:
        raise ValueError('The symbol extends beyond the 64x64 canvas.')

    ET.register_namespace('', NS)
    out = ET.Element('{%s}svg' % NS, {'width': str(CANVAS), 'height': str(CANVAS), 'viewBox': f'0 0 {CANVAS} {CANVAS}',
                                      'fill': 'none', 'stroke': 'currentColor', 'stroke-width': str(STROKE),
                                      'stroke-linecap': 'round', 'stroke-linejoin': 'round'})
    for gid, document in (('container', main_svg), ('symbol', baked['document'])):
        root = ET.fromstring(document)
        group = ET.SubElement(out, '{%s}g' % NS, {'id': gid, **{a: root.get(a) for a in PRESENTATION if root.get(a)}})
        for child in root:
            if child.tag.rsplit('}', 1)[-1] not in ('title', 'desc', 'metadata'):
                group.append(child)
    main_box = union(g['box'] for g in measured['main']['elements'])

    def painted(box):
        return {'x': box[0] - STROKE / 2, 'y': box[1] - STROKE / 2, 'w': box[2] - box[0] + STROKE, 'h': box[3] - box[1] + STROKE}
    svg = ET.tostring(out, encoding='unicode')
    # The drawing's stroke geometry, so the geometry editor can select and edit the container and symbol strokes.
    from icon_set.scripts.svg_graph import graph_from_svg
    graph = graph_from_svg(svg, canvas=CANVAS, family='container_combination64', profile='CONTAINER64')
    return {'svg': svg, 'canvas': CANVAS, 'graph': graph,
            'placements': [{'role': 'main', 'painted_box': painted(main_box)}, {'role': 'sub', 'painted_box': painted(b)}],
            'center': center, 'ink': ink}
