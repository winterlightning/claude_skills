from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5521723a-f61f-58b0-9d3b-7bb857fa845d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-mask/20260927T104205Z-thuan-mac-1/reference/cosplay_5521723a-f61f-58b0-9d3b-7bb857fa845d.svg'
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
    icon_id = 'hand-holding-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('hand', 'holding', 'mask')

    def build(self) -> None:
        # Plan (reference): a theatre / cosplay face mask held up by a hand from
        # the lower left. Mask = tall shield (walls x=10/42, gently dipped top,
        # rounded top corners) whose right side curves down into a rounded chin
        # that tucks under the thumb. Two slanted eye slits (solid almonds drawn
        # as short strokes) dropping toward their pointed inner corners, like the
        # reference's eye holes. The hand, in front of the mask's lower left: a
        # thumb laid across the mask (8 tall, r4 tip about (28,34)) with the back
        # of the hand slanting down to the corner and the wrist beside it.
        _path(self, "mask", (10, 30), [(10, 9),
                                       ('c', (10, 7), (11, 6), (13, 6)),
                                       ('c', (22, 8), (31, 8), (39, 6)),
                                       ('c', (41, 6), (42, 7), (42, 9)),
                                       (42, 22),
                                       ('c', (42, 31), (37, 36), (32, 34))])
        self.add_bezier("eye-left", (19, 16), ((21, 16), (22, 17.5), (22, 21)))
        self.add_bezier("eye-right", (33, 16), ((31, 16), (30, 17.5), (30, 21)))
        _path(self, "hand", (6, 42), [(10, 30), (28, 30), ((32, 34), 4, 4, True),
                                      ((28, 38), 4, 4, True), (18, 38), (14, 42)])
        self.relate("connect", "hand", "mask")
