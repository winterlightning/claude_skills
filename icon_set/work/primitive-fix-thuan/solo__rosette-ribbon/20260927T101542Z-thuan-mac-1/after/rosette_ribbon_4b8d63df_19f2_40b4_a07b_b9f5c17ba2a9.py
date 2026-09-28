from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rosette-ribbon/20260927T101542Z-thuan-mac-1/reference/ribbon_4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9.svg'
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


class Drawing(Solo48):
    icon_id = 'rosette-ribbon'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('rosette', 'ribbon', 'award', 'badge', 'prize', 'medal', 'winner', 'achievement')

    def build(self) -> None:
        import math
        cx, cy = 24, 18
        # Eight shallow lobes: valleys (+-11,+-5)/(+-5,+-11) (r12.1), cardinal peaks r14, diagonal peaks (10,10).
        base = [(14, 0), (11, 5), (10, 10), (5, 11), (0, 14), (-5, 11), (-10, 10), (-11, 5),
                (-14, 0), (-11, -5), (-10, -10), (-5, -11), (0, -14), (5, -11), (10, -10), (11, -5)]
        pts = base[1:] + base[:1]   # start on a valley
        members = []

        def unit(v):
            n = math.hypot(*v); return (v[0] / n, v[1] / n)

        for i in range(16):
            a, b = pts[i], pts[(i + 1) % 16]
            valley_first = i % 2 == 0
            V, Pk = (a, b) if valley_first else (b, a)
            w = (Pk[0] - V[0], Pk[1] - V[1]); L = math.hypot(*w)
            ur, uw = unit(V), unit(w)
            d = unit((0.3 * ur[0] + uw[0], 0.3 * ur[1] + uw[1]))
            cv = (V[0] + 0.45 * L * d[0], V[1] + 0.45 * L * d[1])
            t = (-Pk[1], Pk[0])
            if t[0] * w[0] + t[1] * w[1] > 0:
                t = (-t[0], -t[1])
            t = unit(t)
            cp = (Pk[0] + 0.45 * L * t[0], Pk[1] + 0.45 * L * t[1])
            c1, c2 = (cv, cp) if valley_first else (cp, cv)
            m = f"head-{i + 1}"
            self.add_bezier(m, (cx + a[0], cy + a[1]), ((cx + c1[0], cy + c1[1]), (cx + c2[0], cy + c2[1]), (cx + b[0], cy + b[1])))
            members.append(m)
        self.add_contour("head", *members, closed=True)
        _circle(self, "centre", cx, cy, 4)
        # Ribbon band behind the head, leaving the lower diagonal peaks, swallowtail notch 9 below the head.
        _path(self, "ribbon", (14, 28), [(14, 44), (24, 41), (34, 44), (34, 28)])
        self.relate("connect", "head", "ribbon")
