from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e73cd4c7-5003-4fa0-b716-19121f8fa738'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plow-back-stretch/20260927T133650Z-thuan-mac-1/reference/yoga back stretch_e73cd4c7-5003-4fa0-b716-19121f8fa738.svg'
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
    icon_id = 'plow-back-stretch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('plow', 'back', 'stretch', 'yoga', 'exercise')

    def build(self) -> None:
        # Plow pose (halasana), as in the reference: hips raised at the top right, the straight legs
        # reaching back over the head to the left, the back running down to the shoulders on the
        # floor, arms reaching along the floor to the right and a large head resting low beside a
        # short level neck (exactly 8 from the head outline), in the shared stick-figure style.
        _circle(self, "head", 20, 34, 6)
        self.add_line("legs", (4, 16), (32, 8))
        self.add_line("back", (32, 8), (36, 34))
        self.add_line("torso", (34, 34), (36, 34))
        self.add_line("arms", (36, 34), (44, 40))
        for a, b in (("legs", "back"), ("back", "torso"), ("back", "arms"), ("torso", "arms")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
