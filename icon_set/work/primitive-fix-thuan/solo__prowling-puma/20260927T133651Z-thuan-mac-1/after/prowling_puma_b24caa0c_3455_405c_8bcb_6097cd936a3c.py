from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b24caa0c-3455-405c-8bcb-6097cd936a3c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__prowling-puma/20260927T133651Z-thuan-mac-1/reference/puma_b24caa0c-3455-405c-8bcb-6097cd936a3c.svg'
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
    icon_id = 'prowling-puma'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('puma', 'cougar', 'mountain lion', 'prowl', 'big cat', 'feline', 'stalk', 'wildlife')

    def build(self) -> None:
        # Prowling puma facing left (reference): pointed snout and small ear, a long level back, the rump
        # dropping into the hind leg, a front leg reaching forward at 45 degrees (edges on x+y=38 / x+y=50,
        # 8.5 apart), and a long tail sweeping back from the rump.
        _path(self, "body", (4, 20), [('c', (5, 16), (6, 14), (8, 13)), (10, 10), (13, 14),
                                      ('c', (16, 15), (18, 16), (22, 16)), (28, 16), ('c', (31, 16), (33, 17), (34, 18)),
                                      ('c', (35, 20), (36, 23), (36, 26)), (36, 38), (27, 38), (27, 30), (20, 30),
                                      (12, 38), (4, 38), (4, 34), (12, 26), (4, 20)], True)
        self.add_bezier("tail", (34, 18), ((38, 15), (42, 17), (44, 22)))
        self.relate("connect", "tail", "body-6", "body-7")
