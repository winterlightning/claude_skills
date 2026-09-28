from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bdca2a7c-183f-49ac-8b41-214cea119125'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__angled-toothbrush-with-long-handle/20260927T141159Z-thuan-mac-1/reference/body care toothbrush_bdca2a7c-183f-49ac-8b41-214cea119125.svg'
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
    icon_id = 'angled-toothbrush-with-long-handle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angled', 'toothbrush', 'with', 'long', 'handle')

    def build(self) -> None:
        # Toothbrush on the 45-degree axis x+y=52 (reference: long diagonal handle, bristle head at the
        # upper right). Straight handle from (12,40) on r20 into the head, which ends at (40,12) on r20;
        # three bristle tufts rise perpendicular from the head, 8.49 apart (6,-6), each (-6,-6) long.
        pts = [(12, 40), (24, 28), (30, 22), (36, 16), (40, 12)]
        names = []
        for i in range(4):
            n = f"stick-{i}"; self.add_line(n, pts[i], pts[i + 1]); names.append(n)
        for i in range(3):
            self.relate("connect", names[i], names[i + 1])
        for j, p in enumerate(pts[1:4]):
            n = f"bristle-{j}"
            self.add_line(n, p, (p[0] - 6, p[1] - 6))
            self.relate("connect", n, names[j]); self.relate("connect", n, names[j + 1])
