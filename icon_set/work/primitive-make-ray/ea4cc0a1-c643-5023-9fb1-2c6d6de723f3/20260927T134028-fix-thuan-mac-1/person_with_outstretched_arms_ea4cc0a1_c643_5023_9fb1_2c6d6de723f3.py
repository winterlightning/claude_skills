from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ea4cc0a1-c643-5023-9fb1-2c6d6de723f3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-outstretched-arms-ea4cc0a1/20260927T133650Z-thuan-mac-1/reference/anatomical_ea4cc0a1-c643-5023-9fb1-2c6d6de723f3.svg'
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
    icon_id = 'person-with-outstretched-arms-ea4cc0a1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('person', 'with', 'outstretched', 'arms')

    def build(self) -> None:
        # Standing figure with arms stretched up and out and legs apart, as in the reference, in the
        # shared stick-figure vocabulary (full_body_ref.png): a round head exactly 8 above a short
        # vertical neck, both arms rising outward from the shoulder, a long straight torso so the
        # limbs no longer cross in an X, and legs spread from the hip.
        _circle(self, "head", 24, 9, 5)
        self.add_line("torso", (24, 22), (24, 24))
        self.add_line("torso-low", (24, 24), (24, 34))
        self.add_line("arm-l", (24, 24), (8, 16))
        self.add_line("arm-r", (24, 24), (40, 16))
        self.add_line("leg-l", (24, 34), (14, 44))
        self.add_line("leg-r", (24, 34), (34, 44))
        for a, b in (("torso", "torso-low"), ("torso", "arm-l"), ("torso", "arm-r"), ("torso-low", "arm-l"),
                     ("torso-low", "arm-r"), ("arm-l", "arm-r"), ("torso-low", "leg-l"), ("torso-low", "leg-r"), ("leg-l", "leg-r")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
