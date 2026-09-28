from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a2a08b2a-e688-4bab-8c8e-c60515c88862'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bowler-approaching-a-pin/20260927T142727Z-thuan-mac-1/reference/bowling player_a2a08b2a-e688-4bab-8c8e-c60515c88862.svg'
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
    icon_id = 'bowler-approaching-a-pin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bowler', 'bowling', 'ball', 'pin', 'sport', 'person', 'game')

    def build(self) -> None:
        # Bowler approaching a pin, as in the reference (human ref:
        # icon_set/references/human_ref/full_body_ref.png): a stick figure leaning forward in the
        # delivery stride - head held exactly 8 above a short vertical neck, torso leaning back to
        # the hip, the ball arm swung back holding the ball behind, the back leg extended behind
        # and the front leg bent - with a tall bowling pin standing ahead of the front foot.
        _circle(self, "head", 24, 10, 4)
        self.add_line("torso", (24, 22), (24, 24))
        self.add_line("torso-lean", (24, 24), (17, 31))
        self.add_line("arm-back", (24, 24), (12, 19))
        _circle(self, "ball", 9, 19, 3)
        self.add_line("leg-back", (17, 31), (8, 42))
        _path(self, "leg-front", (17, 31), [(23, 35), (23, 42)])
        _path(self, "pin", (37, 24), [((41, 28), 4, 4, True), (41, 32), ('c', (41, 34), (42, 35), (42, 37)),
                                      ('c', (42, 39.5), (41, 41), (40, 42)), (34, 42),
                                      ('c', (33, 41), (32, 39.5), (32, 37)), ('c', (32, 35), (33, 34), (33, 32)),
                                      (33, 28), ((37, 24), 4, 4, True)], True)
        for a, b in (("torso", "torso-lean"), ("torso", "arm-back"), ("torso-lean", "arm-back"), ("arm-back", "ball"),
                     ("torso-lean", "leg-back"), ("torso-lean", "leg-front"), ("leg-back", "leg-front")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
