from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5ab9f3b5-03e7-4655-9d6a-e84a5583b790'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__braided-yarn-skein/20260927T153247Z-thuan-mac-1/reference/yarn_5ab9f3b5-03e7-4655-9d6a-e84a5583b790.svg'
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
    icon_id = 'braided-yarn-skein'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('braided', 'yarn', 'skein')

    def build(self) -> None:
        # Braided yarn skein, as in the reference: three round loops of yarn overlapping along the
        # diagonal (the upper-right loop in front, each lower loop tucked behind the one above it),
        # the front and back loops crossed by an S-shaped strand (a third strand in the middle loop
        # would run parallel to its neighbours under 8 apart). r9 loops with centres 9 apart on both axes meet
        # exactly at their cardinal points.
        _circle(self, "loop-front", 33, 15, 9)
        _path(self, "loop-middle", (24, 15), [((15, 24), 9, 9, False), ((24, 33), 9, 9, False), ((33, 24), 9, 9, False)])
        _path(self, "loop-back", (15, 24), [((6, 33), 9, 9, False), ((15, 42), 9, 9, False), ((24, 33), 9, 9, False)])
        _path(self, "strand-front", (33, 24), [('c', (29, 19), (37, 11), (33, 6))])
        _path(self, "strand-back", (15, 42), [('c', (11, 37), (19, 29), (15, 24))])
        for a, b in (("loop-front", "loop-middle"), ("loop-middle", "loop-back"), ("strand-front", "loop-front"),
                     ("strand-front", "loop-middle"),
                     ("strand-back", "loop-back"), ("strand-back", "loop-middle")):
            self.relate("connect", a, b)
