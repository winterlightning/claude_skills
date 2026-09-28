from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a5f26275-d65e-486b-af08-f77f5cc364f2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bow-and-arrow-with-unresolved-adjacent-forms-batch-014-10/20260927T153247Z-thuan-mac-1/reference/vijayadashami_a5f26275-d65e-486b-af08-f77f5cc364f2.svg'
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
    icon_id = 'bow-and-arrow-with-unresolved-adjacent-forms-batch-014-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('bow', 'arrow', 'archery', 'festival', 'string', 'weapon')

    def build(self) -> None:
        # Bow and arrow (Vijayadashami), as in the reference: a tall bow whose limb arcs out to the
        # right between its tips, a straight bowstring between the tips, and an arrow crossing the
        # string and the limb on its way up to the right, ending in a V arrowhead. The upper limb
        # is a quarter circle r18 about (12,24) from the top tip to the crossing (30,24); the arrow
        # runs on a 4:3 slope through lattice points on the string (22,30) and the limb.
        _path(self, "limb", (12, 6), [((30, 24), 18, 18, True), ((27, 42), 10, 10, True)])
        _path(self, "string", (12, 6), [(22, 30), (27, 42)])
        _path(self, "arrow", (6, 42), [(22, 30), (30, 24), (42, 15)])
        self.add_line("head-a", (42, 15), (36, 14))
        self.add_line("head-b", (42, 15), (39, 21))
        for a, b in (("limb", "string"), ("arrow", "string"), ("arrow", "limb"), ("head-a", "arrow"), ("head-b", "arrow"),
                     ("head-a", "head-b")):
            self.relate("connect", a, b)
