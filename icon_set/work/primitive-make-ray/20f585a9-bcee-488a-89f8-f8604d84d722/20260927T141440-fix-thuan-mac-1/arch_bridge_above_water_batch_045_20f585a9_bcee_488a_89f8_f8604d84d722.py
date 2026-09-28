from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '20f585a9-bcee-488a-89f8-f8604d84d722'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arch-bridge-above-water-batch-045/20260927T141159Z-thuan-mac-1/reference/ford_20f585a9-bcee-488a-89f8-f8604d84d722.svg'
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
    icon_id = 'arch-bridge-above-water-batch-045'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bridge', 'arch', 'water', 'waves', 'span', 'crossing', 'structure')

    def build(self) -> None:
        # Arch bridge above water (reference: one thick semicircular stone arch with flat feet over two
        # rows of waves). Arch band: outer r14 and inner r6 semicircles about (24,20), the flat feet
        # on y20 as standalone lines so their exact 8-unit gap to the wave crests certifies.
        # Waves: two in-phase Lucide-style rows (knots every 12, controls +-8/3 so crests sit exactly
        # 2 off the baseline; troughs under the arch feet, a crest under the opening) on y30 and y40, 10 apart.
        self.add_arc("arch-outer", (10, 20), (38, 20), radius_x=14, radius_y=14, sweep=True)
        self.add_line("foot-right", (38, 20), (30, 20))
        self.add_arc("arch-inner", (30, 20), (18, 20), radius_x=6, radius_y=6, sweep=False)
        self.add_line("foot-left", (18, 20), (10, 20))
        for a in ("arch-outer", "arch-inner"):
            self.relate("connect", a, "foot-right"); self.relate("connect", a, "foot-left")
        k = 8 / 3
        for n, y in (("wave-1", 30), ("wave-2", 40)):
            steps, x = [], 6
            for i in range(3):
                d = k if i % 2 == 0 else -k
                steps.append(('c', (x + 4, y + d), (x + 8, y + d), (x + 12, y)))
                x += 12
            _path(self, n, (6, y), steps)
