from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ebba6b28-aad4-41af-8355-36c8928b07d0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bucket-with-draped-cleaning-cloth/20260927T142733Z-thuan-mac-1/reference/cleaning bucket cloth_ebba6b28-aad4-41af-8355-36c8928b07d0.svg'
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
    icon_id = 'bucket-with-draped-cleaning-cloth'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bucket', 'cloth', 'cleaning', 'rag', 'rim', 'household', 'pail')

    def build(self) -> None:
        # Cloth draped over the left of the rim: rounded top-left corner, a
        # concave right edge that folds over the rim, and one fold line. The rim
        # band runs right with a round end; the tapered pail hangs below.
        _path(self, 'cloth', (12, 6), [
            (27, 6),
            ('c', (26, 9), (25.5, 11), (25, 14)),
            ('c', (24, 20), (23, 26), (27, 32)),
            (16, 32), (14, 32), (10, 32),
            ((6, 28), 4, 4, True),
            (6, 12),
            ((12, 6), 6, 6, True),
        ], closed=True)
        _path(self, 'rim', (27, 6), [(38, 6), ((38, 14), 4, 4, True), (25, 14)])
        _path(self, 'pail', (38, 14), [(36, 38), ((32, 42), 4, 4, True), (18, 42), ((14, 38), 4, 4, True), (14, 32)])
        self.add_line('fold', (14, 20), (16, 32))
        self.relate('connect', 'cloth', 'rim')
        self.relate('connect', 'rim', 'pail')
        self.relate('connect', 'cloth', 'pail')
        self.relate('connect', 'cloth', 'fold')
