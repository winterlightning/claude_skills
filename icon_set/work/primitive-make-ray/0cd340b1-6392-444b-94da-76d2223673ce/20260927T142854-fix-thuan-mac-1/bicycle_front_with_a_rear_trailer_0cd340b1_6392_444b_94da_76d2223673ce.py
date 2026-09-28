from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0cd340b1-6392-444b-94da-76d2223673ce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bicycle-front-with-a-rear-trailer/20260927T142727Z-thuan-mac-1/reference/bike stroller back_0cd340b1-6392-444b-94da-76d2223673ce.svg'
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
    icon_id = 'bicycle-front-with-a-rear-trailer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bicycle', 'trailer', 'cart', 'wheel', 'transport', 'frame', 'towing')

    def build(self) -> None:
        import math

        def wheel(name, cx, cy):
            """Near-circle r8 through 12 lattice knots (cardinals + (4,7)/(7,4) family)."""
            offs = [(0, -8), (4, -7), (7, -4), (8, 0), (7, 4), (4, 7), (0, 8), (-4, 7), (-7, 4), (-8, 0), (-7, -4), (-4, -7)]
            members = []
            for i, (a, b) in enumerate(offs):
                c, d = offs[(i + 1) % 12]
                t0, t1 = math.atan2(b, a), math.atan2(d, c)
                dt = (t1 - t0) % (2 * math.pi)
                r0, r1 = math.hypot(a, b), math.hypot(c, d)
                k0 = 4 / 3 * math.tan(dt / 4) * r0
                k1 = 4 / 3 * math.tan(dt / 4) * r1
                c1 = (cx + a - k0 * b / r0, cy + b + k0 * a / r0)
                c2 = (cx + c + k1 * d / r1, cy + d - k1 * c / r1)
                m = f"{name}-{i + 1}"
                self.add_bezier(m, (cx + a, cy + b), (c1, c2, (cx + c, cy + d)))
                members.append(m)
            self.add_contour(name, *members, closed=True)
            return members
        # Front half of a bicycle towing a child trailer, as in the reference: a box trailer with a
        # rounded front-top corner riding on one small wheel tucked under its floor, a hitch bar
        # running level then up to the bike's steering head, and the bike's large front wheel with
        # the fork running from the hub through the rim up to a short handlebar.
        wheel("front-wheel", 36, 32)
        _path(self, "fork", (35, 30), [(32, 25), (29, 12), (28, 8), (33, 8)])
        _path(self, "trailer", (11, 28), [(7, 28), ((4, 25), 3, 3, True), (4, 14), (12, 14), ((18, 20), 6, 6, True), (18, 22),
                                          (18, 25), ((15, 28), 3, 3, True), (11, 28)], True)
        _circle(self, "trailer-wheel", 11, 32, 4)
        _path(self, "hitch", (18, 22), [(23, 22), (29, 12)])
        for a, b in (("fork", "front-wheel"), ("trailer", "trailer-wheel"), ("hitch", "trailer"), ("hitch", "fork")):
            self.relate("connect", a, b)
