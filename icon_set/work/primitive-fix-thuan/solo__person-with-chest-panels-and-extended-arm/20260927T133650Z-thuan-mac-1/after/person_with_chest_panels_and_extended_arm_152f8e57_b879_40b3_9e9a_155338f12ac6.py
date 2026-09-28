from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '152f8e57-b879-40b3-9e9a-155338f12ac6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-chest-panels-and-extended-arm/20260927T133650Z-thuan-mac-1/reference/suicide bombing_152f8e57-b879-40b3-9e9a-155338f12ac6.svg'
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
    icon_id = 'person-with-chest-panels-and-extended-arm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('person', 'with', 'chest', 'panels', 'and', 'extended', 'arm')

    def build(self) -> None:
        # Person with chest panels and an extended arm, as in the reference: a round head above a
        # figure whose shoulder line runs straight out into an arm held level to the right and bent
        # down at the hand, a row of panels strapped across the chest, and a lower body tapering to
        # the ground.
        _circle(self, "head", 15, 11, 5)
        _path(self, "figure", (24, 32), [(34, 32), (34, 38), ((42, 38), 4, 4, False), (42, 28), ((38, 24), 4, 4, False),
                                         (10, 24), ((6, 28), 4, 4, False), (6, 32)])
        self.add_line("vest-hem", (6, 32), (24, 32))
        self.add_line("panel-1", (14, 24), (14, 32))
        self.add_line("hip-l", (6, 32), (9, 42))
        self.add_line("hip-r", (24, 32), (21, 42))
        self.add_line("feet", (9, 42), (21, 42))
        for a, b in (("figure", "vest-hem"), ("figure", "panel-1"), ("vest-hem", "panel-1"), ("figure", "hip-l"),
                     ("figure", "hip-r"), ("vest-hem", "hip-l"), ("vest-hem", "hip-r"), ("hip-l", "feet"), ("hip-r", "feet")):
            self.relate("connect", a, b)
