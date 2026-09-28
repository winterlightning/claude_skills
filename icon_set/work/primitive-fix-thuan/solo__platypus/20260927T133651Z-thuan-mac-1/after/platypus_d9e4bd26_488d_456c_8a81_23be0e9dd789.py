from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd9e4bd26-488d-456c-8a81-23be0e9dd789'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__platypus/20260927T133651Z-thuan-mac-1/reference/duck bill platypus_d9e4bd26-488d-456c-8a81-23be0e9dd789.svg'
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
    icon_id = 'platypus'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('platypus', 'duckbill', 'australia', 'mammal', 'monotreme', 'animal', 'wildlife', 'aquatic')

    def build(self) -> None:
        # Platypus in profile: a flat duck bill with a rounded tip at the front (left), a low body whose
        # back rises into the flat paddle tail held up at the back (the reference's tail flick), two short
        # legs and an eye behind the bill. The reference's top-down view reads as a beetle or gourd at
        # 48 px, so the same parts are shown from the side.
        _path(self, "body", (8, 22), [(14, 22), ('c', (16, 17), (18, 14), (22, 14)), ('c', (28, 14), (31, 10), (34, 10)),
                                      (40, 10), ((40, 18), 4, 4, True), (38, 18), ('c', (36, 26), (36, 32), (30, 32)),
                                      (28, 32), (20, 32), (18, 32), ('c', (16, 32), (15, 30), (14, 30)), (8, 30),
                                      ((8, 22), 4, 4, True)], True)
        self.add_line("leg-front", (20, 32), (18, 38))
        self.add_line("leg-hind", (28, 32), (30, 38))
        self.relate("connect", "leg-front", "body-9", "body-10")
        self.relate("connect", "leg-hind", "body-8", "body-9")
        self.add_dot("eye", (23, 23))
