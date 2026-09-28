from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a1ebcd1c-faf5-4d0c-93f2-8b0f08933387'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__isometric-cube-with-three-circular-nodes/20260927T133651Z-thuan-mac-1/reference/rotate 3d_a1ebcd1c-faf5-4d0c-93f2-8b0f08933387.svg'
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
    icon_id = 'isometric-cube-with-three-circular-nodes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('three', 'dimensional', 'cube', 'rotation', 'tool')

    def build(self) -> None:
        # Isometric cube (half-width 8, face rise 5, vertical edges 10) with three spokes to solid
        # node discs (r2 rings paint as filled 8-wide discs): top, bottom-left, bottom-right.
        T, UL, UR, C = (24, 18), (16, 23), (32, 23), (24, 28)
        LL, LR, B = (16, 33), (32, 33), (24, 38)
        edges = [("edge-tl", T, UL), ("edge-tr", T, UR), ("edge-lc", UL, C), ("edge-rc", UR, C),
                 ("edge-left", UL, LL), ("edge-right", UR, LR), ("edge-bl", LL, B), ("edge-br", LR, B),
                 ("edge-centre", C, B), ("spoke-top", T, (24, 8)), ("spoke-left", LL, (10, 40)),
                 ("spoke-right", LR, (38, 40))]
        for name, a, b in edges:
            self.add_line(name, a, b)
        for i, (n1, a1, b1) in enumerate(edges):
            for n2, a2, b2 in edges[i + 1:]:
                if {a1, b1} & {a2, b2}:
                    self.relate("connect", n1, n2)
        for name, (cx, cy), spoke in (("node-top", (24, 6), "spoke-top"), ("node-left", (10, 42), "spoke-left"),
                                      ("node-right", (38, 42), "spoke-right")):
            _circle(self, name, cx, cy, 2)
        self.relate("connect", "spoke-top", "node-top-2", "node-top-3")
        self.relate("connect", "spoke-left", "node-left-4", "node-left-1")
        self.relate("connect", "spoke-right", "node-right-4", "node-right-1")
