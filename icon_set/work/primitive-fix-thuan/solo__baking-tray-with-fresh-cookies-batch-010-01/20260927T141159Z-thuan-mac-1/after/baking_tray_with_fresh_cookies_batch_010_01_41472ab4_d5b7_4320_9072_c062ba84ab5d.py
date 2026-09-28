from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '41472ab4-d5b7-4320-9072-c062ba84ab5d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baking-tray-with-fresh-cookies-batch-010-01/20260927T141159Z-thuan-mac-1/reference/cooking baking tray oven_41472ab4-d5b7-4320-9072-c062ba84ab5d.svg'
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
    icon_id = 'baking-tray-with-fresh-cookies-batch-010-01'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('baking', 'tray', 'with', 'fresh', 'cookies')

    def build(self) -> None:
        # Baking tray with fresh cookies (reference: a tray of round cookies just out of the oven with
        # steam rising). Tray: a flat pan line on y40 with upturned rims to (4,37)/(44,37). Cookies:
        # three r3 rings about (10,27), (24,27), (38,27), 8 apart and 10 above the tray. Steam: an
        # S-wisp above each cookie from y16 up to y8.
        _path(self, "tray", (4, 37), [(7, 40), (41, 40), (44, 37)])
        for i, x in enumerate((10, 24, 38)):
            _circle(self, f"cookie-{i}", x, 27, 3)
            _path(self, f"steam-{i}", (x, 16), [('c', (x - 2, 13), (x + 2, 11), (x, 8))])
