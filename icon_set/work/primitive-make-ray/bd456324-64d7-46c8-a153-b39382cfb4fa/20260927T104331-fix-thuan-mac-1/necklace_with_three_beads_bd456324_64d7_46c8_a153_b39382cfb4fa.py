from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bd456324-64d7-46c8-a153-b39382cfb4fa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__necklace-with-three-beads/20260927T104205Z-thuan-mac-1/reference/diy jewelry_bd456324-64d7-46c8-a153-b39382cfb4fa.svg'
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
    icon_id = 'necklace-with-three-beads'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('necklace', 'bead', 'beaded', 'jewellery', 'jewelry', 'diy', 'craft', 'cord', 'accessory')

    def build(self) -> None:
        # Plan: a bead necklace, mirrored about x=24: two strands hang from the
        # top edge and thread three beads - a small r4 bead on each side (outer
        # points on x=6/42) and a big r6 pendant bead at the bottom middle
        # (bottom at 42). Beads sit 8+ apart; the strand runs between them.
        _circle(self, "bead-middle", 24, 36, 6)
        for side, s in (("left", 1), ("right", -1)):
            X = lambda x: 24 + s * (x - 24)
            _circle(self, f"bead-{side}", X(10), 24, 4)
            self.add_bezier(f"strand-{side}-top", (X(14), 6), ((X(13), 11), (X(10), 15), (X(10), 20)))
            self.add_bezier(f"strand-{side}-low", (X(10), 28), ((X(10), 32), (X(14), 36), (X(18), 36)))
            self.relate("connect", f"strand-{side}-top", f"bead-{side}")
            self.relate("connect", f"strand-{side}-low", f"bead-{side}")
            self.relate("connect", f"strand-{side}-low", "bead-middle")
