from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '22174314-84c2-4a0b-ab71-585364fe91f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__angel-and-kneeling-person/20260927T150142Z-thuan-mac-1/reference/feast of the annunciation_22174314-84c2-4a0b-ab71-585364fe91f9.svg'
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
    icon_id = 'angel-and-kneeling-person'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('angel', 'and', 'kneeling', 'person')

    def build(self) -> None:
        # annunciation: a standing angel (stick figure, r4 head 8 above a short neck, stepping toward the right)
        # with a large scalloped wing spread behind the shoulder and one arm reaching toward a person kneeling on
        # the right (r4 head resting on a rounded back, shared axis x=38, shins folded along the ground)
        _circle(self, "angel-head", 20, 12, 4)
        self.add_line("angel-torso", (20, 24), (20, 26))
        self.add_line("angel-torso-low", (20, 26), (16, 32))
        self.mark_human_figure("angel", head="angel-head", torso="angel-torso", torso_junction="start")
        self.add_line("angel-arm", (20, 26), (26, 24))
        self.add_line("angel-leg-l", (16, 32), (12, 40))
        self.add_line("angel-leg-r", (16, 32), (20, 40))
        _path(self, "wing", (20, 26), [(4, 17), ('c', (4, 20), (5, 24), (7, 24)), ('c', (6, 27), (7, 30), (10, 30)), (20, 26)], True)
        g = ("angel-torso", "angel-torso-low", "angel-arm", "wing")
        for i, a in enumerate(g):
            for b in g[i + 1:]:
                self.relate("connect", a, b)
        for leg in ("angel-leg-l", "angel-leg-r"):
            self.relate("connect", leg, "angel-torso-low")

        self.relate("connect", "angel-leg-l", "angel-leg-r")
        _circle(self, "kneeler-head", 38, 26, 4)
        _path(self, "kneeler-body", (28, 40), [(32, 40), ((38, 34), 6, 6, True), ((44, 40), 6, 6, True)])
        self.relate("connect", "kneeler-head", "kneeler-body")
