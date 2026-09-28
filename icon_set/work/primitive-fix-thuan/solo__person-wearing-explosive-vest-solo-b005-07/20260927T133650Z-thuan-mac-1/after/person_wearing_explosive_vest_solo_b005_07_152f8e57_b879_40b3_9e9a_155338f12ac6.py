from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '152f8e57-b879-40b3-9e9a-155338f12ac6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-wearing-explosive-vest-solo-b005-07/20260927T133650Z-thuan-mac-1/reference/suicide bombing_152f8e57-b879-40b3-9e9a-155338f12ac6.svg'
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
    icon_id = 'person-wearing-explosive-vest-solo-b005-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('person', 'wearing', 'explosive', 'vest')

    def build(self) -> None:
        # Person wearing an explosive vest, after the reference: a round head exactly 8 above a
        # user-style shoulder dome, with the vest's three charge panels strapped across the chest
        # (strap line, hem and two dividers).
        _circle(self, "head", 24, 11, 5)
        _path(self, "shoulders", (6, 32), [((14, 24), 8, 8, True), (34, 24), ((42, 32), 8, 8, True)])
        self.add_line("side-l", (6, 32), (6, 42))
        self.add_line("side-r", (42, 32), (42, 42))
        self.add_line("strap-1", (6, 32), (18, 32))
        self.add_line("strap-2", (18, 32), (30, 32))
        self.add_line("strap-3", (30, 32), (42, 32))
        self.add_line("hem-1", (6, 42), (18, 42))
        self.add_line("hem-2", (18, 42), (30, 42))
        self.add_line("hem-3", (30, 42), (42, 42))
        self.add_line("div-1", (18, 32), (18, 42))
        self.add_line("div-2", (30, 32), (30, 42))
        pairs = [("shoulders", "side-l"), ("shoulders", "side-r"), ("shoulders", "strap-1"), ("shoulders", "strap-3"),
                 ("side-l", "strap-1"), ("side-r", "strap-3"), ("strap-1", "strap-2"), ("strap-2", "strap-3"),
                 ("side-l", "hem-1"), ("side-r", "hem-3"), ("hem-1", "hem-2"), ("hem-2", "hem-3"),
                 ("strap-1", "div-1"), ("strap-2", "div-1"), ("strap-2", "div-2"), ("strap-3", "div-2"),
                 ("hem-1", "div-1"), ("hem-2", "div-1"), ("hem-2", "div-2"), ("hem-3", "div-2")]
        for a, b in pairs:
            self.relate("connect", a, b)
