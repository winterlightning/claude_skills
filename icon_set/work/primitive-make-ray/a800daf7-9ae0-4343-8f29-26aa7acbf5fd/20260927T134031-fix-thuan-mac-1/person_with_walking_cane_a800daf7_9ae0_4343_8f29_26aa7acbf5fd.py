from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a800daf7-9ae0-4343-8f29-26aa7acbf5fd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-walking-cane/20260927T133650Z-thuan-mac-1/reference/disability cane_a800daf7-9ae0-4343-8f29-26aa7acbf5fd.svg'
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
    icon_id = 'person-with-walking-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'cane', 'walking', 'mobility', 'accessibility', 'support')

    def build(self) -> None:
        # Person walking with a cane, after the reference: a user-style figure (round head above a
        # tall round-shouldered body whose legs part at the bottom) with the near arm reaching down
        # to the crook of a long walking cane standing at the left.
        _circle(self, "head", 32, 9, 5)
        _path(self, "shoulders", (24, 28), [((30, 22), 6, 6, True), (34, 22), ((40, 28), 6, 6, True)])
        self.add_line("side-l", (24, 28), (24, 44))
        self.add_line("side-r", (40, 28), (40, 44))
        self.add_line("leg-gap", (32, 44), (32, 34))
        self.add_line("arm", (24, 28), (16, 32))
        _path(self, "cane", (16, 44), [(16, 32), ((8, 32), 4, 4, False)])
        for a, b in (("shoulders", "side-l"), ("shoulders", "side-r"), ("shoulders", "arm"), ("side-l", "arm"), ("cane", "arm")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="shoulders-2", torso_junction="end")
