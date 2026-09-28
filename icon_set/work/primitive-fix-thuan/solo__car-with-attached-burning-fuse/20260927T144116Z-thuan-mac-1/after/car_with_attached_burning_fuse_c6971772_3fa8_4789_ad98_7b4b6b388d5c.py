from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c6971772-3fa8-4789-ad98-7b4b6b388d5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-with-attached-burning-fuse/20260927T144116Z-thuan-mac-1/reference/car bomb 2_c6971772-3fa8-4789-ad98-7b4b6b388d5c.svg'
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
    icon_id = 'car-with-attached-burning-fuse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'with', 'attached', 'burning', 'fuse')

    def build(self) -> None:
        # Car bomb: a side-view car (same build as the car-wash hatchback)
        # with a fuse wire rising from the rear of the roof, curling over the
        # roof toward the front and ending short of a four-point spark.
        _circle(self, 'wheel-front', 17, 39, 3)
        _circle(self, 'wheel-rear', 31, 39, 3)
        _path(self, 'body', (14, 39), [
            (9, 39), ((6, 36), 3, 3, True), (6, 30), ((9, 27), 3, 3, True), (12, 27),
            ('c', (14, 21), (15, 18), (19, 18)), (29, 18), ('c', (33, 18), (34, 21), (36, 27)),
            (39, 27), ((42, 30), 3, 3, True), (42, 36), ((39, 39), 3, 3, True), (34, 39),
        ])
        self.add_line('belt', (12, 27), (36, 27))
        self.add_line('under', (20, 39), (28, 39))
        for part in ('wheel-front', 'wheel-rear', 'belt'):
            self.relate('connect', 'body', part)
        self.relate('connect', 'under', 'wheel-front')
        self.relate('connect', 'under', 'wheel-rear')
        _path(self, 'fuse', (29, 18), [(29, 13), ((25, 9), 4, 4, False), (21, 9)])
        self.relate('connect', 'body', 'fuse')
        # Spark: three short rays fanning out from the fuse tip (shared
        # node), 34 degrees apart, like the reference's burst.
        self.add_line('spark-up', (21, 9), (16, 6))
        self.add_line('spark-left', (21, 9), (15, 9))
        self.add_line('spark-down', (21, 9), (16, 12))
        for ray in ('spark-up', 'spark-left', 'spark-down'):
            self.relate('connect', 'fuse', ray)
