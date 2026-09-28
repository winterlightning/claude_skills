from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c8ed2a82-660e-4fb3-97c4-3f6f0a34445d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__furby-toy/20260927T104205Z-thuan-mac-1/reference/toys furby_c8ed2a82-660e-4fb3-97c4-3f6f0a34445d.svg'
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
    icon_id = 'furby-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'kids'
    categories = ('primitives', 'kids')
    aliases = ()
    keywords = ('furby', 'toy')

    def build(self) -> None:
        # Plan (reference): a Furby toy from the front, mirrored about x=24.
        # A big egg body filling the square (sides on x=6/42, flat bottom on
        # y=42, drawn as its own line so the beak gap certifies) with two big
        # ears flaring up and out from its shoulders to tips on y=6. Face: two
        # wide-set eye dots and the round open beak (r3 ring) centred below
        # them, as in the reference.
        _path(self, "body", (18, 42), [('c', (11, 42), (6, 36), (6, 28)),
                                       ('c', (6, 23), (7, 19), (10, 16)),
                                       (8, 6), (18, 12),
                                       ('c', (21, 11), (27, 11), (30, 12)),
                                       (40, 6), (38, 16),
                                       ('c', (41, 19), (42, 23), (42, 28)),
                                       ('c', (42, 36), (37, 42), (30, 42))])
        self.add_line("base", (18, 42), (30, 42))
        self.relate("connect", "base", "body")
        self.add_dot("eye-left", (16, 23))
        self.add_dot("eye-right", (32, 23))
        _circle(self, "beak", 24, 31, 3)
