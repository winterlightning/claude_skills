from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f6e6d80b-db8f-4ede-9278-c10ce856fdd2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__finger-touch-gesture-batch-024-03/20260927T153247Z-thuan-mac-1/reference/finger touch_f6e6d80b-db8f-4ede-9278-c10ce856fdd2.svg'
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
    icon_id = 'finger-touch-gesture-batch-024-03'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('finger', 'touch', 'gesture')

    def build(self) -> None:
        # Finger touch gesture, as in the reference: a hand seen from the side with its index
        # finger pointing down and to the right onto a surface, the back of the hand arching over
        # the top, the other fingers curled as knuckle bumps under the hand, and two short touch
        # ticks radiating from the fingertip. The finger is a 1:2 tube ending in a rounded tip.
        _path(self, "hand", (19, 20), [(23, 28), ((31, 24), 5, 5, False), (24, 10),
                                       ('c', (21, 7), (18, 6), (14, 6)), ('c', (9, 6), (6, 9), (6, 14)), (6, 18),
                                       ((12, 19), 4, 4, False), ((19, 20), 4, 4, False)], True)
        self.add_line("tick-a", (40, 34), (42, 35))
        self.add_line("tick-b", (34, 40), (35, 42))
