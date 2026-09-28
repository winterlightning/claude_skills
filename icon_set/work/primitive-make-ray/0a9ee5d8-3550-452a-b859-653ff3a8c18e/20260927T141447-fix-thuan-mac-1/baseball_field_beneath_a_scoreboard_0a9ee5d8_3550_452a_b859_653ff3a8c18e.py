from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0a9ee5d8-3550-452a-b859-653ff3a8c18e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baseball-field-beneath-a-scoreboard/20260927T141159Z-thuan-mac-1/reference/baseball score_0a9ee5d8-3550-452a-b859-653ff3a8c18e.svg'
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
    icon_id = 'baseball-field-beneath-a-scoreboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('baseball', 'field', 'scoreboard')

    def build(self) -> None:
        # Baseball field beneath a scoreboard (reference: a wide scoreboard standing on posts at the
        # top of the stadium, the fan-shaped field below with home plate at its point).
        # Field: a true sector about home plate (24,42), r20, its foul lines running out along
        # 3-4-5 directions to (8,30)/(40,30), the outfield arc cresting at y22. The infield
        # diamond: home, first (32,36), second (24,31), third (16,36), bases on the foul lines.
        # Scoreboard: a wide board x6-42, y6-14 on two posts standing on the outfield arc at the
        # lattice points (12,26)/(36,26).
        _path(self, "field", (24, 42), [(16, 36), (8, 30), ((12, 26), 20, 20, True), ((36, 26), 20, 20, True),
                                        ((40, 30), 20, 20, True), (32, 36), (24, 42)], closed=True)
        _path(self, "infield", (16, 36), [(24, 31), (32, 36)])
        self.relate("connect", "infield", "field")
        _path(self, "board", (6, 6), [(42, 6), (42, 14), (36, 14), (12, 14), (6, 14), (6, 6)], closed=True)
        self.add_line("post-left", (12, 14), (12, 26))
        self.add_line("post-right", (36, 14), (36, 26))
        for p in ("post-left", "post-right"):
            self.relate("connect", p, "board"); self.relate("connect", p, "field")
