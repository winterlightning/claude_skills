from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b62f90b2-531e-43c6-ad69-f18b9bf695f8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__adult-child-stretching/20260927T150142Z-thuan-mac-1/reference/yoga stretch_b62f90b2-531e-43c6-ad69-f18b9bf695f8.svg'
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
    icon_id = 'adult-child-stretching'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('adult', 'child', 'stretching', 'yoga', 'exercise')

    def build(self) -> None:
        # adult stretching with both arms raised in a Y (arms leave the torso 17 below the head centre so they keep
        # 8 from the head), beside a small seated child: r4 head resting on a rounded body (bust contact)
        _circle(self, "adult-head", 32, 10, 4)
        self.add_line("adult-torso", (32, 22), (32, 27))
        self.add_line("adult-torso-low", (32, 27), (32, 32))
        self.mark_human_figure("adult", head="adult-head", torso="adult-torso", torso_junction="start")
        self.add_line("adult-arm-r", (32, 27), (42, 17))
        self.add_line("adult-arm-l", (32, 27), (22, 17))
        self.add_line("adult-leg-l", (32, 32), (26, 42))
        self.add_line("adult-leg-r", (32, 32), (38, 42))
        for a, b in (("adult-torso", "adult-torso-low"), ("adult-torso", "adult-arm-r"), ("adult-torso", "adult-arm-l"),
                     ("adult-torso-low", "adult-arm-r"), ("adult-torso-low", "adult-arm-l"), ("adult-arm-r", "adult-arm-l"),
                     ("adult-torso-low", "adult-leg-l"), ("adult-torso-low", "adult-leg-r"), ("adult-leg-l", "adult-leg-r")):
            self.relate("connect", a, b)
        _circle(self, "child-head", 12, 26, 4)
        self.add_arc("child-body", (6, 42), (18, 42), radius_x=6, radius_y=8, sweep=True)
        self.relate("connect", "child-head", "child-body")
