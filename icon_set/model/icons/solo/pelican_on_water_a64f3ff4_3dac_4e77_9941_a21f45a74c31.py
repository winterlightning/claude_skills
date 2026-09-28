from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a64f3ff4-3dac-4e77-9941-a21f45a74c31'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pelican-on-water/20260927T104205Z-thuan-mac-1/reference/pelican_a64f3ff4-3dac-4e77-9941-a21f45a74c31.svg'
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
    icon_id = 'pelican-on-water-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('pelican', 'water', 'bird', 'pouch', 'beak', 'sea', 'float', 'waterfowl')

    def build(self) -> None:
        # Plan (reference): a pelican floating on water, facing left. One closed
        # smooth silhouette: a long straight upper bill from the tip (6,18) up
        # to a round head (r6 about (27,12), crown on y=6); the back of the neck
        # curves down and turns smoothly into the back, ending at the tail tip on
        # x=42; the belly rounds under the body and sweeps forward as one long
        # curve that forms the chest and the deep throat pouch, back to the bill
        # tip. A lower-bill line from the tip separates the bill from the pouch.
        # Below, a Lucide-style water line (cubic knots every 9 on y=40,
        # extremes 38..42), a trough under the belly.
        _path(self, "pelican", (6, 18), [(21, 12),
                                         ((33, 12), 6, 6, True),
                                         ('c', (33, 17), (29, 19), (30, 23)),
                                         ('c', (30.5, 25), (36, 23), (42, 20)),
                                         ('c', (40, 27), (33, 29), (25, 29)),
                                         ('c', (15, 29), (8, 25), (6, 18))], True)
        self.add_line("lower-bill", (6, 18), (16, 20))
        self.relate("connect", "lower-bill", "pelican")
        k = 8 / 3
        steps = []
        for i, x in enumerate(range(6, 42, 9)):
            d = k if i % 2 == 0 else -k
            steps.append(('c', (x + 3, 40 + d), (x + 6, 40 + d), (x + 9, 40)))
        _path(self, "water", (6, 40), steps)
