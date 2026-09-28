from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8b9fd40e-030d-4023-801b-5cc4a7e68ec9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reacting-to-spicy-food-batch-012-06/20260927T133650Z-thuan-mac-1/reference/spicy weakness person very spicy level_8b9fd40e-030d-4023-801b-5cc4a7e68ec9.svg'
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
    icon_id = 'person-reacting-to-spicy-food-batch-012-06'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    human_construction = "bust"
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('person', 'spicy', 'flame', 'face', 'food', 'reaction')

    def build(self) -> None:
        # Person reacting to very spicy food, as in the reference: a round head with a dazed eye and
        # its mouth gaping open toward the upper left, where a large fireball bursts out (a round
        # flame body with a tall main tongue and a smaller side tongue).
        _path(self, "head", (26, 24), [((44, 30), 10, 10, True), ((26, 36), 10, 10, True)])
        self.add_dot("eye", (35, 30))
        _path(self, "flame", (9, 8), [('c', (6, 12), (4, 16), (4, 21)), ('c', (4, 25), (7, 28), (11, 28)),
                                      ('c', (15, 28), (18, 25), (18, 21)), ('c', (19, 18), (21, 16), (22, 12)),
                                      ('c', (19, 13), (17, 14), (15, 16)), ('c', (13, 14), (11, 11), (9, 8))], True)
