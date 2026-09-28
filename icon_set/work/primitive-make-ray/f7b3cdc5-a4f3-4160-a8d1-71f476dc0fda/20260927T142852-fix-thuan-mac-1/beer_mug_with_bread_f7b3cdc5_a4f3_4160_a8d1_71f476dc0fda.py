from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__beer-mug-with-bread/20260927T142727Z-thuan-mac-1/reference/tarvern shop restuarant_f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda.svg'
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
    icon_id = 'beer-mug-with-bread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('beer', 'mug', 'with', 'bread')

    def build(self) -> None:
        # Beer mug with a bread loaf, as in the reference: a mug with a cloud of foam spilling over
        # its rim, a D handle on the right, and an oblong loaf with two vertical score marks standing
        # in front of the mug's lower left, hiding the lower part of its left wall.
        _path(self, "foam", (12, 20), [((16, 12), 5, 5, True), ((28, 12), 6, 6, True),
                                       ((34, 20), 5, 5, True), (12, 20)], True)
        _path(self, "mug-right", (34, 20), [(34, 29), (34, 37), ((29, 42), 5, 5, True), (26, 42)])
        _path(self, "handle", (34, 29), [((34, 37), 5, 5, True, True)])
        _path(self, "loaf", (6, 42), [('c', (6, 35.4), (8.2, 30), (11, 30)), (19, 30),
                                      ('c', (22.8, 30), (26, 35.4), (26, 42)), (6, 42)], True)
        self.add_line("score-left", (11, 30), (11, 35))
        self.add_line("score-right", (19, 30), (19, 35))
        for a, b in (("foam", "mug-right"), ("loaf", "mug-right"),
                     ("handle", "mug-right"), ("score-left", "loaf"), ("score-right", "loaf")):
            self.relate("connect", a, b)
