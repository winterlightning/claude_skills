from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0541fbf8-91e3-430d-b90b-d3ebc73efb34'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chisel-with-wood-shaving/20260927T153247Z-thuan-mac-1/reference/crafts carving_0541fbf8-91e3-430d-b90b-d3ebc73efb34.svg'
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
    icon_id = 'chisel-with-wood-shaving'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('chisel', 'with', 'wood', 'shaving')

    def build(self) -> None:
        # Wood chisel with a curled shaving, as in the reference: a long round-ended handle running
        # diagonally from the upper right down to a ferrule, then a flat steel blade flaring out to
        # a straight cutting edge at the lower left, and a curled wood shaving beside it. The
        # handle cap is r5 about (37,11) with 3-4-5 ends, giving sides x+y=41 and x+y=55.
        _path(self, "handle", (34, 7), [((41, 14), 5, 5, True), (30, 25), (23, 18), (34, 7)], True)
        _path(self, "blade", (23, 18), [(6, 33), (15, 42), (30, 25)])
        self.relate("connect", "handle", "blade")
        _path(self, "shaving", (11, 16), [((6, 11), 5, 5, True), ((11, 6), 5, 5, True), ((16, 11), 5, 5, True),
                                          ('c', (16, 13), (15, 14), (13, 14))])
