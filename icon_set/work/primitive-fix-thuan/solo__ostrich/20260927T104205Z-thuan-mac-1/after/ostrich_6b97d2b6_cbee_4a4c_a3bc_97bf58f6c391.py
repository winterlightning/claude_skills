from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b97d2b6-cbee-4a4c-a3bc-97bf58f6c391'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ostrich/20260927T104205Z-thuan-mac-1/reference/wild bird_6b97d2b6-cbee-4a4c-a3bc-97bf58f6c391.svg'
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
    icon_id = 'ostrich'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('ostrich', 'emu', 'bird', 'standing', 'neck', 'legs', 'flightless', 'africa')

    def build(self) -> None:
        # Plan (reference): a long-necked bird in side view facing right. One
        # closed silhouette: a rounded head with the crown on y=4 and a beak
        # pointing right (tip on x=40), a thick upright neck (walls x=24/32, 8
        # apart), a plump body with a round chest, flat belly and a pointed tail
        # on the left edge; two long legs hang from the belly to the floor.
        _path(self, "body", (40, 9), [('c', (37, 11), (34, 12), (32, 12)),
                                      (32, 28),
                                      ('c', (32, 33), (29, 36), (24, 36)),
                                      (16, 36),
                                      ('c', (12, 36), (9, 31), (8, 26)),
                                      ('c', (12, 22), (18, 20), (24, 20)),
                                      (24, 10),
                                      ('c', (24, 6), (26, 4), (29, 4)),
                                      ('c', (33, 4), (36, 6), (40, 9))], True)
        self.add_line("leg-back", (16, 36), (16, 44))
        self.add_line("leg-front", (24, 36), (24, 44))
        self.relate("connect", "leg-back", "body")
        self.relate("connect", "leg-front", "body")
