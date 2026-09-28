from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '799ea4de-0531-534a-9c5e-9d0bf37abe6f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__breakfast-pancake-stack/20260927T072058Z-thuan-mac-1/reference/exotic food oyster_799ea4de-0531-534a-9c5e-9d0bf37abe6f.svg'
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


def _smooth(knots, closed=False):
    """Catmull-Rom steps through integer knots (horizontal/vertical tangents stay exact)."""
    pts = list(knots)
    n = len(pts)
    steps = []
    for i in range(n - 1 if not closed else n):
        p0 = pts[i - 1] if (i > 0 or closed) else pts[i]
        p1, p2 = pts[i], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (i + 2 < n or closed) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        steps.append(('c', c1, c2, p2))
    return steps


class Drawing(Solo48):
    icon_id = 'breakfast-pancake-stack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('breakfast', 'pancake', 'stack')

    def build(self) -> None:
        # Plan: three soft pancakes stacked as 8-tall pill layers (r4 end caps
        # bulging out, middle one wider), sharing the seam lines; a dish below.
        caps = [(12, 36), (10, 38), (12, 36)]   # (left cap x, right cap x) per layer
        ys = [6, 14, 22, 30]
        # Left side: caps top to bottom, joined by short runs where widths step.
        left = []
        pt = (caps[0][0], 6)
        for k, (l, r) in enumerate(caps):
            y0, y1 = ys[k], ys[k + 1]
            if pt[0] != l:
                left.append((l, y0))
            left.append(((l, y1), 4, 4, False))
            pt = (l, y1)
        _path(self, 'left', (caps[0][0], 6), left)
        right = []
        pt = (caps[0][1], 6)
        for k, (l, r) in enumerate(caps):
            y0, y1 = ys[k], ys[k + 1]
            if pt[0] != r:
                right.append((r, y0))
            right.append(((r, y1), 4, 4, True))
            pt = (r, y1)
        _path(self, 'right', (caps[0][1], 6), right)
        self.add_line('top', (12, 6), (36, 6))
        self.add_line('seam-1', (12, 14), (36, 14))
        self.add_line('seam-2', (12, 22), (36, 22))
        self.add_line('bottom', (12, 30), (36, 30))
        for part in ('top', 'seam-1', 'seam-2', 'bottom'):
            self.relate('connect', part, 'left')
            self.relate('connect', part, 'right')
        # Dish: flat base with raised rims.
        _path(self, 'plate', (6, 38), [(10, 42), (38, 42), (42, 38)])
