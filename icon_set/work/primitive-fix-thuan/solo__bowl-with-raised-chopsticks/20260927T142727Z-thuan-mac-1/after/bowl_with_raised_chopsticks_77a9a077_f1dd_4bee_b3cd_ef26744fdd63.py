from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '77a9a077-f1dd-4bee-b3cd-ef26744fdd63'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bowl-with-raised-chopsticks/20260927T142727Z-thuan-mac-1/reference/soup_77a9a077-f1dd-4bee-b3cd-ef26744fdd63.svg'
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
    icon_id = 'bowl-with-raised-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('bowl', 'chopsticks', 'dining', 'meal', 'utensil', 'food', 'kitchen')

    def build(self) -> None:
        # Soup bowl with raised chopsticks, as in the reference: a deep round bowl seen from slightly
        # above, its rim an open ellipse (back edge higher, front edge sagging), and a pair of
        # chopsticks dipping into the bowl behind the front rim and leaning up to the right,
        # slightly spread apart; the back rim breaks between the sticks, as in the reference.
        _path(self, "body", (6, 24), [((42, 24), 18, 18, False)])
        _path(self, "rim-back-left", (6, 24), [('c', (9, 22.7), (12.5, 22), (16, 22)), (19, 22)])
        _path(self, "rim-back-right", (32, 22), [('c', (36, 22), (39, 22.7), (42, 24))])
        _path(self, "rim-front", (6, 24), [('c', (8, 27), (10.5, 30), (14, 30)), (15, 30), (27, 30), (32, 30),
                                           ('c', (37, 30), (40, 27.5), (42, 24))])
        _path(self, "stick-a", (15, 30), [(19, 22), (27, 6)])
        _path(self, "stick-b", (27, 30), [(32, 22), (42, 6)])
        for a, b in (("body", "rim-back-left"), ("body", "rim-back-right"), ("body", "rim-front"),
                     ("rim-back-left", "rim-front"), ("rim-back-right", "rim-front"), ("stick-a", "rim-front"),
                     ("stick-a", "rim-back-left"), ("stick-b", "rim-front"), ("stick-b", "rim-back-right")):
            self.relate("connect", a, b)
