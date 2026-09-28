from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f57926de-818d-4de1-800d-b8700615be01'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__and-gate-connected-to-triangular-buffer/20260927T150142Z-thuan-mac-1/reference/xor_f57926de-818d-4de1-800d-b8700615be01.svg'
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
    icon_id = 'and-gate-connected-to-triangular-buffer'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'diagrams'
    categories = ('diagrams', 'primitives')
    aliases = ()
    keywords = ('logic', 'and', 'gate', 'and', 'buffer')

    def build(self) -> None:
        # AND gate (flat back, r10 nose) wired to a triangular buffer; thin horizontal circuit fits CIRCLE
        self.add_line("in-a", (6, 18), (10, 18))
        self.add_line("in-b", (6, 30), (10, 30))
        _path(self, "gate", (10, 18), [(10, 14), (14, 14), ((24, 24), 10, 10, True), ((14, 34), 10, 10, True),
                                       (10, 34), (10, 30), (10, 18)], True)
        self.add_line("link", (24, 24), (32, 24))
        _path(self, "buffer", (32, 24), [(32, 17), (40, 24), (32, 31), (32, 24)], True)
        self.add_line("out", (40, 24), (44, 24))
        for a, b in (("in-a", "gate"), ("in-b", "gate"), ("link", "gate"), ("link", "buffer"), ("out", "buffer")):
            self.relate("connect", a, b)
