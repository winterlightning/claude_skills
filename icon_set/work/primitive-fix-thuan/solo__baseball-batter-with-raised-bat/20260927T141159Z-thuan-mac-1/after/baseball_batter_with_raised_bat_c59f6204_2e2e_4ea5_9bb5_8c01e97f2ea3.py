from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c59f6204-2e2e-4ea5-9bb5-8c01e97f2ea3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baseball-batter-with-raised-bat/20260927T141159Z-thuan-mac-1/reference/baseball player_c59f6204-2e2e-4ea5-9bb5-8c01e97f2ea3.svg'
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
    icon_id = 'baseball-batter-with-raised-bat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('baseball', 'batter', 'holding', 'bat')

    def build(self) -> None:
        # Baseball batter with the bat raised (reference: a batter standing upright, legs apart, arms
        # reaching across to the hands at the left, the bat held up from the hands at a steep angle
        # beside the head). Shared stick-figure construction (human_ref/full_body_ref.png): r5 ring
        # head exactly 8 above an upright torso (31,24)-(31,34), legs apart to y44. The arms run out
        # level to the elbow (21,29) and down-left to the hands (11,24). The bat is one straight
        # 3:10 line through the hands, its knob end poking out below them at (8,34) and its barrel
        # rising to (17,4), 8.8+ clear of the head.
        _circle(self, "head", 31, 11, 5)
        self.add_line("torso", (31, 24), (31, 27))
        self.add_line("torso-low", (31, 27), (31, 34))
        self.add_line("leg-left", (31, 34), (23, 44))
        self.add_line("leg-right", (31, 34), (40, 44))
        _path(self, "arms", (31, 27), [(21, 29), (11, 24)])
        self.add_line("bat-knob", (8, 34), (11, 24))
        self.add_line("bat", (11, 24), (17, 4))
        for a, b in (("torso", "torso-low"), ("torso", "arms"), ("torso-low", "arms"), ("torso-low", "leg-left"),
                     ("torso-low", "leg-right"), ("leg-left", "leg-right"), ("arms", "bat"), ("arms", "bat-knob"),
                     ("bat", "bat-knob")):
            self.relate("connect", a, b)
        self.mark_human_figure("batter", head="head", torso="torso", torso_junction="start")
