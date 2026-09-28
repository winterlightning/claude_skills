from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '787783f6-901a-45ae-a710-84ce8a165876'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-feeding-bottle-batch-019-06/20260927T150142Z-thuan-mac-1/reference/drop bottle_787783f6-901a-45ae-a710-84ce8a165876.svg'
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
    icon_id = 'baby-feeding-bottle-batch-019-06'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('baby', 'bottle', 'feeding', 'nipple', 'teat', 'milk', 'infant', 'nursery')

    def build(self) -> None:
        # baby bottle: r4 nipple flaring onto rounded shoulders, cap seam, taller body with rounded base
        _path(self, "bottle", (14, 26), [(14, 22), ((18, 18), 4, 4, True), ('c', (19.5, 18), (20, 15.5), (20, 13)),
                                         (20, 8), ((28, 8), 4, 4, True), (28, 13), ('c', (28, 15.5), (28.5, 18), (30, 18)),
                                         ((34, 22), 4, 4, True), (34, 26), (34, 38), ((30, 42), 4, 4, True), (18, 42),
                                         ((14, 38), 4, 4, True), (14, 26)], True)
        self.add_line("seam", (14, 26), (34, 26))
        self.relate("connect", "seam", "bottle")
