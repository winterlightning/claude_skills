from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '459ca9bc-41c3-44a7-bd18-4322e40df660'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__briefcase-carrying-hailing-person/20260927T142727Z-thuan-mac-1/reference/taxi wave businessman_459ca9bc-41c3-44a7-bd18-4322e40df660.svg'
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
    icon_id = 'briefcase-carrying-hailing-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('briefcase', 'carrying', 'hailing', 'person')

    def build(self) -> None:
        # Person hailing a taxi while carrying a briefcase, drawn as an outline figure like the
        # reference (human ref: icon_set/references/human_ref/user.svg for the bust): a round head
        # held exactly 8 above a flat shoulder line with rounded shoulders, one arm raised high to
        # the upper left from the left shoulder, the torso's open sides dropping to the bottom, and
        # a wide briefcase held in front of the lower right side.
        _circle(self, "head", 24, 11, 5)
        self.add_line("shoulder", (18, 24), (30, 24))
        _path(self, "side-left", (18, 24), [((14, 28), 4, 4, False), (14, 42)])
        _path(self, "side-right", (30, 24), [((34, 28), 4, 4, True), (34, 32)])
        self.add_line("arm-up", (18, 24), (6, 11))
        _path(self, "briefcase", (34, 32), [(40, 32), ((42, 34), 2, 2, True), (42, 40), ((40, 42), 2, 2, True), (30, 42),
                                            ((28, 40), 2, 2, True), (28, 34), ((30, 32), 2, 2, True), (34, 32)], True)
        for a, b in (("shoulder", "side-left"), ("shoulder", "side-right"), ("shoulder", "arm-up"), ("side-left", "arm-up"),
                     ("side-right", "briefcase")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="shoulder", torso_junction="start")
