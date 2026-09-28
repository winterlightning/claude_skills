from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f746fcda-f75b-56bc-8b21-d20b11cd104f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__carving-a-wooden-bowl/20260927T144116Z-thuan-mac-1/reference/wood carving bowl_f746fcda-f75b-56bc-8b21-d20b11cd104f.svg'
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
    icon_id = 'carving-a-wooden-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('carving', 'a', 'wooden', 'bowl')

    def build(self) -> None:
        # Wood-carving a bowl: a deep half-ellipse bowl under a flat rim, a
        # carving knife coming in at 45 degrees from the top-left (r5 round
        # butt on 3-4-5 points hitting the SQUARE top/left extremes, straight
        # handle behind a ferrule, a tapered blade whose tip rests on the rim) and a wood
        # shaving curling up out of the bowl on the right.
        _path(self, 'bowl', (6, 26), [(26, 26), (32, 26), (42, 26), ((6, 26), 18, 16, True)], closed=True)
        _path(self, 'knife', (15, 8), [
            ((8, 15), 5, 5, False, True), (14, 21), (26, 26), (21, 14), (15, 8),
        ], closed=True)
        self.add_line('knife-ferrule', (14, 21), (21, 14))
        self.relate('connect', 'knife', 'knife-ferrule')
        self.relate('connect', 'bowl', 'knife')
        _path(self, 'shaving', (32, 26), [
            ('c', (32, 20), (40, 20), (40, 13)),
            ((30, 13), 5, 5, False),
        ])
        self.relate('connect', 'bowl', 'shaving')
