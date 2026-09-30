#!/usr/bin/env python3
"""Resize CONTAINER64 icons onto the v2 keyshapes as clean, editable models.

    ICON_CONTRACT_OVERLAY=icon_set/work/container64-v2/overlay.json \\
        python3 icon_set/scripts/container_v2_fit.py [--icons ID ...] [--no-gate]

Each icon is resolved with ``draw()``, so helpers, loops and polylines arrive
as plain primitives. Coordinates are then remapped per axis through a
*lattice*: the distinct node distances from the canvas centre, not each point
on its own. A column shared by ten points moves once, mirrored columns move by
the same amount, and gaps of 8 or less (stroke detail, MIC spacing) keep their
size while the long spans absorb the change. Arc radii are rebuilt from the
snapped endpoints. The stroke is never scaled.

Modules are written to ``icon_set/work/container64-v2/`` with absolute
imports, one per source module, and gated with ``inspect_icon`` under the
overlay. Nothing is registered or published.
"""
from __future__ import annotations

import argparse
import importlib.util
import inspect
import json
import math
import sys
from collections import defaultdict
from copy import deepcopy
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model.keyshapes import Keyshape  # noqa: E402
from icon_set.model.primitives import Arc, Bezier, Line, Point  # noqa: E402

WORK = REPO_ROOT / 'icon_set/work/container64-v2'
AUTHOR = 'claude-opus-5-5'
CENTER = 32
#: Gaps this small are stroke detail or spacing; they keep their size.
PROTECTED_GAP = 8
#: Centerline minimum between separate strokes on CONTAINER64 (MIC 2 + stroke 4).
MIN_GAP = 6
FAMILY_ANCHORS = {'center', 'content-top-left', 'content-bottom-right'}


# -- lattice -----------------------------------------------------------------

def allocate(values: list[int], lo: int, hi: int, notes: list | None = None) -> dict[int, int]:
    """Map sorted source coordinates onto [lo, hi] by moving whole gaps.

    Gaps are grouped with their mirror image about the canvas centre so a
    symmetric drawing stays symmetric. Shrinking takes from the long gaps
    first and never pushes a gap of 8 or less below its size until the long
    gaps are down to 8; then every gap may go to the MIC minimum 6, then 1.
    Each step goes to the class least changed so far, relative to its source
    size, so long spans shrink in proportion.
    """
    # Mirror every value so each gap has a twin and the map stays symmetric
    # even where the drawing is not; the extra values are only breakpoints.
    values = sorted(set(values) | {2 * CENTER - v for v in values})
    if len(values) == 1:
        return {values[0]: (lo + hi) // 2}
    gaps = [b - a for a, b in zip(values, values[1:])]
    index = {(a, b): i for i, (a, b) in enumerate(zip(values, values[1:]))}
    classes, seen = [], set()
    for i, (a, b) in enumerate(zip(values, values[1:])):
        if i in seen:
            continue
        j = index.get((2 * CENTER - b, 2 * CENTER - a))
        if j == i:
            classes.append(([i], 2))           # straddles the centre
        elif j is not None and j not in seen:
            classes.append(([i, j], 1))
            seen.add(j)
        else:
            classes.append(([i], 1))
        seen.add(i)
    cur = list(gaps)
    deficit = sum(gaps) - (hi - lo)
    stages = (lambda g: PROTECTED_GAP if g > PROTECTED_GAP else None,
              lambda g: min(g, MIN_GAP),
              lambda g: 1)
    for relax_symmetry in (False, True):
        for floor_of in stages:
            while deficit:
                sign = 1 if deficit > 0 else -1
                best = None
                for members, step in classes:
                    groups = [[m] for m in members] if relax_symmetry else [members]
                    for group in groups:
                        s = 1 if relax_symmetry else step
                        amount = s * len(group)
                        if amount > abs(deficit):
                            continue
                        i = group[0]
                        floor = floor_of(gaps[i])
                        if floor is None:
                            continue
                        if sign > 0 and cur[i] - s < floor:
                            continue
                        ratio = cur[i] / gaps[i]
                        key = ratio if sign > 0 else -ratio
                        if best is None or (key, gaps[i]) > best[0]:
                            best = ((key, gaps[i]), group, s, amount)
                if best is None:
                    break
                _key, group, s, amount = best
                for i in group:
                    cur[i] -= sign * s
                deficit -= sign * amount
            if not deficit:
                break
        if not deficit:
            break
        if notes is not None:
            notes.append('lattice: symmetric allocation impossible, one side moved alone')
    if deficit:
        raise ValueError(f'cannot fit gaps {gaps} into {hi - lo}')
    out, run = {}, lo
    out[values[0]] = lo
    for value, gap in zip(values[1:], cur):
        run += gap
        out[value] = run
    return out


class AxisMap:
    """Snapped lattice coordinates, linear between them for everything else."""

    def __init__(self, table: dict[int, int]):
        self.table = table
        self.keys = sorted(table)

    def __call__(self, value: float) -> float:
        if value in self.table:
            return float(self.table[value])
        keys = self.keys
        if len(keys) == 1:
            return self.table[keys[0]] + (value - keys[0])
        if value < keys[0]:
            lo, hi = keys[0], keys[1]
        elif value > keys[-1]:
            lo, hi = keys[-2], keys[-1]
        else:
            hi = next(k for k in keys if k > value)
            lo = keys[keys.index(hi) - 1]
        t = (value - lo) / (hi - lo)
        return self.table[lo] + t * (self.table[hi] - self.table[lo])

    def snap(self, value: int) -> int:
        if value not in self.table:
            raise ValueError(f'node coordinate {value} is not on the lattice')
        return self.table[value]


def lattice_values(primitives) -> tuple[set[int], set[int]]:
    """Node coordinates plus the rounded extremes of arc bulges."""
    from icon_set.validation.envelope import arc_geometry
    xs, ys = set(), set()
    for p in primitives:
        for point in (p.start, p.end):
            xs.add(point.x)
            ys.add(point.y)
        if isinstance(p, Arc):
            g = arc_geometry(p)
            for k in range(4):
                angle = k * math.pi / 2
                if g.contains_angle(angle) or g.contains_angle(angle - 2 * math.pi):
                    x, y = g.point(angle)
                    (xs if k % 2 == 0 else ys).add(round(x if k % 2 == 0 else y))
    return xs, ys


# -- fit ---------------------------------------------------------------------

def fit(icon, target: Keyshape, keep_round: bool = True):
    from icon_set.validation.envelope import centerline_bounds, centerline_radial_extent

    drawing = icon.draw()
    source = list(drawing.primitives)
    left, top, right, bottom = centerline_bounds(source)
    xs, ys = lattice_values(source)
    notes: list[str] = []
    tb = target.bounds_for(icon.profile)
    if target.is_radial:
        extent = centerline_radial_extent(source, (CENTER, CENTER))
        scale = target.centerline_radius_for(icon.profile) / extent
        shared = sorted(xs | ys)
        lo = CENTER - round((CENTER - shared[0]) * scale)
        hi = CENTER + round((shared[-1] - CENTER) * scale)
        mx = my = AxisMap(allocate(shared, lo, hi, notes))
    else:
        mx = AxisMap(allocate(sorted(xs), tb[0] + 2, tb[2] - 2, notes))
        my = AxisMap(allocate(sorted(ys), tb[1] + 2, tb[3] - 2, notes))

    envelope = (tb[0] + 2, tb[1] + 2, tb[2] - 2, tb[3] - 2)
    moved, radii = (keep_circles(source, (left, top, right, bottom), envelope, mx, my,
                                 target.is_radial, notes) if keep_round else ({}, {}))

    def move(point: Point) -> Point:
        return moved.get(point, Point(mx.snap(point.x), my.snap(point.y)))

    primitives = []
    for p in source:
        start, end = move(p.start), move(p.end)
        if start == end and p.start != p.end:
            notes.append(f'{p.element_id}: endpoints collapsed')
        if isinstance(p, Line):
            primitives.append(Line(p.element_id, start, end))
        elif isinstance(p, Arc):
            if p.element_id in radii:
                r = radii[p.element_id]
                half = math.hypot(end.x - start.x, end.y - start.y) / 2
                primitives.append(Arc(p.element_id, start, end, max(r, math.ceil(half)),
                                      max(r, math.ceil(half)), p.large_arc, p.sweep))
            else:
                primitives.append(fit_arc(p, start, end, mx, my, notes))
        elif isinstance(p, Bezier):
            segments = []
            for c1, c2, knot in p.segments:
                segments.append((
                    (round(mx(c1[0]), 3), round(my(c1[1]), 3)),
                    (round(mx(c2[0]), 3), round(my(c2[1]), 3)),
                    (round(mx(knot[0]), 3), round(my(knot[1]), 3)),
                ))
            last = segments[-1]
            segments[-1] = (last[0], last[1], (end.x, end.y))
            primitives.append(Bezier(p.element_id, start, end, tuple(segments)))
        else:
            raise TypeError(type(p))
    candidate = deepcopy(icon)
    candidate.keyshape = target
    candidate.primitives = primitives
    candidate.contours = list(drawing.contours)
    candidate.relationships = list(drawing.relationships)
    candidate.anchors = {}
    for name, point in drawing.anchors:
        if name in FAMILY_ANCHORS:
            candidate.anchors[name] = point
        else:
            candidate.anchors[name] = Point(int(round(mx(point.x))), int(round(my(point.y))))
    if not target.is_radial:
        split_to_bounds(candidate, (tb[0] + 2, tb[1] + 2, tb[2] - 2, tb[3] - 2), notes)
    return candidate, notes


# -- repair: split a bulge onto the envelope ---------------------------------

def _sweep(g) -> float:
    return abs(g.delta_angle)


def _part(element_id: str, a: Point, b: Point, rx0: int, ry0: int, sweep: bool,
          axis: int, bound: int, target, touch: bool = True, large: bool = False) -> Arc | None:
    """Integer-radius arc a->b whose extreme on ``axis`` is exactly ``bound``.

    It is the flattest-to-roundest search nearest the source radii whose sweep
    stops at the node instead of passing the cardinal point.
    """
    from icon_set.validation.envelope import arc_geometry, centerline_bounds
    ratio = ry0 / rx0
    best = None
    for rx in range(1, 4 * max(rx0, ry0) + 40):
        ry = rx if rx0 == ry0 else max(1, round(rx * ratio))
        if True:
            arc = Arc(element_id, a, b, rx, ry, large, sweep)
            try:
                g = arc_geometry(arc)
            except ValueError:
                continue
            if abs(g.radius_x - rx) > 1e-9:
                continue                       # radii too small for the chord
            bounds = centerline_bounds([arc])
            inside = (bounds[0] >= target[0] - 1e-9 and bounds[1] >= target[1] - 1e-9
                      and bounds[2] <= target[2] + 1e-9 and bounds[3] <= target[3] + 1e-9)
            index = (0, 1, 2, 3)[axis]
            if inside and (not touch or abs(bounds[index] - bound) < 1e-9):
                cost = abs(rx - rx0) + abs(ry - ry0)
                if best is None or cost < best[0]:
                    best = (cost, arc)
    return None if best is None else best[1]


def split_to_bounds(candidate, target: tuple[int, int, int, int], notes: list) -> None:
    """Split each arc whose bulge misses or overshoots a side onto that side."""
    from icon_set.validation.envelope import arc_geometry, centerline_bounds
    for side in range(4):
        bounds = centerline_bounds(candidate.primitives)
        if abs(bounds[side] - target[side]) < 1e-9:
            continue
        axis_is_x = side in (0, 2)
        extreme = min if side < 2 else max
        coord = (lambda b: b[side])
        # Arcs whose bulge sets this side, within 6 units of the target.
        movers = [p for p in candidate.primitives if isinstance(p, Arc)
                  and abs(coord(centerline_bounds([p])) - bounds[side]) < 1e-6]
        nodes = [q for p in candidate.primitives for q in (p.start, p.end)
                 if abs((q.x if axis_is_x else q.y) - bounds[side]) < 1e-9]
        if not movers or abs(bounds[side] - target[side]) > 6:
            continue
        on_target = [q for p in candidate.primitives for q in (p.start, p.end)
                     if (q.x if axis_is_x else q.y) == target[side]]
        if on_target:
            # A node already touches the side: flatten the overshooting arcs.
            flat = {}
            for p in movers:
                arc = _part(p.element_id, p.start, p.end, p.radius_x, p.radius_y, p.sweep,
                            side, target[side], target, touch=False, large=p.large_arc)
                if arc is None:
                    notes.append(f'{p.element_id}: could not flatten inside side {side}')
                else:
                    flat[p.element_id] = arc
                    notes.append(f'{p.element_id}: radius {p.radius_x} -> {arc.radius_x} to stay inside side {side}')
            candidate.primitives = [flat.get(p.element_id, p) for p in candidate.primitives]
            continue
        angle = {0: math.pi, 1: -math.pi / 2, 2: 0.0, 3: math.pi / 2}[side]
        replaced = {}
        for p in movers:
            g = arc_geometry(p)
            x, y = g.point(angle)
            node = Point(target[side], round(y)) if axis_is_x else Point(round(x), target[side])
            a = _part(p.element_id + '-a', p.start, node, p.radius_x, p.radius_y, p.sweep, side, target[side], target)
            b = _part(p.element_id + '-b', node, p.end, p.radius_x, p.radius_y, p.sweep, side, target[side], target)
            if a is None or b is None:
                notes.append(f'{p.element_id}: could not split onto side {side}')
                continue
            replaced[p.element_id] = (a, b)
        if not replaced:
            continue
        prims = []
        for p in candidate.primitives:
            prims.extend(replaced.get(p.element_id, (p,)))
        candidate.primitives = prims
        in_contour = set()
        contours = []
        for c in candidate.contours:
            members = []
            for m in c.members:
                if m in replaced:
                    members += [replaced[m][0].element_id, replaced[m][1].element_id]
                    in_contour.add(m)
                else:
                    members.append(m)
            contours.append(type(c)(c.contour_id, tuple(members), c.closed))
        for old, (a, b) in replaced.items():
            if old not in in_contour:
                contours.append(type(candidate.contours[0] if candidate.contours else _contour())(
                    old, (a.element_id, b.element_id), False))
            notes.append(f'{old}: split at its bulge onto side {side}')
        candidate.contours = contours
        owner = {m: c.contour_id for c in contours for m in c.members}
        rels = []
        for r in candidate.relationships:
            members = tuple(owner.get(replaced[m][0].element_id, m) if m in replaced else m for m in r.members)
            rels.append(type(r)(r.kind, members))
        candidate.relationships = rels


def _contour():
    from icon_set.model.primitives import Contour
    return Contour('x', ())


def _ring(r: int) -> list[tuple[int, int]]:
    """Integer points exactly on a circle of radius r about the origin."""
    out = []
    for x in range(-r, r + 1):
        y2 = r * r - x * x
        y = math.isqrt(y2)
        if y * y == y2:
            out += [(x, y), (x, -y)]
    return out


def _angle_gap(a: float, b: float) -> float:
    return abs((a - b + math.pi) % (2 * math.pi) - math.pi)


def keep_circles(source, source_bounds, envelope, mx, my, radial: bool, notes: list):
    """Give every source circle one centre and one radius in the new drawing.

    Independent x and y lattices would turn a circle into an ellipse. A
    circle here is a set of equal-radius arcs on one centre sweeping at least
    half a turn. Its new radius is the mean of the two mapped radii, unless
    the circle touched the envelope on both sides of an axis, which then sets
    it. A single touched side pins the centre so the circle still touches.
    A circle that shares nodes with other geometry is only kept round when
    its nodes land within 1.5 units of where the lattice puts them.
    Returns {old node: new node} and {arc id: radius}.
    """
    from icon_set.validation.envelope import arc_geometry
    groups = defaultdict(list)
    for p in source:
        if isinstance(p, Arc) and p.radius_x == p.radius_y and p.radius_x >= 3:
            g = arc_geometry(p)
            if abs(g.radius_x - p.radius_x) > 1e-9:
                continue
            groups[(round(g.center_x, 3), round(g.center_y, 3), p.radius_x)].append((p, g))
    moved, radii = {}, {}
    L, T, R, B = source_bounds
    for (cx, cy, r), members in groups.items():
        if sum(abs(g.delta_angle) for _p, g in members) < math.pi - 1e-6:
            continue
        rx_m = (mx(cx + r) - mx(cx - r)) / 2
        ry_m = (my(cy + r) - my(cy - r)) / 2
        if abs(rx_m - ry_m) < 1e-9 and float(rx_m).is_integer() and mx(cx) == round(mx(cx)) \
                and my(cy) == round(my(cy)):
            continue                                  # already a circle
        # A side counts as touched only by the circle's own extreme on it,
        # never by chord endpoints that happen to sit on the edge.
        swept = [any(g.contains_angle(a) or g.contains_angle(a - 2 * math.pi) for _p, g in members)
                 for a in (math.pi, -math.pi / 2, 0.0, math.pi / 2)]
        touch = [swept[0] and abs(cx - r - L) < 1e-6, swept[1] and abs(cy - r - T) < 1e-6,
                 swept[2] and abs(cx + r - R) < 1e-6, swept[3] and abs(cy + r - B) < 1e-6]
        if radial:
            touch = [False] * 4
        if touch[0] and touch[2]:
            new_r = (envelope[2] - envelope[0]) / 2
        elif touch[1] and touch[3]:
            new_r = (envelope[3] - envelope[1]) / 2
        else:
            new_r = round((rx_m + ry_m) / 2)
        if (touch[0] and touch[2] and touch[1] and touch[3]
                and envelope[2] - envelope[0] != envelope[3] - envelope[1]):
            notes.append(f'circle r{r} at ({cx:g},{cy:g}): fills both axes of a non-square envelope; left as an ellipse')
            continue
        if not float(new_r).is_integer():
            continue
        fixed = any(touch)
        nodes = {q for p, _g in members for q in (p.start, p.end)}
        angles = {q: math.atan2(q.y - cy, q.x - cx) for q in nodes}
        best = None
        for k in ([0] if fixed and ((touch[0] and touch[2]) or (touch[1] and touch[3])) else range(-3, 4)):
            rr = int(new_r) + k
            if rr < 3:
                continue
            ring = _ring(rr)
            chosen, worst = {}, 0.0
            for q, a in angles.items():
                pt = min(ring, key=lambda v: _angle_gap(math.atan2(v[1], v[0]), a))
                worst = max(worst, _angle_gap(math.atan2(pt[1], pt[0]), a))
                chosen[q] = pt
            score = (worst > 0.13, abs(k) + 20 * worst)
            if best is None or score < best[0]:
                best = (score, rr, chosen)
        (_too_far, _cost), new_r, chosen = best
        if _too_far:
            notes.append(f'circle r{r} at ({cx:g},{cy:g}): no integer ring near r{new_r} fits its nodes')
        ncx = (32 if touch[0] and touch[2] else envelope[0] + new_r if touch[0]
               else envelope[2] - new_r if touch[2] else round(mx(cx)))
        ncy = (32 if touch[1] and touch[3] else envelope[1] + new_r if touch[1]
               else envelope[3] - new_r if touch[3] else round(my(cy)))
        ids = {p.element_id for p, _g in members}
        shared = {q for o in source if o.element_id not in ids for q in (o.start, o.end)} & set(chosen)
        drift = max((math.hypot(ncx + dx - mx(q.x), ncy + dy - my(q.y))
                     for q, (dx, dy) in chosen.items() if q in shared), default=0.0)
        if drift > 1.5:
            notes.append(f'circle r{r} at ({cx:g},{cy:g}): left to the lattice, keeping it round '
                         f'would move shared nodes by {drift:.1f}')
            continue
        for q, (dx, dy) in chosen.items():
            moved.setdefault(q, Point(ncx + dx, ncy + dy))
        for p, _g in members:
            radii[p.element_id] = new_r
        notes.append(f'circle r{r} at ({cx:g},{cy:g}) kept round: r{new_r} at ({ncx},{ncy})')
    return moved, radii


def fit_arc(p: Arc, start: Point, end: Point, mx: AxisMap, my: AxisMap, notes: list) -> Arc:
    from icon_set.validation.envelope import arc_geometry
    dx0, dy0 = abs(p.end.x - p.start.x), abs(p.end.y - p.start.y)
    dx, dy = abs(end.x - start.x), abs(end.y - start.y)
    if dx0 == p.radius_x and dy0 == p.radius_y:
        rx, ry = dx, dy
    elif dy0 == 0 and dx0 == 2 * p.radius_x:
        rx = dx / 2
        ry = _bulge(p, 1, p.start.y, my)
        if p.radius_x == p.radius_y and ry != rx:
            notes.append(f'{p.element_id}: half circle became a {rx:g}x{ry:g} half ellipse')
    elif dx0 == 0 and dy0 == 2 * p.radius_y:
        ry = dy / 2
        rx = _bulge(p, 0, p.start.x, mx)
        if p.radius_x == p.radius_y and ry != rx:
            notes.append(f'{p.element_id}: half circle became a {rx:g}x{ry:g} half ellipse')
    else:
        # Keep the arc's centre where the lattice puts it and fit the radius
        # to the snapped endpoints.
        g = arc_geometry(p)
        cx, cy = mx(g.center_x), my(g.center_y)
        if p.radius_x == p.radius_y:
            r = (math.hypot(start.x - cx, start.y - cy) + math.hypot(end.x - cx, end.y - cy)) / 2
            rx = ry = r
        else:
            rx = (mx(g.center_x + g.radius_x) - mx(g.center_x - g.radius_x)) / 2
            ry = (my(g.center_y + g.radius_y) - my(g.center_y - g.radius_y)) / 2
        rx, ry = search_radius(p, g, start, end, round(rx), round(ry), mx, my)
    if rx != int(rx) or ry != int(ry):
        notes.append(f'{p.element_id}: odd chord gives half-unit radius {rx}x{ry}')
        rx, ry = math.ceil(rx), math.ceil(ry)
    return Arc(p.element_id, start, end, max(1, int(rx)), max(1, int(ry)), p.large_arc, p.sweep)


def _extremes(g) -> list[tuple[int, float]]:
    """(axis, value) for each cardinal extreme the arc actually sweeps through."""
    out = []
    for k in range(4):
        angle = k * math.pi / 2
        if g.contains_angle(angle) or g.contains_angle(angle - 2 * math.pi):
            x, y = g.point(angle)
            out.append((0, x) if k % 2 == 0 else (1, y))
    return out


def _bulge(p: Arc, axis: int, chord_line: int, m) -> float:
    """Mapped distance from a half-arc's chord to its bulge on ``axis``."""
    from icon_set.validation.envelope import arc_geometry
    values = [v for a, v in _extremes(arc_geometry(p)) if a == axis]
    far = max(values, key=lambda v: abs(v - chord_line))
    return abs(m(round(far)) - m(chord_line))


def search_radius(p: Arc, g, start: Point, end: Point, rx0: int, ry0: int, mx, my) -> tuple[int, int]:
    """Integer radii whose bulge lands where the lattice put the source bulge."""
    from icon_set.validation.envelope import arc_geometry
    wanted = [(axis, (mx if axis == 0 else my)(round(v))) for axis, v in _extremes(g)]
    dx, dy = abs(end.x - start.x), abs(end.y - start.y)
    best = None
    for k in range(-8, 9):
        rx, ry = rx0 + k, ry0 + k
        if rx < 1 or ry < 1 or (dx / 2 / rx) ** 2 + (dy / 2 / ry) ** 2 > 1 + 1e-9:
            continue
        got = _extremes(arc_geometry(Arc(p.element_id, start, end, rx, ry, p.large_arc, p.sweep)))
        if len(got) != len(wanted):
            error = 99.0
        else:
            error = max((abs(a[1] - b[1]) for a, b in zip(sorted(got), sorted(wanted))), default=0.0)
        key = (round(error, 9), abs(k))
        if best is None or key < best[0]:
            best = (key, rx, ry)
    if best is None:
        rx, ry = max(rx0, 1), max(ry0, 1)
        while (dx / 2 / rx) ** 2 + (dy / 2 / ry) ** 2 > 1 + 1e-9:
            rx, ry = rx + 1, ry + 1
        return rx, ry
    return best[1], best[2]


# -- emit --------------------------------------------------------------------

def _pt(point: Point) -> str:
    return f'({point.x}, {point.y})'


def _num(value: float) -> str:
    return str(int(value)) if float(value).is_integer() else repr(round(float(value), 3))


def build_lines(candidate) -> list[str]:
    out = []
    for p in candidate.primitives:
        if isinstance(p, Line):
            if p.is_dot:
                out.append(f'self.add_dot({p.element_id!r}, {_pt(p.start)})')
            else:
                out.append(f'self.add_line({p.element_id!r}, {_pt(p.start)}, {_pt(p.end)})')
        elif isinstance(p, Arc):
            radius = f'radius_x={p.radius_x}' + (f', radius_y={p.radius_y}' if p.radius_y != p.radius_x else '')
            flags = (', large_arc=True' if p.large_arc else '') + ('' if p.sweep else ', sweep=False')
            out.append(f'self.add_arc({p.element_id!r}, {_pt(p.start)}, {_pt(p.end)}, {radius}{flags})')
        else:
            segs = ', '.join('((%s, %s), (%s, %s), (%s, %s))' % (
                _num(c1[0]), _num(c1[1]), _num(c2[0]), _num(c2[1]), _num(k[0]), _num(k[1]))
                for c1, c2, k in p.segments)
            out.append(f'self.add_bezier({p.element_id!r}, {_pt(p.start)}, {segs})')
    for c in candidate.contours:
        members = ', '.join(repr(m) for m in c.members)
        out.append(f'self.add_contour({c.contour_id!r}, {members}' + (', closed=True)' if c.closed else ')'))
    for r in candidate.relationships:
        out.append(f'self.relate({r.kind!r}, ' + ', '.join(repr(m) for m in r.members) + ')')
    for name, point in candidate.anchors.items():
        if name not in FAMILY_ANCHORS:
            out.append(f'self.add_anchor({name!r}, {_pt(point)})')
    for f in candidate.human_figures:
        out.append(f'self.mark_human_figure({f.figure_id!r}, head={f.head!r}, torso={f.torso!r}, '
                   f'torso_junction={f.torso_junction!r})')
    return out


CLASS_FIELDS = ('icon_id', 'semantic_role', 'semantic_kind', 'category', 'categories', 'aliases', 'keywords')
MODULE_FIELDS = ('SOURCE_ICON_ID', 'SOURCE_ICON_IDS', 'SOURCE_PATH', 'FEEDBACK_PATHS')


def module_source(module, entries: list[tuple[object, Keyshape, Keyshape]]) -> str:
    doc = (inspect.getdoc(module) or '').strip()
    moves = '; '.join(f'{c.icon_id} {old.name} -> {new.name}' for c, old, new in entries)
    doc += ('\n\n' if doc else '') + (
        f'v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by '
        f'container_v2_fit ({moves}). Lattice snap: shared columns and rows move '
        f'together, gaps of 8 or less keep their size, stroke stays 4.')
    lines = [f'"""{doc}\n"""', '', 'from icon_set.model.keyshapes import Keyshape',
             'from icon_set.model.icons.container._base import Container64', '']
    for name in MODULE_FIELDS:
        if hasattr(module, name):
            lines.append(f'{name} = {getattr(module, name)!r}')
    lines.append(f'AUTHOR = {AUTHOR!r}')
    for candidate, _old, new in entries:
        cls = type(candidate)
        lines += ['', '', f'class {cls.__name__}(Container64):']
        if cls.__doc__ and cls.__doc__ is not Container64_doc():
            lines.append(f'    """{inspect.cleandoc(cls.__doc__)}"""')
            lines.append('')
        lines.append(f'    icon_id = {cls.icon_id!r}')
        lines.append(f'    keyshape = Keyshape.{new.name}')
        for name in CLASS_FIELDS[1:]:
            if name in cls.__dict__:
                lines.append(f'    {name} = {cls.__dict__[name]!r}')
        lines += ['', '    def build(self) -> None:']
        lines += [f'        {line}' for line in build_lines(candidate)]
    return '\n'.join(lines) + '\n'


def Container64_doc():
    from icon_set.model.icons.container._base import Container64
    return Container64.__doc__


# -- gate --------------------------------------------------------------------

def load_classes(path: Path) -> list[type]:
    spec = importlib.util.spec_from_file_location(f'_v2_{path.stem}', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [v for v in vars(module).values()
            if isinstance(v, type) and v.__module__ == module.__name__ and getattr(v, 'icon_id', None)]


def gate_icon(icon) -> dict:
    from icon_set.validation.library_qa import inspect_icon
    qa = inspect_icon(icon)
    return {'status': qa['status'], 'errors': qa['errors'], 'warnings': qa['warnings']}


RANK = {'pass': 0, 'review': 1, 'fail': 2, 'crash': 3}


def choose(icon, target: Keyshape):
    """Fit with circles kept round; fall back to the plain lattice if that gates worse."""
    candidate, notes = fit(icon, target)
    if not any('kept round' in n for n in notes):
        return candidate, notes
    try:
        round_status = gate_icon(candidate)['status']
    except Exception:
        round_status = 'crash'
    if round_status == 'pass':
        return candidate, notes
    plain, plain_notes = fit(icon, target, keep_round=False)
    try:
        plain_status = gate_icon(plain)['status']
    except Exception:
        plain_status = 'crash'
    if RANK.get(plain_status, 3) < RANK.get(round_status, 3):
        return plain, plain_notes + ['circles left to the lattice: keeping them round gated worse']
    return candidate, notes


def main(argv=None) -> int:
    import os
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--icons', nargs='*')
    parser.add_argument('--no-gate', action='store_true')
    parser.add_argument('--force', action='store_true',
                        help='also refit modules that were hand-repaired (stage agent-redraw)')
    args = parser.parse_args(argv)
    if not os.environ.get('ICON_CONTRACT_OVERLAY'):
        raise SystemExit('set ICON_CONTRACT_OVERLAY to icon_set/work/container64-v2/overlay.json')
    from icon_set.model.icons.registry import icons_in

    targets = json.loads((WORK / 'targets.json').read_text())
    groups: dict[str, list] = defaultdict(list)
    modules = {}
    for icon in icons_in('container'):
        if args.icons and icon.icon_id not in args.icons:
            continue
        module = sys.modules[type(icon).__module__]
        modules[module.__name__] = module
        groups[module.__name__].append(icon)

    report_path = WORK / 'report.json'
    report = json.loads(report_path.read_text()) if report_path.exists() else {}
    if not args.force:
        for name in list(groups):
            if any(report.get(i.icon_id, {}).get('stage') == 'agent-redraw' for i in groups[name]):
                del groups[name]
    for name, icons in sorted(groups.items()):
        module = modules[name]
        entries, notes = [], {}
        for icon in icons:
            old = icon.keyshape
            new = Keyshape[targets[icon.icon_id]['to']]
            try:
                candidate, icon_notes = choose(icon, new)
            except Exception as error:  # reported, never hidden
                report[icon.icon_id] = {'status': 'fit-error', 'errors': [repr(error)],
                                        'from': old.name, 'to': new.name}
                print(f'FIT-ERROR {icon.icon_id}: {error!r}')
                continue
            entries.append((candidate, old, new))
            notes[icon.icon_id] = icon_notes
        if not entries:
            continue
        out = WORK / Path(module.__file__).name
        out.write_text(module_source(module, entries))
        if args.no_gate:
            continue
        for cls in load_classes(out):
            try:
                result = gate_icon(cls())
            except Exception as error:
                result = {'status': 'crash', 'errors': [repr(error)], 'warnings': []}
            old = next(o for c, o, _n in entries if c.icon_id == cls.icon_id)
            result.update({'from': old.name, 'to': cls.keyshape.name, 'module': out.name,
                           'notes': notes.get(cls.icon_id, []), 'stage': 'auto-fit'})
            report[cls.icon_id] = result
            first = result['errors'][0] if result['errors'] else ''
            print(f"{result['status'].upper():5} {cls.icon_id} {old.name}->{cls.keyshape.name} {str(first)[:110]}")
    report_path.write_text(json.dumps(report, indent=1, sort_keys=True, default=str))
    from collections import Counter
    print(Counter(v['status'] for v in report.values()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
