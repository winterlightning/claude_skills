from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1421392c-5884-4c7e-bf5c-1082165dfba9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__book-open-1421392c/20260927T142727Z-thuan-mac-1/reference/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.svg'
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
    icon_id = 'book-open-1421392c'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'content'
    categories = ('content', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self) -> None:
        # Open book seen from the front, as in the reference: two tall pages whose top edges arch up
        # over the outer half and dip into the spine, whose bottom edges sag down to the spine, and a
        # straight centre spine. Built on the vertical axis x=24 with mirrored coordinates.
        def m(p):
            return (48 - p[0], p[1])

        left_top = [('c', (21, 9), (17, 8), (13, 8)), ('c', (10, 8), (6, 8.6), (4, 10))]
        left_bottom = [('c', (12, 34), (19, 36), (24, 40))]
        steps = left_top + [(4, 36)] + left_bottom
        steps += [('c', m((19, 36)), m((12, 34)), (44, 36)), (44, 10),
                  ('c', m((6, 8.6)), m((10, 8)), m((13, 8))), ('c', m((17, 8)), m((21, 9)), (24, 12))]
        _path(self, "pages", (24, 12), steps, True)
        self.add_line("spine", (24, 12), (24, 40))
        self.relate("connect", "pages", "spine")
