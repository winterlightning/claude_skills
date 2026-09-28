from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6f237c30-c7db-4dfc-91c5-5d21fb166711'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__memory-module-with-notch/20260927T133651Z-thuan-mac-1/reference/computer ram_6f237c30-c7db-4dfc-91c5-5d21fb166711.svg'
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
    icon_id = 'memory-module-with-notch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('ram', 'memory', 'module', 'dimm', 'chip', 'hardware', 'computer', 'upgrade')

    def build(self) -> None:
        # RAM stick: long board with an off-centre key notch in the top edge, a row of three solid chip
        # packages, and a comb of contact pins hanging from the bottom edge. (Two hollow chips read as
        # eyes, so the chips are solid bars.) Board walls are standalone connected lines.
        pts = [(4, 8), (26, 8), (26, 12), (34, 12), (34, 8), (44, 8), (44, 32), (36, 32), (28, 32), (20, 32),
               (12, 32), (4, 32)]
        names = []
        for i, (a, b) in enumerate(zip(pts, pts[1:] + pts[:1])):
            names.append(f"board-{i + 1}")
            self.add_line(names[-1], a, b)
        for a, b in zip(names, names[1:] + names[:1]):
            self.relate("connect", a, b)
        for i, x in enumerate((36, 28, 20, 12)):
            self.add_line(f"pin-{i + 1}", (x, 32), (x, 40))
            self.relate("connect", names[7 + i], "pin-%d" % (i + 1))
        for i, x in enumerate((12, 22, 32)):
            self.add_line(f"chip-{i + 1}", (x, 20), (x + 2, 20))
