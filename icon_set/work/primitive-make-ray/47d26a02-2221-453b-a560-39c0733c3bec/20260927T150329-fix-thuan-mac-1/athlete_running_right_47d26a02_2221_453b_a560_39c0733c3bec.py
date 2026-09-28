from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47d26a02-2221-453b-a560-39c0733c3bec'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__athlete-running-right/20260927T150142Z-thuan-mac-1/reference/athletics running 1_47d26a02-2221-453b-a560-39c0733c3bec.svg'
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
    icon_id = 'athlete-running-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('athlete', 'running', 'right')

    def build(self) -> None:
        # sprinter heading right, pose taken from the reference: head up front, torso leaning forward, front arm
        # bent with the hand raised, back arm swung back, front knee driving forward, back leg kicked out behind.
        # r4 head exactly 8 above a short vertical neck segment (human_ref full_body_ref.png construction).
        _circle(self, "head", 32, 10, 4)
        self.add_line("torso", (32, 22), (32, 24))
        self.add_line("torso-lean", (32, 24), (24, 34))
        self.mark_human_figure("runner", head="head", torso="torso", torso_junction="start")
        self.add_polyline("arm-front", (32, 24), (38, 30), (42, 24))
        self.add_polyline("arm-back", (32, 24), (22, 20), (16, 26))
        self.add_polyline("leg-front", (24, 34), (32, 36), (29, 42))
        self.add_polyline("leg-back", (24, 34), (16, 38), (6, 38))
        parts = ["torso", "torso-lean", "arm-front", "arm-back", "leg-front", "leg-back"]
        for i, a in enumerate(parts):
            for b in parts[i + 1:]:
                if {a, b} & {"torso", "torso-lean"} or (a[:3] == b[:3]):
                    self.relate("connect", a, b)
