from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5d2f4a16-ffda-4c09-85d2-18b66770025f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bee-with-drooping-wings/20260927T141159Z-thuan-mac-1/reference/honeybee_5d2f4a16-ffda-4c09-85d2-18b66770025f.svg'
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
    icon_id = 'bee-with-drooping-wings'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bee', 'insect', 'wings', 'antennae', 'striped', 'pollinator')

    def build(self) -> None:
        # Honeybee with drooping wings (reference: a bee seen from the front/above, round head with
        # antennae, big wings hanging down and out from the shoulders, striped body with a pointed
        # tail). Head: r4 ring about (24,8) with antennae up to (16,4)/(32,4). Body: a slim r6 dome
        # about (24,26) (crown y20, 8 below the head), sides x18/x30 to y34, pointed tail to (24,44),
        # stripes at y26 and y34. Wings: long drooping leaves from the stripe ends (18,26)/(30,26),
        # their outer edges bulging out to x8/x40 and hanging down to tips at (8,40)/(40,40), their
        # inner edges running straight back up to the shoulders.
        _circle(self, "head", 24, 8, 4)
        self.add_line("antenna-left", (20, 8), (16, 4))
        self.add_line("antenna-right", (28, 8), (32, 4))
        self.relate("connect", "antenna-left", "head"); self.relate("connect", "antenna-right", "head")
        _path(self, "body", (18, 26), [((30, 26), 6, 6, True), (30, 34), (24, 44), (18, 34), (18, 26)], closed=True)
        self.add_line("stripe-1", (18, 26), (30, 26))
        self.add_line("stripe-2", (18, 34), (30, 34))
        self.relate("connect", "stripe-1", "body"); self.relate("connect", "stripe-2", "body")
        _path(self, "wing-left", (18, 26), [('c', (14, 23), (8, 24), (8, 30)), ('c', (8, 34), (8, 37), (8, 40)),
                                            (18, 26)], closed=True)
        _path(self, "wing-right", (30, 26), [('c', (34, 23), (40, 24), (40, 30)), ('c', (40, 34), (40, 37), (40, 40)),
                                             (30, 26)], closed=True)
        for w in ("wing-left", "wing-right"):
            self.relate("connect", w, "body"); self.relate("connect", w, "stripe-1")
