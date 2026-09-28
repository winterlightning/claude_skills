from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9de328f1-e686-4c93-955f-3977dc939c3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airplane-side-profile-single-wing/20260927T141159Z-thuan-mac-1/reference/airfield_9de328f1-e686-4c93-955f-3977dc939c3a.svg'
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
    icon_id = 'airplane-side-profile-single-wing'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('airplane', 'side', 'profile', 'single', 'wing')

    def build(self) -> None:
        # Airliner in side profile, nose to the right (reference: long fuselage with a round nose, a
        # swept tail fin rising at the back, one swept wing hanging below the middle).
        # Fuselage 10 tall (y18-28) with an r5 nose; the fin rises from the top line to y=8 at the
        # tail and the tail underside sweeps up; the wing is a 45-degree parallelogram
        # (edges x+y=60 and x+y=48, 8.49 apart) hanging from the belly.
        _path(self, "body", (39, 18), [((39, 28), 5, 5, True), (32, 28), (20, 28), (14, 28), (4, 22),
                                        (4, 8), (8, 8), (16, 18), (39, 18)], closed=True)
        _path(self, "wing", (32, 28), [(20, 40), (8, 40), (20, 28)])
        self.relate("connect", "wing", "body")
