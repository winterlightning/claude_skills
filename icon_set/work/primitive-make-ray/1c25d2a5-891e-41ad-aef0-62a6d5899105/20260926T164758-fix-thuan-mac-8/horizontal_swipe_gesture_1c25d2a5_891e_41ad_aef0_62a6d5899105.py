from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1c25d2a5-891e-41ad-aef0-62a6d5899105'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-swipe-gesture/20260926T164653Z-thuan-mac/reference/gesture tap swipe horizontal_1c25d2a5-891e-41ad-aef0-62a6d5899105.svg'
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


class Drawing(Solo48):
    icon_id = 'horizontal-swipe-gesture'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('touch', 'capsule', 'left', 'right')

    def build(self) -> None:
        # Plan: horizontal (left-right) swipe gesture as in the reference, on
        # HRECT_L (x 4..44, y 8..40): a tall fingertip stadium in the centre
        # (x 19..29, r5 caps, y 8..40) flanked by two outward arrows on y=24,
        # each a tip at the canvas side with 45-degree head arms (5 long) and a
        # shaft that stops 8 short of the stadium side (standalone side lines so
        # the straight-to-straight gaps certify). Mirrored about x=24.
        self.add_line('finger-left', (19, 35), (19, 13))
        self.add_line('finger-right', (29, 13), (29, 35))
        _path(self, 'finger-top', (19, 13), [((24, 8), 5, 5, True), ((29, 13), 5, 5, True)])
        _path(self, 'finger-bottom', (29, 35), [((24, 40), 5, 5, True), ((19, 35), 5, 5, True)])
        for a, b in (('finger-left', 'finger-top'), ('finger-top', 'finger-right'), ('finger-right', 'finger-bottom'),
                     ('finger-bottom', 'finger-left')):
            self.relate('connect', a, b)
        for side, tip, arm, inner in (('left', 4, 9, 11), ('right', 44, 39, 37)):
            self.add_line(f'{side}-shaft', (tip, 24), (inner, 24))
            _path(self, f'{side}-head', (arm, 19), [(tip, 24), (arm, 29)])
            self.relate('connect', f'{side}-shaft', f'{side}-head')
