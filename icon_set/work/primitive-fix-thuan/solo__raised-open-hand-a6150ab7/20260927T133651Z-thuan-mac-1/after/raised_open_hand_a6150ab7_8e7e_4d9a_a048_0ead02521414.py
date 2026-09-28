from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a6150ab7-8e7e-4d9a-a048-0ead02521414'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__raised-open-hand-a6150ab7/20260927T133651Z-thuan-mac-1/reference/hand 1_a6150ab7-8e7e-4d9a-a048-0ead02521414.svg'
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
    icon_id = 'raised-open-hand-a6150ab7'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('raised', 'open', 'hand')

    def build(self) -> None:
        # Raised open hand: three 8-wide fingers (middle tallest, outer finger lowest, r4 tips, slits down to
        # y=26) and a thumb lobe that clearly juts out on the left, over a rounded palm heel.
        _path(self, "hand", (18, 24), [(18, 14), ((26, 14), 4, 4, True), (26, 10), ((34, 10), 4, 4, True), (34, 16),
                                       ((42, 16), 4, 4, True), (42, 32), ((32, 42), 10, 10, True), (26, 42),
                                       ('c', (18, 42), (14, 32), (10, 32)), ((10, 24), 4, 4, True), (18, 24)], True)
        self.add_line("slit-index", (26, 14), (26, 26))
        self.add_line("slit-middle", (34, 16), (34, 26))
        self.relate("connect", "slit-index", "hand-2", "hand-3")
        self.relate("connect", "slit-middle", "hand-5", "hand-6")
