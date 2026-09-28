from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '49b5e4e8-1776-4137-8537-56f05c3dec41'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-pointing-at-map-board/20260927T133650Z-thuan-mac-1/reference/trekking map_49b5e4e8-1776-4137-8537-56f05c3dec41.svg'
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
    icon_id = 'person-pointing-at-map-board'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('map', 'trekking', 'route', 'board', 'briefing', 'person', 'guide', 'planning', 'outdoors-batch-03')

    def build(self) -> None:
        # Presenter pointing at a map board, as in the reference: a user-style bust at the lower left
        # (round head exactly 8 above round shoulders) whose arm reaches up to a tall board standing
        # on a leg at the right, the board showing a winding route that crosses the map from edge to
        # edge. The board edges are standalone lines so the head's 8-unit margin certifies.
        _circle(self, "head", 11, 21, 5)
        _path(self, "body", (6, 42), [(6, 38), ((10, 34), 4, 4, True), (12, 34), ((16, 38), 4, 4, True), (16, 42)])
        self.add_line("arm", (16, 38), (24, 30))
        self.add_line("board-l", (24, 30), (24, 21))
        self.add_line("board-l2", (24, 21), (24, 6))
        self.add_line("board-t", (24, 6), (42, 6))
        self.add_line("board-r", (42, 6), (42, 15))
        self.add_line("board-r2", (42, 15), (42, 30))
        self.add_line("board-b1", (42, 30), (33, 30))
        self.add_line("board-b2", (33, 30), (24, 30))
        self.add_line("stand", (33, 30), (33, 42))
        self.add_bezier("route", (24, 21), ((34, 21), (32, 15), (42, 15)))
        for a, b in (("body", "arm"), ("arm", "board-l"), ("arm", "board-b2"), ("board-l", "board-l2"), ("board-l2", "board-t"),
                     ("board-t", "board-r"), ("board-r", "board-r2"), ("board-r2", "board-b1"), ("board-b1", "board-b2"),
                     ("board-b2", "board-l"), ("board-b1", "stand"), ("board-b2", "stand"), ("route", "board-l"),
                     ("route", "board-l2"), ("route", "board-r"), ("route", "board-r2")):
            self.relate("connect", a, b)
