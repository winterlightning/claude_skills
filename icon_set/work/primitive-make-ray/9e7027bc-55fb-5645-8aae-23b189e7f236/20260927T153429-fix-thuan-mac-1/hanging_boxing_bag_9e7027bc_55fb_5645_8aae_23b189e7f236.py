from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9e7027bc-55fb-5645-8aae-23b189e7f236'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hanging-boxing-bag/20260927T153247Z-thuan-mac-1/reference/boxing bag hanging_9e7027bc-55fb-5645-8aae-23b189e7f236.svg'
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
    icon_id = 'hanging-boxing-bag'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('hanging', 'boxing', 'bag')

    def build(self) -> None:
        # Hanging boxing bag, as in the reference: a tall capsule bag with a flat, softly rounded
        # top and a full round bottom, a band just below the top cap, and a triangular hanger
        # (two chain lines meeting at the hanging point) above it. CIRCLE fits the tall subject: the hanging point
        # and the bag bottom both sit exactly on r20.
        _path(self, "bag", (18, 14), [(30, 14), ((34, 18), 4, 4, True), (34, 22), (34, 34), ((14, 34), 10, 10, True),
                                      (14, 22), (14, 18), ((18, 14), 4, 4, True)], True)
        self.add_line("band", (14, 22), (34, 22))
        _path(self, "hanger", (18, 14), [(24, 4), (30, 14)])
        for a, b in (("bag", "band"), ("bag", "hanger")):
            self.relate("connect", a, b)
