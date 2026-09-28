from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '179dc2f8-89c2-456f-8ce6-03926fbb072a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__alert-message-45-solo/20260927T150142Z-thuan-mac-1/reference/speech bubble with exclamation mark_179dc2f8-89c2-456f-8ce6-03926fbb072a.svg'
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
    icon_id = 'alert-message-45-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('sub icon', 'alert speech bubble')

    def build(self) -> None:
        import math
        cx, cy, rx, ry = 24, 24, 20, 16

        def P(t):
            return (cx + rx * math.cos(t), cy + ry * math.sin(t))

        def D(t):
            return (-rx * math.sin(t), ry * math.cos(t))

        def seg(name, a, b, pa=None, pb=None):
            h = 4 / 3 * math.tan((b - a) / 4)
            p0 = pa or tuple(round(v) for v in P(a))
            p3 = pb or tuple(round(v) for v in P(b))
            d0, d1 = D(a), D(b)
            c1 = (p0[0] + h * d0[0], p0[1] + h * d0[1])
            c2 = (p3[0] - h * d1[0], p3[1] - h * d1[1])
            self.add_bezier(name, p0, (c1, c2, p3))
            return p3

        # oval speech bubble (rx20 ry16) with a pointed tail at the lower left, Lucide message-circle style
        tA = math.pi - math.acos(0.8)      # (8,34)
        tB = math.pi - math.acos(0.5)      # (14,38)
        seg("b1", math.pi, 1.5 * math.pi)
        seg("b2", 1.5 * math.pi, 2 * math.pi)
        seg("b3", 0, 0.5 * math.pi)
        seg("b4", 0.5 * math.pi, tB)
        tip = (4, 40)
        self.add_line("tail-1", (14, 38), tip)
        self.add_line("tail-2", tip, (8, 34))
        seg("b5", tA, math.pi)
        self.add_contour("bubble", "b1", "b2", "b3", "b4", "tail-1", "tail-2", "b5", closed=True)
        # exclamation mark
        self.add_line("bang", (24, 17), (24, 23))
        self.add_dot("bang-dot", (24, 31))
