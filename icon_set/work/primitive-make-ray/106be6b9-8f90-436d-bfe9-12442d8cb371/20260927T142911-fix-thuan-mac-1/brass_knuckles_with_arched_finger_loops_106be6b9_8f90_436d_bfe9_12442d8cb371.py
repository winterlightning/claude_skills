from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '106be6b9-8f90-436d-bfe9-12442d8cb371'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brass-knuckles-with-arched-finger-loops/20260927T142727Z-thuan-mac-1/reference/tools knuckle_106be6b9-8f90-436d-bfe9-12442d8cb371.svg'
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
    icon_id = 'brass-knuckles-with-arched-finger-loops'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('brass', 'knuckles', 'with', 'arched', 'finger', 'loops')

    def build(self) -> None:
        # Brass knuckles, as in the reference: four round finger rings set in an arch (outer rings
        # dropped 6, each ring touching its neighbour at one lattice point), two posts from the outer
        # rings down to a rounded grip bar, and an open palm gap between the rings and the bar.
        # Mirrored about x=24; ring centres (11,17) (19,11) (29,11) (37,17), r5.
        def ring(name, c, pts):
            """Full r5 circle through the given boundary points (clockwise order), as arcs."""
            steps = [(p, 5, 5, True) for p in pts[1:]] + [(pts[0], 5, 5, True)]
            _path(self, name, pts[0], steps, True)

        ring("ring-1", (11, 17), [(15, 14), (16, 17), (8, 21), (6, 17), (11, 12)])
        ring("ring-2", (19, 11), [(24, 11), (19, 16), (15, 14), (14, 11), (19, 6)])
        ring("ring-3", (29, 11), [(29, 6), (34, 11), (33, 14), (29, 16), (24, 11)])
        ring("ring-4", (37, 17), [(37, 12), (42, 17), (40, 21), (32, 17), (33, 14)])
        self.add_line("post-left", (8, 21), (10, 34))
        self.add_line("post-right", (40, 21), (38, 34))
        _path(self, "bar", (10, 34), [(38, 34), ((38, 42), 4, 4, True), (10, 42), ((10, 34), 4, 4, True)], True)
        for a, b in (("ring-1", "ring-2"), ("ring-2", "ring-3"), ("ring-3", "ring-4"), ("post-left", "ring-1"),
                     ("post-right", "ring-4"), ("post-left", "bar"), ("post-right", "bar")):
            self.relate("connect", a, b)
