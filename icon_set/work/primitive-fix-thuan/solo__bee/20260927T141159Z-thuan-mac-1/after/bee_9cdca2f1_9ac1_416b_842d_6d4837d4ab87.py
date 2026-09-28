from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9cdca2f1-9ac1-416b-842d-6d4837d4ab87'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bee/20260927T141159Z-thuan-mac-1/reference/sting_9cdca2f1-9ac1-416b-842d-6d4837d4ab87.svg'
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
    icon_id = 'bee'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bee', 'insect', 'wings', 'antennae', 'striped', 'abdomen', 'honey', 'pollinator')

    def build(self) -> None:
        # Bee (reference "sting": a bee seen from above: round head with two antennae, a striped
        # body ending in a pointed stinger, two wings spread out to the sides).
        # Head: r4 ring about (24,8) with antennae from its side points up to (16,4)/(32,4).
        # Body: an r8 dome about (24,28) (crown y20, 8 below the head), straight sides x16/x32 down
        # to y36, a pointed stinger to (24,44); stripes across at y28 and y36.
        # Wings: teardrop loops from the stripe ends (16,28)/(32,28) out to tips at x8/x40.
        _circle(self, "head", 24, 8, 4)
        self.add_line("antenna-left", (20, 8), (16, 4))
        self.add_line("antenna-right", (28, 8), (32, 4))
        self.relate("connect", "antenna-left", "head"); self.relate("connect", "antenna-right", "head")
        _path(self, "body", (16, 28), [((32, 28), 8, 8, True), (32, 36), (24, 44), (16, 36), (16, 28)], closed=True)
        self.add_line("stripe-1", (16, 28), (32, 28))
        self.add_line("stripe-2", (16, 36), (32, 36))
        self.relate("connect", "stripe-1", "body"); self.relate("connect", "stripe-2", "body")
        _path(self, "wing-left", (16, 28), [('c', (12, 26), (8, 25), (8, 22)), ('c', (8, 18), (12, 17), (15, 19)),
                                            ('c', (17, 21), (17, 25), (16, 28))], closed=True)
        _path(self, "wing-right", (32, 28), [('c', (36, 26), (40, 25), (40, 22)), ('c', (40, 18), (36, 17), (33, 19)),
                                             ('c', (31, 21), (31, 25), (32, 28))], closed=True)
        for w in ("wing-left", "wing-right"):
            self.relate("connect", w, "body"); self.relate("connect", w, "stripe-1")
