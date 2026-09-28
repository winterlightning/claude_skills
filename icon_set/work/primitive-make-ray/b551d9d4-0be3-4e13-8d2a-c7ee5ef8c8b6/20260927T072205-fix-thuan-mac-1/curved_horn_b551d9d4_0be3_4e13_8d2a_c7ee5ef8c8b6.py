from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b551d9d4-0be3-4e13-8d2a-c7ee5ef8c8b6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-horn/20260927T072058Z-thuan-mac-1/reference/trumpet_b551d9d4-0be3-4e13-8d2a-c7ee5ef8c8b6.svg'
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


def _smooth(knots, closed=False):
    """Catmull-Rom steps through integer knots (horizontal/vertical tangents stay exact)."""
    pts = list(knots)
    n = len(pts)
    steps = []
    for i in range(n - 1 if not closed else n):
        p0 = pts[i - 1] if (i > 0 or closed) else pts[i]
        p1, p2 = pts[i], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (i + 2 < n or closed) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        steps.append(('c', c1, c2, p2))
    return steps


class Drawing(Solo48):
    icon_id = 'curved-horn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'music'
    categories = ('primitives', 'music')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: horn seen from the side - the bell mouth opens upward at the
        # top left (a lens rim of two r10 arcs, (6,10)..(22,10)); the tube
        # hangs from its ends, sweeps down and curls up to the right,
        # tapering to a narrow cut end at the right.
        _path(self, 'mouth', (6, 10), [((22, 10), 10, 10, True), ((6, 10), 10, 10, True)], True)
        _path(self, 'outer', (6, 10), [('c', (6, 30), (14, 42), (24, 42)), ('c', (32, 42), (40, 34), (42, 26))])
        _path(self, 'inner', (22, 10), [('c', (22, 22), (23, 31), (28, 31)), ('c', (32, 31), (33, 24), (34, 18))])
        self.add_line('end', (34, 18), (42, 26))
        for a, b in [('mouth', 'inner'), ('mouth', 'outer'), ('inner', 'end'), ('outer', 'end')]:
            self.relate('connect', a, b)
