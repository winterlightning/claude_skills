from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f8a79412-2951-4699-9934-43d0710ff866'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fish-shaped-pastry-batch-011-04/20260927T153247Z-thuan-mac-1/reference/desert fish shaped grilled bun taiyaki_f8a79412-2951-4699-9934-43d0710ff866.svg'
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
    icon_id = 'fish-shaped-pastry-batch-011-04'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('fish', 'pastry', 'taiyaki', 'dessert', 'food', 'bun')

    def build(self) -> None:
        # Taiyaki (fish-shaped grilled bun), as in the reference: a plump rounded fish body with a
        # blunt round nose, a pinched waist and a broad rounded tail with a shallow centre notch,
        # and two scale arcs on the body (a dot eye beside an arc reads as a winking face, so the
        # eye is left out). Mirrored about y=24.
        def m(p):
            return (p[0], 48 - p[1])

        top = [('c', (4, 15), (11, 10), (19, 10)), ('c', (27, 10), (31, 13), (34, 18)),
               ('c', (36, 12), (44, 10), (44, 16)), ('c', (44, 20), (43, 22), (42, 24))]
        bottom = [('c', m((43, 22)), m((44, 20)), m((44, 16))), ('c', m((44, 10)), m((36, 12)), m((34, 18))),
                  ('c', m((31, 13)), m((27, 10)), m((19, 10))), ('c', m((11, 10)), m((4, 15)), (4, 24))]
        _path(self, "body", (4, 24), top + bottom, True)
        _path(self, "scale-1", (15, 20), [((15, 28), 6, 6, True)])
        _path(self, "scale-2", (25, 20), [((25, 28), 6, 6, True)])
