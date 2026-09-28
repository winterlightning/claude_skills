from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a4cdc728-6ddc-5030-90ee-9fd33c53636a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__aerial-yoga-inversion/20260927T150142Z-thuan-mac-1/reference/aerial yogabasic inversion pose_a4cdc728-6ddc-5030-90ee-9fd33c53636a.svg'
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
    icon_id = 'aerial-yoga-inversion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('aerial', 'yoga', 'inversion')

    def build(self) -> None:
        # aerial yoga inversion (three-quarter view): a V of hammock fabric hangs from the ceiling and holds the
        # hips; the person hangs upside down, knees bent over to one side, torso straight down, arms reaching
        # down and out, head at the bottom (r4 head exactly 8 below the neck end of the torso)
        self.add_line("ceiling-l", (6, 6), (16, 6))
        self.add_line("ceiling-m", (16, 6), (28, 6))
        self.add_line("ceiling-r", (28, 6), (42, 6))
        self.add_line("fabric-l", (16, 6), (22, 18))
        self.add_line("fabric-r", (28, 6), (22, 18))
        self.add_line("hips", (22, 18), (22, 21))
        self.add_line("torso", (22, 21), (22, 26))
        _circle(self, "head", 22, 38, 4)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="end")
        self.add_polyline("leg", (22, 18), (36, 14), (42, 22))
        self.add_line("arm-l", (22, 21), (7, 36))
        self.add_line("arm-r", (22, 21), (37, 36))
        pairs = (("ceiling-l", "ceiling-m"), ("ceiling-m", "ceiling-r"), ("fabric-l", "ceiling-m"), ("fabric-r", "ceiling-m"),
                 ("fabric-l", "ceiling-l"), ("fabric-r", "ceiling-r"), ("fabric-l", "fabric-r"),
                 ("fabric-l", "hips"), ("fabric-r", "hips"), ("leg", "hips"), ("leg", "fabric-l"), ("leg", "fabric-r"),
                 ("hips", "torso"), ("hips", "arm-l"), ("hips", "arm-r"), ("torso", "arm-l"), ("torso", "arm-r"),
                 ("arm-l", "arm-r"))
        for a, b in pairs:
            self.relate("connect", a, b)
