from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd7a8728f-7d41-4594-84ad-c41d60d742d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-bug/20260927T104205Z-thuan-mac-1/reference/pet_d7a8728f-7d41-4594-84ad-c41d60d742d9.svg'
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
    icon_id = 'round-bug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'state')
    aliases = ()
    keywords = ('bug', 'insect', 'beetle', 'small', 'antennae', 'legs', 'pest', 'nature')

    def build(self) -> None:
        # Plan: a round beetle seen from above, mirrored about x=24. One closed
        # silhouette: big round body (r13 about (24,29), bottom at 42) with the
        # head as an r5 bump on top, joined at the 5-12-13 points (19,17)/(29,17).
        # Two antennae leave the head at its 3-4-5 points (20,14)/(28,14) and
        # curve up and out to the top edge; two short curved legs per side leave
        # the body at the 5-12-13 side points (12,24)/(12,34) and reach x=6/42.
        _path(self, "body", (29, 17), [((28, 14), 5, 5, False), ((20, 14), 5, 5, False),
                                       ((19, 17), 5, 5, False),
                                       ((12, 24), 13, 13, False), ((12, 34), 13, 13, False),
                                       ((36, 34), 13, 13, False), ((36, 24), 13, 13, False),
                                       ((29, 17), 13, 13, False)], True)
        for side, s in (("left", 1), ("right", -1)):
            X = lambda x: 24 + s * (x - 24)
            self.add_bezier(f"antenna-{side}", (X(20), 14), ((X(18), 10), (X(15), 7), (X(11), 6)))
            self.add_bezier(f"leg-{side}-front", (X(12), 24), ((X(9), 22), (X(7), 22), (X(6), 19)))
            self.add_bezier(f"leg-{side}-back", (X(12), 34), ((X(9), 35), (X(7), 37), (X(6), 40)))
            for part in (f"antenna-{side}", f"leg-{side}-front", f"leg-{side}-back"):
                self.relate("connect", part, "body")
