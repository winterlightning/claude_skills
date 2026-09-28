from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6cabf2c0-0e02-44c3-a22c-a4711d6599f3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mascara-wand-with-small-cap/20260927T133651Z-thuan-mac-1/reference/mascara small_6cabf2c0-0e02-44c3-a22c-a4711d6599f3.svg'
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
    icon_id = 'mascara-wand-with-small-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('mascara', 'wand', 'with', 'small', 'cap')

    def build(self) -> None:
        # Mascara: wand on the left (stem with three bristle bars at the top, a bare stem, rounded
        # handle cap below) and the small tube on the right (domed body with a band near its base).
        self.add_line("stem", (14, 4), (14, 30))
        for i, y in enumerate((4, 12, 20)):
            self.add_line(f"bristle-{i + 1}-l", (10, y), (14, y))
            self.add_line(f"bristle-{i + 1}-r", (14, y), (18, y))
            self.relate("connect", "stem", f"bristle-{i + 1}-l", f"bristle-{i + 1}-r")
        _path(self, "handle", (14, 30), [(16, 30), ((20, 34), 4, 4, True), (20, 40), ((16, 44), 4, 4, True), (12, 44),
                                         ((8, 40), 4, 4, True), (8, 34), ((12, 30), 4, 4, True), (14, 30)], True)
        self.relate("connect", "stem", "handle-1", "handle-9")
        _path(self, "tube", (30, 17), [((40, 17), 5, 5, True), (40, 28), (40, 32), ((36, 36), 4, 4, True), (34, 36),
                                       ((30, 32), 4, 4, True), (30, 28), (30, 17)], True)
        self.add_line("tube-band", (30, 28), (40, 28))
        self.relate("connect", "tube-band", "tube-2", "tube-3", "tube-6", "tube-7")
