from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a4fcb649-0d89-4829-aa18-5a06211d7de9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__banking-glider-with-air-trails/20260927T141159Z-thuan-mac-1/reference/gliding_a4fcb649-0d89-4829-aa18-5a06211d7de9.svg'
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
    icon_id = 'banking-glider-with-air-trails'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('banking', 'glider', 'with', 'air', 'trails')

    def build(self) -> None:
        # Glider with air trails (reference: a sailplane seen from above, flying up to the right, with
        # long thin straight wings crossing a slim fuselage, and curved air trails sweeping behind it
        # at the lower left). Fuselage on the 45-degree axis x+y=44: sides x+y=37/51, an r5 nose cap
        # about (33,11) (3-4-5 ends, touching the top edge) and an r5 tail cap about (18,26) whose
        # ends carry the tailplane. Wings on y=x-3 from the fuselage sides out to (9,6) and (42,39);
        # tailplane on y=x+9, 8.5 behind the wings. Air trail: a sweep round the lower left,
        # 13+ from the tail cap centre.
        _path(self, "fuselage", (30, 7), [((37, 14), 5, 5, True), (27, 24), (21, 30),
                                          ((14, 23), 5, 5, True), (20, 17), (30, 7)], closed=True)
        self.add_line("wing-left", (9, 6), (20, 17))
        self.add_line("wing-right", (27, 24), (42, 39))
        self.add_line("tailplane-left", (10, 19), (14, 23))
        self.add_line("tailplane-right", (21, 30), (25, 34))
        for a in ("wing-left", "wing-right", "tailplane-left", "tailplane-right"):
            self.relate("connect", a, "fuselage")
        self.add_bezier("trail-1", (6, 32), ((7, 37), (11, 41), (18, 42)))
