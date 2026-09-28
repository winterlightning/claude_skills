from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8b3c753d-e676-4e1a-811c-69448f6e158f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__layout-with-left-sidebar-solo-b001-04/20260927T133651Z-thuan-mac-1/reference/sidebar dots left_8b3c753d-e676-4e1a-811c-69448f6e158f.svg'
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
    icon_id = 'layout-with-left-sidebar-solo-b001-04'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('layout', 'with', 'left', 'sidebar')

    def build(self) -> None:
        # Window frame with a dotted sidebar divider near the left edge (reference: dashes at x~15).
        # Straight walls are standalone lines joined to r4 corner arcs so the exact-8 dot gaps certify.
        self.add_line("wall-top", (8, 8), (40, 8))
        self.add_arc("corner-tr", (40, 8), (44, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line("wall-right", (44, 12), (44, 36))
        self.add_arc("corner-br", (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line("wall-bottom", (40, 40), (8, 40))
        self.add_arc("corner-bl", (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line("wall-left", (4, 36), (4, 12))
        self.add_arc("corner-tl", (4, 12), (8, 8), radius_x=4, radius_y=4, sweep=True)
        ring = ["wall-top", "corner-tr", "wall-right", "corner-br", "wall-bottom", "corner-bl", "wall-left", "corner-tl"]
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate("connect", a, b)
        for i, y in enumerate((16, 24, 32)):
            self.add_dot(f"sidebar-dot-{i + 1}", (14, y))
