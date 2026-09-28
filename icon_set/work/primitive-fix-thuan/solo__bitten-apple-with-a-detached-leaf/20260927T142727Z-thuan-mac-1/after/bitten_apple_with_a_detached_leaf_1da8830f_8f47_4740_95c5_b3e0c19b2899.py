from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1da8830f-8f47-4740-95c5-b3e0c19b2899'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitten-apple-with-a-detached-leaf/20260927T142727Z-thuan-mac-1/reference/apple logo_1da8830f-8f47-4740-95c5-b3e0c19b2899.svg'
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
    icon_id = 'bitten-apple-with-a-detached-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('apple', 'fruit', 'bite', 'leaf', 'logo', 'food', 'orchard')

    def build(self) -> None:
        # Bitten apple with a detached leaf, as in the reference: an apple outline with two rounded
        # top lobes meeting in a pointed dip, a concave bite taken out of the right side, two shallow
        # bottom lobes, and a separate curved leaf stroke tilted up to the right above the dip.
        _path(self, "leaf", (26, 11), [((33, 4), 7, 7, True)])
        _path(self, "apple", (24, 21), [('c', (26, 19.5), (29, 19), (32, 19)),
                                        ('c', (35, 19), (37.5, 20.5), (39, 23)),
                                        ((40, 37), 8, 8, False),
                                        ('c', (38, 41), (35.5, 44), (32, 44)),
                                        ('c', (29, 44), (27, 42), (24, 42)),
                                        ('c', (21, 42), (19, 44), (16, 44)),
                                        ('c', (11.5, 44), (8, 38.5), (8, 31)),
                                        ('c', (8, 24.5), (11.5, 19), (16, 19)),
                                        ('c', (19, 19), (22, 19.5), (24, 21))], True)
