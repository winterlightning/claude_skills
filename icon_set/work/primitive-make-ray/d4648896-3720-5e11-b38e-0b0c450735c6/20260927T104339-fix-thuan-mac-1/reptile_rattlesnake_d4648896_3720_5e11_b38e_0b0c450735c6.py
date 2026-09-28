from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd4648896-3720-5e11-b38e-0b0c450735c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rattlesnake/20260927T104205Z-thuan-mac-1/reference/reptile rattlesnake_d4648896-3720-5e11-b38e-0b0c450735c6.svg'
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
    icon_id = 'rattlesnake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('rattlesnake', 'snake', 'rattle', 'reptile', 'slither', 'venom', 'desert', 'serpent')

    def build(self) -> None:
        # Plan (reference layout): an upright S-winding snake. The tail rises on
        # the left (x=10) into a segmented rattle - an 8-wide rounded rattle
        # (r4 cap about (10,10), tapering into the tail at (10,30)) split by one
        # band at y=18 - reaching the top edge. The body drops into a U (r6
        # about (16,34)), climbs to an arch (r7 about (29,16)) and comes down the
        # right side into a broad viper head pointing down (widest at the back,
        # x=30..42, rounded snout at (36,38)) with a tongue flicking down to the
        # floor. Body pieces are separate primitives so 8-unit gaps certify.
        _path(self, "rattle", (6, 26), [(6, 10), ((14, 10), 4, 4, True), (14, 26), (10, 30), (6, 26)], True)
        self.add_line("rattle-band", (6, 18), (14, 18))
        self.add_line("tail", (10, 30), (10, 34))
        self.add_arc("coil-bottom", (10, 34), (22, 34), radius_x=6, radius_y=6, sweep=False)
        self.add_line("body-rise", (22, 34), (22, 16))
        self.add_arc("coil-top", (22, 16), (36, 16), radius_x=7, radius_y=7, sweep=True)
        self.add_line("neck", (36, 16), (36, 24))
        _smooth(self, "head", [(36, 24), (40, 25), (42, 30), (40, 35), (36, 38), (32, 35), (30, 30), (32, 25)])
        self.add_line("tongue", (36, 38), (36, 42))
        chain = ["rattle", "tail", "coil-bottom", "body-rise", "coil-top", "neck", "head"]
        for a, b in zip(chain, chain[1:]):
            self.relate("connect", a, b)
        self.relate("connect", "tongue", "head")
        self.relate("connect", "rattle-band", "rattle")
