from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '28a45b81-4d2d-59c4-aee6-627238431d00'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plate-between-fork-and-knife/20260927T133650Z-thuan-mac-1/reference/restaurant eating set_28a45b81-4d2d-59c4-aee6-627238431d00.svg'
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
    icon_id = 'plate-between-fork-and-knife'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('plate', 'fork', 'knife', 'table setting', 'dining', 'cutlery', 'meal')

    def build(self) -> None:
        # Place setting as in the reference: a fork at the left (U-shaped tine head on a long handle),
        # a large round plate low in the middle and a knife at the right (straight spine with the
        # blade swelling left from the tip and stepping back into the handle above the plate rim).
        self.add_line("tine-l", (4, 8), (4, 14))
        self.add_arc("cup", (4, 14), (12, 14), radius_x=4, radius_y=4, sweep=False)
        self.add_line("tine-r", (12, 14), (12, 8))
        self.add_contour("fork", "tine-l", "cup", "tine-r")
        self.add_line("handle", (8, 18), (8, 40))
        self.relate("connect", "fork", "handle")
        _circle(self, "plate", 26, 31, 9)
        self.add_line("spine", (44, 8), (44, 40))
        self.add_bezier("blade-edge", (44, 8), ((39, 9), (36, 11), (36, 14)))
        self.add_line("blade-side", (36, 14), (36, 17))
        self.add_line("blade-heel", (36, 17), (44, 17))
        self.add_contour("blade", "blade-edge", "blade-side", "blade-heel")
        self.relate("connect", "blade", "spine")
