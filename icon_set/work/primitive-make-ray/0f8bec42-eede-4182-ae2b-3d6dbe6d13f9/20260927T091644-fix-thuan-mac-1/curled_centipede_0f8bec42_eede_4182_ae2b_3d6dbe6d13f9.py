from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0f8bec42-eede-4182-ae2b-3d6dbe6d13f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curled-centipede/20260927T091421Z-thuan-mac-1/reference/insect centipede_0f8bec42-eede-4182-ae2b-3d6dbe6d13f9.svg'
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


class Drawing(Solo48):
    icon_id = 'curled-centipede'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('centipede', 'grub', 'larva', 'bug', 'legs', 'crawl', 'microbe', 'insect')

    def build(self) -> None:
        # Curled centipede seen from above: a thick C-shaped body (smooth loop through integer knots)
        # with the round head at the upper left. Two antennae fan out from the head; legs leave knots
        # on the outer curve and sweep back toward the tail (about 45 degrees off the normal), like the
        # reference's curved legs. Antenna and leg tips set the SQUARE extremes.
        def loop(name, pts):
            n = len(pts)
            members = []
            for i in range(n):
                p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
                c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
                c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
                self.add_bezier(f"{name}-{i + 1}", p1, (c1, c2, p2)); members.append(f"{name}-{i + 1}")
            self.add_contour(name, *members, closed=True)

        knots = [(14, 12), (24, 12), (32, 16), (36, 24), (36, 32), (31, 37), (24, 36), (22, 30), (19, 25),
                 (13, 24), (11, 18)]
        loop("body", knots)
        legs = {"antenna-a": ((14, 12), (12, 6)), "antenna-b": ((11, 18), (6, 16)),
                "leg-1": ((24, 12), (30, 8)), "leg-2": ((32, 16), (38, 15)), "leg-3": ((36, 24), (42, 27)),
                "leg-4": ((36, 32), (39, 38)), "leg-5": ((31, 37), (28, 42))}
        for name, (a, b) in legs.items():
            self.add_line(name, a, b)
            self.relate("connect", "body", name)
