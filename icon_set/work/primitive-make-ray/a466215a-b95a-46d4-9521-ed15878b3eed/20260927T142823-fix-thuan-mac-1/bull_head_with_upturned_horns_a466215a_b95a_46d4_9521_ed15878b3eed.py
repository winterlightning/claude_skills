from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a466215a-b95a-46d4-9521-ed15878b3eed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bull-head-with-upturned-horns/20260927T142733Z-thuan-mac-1/reference/beast_a466215a-b95a-46d4-9521-ed15878b3eed.svg'
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
    icon_id = 'bull-head-with-upturned-horns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bull', 'head', 'with', 'upturned', 'horns')

    def build(self) -> None:
        # Mirrored bull head about x=24: domed crown, horns curling up from the
        # crown corners, ears pointing out, cheeks narrowing into a long muzzle
        # with a round nose; two eyes 8 apart.
        _path(self, 'head', (14, 14), [
            ('c', (18, 9), (30, 9), (34, 14)),
            (42, 17),
            ('c', (40, 21), (38, 24), (36, 24)),
            ('c', (36, 28), (36, 28), (31, 32)),
            (31, 35),
            ((17, 35), 7, 7, True),
            (17, 32),
            ('c', (12, 28), (12, 28), (12, 24)),
            ('c', (10, 24), (8, 21), (6, 17)),
            (14, 14),
        ], closed=True)
        self.add_bezier('horn-left', (14, 14), ((12, 11), (8, 10), (8, 6)))
        self.add_bezier('horn-right', (34, 14), ((36, 11), (40, 10), (40, 6)))
        self.relate('connect', 'head', 'horn-left')
        self.relate('connect', 'head', 'horn-right')
        self.add_dot('eye-left', (20, 22))
        self.add_dot('eye-right', (28, 22))
