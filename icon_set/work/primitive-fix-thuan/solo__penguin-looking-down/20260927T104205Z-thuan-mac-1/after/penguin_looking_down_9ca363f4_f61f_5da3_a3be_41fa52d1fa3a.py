from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9ca363f4-f61f-5da3-a3be-41fa52d1fa3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__penguin-looking-down/20260927T104205Z-thuan-mac-1/reference/penguin mother_9ca363f4-f61f-5da3-a3be-41fa52d1fa3a.svg'
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
    icon_id = 'penguin-looking-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('penguin', 'bending', 'looking', 'down', 'bird', 'antarctic', 'nurture', 'care')

    def build(self) -> None:
        # Plan (reference): a penguin in side view with its head bowed, beak
        # pointing down-left. One closed silhouette: long beak (tip (8,24)),
        # round crown on y=4, back of the head curving into a long back that
        # swells to x=40, a flat base on y=44, and the belly rising to the
        # throat under the beak. One eye dot in the head; a flipper hangs from
        # the back at (36,22), angled down and forward.
        _path(self, "body", (8, 24), [(15, 13),
                                      ('c', (15, 7), (19, 4), (23, 4)),
                                      ('c', (29, 4), (32, 9), (33, 14)),
                                      ('c', (34, 17), (35, 19), (36, 22)),
                                      ('c', (37, 26), (40, 30), (40, 36)),
                                      ('c', (40, 41), (37, 44), (32, 44)),
                                      (22, 44),
                                      ('c', (18, 44), (17, 38), (18, 32)),
                                      ('c', (19, 27), (19, 24), (17, 21)),
                                      (8, 24)], True)
        self.add_dot("eye", (24, 13))
        self.add_line("flipper", (36, 22), (30, 34))
        self.relate("connect", "flipper", "body")
