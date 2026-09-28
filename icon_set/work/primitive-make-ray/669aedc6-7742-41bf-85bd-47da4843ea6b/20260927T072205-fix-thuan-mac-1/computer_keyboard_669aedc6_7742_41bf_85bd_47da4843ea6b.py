from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '669aedc6-7742-41bf-85bd-47da4843ea6b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__computer-keyboard/20260927T072058Z-thuan-mac-1/reference/keyboard_669aedc6-7742-41bf-85bd-47da4843ea6b.svg'
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
    icon_id = 'computer-keyboard'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'typing', 'input', 'keys', 'peripheral', 'computer', 'hardware', 'text')

    def build(self) -> None:
        # Plan (Lucide keyboard at 2x): wide square-cornered case, two staggered
        # rows of key dots on an 8 pitch, and a space bar on the bottom row.
        _path(self, 'case', (4, 8), [(44, 8), (44, 40), (4, 40), (4, 8)], True)
        for i, x in enumerate((12, 20, 28, 36)):
            self.add_dot(f'key-a{i}', (x, 16))
        for i, x in enumerate((16, 24, 32)):
            self.add_dot(f'key-b{i}', (x, 24))
        self.add_line('space-bar', (14, 32), (34, 32))
