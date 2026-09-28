from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '076bc927-b602-45b8-bfda-183eca16fa3c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__angry-person-bust-batch-019-03/20260927T150142Z-thuan-mac-1/reference/angry person_076bc927-b602-45b8-bfda-183eca16fa3c.svg'
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
    icon_id = 'angry-person-bust-batch-019-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'angry', 'face', 'bust', 'emotion', 'frown', 'user', 'expression')

    def build(self) -> None:
        # angry bust: rounded-top head with a U jaw (r16) resting on a shallow shoulder arch (shared axis x=24,
        # jaw bottom 4 above the arch top), slanted brows and a straight-cornered frown.
        # Crown and sides are standalone lines so the brow clearances of exactly 8 certify.
        self.add_line("crown", (14, 4), (34, 4))
        self.add_arc("corner-r", (34, 4), (40, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_line("side-r", (40, 10), (40, 20))
        _path(self, "jaw", (40, 20), [((24, 36), 16, 16, True), ((8, 20), 16, 16, True)])
        self.add_line("side-l", (8, 20), (8, 10))
        self.add_arc("corner-l", (8, 10), (14, 4), radius_x=6, radius_y=6, sweep=True)
        ring = ["crown", "corner-r", "side-r", "jaw", "side-l", "corner-l"]
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate("connect", a, b)
        self.add_arc("shoulders", (8, 44), (40, 44), radius_x=34, radius_y=34, sweep=True)
        self.relate("connect", "jaw", "shoulders")
        self.add_line("brow-l", (16, 13), (20, 15))
        self.add_line("brow-r", (32, 13), (28, 15))
        self.add_polyline("mouth", (19, 26), (21, 23), (27, 23), (29, 26))
