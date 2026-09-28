from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '317da08d-c0ee-4af0-b5d9-a57e3f5420c2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-climbing-stairs/20260927T153339Z-thuan-mac-1/reference/stairs person ascend_317da08d-c0ee-4af0-b5d9-a57e3f5420c2.svg'
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
    icon_id = 'person-climbing-stairs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'stairs', 'ascending', 'climbing', 'steps', 'wayfinding')

    def build(self) -> None:
        # Person climbing stairs, as in the reference (human ref:
        # icon_set/references/human_ref/full_body_ref.png): a walking figure on the left - head
        # held exactly 8 above a short neck, upright torso, one arm reaching forward and up, the
        # other swinging back, the back leg planted and the front leg lifted onto the first step -
        # and a staircase of 8x8 steps rising to the upper right.
        _circle(self, "head", 12, 10, 4)
        self.add_line("torso", (12, 22), (12, 24))
        self.add_line("torso-low", (12, 24), (12, 34))
        self.add_line("arm-front", (12, 24), (19, 20))
        self.add_line("arm-back", (12, 24), (6, 27))
        self.add_line("leg-back", (12, 34), (8, 42))
        _path(self, "leg-front", (12, 34), [(19, 31), (22, 34)])
        _path(self, "stairs", (22, 42), [(22, 34), (30, 34), (30, 26), (38, 26), (38, 18), (42, 18)])
        for a, b in (("torso", "torso-low"), ("torso", "arm-front"), ("torso", "arm-back"), ("torso-low", "arm-front"),
                     ("torso-low", "arm-back"), ("arm-front", "arm-back"), ("torso-low", "leg-back"),
                     ("torso-low", "leg-front"), ("leg-back", "leg-front"), ("leg-front", "stairs")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
