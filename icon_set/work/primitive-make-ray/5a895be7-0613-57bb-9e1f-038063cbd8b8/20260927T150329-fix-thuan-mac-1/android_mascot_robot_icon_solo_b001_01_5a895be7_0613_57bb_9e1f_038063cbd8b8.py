from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5a895be7-0613-57bb-9e1f-038063cbd8b8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__android-mascot-robot-icon-solo-b001-01/20260927T150142Z-thuan-mac-1/reference/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
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
    icon_id = 'android-mascot-robot-icon-solo-b001-01'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('android', 'mascot', 'robot', 'icon')

    def build(self) -> None:
        import math
        cx, cy, r = 24, 20, 14

        def arc(name, p0, p3):
            a0 = math.atan2(p0[1] - cy, p0[0] - cx); a1 = math.atan2(p3[1] - cy, p3[0] - cx)
            if a1 < a0:
                a1 += 2 * math.pi
            h = 4 / 3 * math.tan((a1 - a0) / 4) * r
            t0 = (-math.sin(a0), math.cos(a0)); t1 = (-math.sin(a1), math.cos(a1))
            self.add_bezier(name, p0, ((p0[0] + h * t0[0], p0[1] + h * t0[1]), (p3[0] - h * t1[0], p3[1] - h * t1[1]), p3))

        # Android mascot: r14 dome head with two antennas, flat seam, rounded body, two stroke legs
        arc("dome-1", (10, 20), (14, 10))
        arc("dome-2", (14, 10), (24, 6))
        arc("dome-3", (24, 6), (34, 10))
        arc("dome-4", (34, 10), (38, 20))
        self.add_line("seam", (38, 20), (10, 20))
        self.add_contour("head", "dome-1", "dome-2", "dome-3", "dome-4", "seam", closed=True)
        self.add_line("antenna-l", (14, 10), (10, 4))
        self.add_line("antenna-r", (34, 10), (38, 4))
        _path(self, "body", (38, 20), [(38, 34), ((34, 38), 4, 4, True), (29, 38), (19, 38), (14, 38), ((10, 34), 4, 4, True), (10, 20)])
        self.add_line("leg-l", (19, 38), (19, 44))
        self.add_line("leg-r", (29, 38), (29, 44))
        for a, b in (("antenna-l", "head"), ("antenna-r", "head"), ("body", "head"), ("leg-l", "body"), ("leg-r", "body")):
            self.relate("connect", a, b)
