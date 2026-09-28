from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ab4d1610-e735-4977-967a-897386cdcc6d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-intersection-sensor-waves/20260927T144116Z-thuan-mac-1/reference/intersection assistant_ab4d1610-e735-4977-967a-897386cdcc6d.svg'
AUTHOR = "claude-opus-5-5"


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


def _smooth(icon, name, pts, closed=True):
    """Catmull-Rom through integer knots, as cubics (closed loop or open run)."""
    n = len(pts)
    members = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p1, p2 = pts[i], pts[(i + 1) % n]
        p0 = pts[i - 1] if (closed or i > 0) else p1
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        m = f"{name}-{i + 1}"
        icon.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
    icon.add_contour(name, *members, closed=closed)
    return members


class Drawing(Solo48):
    icon_id = 'car-intersection-sensor-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('car', 'intersection', 'sensor', 'waves')

    def build(self) -> None:
        # Intersection assistant: front view of a car between two converging
        # road edges, with two sensor waves fanning diagonally out from each
        # top corner of the windscreen (radii about 9 and 18 about the roof
        # corners). Mirrored about x=24.
        import math

        def wave(name, cx, cy, p, q):
            a0 = math.atan2(p[1] - cy, p[0] - cx)
            a1 = math.atan2(q[1] - cy, q[0] - cx)
            r0 = math.hypot(p[0] - cx, p[1] - cy)
            r1 = math.hypot(q[0] - cx, q[1] - cy)
            d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
            k = 4 / 3 * math.tan(d / 4)
            c1 = (p[0] - k * r0 * math.sin(a0), p[1] + k * r0 * math.cos(a0))
            c2 = (q[0] + k * r1 * math.sin(a1), q[1] - k * r1 * math.cos(a1))
            self.add_bezier(name, p, (c1, c2, q))

        for side, m in (('left', lambda x: x), ('right', lambda x: 48 - x)):
            wave(f'wave-inner-{side}', m(19), 24, (m(11), 20), (m(15), 16))
            wave(f'wave-outer-{side}', m(19), 24, (m(4), 14), (m(10), 8))
            self.add_line(f'road-{side}', (m(4), 40), (m(7), 28))
        _path(self, 'body', (15, 31), [
            (16, 31), (32, 31), (33, 31), (33, 36), ((30, 39), 3, 3, True), (18, 39),
            ((15, 36), 3, 3, True), (15, 31),
        ], closed=True)
        _path(self, 'cabin', (16, 31), [(19, 23), (29, 23), (32, 31)])
        self.add_line('tyre-left', (18, 39), (18, 40))
        self.add_line('tyre-right', (30, 39), (30, 40))
        for part in ('cabin', 'tyre-left', 'tyre-right'):
            self.relate('connect', 'body', part)
