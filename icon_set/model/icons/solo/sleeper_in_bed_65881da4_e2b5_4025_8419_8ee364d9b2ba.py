from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65881da4-e2b5-4025-8419-8ee364d9b2ba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-sleeping-in-bed/20260927T133650Z-thuan-mac-1/reference/hotel bed_65881da4-e2b5-4025-8419-8ee364d9b2ba.svg'
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
    icon_id = 'sleeper-in-bed'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('person', 'sleeping', 'in', 'bed')

    def build(self) -> None:
        # Side view of a person asleep in bed, as in the reference: a tall headboard at the left, a
        # mattress band on legs, the sleeper's round head resting on the mattress by the headboard
        # and a rounded blanket hump covering the body towards the foot end.
        self.add_line("headboard", (4, 8), (4, 40))
        self.add_line("mat-1", (4, 28), (17, 28))
        self.add_line("mat-2", (17, 28), (30, 28))
        self.add_line("mat-3", (30, 28), (44, 28))
        self.add_line("base", (4, 36), (44, 36))
        self.add_line("foot", (44, 28), (44, 40))
        _circle(self, "head", 17, 23, 5)
        _path(self, "blanket", (30, 28), [(30, 20), ((36, 14), 6, 6, True), (38, 14), ((44, 20), 6, 6, True), (44, 28)])
        for a, b in (("headboard", "mat-1"), ("mat-1", "mat-2"), ("mat-2", "mat-3"), ("mat-3", "foot"),
                     ("headboard", "base"), ("base", "foot"), ("head", "mat-1"), ("head", "mat-2"),
                     ("blanket", "mat-2"), ("blanket", "mat-3"), ("blanket", "foot")):
            self.relate("connect", a, b)
