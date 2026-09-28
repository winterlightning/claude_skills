from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9dd77b0b-b0e7-4f89-85b4-16b5bb714516'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-crane-pose-with-bird/20260927T153339Z-thuan-mac-1/reference/takengei person_9dd77b0b-b0e7-4f89-85b4-16b5bb714516.svg'
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
    icon_id = 'person-crane-pose-with-bird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('balance', 'pose', 'person', 'martial-arts', 'crane', 'beach', 'bird', 'exercise', 'outdoors-batch-03')

    def build(self) -> None:
        # Person in a crane pose with a bird, as in the reference (human ref:
        # icon_set/references/human_ref/full_body_ref.png): a figure balancing on one straight leg
        # with both arms spread wide, the other leg lifted forward with the knee bent and the shin
        # hanging, standing on a ground line broken under the lifted foot, and a small gull-winged
        # bird flying at the upper left.
        _circle(self, "head", 30, 10, 4)
        self.add_line("torso", (30, 22), (30, 24))
        self.add_line("torso-low", (30, 24), (30, 32))
        self.add_line("arm-left", (30, 24), (10, 20))
        self.add_line("arm-right", (30, 24), (42, 21))
        self.add_line("leg-standing", (30, 32), (30, 42))
        _path(self, "leg-lifted", (30, 32), [(22, 32), (22, 38)])
        self.add_line("ground-left", (6, 42), (14, 42))
        self.add_line("ground-right", (30, 42), (40, 42))
        _path(self, "bird", (7, 11), [('c', (8, 8.5), (9.5, 7), (12, 10)), ('c', (14.5, 7), (16, 8.5), (17, 11))])
        for a, b in (("torso", "torso-low"), ("torso", "arm-left"), ("torso", "arm-right"), ("torso-low", "arm-left"),
                     ("torso-low", "arm-right"), ("arm-left", "arm-right"), ("torso-low", "leg-standing"),
                     ("torso-low", "leg-lifted"), ("leg-standing", "leg-lifted"), ("leg-standing", "ground-right")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
