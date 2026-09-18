"""Ink-triggered mirror checks against the union of authored centerlines.

Ink is a heuristic (alpha-mask intersection/union), not a symmetry proof.
Geometry is compared independently of path names, direction or segmentation.
Curves are flattened with a bounded chord error; the centerline comparison
samples chord endpoints and midpoints. This is a diagnostic with explicit
numerical resolution, not a symbolic proof of arbitrary curve equality.
"""
from __future__ import annotations

import io
import math
import xml.etree.ElementTree as ET

from ..model.primitives import Arc, Bezier, Line
from .envelope import arc_geometry, centerline_bounds

RULES = {
    'version': 1,
    'ink_min_iou': 0.98,
    'ink_samples_per_unit': 16,
    'centerline_tolerance': 0.0001,
    'curve_flatness': 0.00001,
    'maximum_sample_spacing': 0.25,
    'axes': ['vertical', 'horizontal'],
    'axis_origin': 'painted bounds midpoint (not canvas midpoint)',
    'centerline_measurement': 'sampled distance to union of bounded-error chords',
}


def _chords(primitive, flatness):
    if isinstance(primitive, Line):
        return [(primitive.start.as_tuple(), primitive.end.as_tuple())]
    if isinstance(primitive, Arc):
        arc = arc_geometry(primitive)
        # max radius bounds the second derivative of the ellipse. The linear
        # interpolation error on an angular interval is <= R * delta**2 / 8.
        count = max(1, math.ceil(abs(arc.delta_angle) *
                                math.sqrt(max(arc.radius_x, arc.radius_y) / (8 * flatness))))
        if count > 20000:
            raise ValueError('symmetry: arc exceeds subdivision budget')
        points = [arc.point(arc.start_angle + arc.delta_angle * i / count)
                  for i in range(count + 1)]
        return list(zip(points, points[1:]))
    if not isinstance(primitive, Bezier):
        raise TypeError(f'symmetry: unsupported primitive {type(primitive).__name__}')
    result = []
    pending = [(cubic, 0) for cubic in reversed(primitive.cubics())]
    while pending:
        (a, b, c, d), depth = pending.pop()
        # Distance to the finite chord (not its infinite line) also catches
        # collinear reversals and overshooting cubic controls.
        def distance(p):
            vx, vy = d[0] - a[0], d[1] - a[1]
            length2 = vx * vx + vy * vy
            t = max(0, min(1, ((p[0]-a[0])*vx + (p[1]-a[1])*vy) / length2)) if length2 else 0
            return math.hypot(p[0]-a[0]-t*vx, p[1]-a[1]-t*vy)
        if max(distance(b), distance(c)) <= flatness:
            result.append((a, d))
            continue
        if depth >= 24 or len(result) + len(pending) > 20000:
            raise ValueError('symmetry: cubic exceeds subdivision budget')
        def mid(p, q):
            return ((p[0]+q[0])/2, (p[1]+q[1])/2)
        ab, bc, cd = mid(a, b), mid(b, c), mid(c, d)
        abc, bcd = mid(ab, bc), mid(bc, cd)
        middle = mid(abc, bcd)
        pending.extend([((middle, bcd, cd, d), depth+1), ((a, ab, abc, middle), depth+1)])
    return result


def _nearest(points, segments):
    """Nearest points on the whole centerline union, in bounded memory."""
    import numpy as np
    best = np.full(len(points), np.inf)
    positions = np.zeros_like(points)
    for start in range(0, len(segments), 256):
        block = segments[start:start+256]
        a = block[:, 0]
        delta = block[:, 1] - a
        length2 = (delta * delta).sum(axis=1)
        offset = points[:, None, :] - a
        t = np.clip((offset * delta).sum(axis=2) / np.where(length2 > 0, length2, 1), 0, 1)
        closest = a + t[:, :, None] * delta
        squared = ((points[:, None, :] - closest)**2).sum(axis=2)
        indices = squared.argmin(axis=1)
        values = squared[np.arange(len(points)), indices]
        take = values < best
        positions[take] = closest[np.arange(len(points)), indices][take]
        best[take] = values[take]
    return np.sqrt(best), positions


def _spatial_index(segments):
    """Index chord boxes in unit cells, retaining long lines and boundary hits."""
    from collections import defaultdict
    import numpy as np
    cells = defaultdict(list)
    for index, (a, b) in enumerate(segments):
        low = np.floor(np.minimum(a, b)).astype(int)
        high = np.floor(np.maximum(a, b)).astype(int)
        for x in range(low[0], high[0]+1):
            for y in range(low[1], high[1]+1):
                cells[x, y].append(index)
    return cells


def _nearest_indexed(points, segments, cells):
    import numpy as np
    distances = np.empty(len(points))
    positions = np.empty_like(points)
    keys = np.floor(points).astype(int)
    for x, y in np.unique(keys, axis=0):
        selected = np.flatnonzero((keys == (x, y)).all(axis=1))
        batch = points[selected]
        nearby = sorted({i for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                         for i in cells.get((x+dx, y+dy), ())})
        if nearby:
            d, p = _nearest(batch, segments[nearby])
            # The searched square's exterior is at least this far away.
            # Fall back whenever an omitted chord could improve the answer.
            edge = np.minimum(batch - (x-1, y-1), (x+2, y+2) - batch).min(axis=1)
            retry = d >= edge
            if retry.any():
                d[retry], p[retry] = _nearest(batch[retry], segments)
        else:
            d, p = _nearest(batch, segments)
        distances[selected], positions[selected] = d, p
    return distances, positions


def analyze(icon, *, drawing=None, document=None, ink_min_iou=None):
    import cairosvg
    import numpy as np
    from PIL import Image

    threshold = RULES['ink_min_iou'] if ink_min_iou is None else ink_min_iou
    if not math.isfinite(threshold) or not 0 < threshold <= 1:
        raise ValueError('ink_min_iou must be in (0, 1]')
    drawing = icon.draw() if drawing is None else drawing
    document = icon.to_svg() if document is None else document
    if not drawing.primitives:
        raise ValueError('symmetry: empty drawing')
    left, top, right, bottom = centerline_bounds(list(drawing.primitives))
    cx, cy = (left + right)/2, (top + bottom)/2
    # Reframe without moving geometry. This avoids clipping and places the
    # actual ink axes exactly between mirror pixel pairs, even off canvas.
    scale = RULES['ink_samples_per_unit']
    width = max(2, 2 * math.ceil((right-left+8) * scale/2))
    height = max(2, 2 * math.ceil((bottom-top+8) * scale/2))
    from ..model.icons.sub._text_base import TextSub32
    over_budget = width * height > 4096 * 4096 if isinstance(icon, TextSub32) else max(width, height) > 4096
    if over_budget:
        raise ValueError('symmetry: render exceeds measurement budget')
    root = ET.fromstring(document)
    root.set('viewBox', f'{cx-width/scale/2} {cy-height/scale/2} {width/scale} {height/scale}')
    png = cairosvg.svg2png(bytestring=ET.tostring(root), output_width=width, output_height=height)
    ink = np.asarray(Image.open(io.BytesIO(png)).convert('RGBA'))[:, :, 3].astype(float)/255
    if not ink.any():
        raise ValueError('symmetry: empty rendered ink')
    axes = []
    for name, dimension, center in [('vertical', 1, cx), ('horizontal', 0, cy)]:
        mirror = np.flip(ink, axis=dimension)
        iou = float(np.minimum(ink, mirror).sum() / np.maximum(ink, mirror).sum())
        axes.append(dict(axis=name, coordinate=center, ink_iou=iou,
                         ink_symmetric=iou >= threshold, status='not_applicable', mismatches=[]))
    candidates = [axis for axis in axes if axis['ink_symmetric']]
    if candidates:
        groups = [(p.element_id, np.asarray(_chords(p, RULES['curve_flatness']), dtype=float))
                  for p in drawing.primitives]
        # SVG Z contributes a real closing line even when no primitive owns it.
        by_id = drawing.by_id()
        for contour in drawing.contours:
            if contour.closed:
                a = by_id[contour.members[-1]].end.as_tuple()
                b = by_id[contour.members[0]].start.as_tuple()
                if a != b:
                    groups.append((contour.contour_id + ':close', np.asarray([(a, b)], dtype=float)))
        segments = np.concatenate([group for _, group in groups])
        if len(segments) > 20000:
            raise ValueError('symmetry: drawing exceeds subdivision budget')
        cells = _spatial_index(segments)
        for axis in candidates:
            dimension = 0 if axis['axis'] == 'vertical' else 1
            maximum = 0.0
            for element_id, chords in groups:
                # Subdivide straight spans for coverage, too: endpoints alone
                # cannot distinguish a full line from two disconnected ends.
                samples = []
                for a, b in chords:
                    count = max(2, math.ceil(float(np.linalg.norm(b-a)) / RULES['maximum_sample_spacing']))
                    samples.extend(a + (b-a) * (i/count) for i in range(count+1))
                points = np.asarray(samples)
                points[:, dimension] = 2*axis['coordinate'] - points[:, dimension]
                worst = None
                for start in range(0, len(points), 64):
                    batch = points[start:start+64]
                    distances, positions = _nearest_indexed(batch, segments, cells)
                    index = int(distances.argmax())
                    distance = float(distances[index])
                    if worst is None or distance > worst[0]:
                        worst = (distance, batch[index].tolist(), positions[index].tolist())
                maximum = max(maximum, worst[0])
                # Subtract both curve approximation errors before declaring a
                # mismatch. Numerical flattening alone cannot fail a mirror.
                lower = max(0.0, worst[0] - 2*RULES['curve_flatness'])
                if lower > RULES['centerline_tolerance']:
                    axis['mismatches'].append(dict(element_id=element_id,
                        distance=worst[0], distance_lower_bound=lower,
                        mirrored_point=worst[1], nearest_point=worst[2]))
            axis['max_sampled_distance'] = maximum
            axis['status'] = 'fail' if axis['mismatches'] else 'pass'
    return dict(status='fail' if any(a['status'] == 'fail' for a in axes) else
                ('pass' if candidates else 'not_applicable'), axes=axes,
                rules={**RULES, 'ink_min_iou': threshold})


def failure_messages(result):
    for axis in result['axes']:
        for mismatch in axis['mismatches']:
            yield (f"symmetry [{mismatch['element_id']}]: ink is {axis['ink_iou']:.2%} mirrored "
                   f"about {axis['axis']} axis {axis['coordinate']:g}, but centerline differs "
                   f"by {mismatch['distance']:.6g} units near {mismatch['mirrored_point']}")
