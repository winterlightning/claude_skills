from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bb435dbc-a51b-4359-a39d-23ed29b0bbb3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__all-might-head-batch-086/20260927T141159Z-thuan-mac-1/reference/my hero acadiamia allmight_bb435dbc-a51b-4359-a39d-23ed29b0bbb3.svg'
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
    icon_id = 'all-might-head-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('all', 'might', 'head')

    def build(self) -> None:
        # All Might head (reference: square-jawed face under a hairline, two big curved hair blades
        # rising from the hairline into a V and flaring out to tall tips at the top corners, the
        # crown peeking out between them; shadowed eyes). Face: sides x8/x40, r6 temple and jaw
        # corners, hairline y22, chin y42. Blades: base (14,22)-(24,22) and (24,22)-(34,22) sharing
        # the V point (24,22); their inner edges run straight to (19,14)/(29,14), where an r5 crown
        # dome joins them, then curve out to the tips (6,6)/(42,6); outer edges bow outward.
        _path(self, "face", (8, 28), [(8, 36), ((14, 42), 6, 6, False), (34, 42), ((40, 36), 6, 6, False),
                                      (40, 28), ((34, 22), 6, 6, False), (24, 22), (14, 22),
                                      ((8, 28), 6, 6, False)], closed=True)
        self.add_line("blade-l-v", (24, 22), (19, 14))
        self.add_bezier("blade-l-in", (19, 14), ((15, 10), (11, 7), (6, 6)))
        self.add_bezier("blade-l-out", (6, 6), ((6, 13), (9, 19), (14, 22)))
        self.add_contour("blade-l", "blade-l-v", "blade-l-in", "blade-l-out")
        self.add_line("blade-r-v", (24, 22), (29, 14))
        self.add_bezier("blade-r-in", (29, 14), ((33, 10), (37, 7), (42, 6)))
        self.add_bezier("blade-r-out", (42, 6), ((42, 13), (39, 19), (34, 22)))
        self.add_contour("blade-r", "blade-r-v", "blade-r-in", "blade-r-out")
        self.add_arc("crown", (19, 14), (29, 14), radius_x=5, radius_y=5, sweep=True)
        self.relate("connect", "blade-l", "face"); self.relate("connect", "blade-r", "face")
        self.relate("connect", "blade-l", "blade-r")
        self.relate("connect", "crown", "blade-l"); self.relate("connect", "crown", "blade-r")
        # shadowed eyes, tilted down toward the nose
        self.add_line("eye-l", (17, 31), (20, 32))
        self.add_line("eye-r", (28, 32), (31, 31))
