from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__interlocking-chain-links/20260927T104205Z-thuan-mac-1/reference/chain_7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885.svg'
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
    icon_id = 'interlocking-chain-links'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('interlocking', 'chain', 'links')

    def build(self) -> None:
        # Plan: two closed chain links (45-degree pills, r5 caps with 3-4-5 side
        # points, sides x+y=c+-7) on the rising diagonal, point-symmetric about
        # (24,24). Outer caps about (37,11)/(11,37) hit the SQUARE corners. A short
        # connecting bar joins the two inner caps across the gap, as in the
        # reference where the bar bridges the two links.
        def link(name, ci, co, s):
            p = lambda c, a, b: (c[0] + s * a, c[1] + s * b)
            _path(self, name, p(ci, 3, 4), [p(co, 3, 4),
                                             (p(co, -4, -3), 5, 5, False, True),
                                             p(ci, -4, -3),
                                             (p(ci, -3, 4), 5, 5, False),
                                             (p(ci, 3, 4), 5, 5, False)], True)
        link("link-top", (31, 17), (37, 11), 1)
        link("link-bottom", (17, 31), (11, 37), -1)
        self.add_line("bar", (28, 21), (20, 27))
        self.relate("connect", "bar", "link-top")
        self.relate("connect", "bar", "link-bottom")
