from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dc9fedbc-8058-5e3a-8a22-47f1828e3da5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wide-ski-goggles/20260927T104205Z-thuan-mac-1/reference/glasses ski_dc9fedbc-8058-5e3a-8a22-47f1828e3da5.svg'
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
    icon_id = 'wide-ski-goggles'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('goggles', 'ski goggles', 'snow', 'ski', 'eyewear', 'winter', 'sports', 'visor')

    def build(self) -> None:
        # Plan: one wide, low wraparound visor lens, mirrored about x=24 (about
        # 40 x 18 like the reference). Rounded ends are r9 half-circles about
        # (13,24)/(35,24), so only their outer points touch radius 20; the top
        # edge runs straight and tangent into both ends; the bottom edge has a
        # rounded nose-bridge notch (r6 semicircle about (24,33)).
        _path(self, "lens", (13, 15), [(35, 15),
                                       ((35, 33), 9, 9, True),
                                       (30, 33),
                                       ((18, 33), 6, 6, False),
                                       (13, 33),
                                       ((13, 15), 9, 9, True)], True)
