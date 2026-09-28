from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '42f8bd3b-a505-5e06-aa4e-65cccbc46650'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__swan-on-water/20260927T133656Z-thuan-mac-1/reference/swan water_42f8bd3b-a505-5e06-aa4e-65cccbc46650.svg'
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
    icon_id = 'swan-on-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('swan', 'water', 'float', 'pond', 'bird', 'waterfowl', 'waves', 'elegant')

    def build(self) -> None:
        # Swan facing right as in the reference: raised tail tip, back dipping into the neck notch, S-shaped
        # outlined neck (9 wide) into a head loop with a pointed beak; the body closes on three water scallops.
        import math
        def unit(v):
            n = math.hypot(*v); return (v[0] / n, v[1] / n)
        def chain(name, knots, closed=False):
            """knots: (point, tangent_in, tangent_out, k_in, k_out); consecutive knots joined by Hermite cubics."""
            members = []
            for i in range(len(knots) - 1):
                p0, _, t0, _, k0 = knots[i]
                p1, t1, _, k1, _ = knots[i + 1]
                t0, t1 = unit(t0), unit(t1)
                if k0 == 0 and k1 == 0:
                    m = f"{name}-{i + 1}"; self.add_line(m, p0, p1); members.append(m); continue
                c1 = (p0[0] + t0[0] * k0, p0[1] + t0[1] * k0)
                c2 = (p1[0] - t1[0] * k1, p1[1] - t1[1] * k1)
                m = f"{name}-{i + 1}"
                self.add_bezier(m, p0, (c1, c2, p1)); members.append(m)
            return members
        K = lambda p, t, k1, k2=None, t2=None: (p, t, t2 or t, k1, k1 if k2 is None else k2)
        body = chain("swan", [
            K((9, 38), (-0.5, -1), 4),
            K((6, 29), (0, -1), 4),
            K((8, 19), (0.2, -1), 4, 6, (1, -0.1)),
            K((18, 26), (1, 0.8), 5, 3),
            K((24, 29), (1, 0), 2),
            K((26, 24), (0, -1), 2),
            K((23, 15), (0, -1), 4),
            K((30, 6), (1, 0), 5),
            K((38, 12), (0, 1), 3),
            K((35, 17), (-1, 0.3), 2),
            K((33, 21), (0, 1), 2),
            K((40, 32), (0.35, 1), 7, 2),
            K((42, 38), (0, 1), 2, 0, (0, 1)),
        ])
        # water scallops from (42,38) back to (6,38), each sagging to y42
        pts = [(42, 38), (31, 38), (20, 38), (9, 38)]
        sag = 38 + 4 / 0.75
        for i in range(3):
            (x0, y0), (x1, y1) = pts[i], pts[i + 1]
            m = f"water-{i + 1}"
            self.add_bezier(m, (x0, y0), ((x0 - 3, sag), (x1 + 3, sag), (x1, y1))); body.append(m)
        self.add_contour("swan", *body, closed=True)
        self.add_line("beak", (38, 12), (42, 16))
        self.add_contour("bill", "beak")
        self.relate("connect", "swan", "bill")
