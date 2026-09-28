from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b629a3fa-3ca7-4b1e-97fa-bddfb9e31f58'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__neural-head-profile-with-branching-nodes/20260927T133656Z-thuan-mac-1/reference/head ai neurolink_b629a3fa-3ca7-4b1e-97fa-bddfb9e31f58.svg'
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
    icon_id = 'neural-head-profile-with-branching-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('neural', 'head', 'profile', 'with', 'branching', 'nodes')

    def build(self) -> None:
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
        # Left-facing head profile (reference): cranium dome open at the back, brow, nose, mouth step, chin, neck.
        face = chain("face", [
            K((23, 6), (-1, 0), 7),
            K((9, 18), (-0.3, 1), 4),
            K((6, 26), (-0.3, 1), 3, 0, (1, 0.2)),
            K((11, 28), (1, 0.2), 0, 3, (0, 1)),
            K((11, 34), (0, 1), 2),
            K((13, 37), (1, 0.3), 2),
            K((14, 42), (0, 1), 3),
        ])
        self.add_contour("face", *face)
        # Circuit under the dome: root node, three branches to staggered r3 rings (the middle one inside the head).
        R = (20, 26)
        top = chain("top", [K(R, (0, -1), 0), K((20, 20), (0, -1), 0, 4), K((36, 13), (1, 0), 7)])
        self.add_contour("top", *top)
        self.add_line("mid-1", R, (29, 26)); self.add_contour("mid", "mid-1")
        bot = chain("bot", [K(R, (0, 1), 8), K((36, 39), (1, 0), 8)])
        self.add_contour("bot", *bot)
        for n, cx, cy in (("node-top", 39, 13), ("node-mid", 32, 26), ("node-bot", 39, 39)):
            _circle(self, n, cx, cy, 3)
        self.relate("connect", "top", "mid"); self.relate("connect", "top", "bot"); self.relate("connect", "mid", "bot")
        self.relate("connect", "top", "node-top"); self.relate("connect", "mid", "node-mid"); self.relate("connect", "bot", "node-bot")
