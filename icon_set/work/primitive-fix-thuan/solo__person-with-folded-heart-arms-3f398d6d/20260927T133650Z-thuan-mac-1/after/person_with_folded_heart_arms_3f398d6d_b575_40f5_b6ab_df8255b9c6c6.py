from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3f398d6d-b575-40f5-b6ab-df8255b9c6c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-folded-heart-arms-3f398d6d/20260927T133650Z-thuan-mac-1/reference/phone digital well being heart_3f398d6d-b575-40f5-b6ab-df8255b9c6c6.svg'
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
    icon_id = 'person-with-folded-heart-arms-3f398d6d'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('person', 'with', 'folded', 'heart', 'arms')

    def build(self) -> None:
        # Person whose folded arms form a heart, as in the reference: a round head above a heart built
        # like the reference - a 45-degree diamond (notch, side corners, point) with a three-quarter
        # r8 lobe on each upper side - and the folded forearms drawn as the diamond's upper sides,
        # the inverted V from the notch.
        _circle(self, "head", 24, 8, 4)
        _path(self, "heart", (24, 44), [(16, 36), ((8, 28), 8, 8, True), ((16, 20), 8, 8, True), ((24, 28), 8, 8, True),
                                        ((32, 20), 8, 8, True), ((40, 28), 8, 8, True), ((32, 36), 8, 8, True), (24, 44)], True)
        self.add_line("arm-l", (24, 28), (16, 36))
        self.add_line("arm-r", (24, 28), (32, 36))
        self.relate("connect", "heart", "arm-l")
        self.relate("connect", "heart", "arm-r")
        self.relate("connect", "arm-l", "arm-r")
