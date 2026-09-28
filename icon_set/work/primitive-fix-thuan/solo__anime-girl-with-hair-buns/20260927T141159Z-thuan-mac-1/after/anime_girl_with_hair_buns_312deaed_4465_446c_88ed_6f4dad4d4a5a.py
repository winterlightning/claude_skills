from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '312deaed-4465-446c-88ed-6f4dad4d4a5a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__anime-girl-with-hair-buns/20260927T141159Z-thuan-mac-1/reference/sailormoon usagi_312deaed-4465-446c-88ed-6f4dad4d4a5a.svg'
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
    icon_id = 'anime-girl-with-hair-buns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('anime', 'girl', 'with', 'hair', 'buns')

    def build(self) -> None:
        # Anime girl with hair buns (reference: Sailor Moon style head: round buns on top of a domed
        # head of hair that falls down both sides to the bottom corners, the face set inside under a
        # fringe of two curls meeting in a V).
        # Hair: r5 bun lobes about (11,11)/(37,11) (three-quarter arcs from their bottom points), an
        # r10 crown arc about (24,17) between them, side locks curving from each bun's bottom out to
        # x6/x42 and falling straight to y42 (standalone lines so the 8-unit face gap certifies).
        # Face: fringe of two r5 curls about (19,27)/(29,27) meeting at (24,27), sides x14/x34,
        # r10 chin about (24,32) to y42.
        self.add_line("lock-left", (6, 42), (6, 24))
        _path(self, "hair", (6, 24), [('c', (6, 20), (8, 18), (11, 16)), ((16, 11), 5, 5, True, True),
                                      ((32, 11), 10, 10, True), ((37, 16), 5, 5, True, True),
                                      ('c', (40, 18), (42, 20), (42, 24))])
        self.add_line("lock-right", (42, 24), (42, 42))
        self.relate("connect", "lock-left", "hair"); self.relate("connect", "lock-right", "hair")
        _path(self, "face", (24, 27), [((14, 27), 5, 5, False), (14, 32), ((34, 32), 10, 10, False), (34, 27),
                                       ((24, 27), 5, 5, False)], closed=True)
