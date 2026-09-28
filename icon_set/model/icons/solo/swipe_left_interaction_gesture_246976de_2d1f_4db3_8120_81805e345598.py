from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '246976de-2d1f-4db3-8120-81805e345598'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__swipe-left-interaction-gesture/20260926T164653Z-thuan-mac/reference/gesture tap swipe left_246976de-2d1f-4db3-8120-81805e345598.svg'
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


class Drawing(Solo48):
    icon_id = 'swipe-left-interaction-gesture'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('capsule', 'arrow', 'left')

    def build(self) -> None:
        # Plan: swipe-left gesture as in the reference, on HRECT_L (x 4..44,
        # y 8..40): a tall fingertip stadium on the right (x 24..44, r10 caps,
        # y 8..40) and a left-pointing arrow in the upper half (y=18): tip
        # (4,18), 45-degree head arms to (10,12)/(10,24) and a shaft to x=16,
        # exactly 8 from the stadium's left side (kept a standalone line so the
        # straight-to-straight gap certifies).
        self.add_line('finger-left', (24, 30), (24, 18))
        _path(self, 'finger', (24, 18), [((34, 8), 10, 10, True), ((44, 18), 10, 10, True), (44, 30),
                                         ((34, 40), 10, 10, True), ((24, 30), 10, 10, True)])
        self.relate('connect', 'finger-left', 'finger')
        self.add_line('arrow-shaft', (4, 18), (16, 18))
        _path(self, 'arrow-head', (10, 12), [(4, 18), (10, 24)])
        self.relate('connect', 'arrow-shaft', 'arrow-head')
