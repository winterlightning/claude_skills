from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0f17f506-249c-43ae-928f-f9f965a37095'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__banknote-catching-fire/20260927T141159Z-thuan-mac-1/reference/business burn money_0f17f506-249c-43ae-928f-f9f965a37095.svg'
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
    icon_id = 'banknote-catching-fire'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('banknote', 'catching', 'fire')

    def build(self) -> None:
        # Banknote catching fire (reference: a banknote tilted 45 degrees whose lower-left end
        # disappears into a big upright flame). Axis frame ab(a,b) = (24+a+b, 24-a+b).
        # Note: sides b=-6 (x+y=36) and b=+6 (x+y=60) from its far end ab(12,+-6) = (30,6)/(42,18),
        # touching the top and right edges, down to where they enter the flame at (18,18)/(30,30).
        # Flame in front of the note's near end: round base on the bottom (16,42) and left (6,32)
        # edges, a tall tip at (10,10), and a second tongue licking up the note to (26,20).
        _path(self, "note", (18, 18), [(30, 6), (42, 18), (30, 30)])
        _path(self, "flame", (16, 42), [('c', (10, 42), (6, 38), (6, 32)), ('c', (6, 24), (12, 18), (10, 10)),
                                        ('c', (15, 13), (17, 16), (18, 18)), ('c', (21, 20), (24, 21), (26, 20)),
                                        ('c', (28, 24), (30, 27), (30, 30)), ('c', (30, 36), (24, 42), (16, 42))],
              closed=True)
        self.relate("connect", "note", "flame")
