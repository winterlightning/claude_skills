from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e918e425-b0c9-444c-bdb5-9884044e4703'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bicycle-reference-165-solo/20260927T142727Z-thuan-mac-1/reference/bike_e918e425-b0c9-444c-bdb5-9884044e4703.svg'
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
    icon_id = 'bicycle-reference-165-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('sub icon', 'simple bicycle icon')

    def build(self) -> None:
        import math

        def wheel(name, cx, cy):
            """Near-circle r8 through 12 lattice knots (cardinals + (4,7)/(7,4) family)."""
            offs = [(0, -8), (4, -7), (7, -4), (8, 0), (7, 4), (4, 7), (0, 8), (-4, 7), (-7, 4), (-8, 0), (-7, -4), (-4, -7)]
            members = []
            for i, (a, b) in enumerate(offs):
                c, d = offs[(i + 1) % 12]
                t0, t1 = math.atan2(b, a), math.atan2(d, c)
                dt = (t1 - t0) % (2 * math.pi)
                r0, r1 = math.hypot(a, b), math.hypot(c, d)
                k0 = 4 / 3 * math.tan(dt / 4) * r0
                k1 = 4 / 3 * math.tan(dt / 4) * r1
                c1 = (cx + a - k0 * b / r0, cy + b + k0 * a / r0)
                c2 = (cx + c + k1 * d / r1, cy + d - k1 * c / r1)
                m = f"{name}-{i + 1}"
                self.add_bezier(m, (cx + a, cy + b), (c1, c2, (cx + c, cy + d)))
                members.append(m)
            self.add_contour(name, *members, closed=True)
            return members
        # Bicycle side view traced from the reference: two large wheels, a seat post leaning back
        # from the rear wheel's upper rim to a flat saddle, one top tube from that junction to the
        # front fork, and a fork rising from the front wheel into a kinked handlebar.
        wheel("rear-wheel", 12, 32)
        wheel("front-wheel", 36, 32)
        _path(self, "seat-post", (16, 25), [(13, 16), (11, 10)])
        self.add_line("saddle", (7, 10), (15, 10))
        self.add_line("top-tube", (16, 25), (34, 14))
        _path(self, "fork", (36, 24), [(34, 14), (33, 9), (38, 8)])
        for a, b in (("seat-post", "rear-wheel"), ("top-tube", "rear-wheel"), ("seat-post", "saddle"),
                     ("seat-post", "top-tube"), ("top-tube", "fork"), ("fork", "front-wheel")):
            self.relate("connect", a, b)
