from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '35453f6e-cd21-46fc-9fb9-1211c1c34319'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__right-double-click-mouse/20260927T133651Z-thuan-mac-1/reference/right double click mouse_35453f6e-cd21-46fc-9fb9-1211c1c34319.svg'
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
    icon_id = 'right-double-click-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('right', 'double', 'click', 'mouse')

    def build(self) -> None:
        # Mouse pill low-left (16 wide, 23 tall) with the right button outlined by a centre line that
        # turns right into a crossbar; two quarter-circle click waves (r7, r16: 9 apart so the concentric
        # gap certifies) about P=(24,20), just off the mouse's top-right shoulder.
        _path(self, "body", (16, 21), [((24, 29), 8, 8, True), (24, 33), (24, 36), ((16, 44), 8, 8, True),
                                       ((8, 36), 8, 8, True), (8, 29), ((16, 21), 8, 8, True)], True)
        _path(self, "right-button", (16, 21), [(16, 29), ((20, 33), 4, 4, False), (24, 33)])
        self.relate("connect", "body-1", "body-7", "right-button-1")
        self.relate("connect", "right-button-3", "body-2", "body-3")
        self.add_arc("click-wave-1", (24, 13), (31, 20), radius_x=7, radius_y=7, sweep=True)
        self.add_arc("click-wave-2", (24, 4), (40, 20), radius_x=16, radius_y=16, sweep=True)
