from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7eb10cf4-5263-45f8-929d-49906b04ace0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cloud-with-moon-and-lightning/20260927T144116Z-thuan-mac-1/reference/weather night snow thunder_7eb10cf4-5263-45f8-929d-49906b04ace0.svg'
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
    icon_id = 'cloud-with-moon-and-lightning'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cloud', 'with', 'moon', 'and', 'lightning')

    def build(self) -> None:
        # Night thunderstorm: a cloud (r8 dome + r4 lobe on a flat base)
        # in front of a crescent moon that rises from the cloud's notch to the
        # top horn, bites back to a right horn and returns to the lobe
        # (Lucide cloud-moon build), with three lightning bolts beneath.
        _path(self, 'cloud', (14, 26), [
            ((6, 18), 8, 8, True), ((14, 10), 8, 8, True), ((22, 18), 8, 8, True),
            ('c', (23, 17), (25, 18), (27, 18)),
            ((31, 22), 4, 4, True), ((27, 26), 4, 4, True), (14, 26),
        ], closed=True)
        _path(self, 'moon', (22, 18), [
            ('c', (22, 11), (26, 6), (32, 6)),
            ('c', (31, 10), (35, 14), (42, 14)),
            ('c', (42, 19), (37, 22), (31, 22)),
        ])
        self.relate('connect', 'cloud', 'moon')
        # Each bolt: a slash down-left, a short step right, then a drop
        # down-right (the last leg leaves at more than 30 degrees from the
        # first, so the two legs never run parallel).
        for i, x in enumerate((9, 20, 31)):
            _path(self, f'bolt-{i + 1}', (x + 2, 34), [(x - 1, 38), (x + 2, 38), (x + 1, 42)])
