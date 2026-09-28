from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5240dbe0-19a2-54d5-b0f7-5cc3089e49e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-supported-balance/20260927T150142Z-thuan-mac-1/reference/acro yoga pose_5240dbe0-19a2-54d5-b0f7-5cc3089e49e4.svg'
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
    icon_id = 'acro-yoga-supported-balance'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('acro', 'yoga', 'supported', 'balance')

    def build(self) -> None:
        # after the reference: a person in profile facing left, kneeling upright with a rounded back, the arm
        # stretched forward and the legs folded down with the feet forward along the ground (r4 head exactly 8
        # above a short neck), beside two round props stacked on the right
        _circle(self, "head", 20, 10, 4)
        self.add_line("torso", (20, 22), (20, 24))
        self.add_bezier("back", (20, 24), ((27, 25), (27, 33), (20, 34)))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", (20, 24), (6, 26))
        self.add_polyline("legs", (20, 34), (18, 42), (8, 42))
        for a, b in (("torso", "back"), ("torso", "arm"), ("back", "arm"), ("back", "legs")):
            self.relate("connect", a, b)
        _circle(self, "prop-top", 38, 20, 4)
        _circle(self, "prop-bottom", 38, 36, 4)
