from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4e348568-3af9-4250-a67d-883882fbc6e6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__otter-with-paws/20260927T104205Z-thuan-mac-1/reference/otter_4e348568-3af9-4250-a67d-883882fbc6e6.svg'
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
    icon_id = 'otter-with-paws'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('otter', 'with', 'paws')

    def build(self) -> None:
        # Plan (reference): an otter peeking up, head in profile facing right,
        # two big front paws resting on the ground. One long outline: the back
        # rises from the top of the left paw, arcs over the crown (top on y=6)
        # and runs out to the rounded snout (x=42), turns under the chin and
        # drops as the chest onto the top of the right paw. Each paw = r6 dome
        # about (12,40)/(34,40) closed underneath by three r2 toe scallops (toe
        # bottoms on y=42). One eye dot in the head.
        _path(self, "outline", (12, 34), [('c', (9, 22), (12, 6), (26, 6)),
                                          ('c', (34, 6), (40, 8), (42, 12)),
                                          ('c', (42, 16), (39, 18), (36, 18)),
                                          ('c', (33, 24), (34, 30), (34, 34))])
        for name, cx in (("paw-left", 12), ("paw-right", 34)):
            _path(self, name, (cx - 6, 40), [((cx, 34), 6, 6, True), ((cx + 6, 40), 6, 6, True),
                                             ((cx + 2, 40), 2, 2, True), ((cx - 2, 40), 2, 2, True),
                                             ((cx - 6, 40), 2, 2, True)], True)
            self.relate("connect", "outline", name)
        self.add_dot("eye", (28, 15))
