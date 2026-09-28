from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '68a9474e-3bef-4c47-a3ff-c7de0c572e84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__buckingham-palace-reference/20260927T142733Z-thuan-mac-1/reference/landmark buckingham palace_68a9474e-3bef-4c47-a3ff-c7de0c572e84.svg'
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
    icon_id = 'buckingham-palace-reference'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('buckingham', 'palace', 'reference')

    def build(self) -> None:
        # Two V-topped side towers flank a low central block; the central tower
        # stands on the block with a flat roof and a spire.
        self.add_polyline('facade', (4, 40), (4, 20), (8, 24), (12, 20), (12, 30), (20, 30), (20, 16), (24, 16),
                          (28, 16), (28, 30), (36, 30), (36, 20), (40, 24), (44, 20), (44, 40), (36, 40), (12, 40), (4, 40),
                          closed=True)
        self.add_line('left-tower-wall', (12, 30), (12, 40))
        self.add_line('right-tower-wall', (36, 30), (36, 40))
        self.add_line('tower-base', (20, 30), (28, 30))
        self.add_line('spire', (24, 16), (24, 8))
        for part in ('left-tower-wall', 'right-tower-wall', 'tower-base', 'spire'):
            self.relate('connect', 'facade', part)
