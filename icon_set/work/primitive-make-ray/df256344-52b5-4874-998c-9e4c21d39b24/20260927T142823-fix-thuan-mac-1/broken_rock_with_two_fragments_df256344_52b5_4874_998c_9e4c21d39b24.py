from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'df256344-52b5-4874-998c-9e4c21d39b24'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broken-rock-with-two-fragments/20260927T142733Z-thuan-mac-1/reference/debris_df256344-52b5-4874-998c-9e4c21d39b24.svg'
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
    icon_id = 'broken-rock-with-two-fragments'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('broken', 'rock', 'with', 'two', 'fragments')

    def build(self) -> None:
        # Angular rock with its broken side face: the crack runs parallel to the
        # right-hand face edge, offset (-8,-4), from the top-right corner down to
        # the lower-left corner. Two outlined fragments sit to the right.
        self.add_polyline('rock', (4, 18), (15, 8), (26, 14), (26, 24), (20, 36), (16, 40), (8, 36), (4, 32), closed=True)
        self.add_polyline('crack', (26, 14), (18, 20), (12, 32), (8, 36))
        self.relate('connect', 'rock', 'crack')
        self.add_polyline('chip-upper', (39, 11), (44, 22), (34, 22), closed=True)
        self.add_polyline('chip-lower', (35, 30), (44, 36), (35, 40), (31, 37), closed=True)
