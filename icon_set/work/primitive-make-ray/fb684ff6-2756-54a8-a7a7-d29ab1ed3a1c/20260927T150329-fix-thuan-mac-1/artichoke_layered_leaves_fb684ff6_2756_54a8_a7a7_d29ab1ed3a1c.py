from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fb684ff6-2756-54a8-a7a7-d29ab1ed3a1c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__artichoke-layered-leaves/20260927T150142Z-thuan-mac-1/reference/artichoke_fb684ff6-2756-54a8-a7a7-d29ab1ed3a1c.svg'
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
    icon_id = 'artichoke-layered-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'artichoke', 'vegetable')

    def build(self) -> None:
        # artichoke: globe of pointed scales. Outer outline = left and right scales curling to up-pointing tips
        # and a tall top scale between deep notches; a pointed front scale rises from the base; seams from the
        # notches down to the front scale's flanks make the second row; box stem below.
        _path(self, "bud", (16, 36), [('c', (10, 34), (8, 29), (8, 24)),        # left scale belly
                                      ('c', (8, 21), (8, 19), (9, 16)),         # left scale tip
                                      ('c', (12, 16), (14, 16.5), (17, 18)),    # into left notch
                                      ('c', (17, 12), (20, 7), (24, 4)),        # top scale tip
                                      ('c', (28, 7), (31, 12), (31, 18)),
                                      ('c', (34, 16.5), (36, 16), (39, 16)),
                                      ('c', (40, 19), (40, 21), (40, 24)),
                                      ('c', (40, 29), (38, 34), (32, 36)),
                                      (28, 36), (20, 36), (16, 36)], True)
        _path(self, "front", (16, 36), [('c', (16, 31), (17, 28), (18, 26)), ('c', (20, 23), (22, 21), (24, 18)),
                                        ('c', (26, 21), (28, 23), (30, 26)), ('c', (31, 28), (32, 31), (32, 36))])
        self.add_line("seam-l", (17, 18), (18, 26))
        self.add_line("seam-r", (31, 18), (30, 26))
        _path(self, "stem", (20, 36), [(20, 44), (28, 44), (28, 36)])
        for p in ("front", "stem", "seam-l", "seam-r"):
            self.relate("connect", p, "bud")
        self.relate("connect", "seam-l", "front")
        self.relate("connect", "seam-r", "front")
