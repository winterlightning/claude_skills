from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6061b2ad-a34e-4da4-a716-1952152438f8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gym-logo/20260927T055730Z-thuan-mac-1/reference/gym logo_6061b2ad-a34e-4da4-a716-1952152438f8.svg'
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


class Drawing(Solo48):
    icon_id = 'gym-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('gym', 'circle', 'target', 'logo', 'brand', 'rings', 'reinforcement-learning')

    def build(self) -> None:
        # lifebuoy-style mark like the reference: two rings joined by four DIAGONAL spokes.
        # Each ring is eight 45-degree cubic segments with integer knots on the cardinal points (radius c)
        # and the diagonal points (offset d); controls are fractional (k = 0.2652 * radius).
        import math
        def ring(name, c, d):
            pts = [(24 + c, 24), (24 + d, 24 + d), (24, 24 + c), (24 - d, 24 + d),
                   (24 - c, 24), (24 - d, 24 - d), (24, 24 - c), (24 + d, 24 - d)]
            members = []
            for i in range(8):
                a, b = pts[i], pts[(i + 1) % 8]
                ra, rb = math.hypot(a[0] - 24, a[1] - 24), math.hypot(b[0] - 24, b[1] - 24)
                ta = ((a[1] - 24) / ra * -1, (a[0] - 24) / ra)      # clockwise tangent at a (screen coords)
                tb = ((b[1] - 24) / rb * -1, (b[0] - 24) / rb)
                k = 0.2652 * (ra + rb) / 2
                c1 = (a[0] + ta[0] * k, a[1] + ta[1] * k)
                c2 = (b[0] - tb[0] * k, b[1] - tb[1] * k)
                self.add_bezier(f"{name}-{i}", a, (c1, c2, b))
                members.append(f"{name}-{i}")
            self.add_contour(name, *members, closed=True)
        ring("outer", 20, 14)       # cardinal radius 20 (sets the CIRCLE fit), diagonal radius 19.8
        # inner ring: four 90-degree cubics through the diagonal knots only (all at radius 8*sqrt(2))
        knots = [(32, 32), (16, 32), (16, 16), (32, 16)]
        k = 0.5523
        members = []
        for i in range(4):
            a, b = knots[i], knots[(i + 1) % 4]
            ta = (-(a[1] - 24), a[0] - 24)          # clockwise tangent, length = radius
            tb = (-(b[1] - 24), b[0] - 24)
            c1 = (a[0] + ta[0] * k, a[1] + ta[1] * k)
            c2 = (b[0] - tb[0] * k, b[1] - tb[1] * k)
            self.add_bezier(f"inner-{i}", a, (c1, c2, b))
            members.append(f"inner-{i}")
        self.add_contour("inner", *members, closed=True)
        for i, (sx, sy) in enumerate(((1, 1), (-1, 1), (-1, -1), (1, -1))):
            self.add_line(f"spoke-{i}", (24 + 8 * sx, 24 + 8 * sy), (24 + 14 * sx, 24 + 14 * sy))
            self.relate("connect", "outer", f"spoke-{i}")
            self.relate("connect", "inner", f"spoke-{i}")
