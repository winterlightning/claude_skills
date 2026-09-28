from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '30fe08b3-f765-4860-bb20-5c7cdf3b8b52'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__adult-with-arm-around-child/20260927T141159Z-thuan-mac-1/reference/family child hold hand_30fe08b3-f765-4860-bb20-5c7cdf3b8b52.svg'
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
    icon_id = 'adult-with-arm-around-child'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('adult', 'with', 'arm', 'around', 'child')

    def build(self) -> None:
        # Adult with an arm around a child (reference: tall outlined adult on the left, shorter child
        # on the right, the adult's arm reaching across onto the child's shoulder). Human parameters
        # from human_ref/user.svg: ring heads with the body top 8 below the head outline, open-bottom
        # rounded bodies. Adult: head r4 about (14,10); body x6-22 from the shoulder line y22 down to
        # the feet at y42, r4 shoulders, a leg gap (14,32)-(14,42) between the legs. The straight
        # sides are standalone lines so the 8-unit leg gap certifies.
        # Child: head r4 about (36,20); body x30-42 from y32 down to y42.
        # Arm: from the adult's right side (22,28) down to the child's shoulder top (34,32).
        _circle(self, "adult-head", 14, 10, 4)
        _path(self, "adult-top", (6, 26), [((10, 22), 4, 4, True), (18, 22), ((22, 26), 4, 4, True)])
        self.add_line("adult-left", (6, 26), (6, 42))
        self.add_line("adult-right-up", (22, 26), (22, 28))
        self.add_line("adult-right", (22, 28), (22, 42))
        for a, b in (("adult-top", "adult-left"), ("adult-top", "adult-right-up"), ("adult-right-up", "adult-right")):
            self.relate("connect", a, b)
        self.add_line("adult-legs", (14, 42), (14, 32))
        _circle(self, "child-head", 36, 20, 4)
        _path(self, "child-body", (30, 42), [(30, 36), ((34, 32), 4, 4, True), (38, 32),
                                             ((42, 36), 4, 4, True), (42, 42)])
        self.add_line("arm", (22, 28), (34, 32))
        for a in ("adult-right-up", "adult-right", "child-body"):
            self.relate("connect", "arm", a)
