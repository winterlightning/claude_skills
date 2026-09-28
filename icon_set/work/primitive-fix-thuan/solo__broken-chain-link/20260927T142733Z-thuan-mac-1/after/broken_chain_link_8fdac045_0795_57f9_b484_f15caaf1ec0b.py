from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8fdac045-0795-57f9-b484-f15caaf1ec0b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broken-chain-link/20260927T142733Z-thuan-mac-1/reference/link broken_8fdac045-0795-57f9-b484-f15caaf1ec0b.svg'
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
    icon_id = 'broken-chain-link'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('broken', 'chain', 'link')

    def build(self) -> None:
        # Two mirrored half-capsules (r6 caps) with a 12-wide break; three spark
        # strokes above and three below the break, as in the reference.
        for side, sx in (('left', -1), ('right', 1)):
            cx, inner = 24 + sx * 12, 24 + sx * 6
            self.add_line(f'{side}-top', (inner, 18), (cx, 18))
            self.add_arc(f'{side}-cap', (cx, 18), (cx, 30), radius_x=6, radius_y=6, sweep=(sx > 0))
            self.add_line(f'{side}-bottom', (cx, 30), (inner, 30))
            self.relate('connect', f'{side}-top', f'{side}-cap')
            self.relate('connect', f'{side}-cap', f'{side}-bottom')
        for tag, y0, y1 in (('top', 6, 10), ('bottom', 42, 38)):
            self.add_line(f'spark-{tag}-mid', (24, y0), (24, y1))
            self.add_line(f'spark-{tag}-left', (12, y0), (16, y1))
            self.add_line(f'spark-{tag}-right', (36, y0), (32, y1))
