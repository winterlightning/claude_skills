from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ff489ec3-8055-4cf9-be9d-85532a1e5a38'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bowling-pin-beside-ball/20260927T142727Z-thuan-mac-1/reference/bowling set_ff489ec3-8055-4cf9-be9d-85532a1e5a38.svg'
AUTHOR = 'claude-opus-5-5'


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
    icon_id = 'bowling-pin-beside-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bowling', 'pin', 'ball', 'sport', 'game', 'lanes', 'equipment')

    def build(self) -> None:
        import math

        def near_circle(cx, cy, base, start=None, end=None):
            """Cubic steps around a near-circle through integer knot offsets (mirrored to all octants),
            clockwise from knot `start` to knot `end` (full loop when both are None)."""
            pts = set()
            for a, b in base:
                for sa in (1, -1):
                    for sb in (1, -1):
                        pts.add((sa * a, sb * b)); pts.add((sa * b, sb * a))
            offs = sorted(pts, key=lambda p: math.atan2(p[1], p[0]) % (2 * math.pi))
            n = len(offs)
            i0 = offs.index((start[0] - cx, start[1] - cy)) if start else 0
            i1 = offs.index((end[0] - cx, end[1] - cy)) if end else i0
            steps, i = [], i0
            while True:
                j = (i + 1) % n
                (a, b), (c, d) = offs[i], offs[j]
                dt = (math.atan2(d, c) - math.atan2(b, a)) % (2 * math.pi)
                r0, r1 = math.hypot(a, b), math.hypot(c, d)
                k0, k1 = 4 / 3 * math.tan(dt / 4) * r0, 4 / 3 * math.tan(dt / 4) * r1
                steps.append(('c', (cx + a - k0 * b / r0, cy + b + k0 * a / r0),
                              (cx + c + k1 * d / r1, cy + d - k1 * c / r1), (cx + c, cy + d)))
                i = j
                if i == i1:
                    break
            return steps
        # Bowling pin beside a ball, as in the reference: a pin with a round head, a banded neck, a
        # bulging belly and a flat base, and a large bowling ball with three finger holes standing
        # in front of the pin's lower right. The ball is an r13 near-circle through lattice knots
        # (r13 and r13.04), so the holes keep a full 8 from its rim.
        ball = near_circle(29, 29, [(0, 13), (5, 12), (7, 11)], (18, 22), (18, 22))
        _path(self, "ball", (18, 22), ball, True)
        _path(self, "pin", (18, 36), [('c', (17.7, 38), (17.4, 40), (17, 42)), (9, 42),
                                      ('c', (7.5, 39), (6, 35), (6, 30)), ('c', (6, 25), (7.5, 21.5), (9, 19)), (9, 14),
                                      ((17, 14), 5, 5, True, True), (17, 19), ('c', (17.4, 20), (17.7, 21), (18, 22))])
        self.add_line("band", (9, 19), (17, 19))
        for i, p in enumerate(((25, 29), (32, 25), (32, 33))):
            self.add_dot(f"hole-{i + 1}", p)
        self.relate("connect", "pin", "band")
        self.relate("connect", "pin", "ball")
