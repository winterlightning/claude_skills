from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fd01520f-b3df-486e-853b-7c06e4805eb9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__multi-chart-trading-monitor-solo-b002-09/20260927T133651Z-thuan-mac-1/reference/trading monitor_fd01520f-b3df-486e-853b-7c06e4805eb9.svg'
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
    icon_id = 'multi-chart-trading-monitor-solo-b002-09'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('multi', 'chart', 'trading', 'monitor')

    def build(self) -> None:
        # Trading monitor: rounded screen (standalone connected walls so exact-8 gaps certify),
        # neck + foot, and a zigzag price line across the screen like the reference's chart panels.
        parts = [
            ("wall-top", "line", (8, 8), (40, 8)), ("corner-tr", "arc", (40, 8), (44, 12)),
            ("wall-right", "line", (44, 12), (44, 26)), ("corner-br", "arc", (44, 26), (40, 30)),
            ("wall-bottom-r", "line", (40, 30), (24, 30)), ("wall-bottom-l", "line", (24, 30), (8, 30)),
            ("corner-bl", "arc", (8, 30), (4, 26)), ("wall-left", "line", (4, 26), (4, 12)),
            ("corner-tl", "arc", (4, 12), (8, 8)),
        ]
        for name, kind, a, b in parts:
            if kind == "line":
                self.add_line(name, a, b)
            else:
                self.add_arc(name, a, b, radius_x=4, radius_y=4, sweep=True)
        names = [p[0] for p in parts]
        for a, b in zip(names, names[1:] + names[:1]):
            self.relate("connect", a, b)
        self.add_line("neck", (24, 30), (24, 40))
        self.add_line("foot", (16, 40), (32, 40))
        self.relate("connect", "wall-bottom-r", "wall-bottom-l", "neck")
        self.relate("connect", "neck", "foot")
        self.add_polyline("price-line", (12, 22), (18, 18), (24, 21), (36, 16))
