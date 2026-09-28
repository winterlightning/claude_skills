from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ad5be048-1dc2-486c-81ca-f13c84abf2da'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__adult-swinging-child-by-hands/20260927T150142Z-thuan-mac-1/reference/family child play_ad5be048-1dc2-486c-81ca-f13c84abf2da.svg'
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
    icon_id = 'adult-swinging-child-by-hands'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('adult', 'child', 'play', 'swinging', 'hands', 'family')

    def build(self) -> None:
        # adult on the left holding a child by the hands and swinging it out to the right: the adult's arms and
        # the child's arms meet at the joined hands; the child's body and bent legs fly out behind it
        _circle(self, "adult-head", 10, 12, 4)
        self.add_line("adult-torso", (10, 24), (10, 26))
        self.add_line("adult-torso-low", (10, 26), (8, 34))
        self.mark_human_figure("adult", head="adult-head", torso="adult-torso", torso_junction="start")
        self.add_line("adult-arm", (10, 26), (20, 32))
        self.add_line("adult-leg-l", (8, 34), (4, 40))
        self.add_line("adult-leg-r", (8, 34), (13, 40))
        _circle(self, "child-head", 27, 17, 3)
        self.add_line("child-torso", (27, 28), (27, 30))
        self.add_line("child-torso-low", (27, 30), (35, 33))
        self.mark_human_figure("child", head="child-head", torso="child-torso", torso_junction="start")
        self.add_line("child-arm", (27, 30), (20, 32))
        self.add_polyline("child-leg", (35, 33), (42, 33), (44, 40))
        groups = (("adult-torso", "adult-torso-low", "adult-arm"), ("adult-torso-low", "adult-leg-l", "adult-leg-r"),
                  ("child-torso", "child-torso-low", "child-arm"), ("child-torso-low", "child-leg"),
                  ("adult-arm", "child-arm"))
        for g in groups:
            for i, a in enumerate(g):
                for b in g[i + 1:]:
                    self.relate("connect", a, b)
