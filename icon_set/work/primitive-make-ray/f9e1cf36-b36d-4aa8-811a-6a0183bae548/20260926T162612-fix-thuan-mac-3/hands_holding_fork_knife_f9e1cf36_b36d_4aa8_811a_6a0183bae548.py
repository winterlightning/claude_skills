from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f9e1cf36-b36d-4aa8-811a-6a0183bae548'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-holding-fork-knife/20260926T162509Z-thuan-mac/reference/fork and khife_f9e1cf36-b36d-4aa8-811a-6a0183bae548.svg'
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
    icon_id = 'hands-holding-fork-knife'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hands', 'holding', 'fork', 'knife')

    def build(self) -> None:
        # Plan: two raised fists, fork in the left and knife in the right, as in
        # the reference, on HRECT_L (x 4..44, y 8..40). Each fist (x0..x0+16,
        # top y=26) has r4 top corners, a straight outer side and an inner side
        # that tapers in toward the wrist; 8 apart. Each handle enters the fist
        # top and runs down its middle to y=34, as in the reference.
        # Fork: three tines 8 apart (x 4, 12, 20) whose outer pair closes in an
        # r8 U; the centre tine continues as the handle.
        # Knife: spine on the fist centre line (x=36) from the tip into the fist;
        # the blade hangs on its left: an r8 quarter curve from the tip to
        # (28,16), a short straight edge and a heel line back to the spine.
        for side, x0 in (('left', 4), ('right', 28)):
            _path(self, f'{side}-fist', (x0, 40), [
                (x0, 30), ((x0 + 4, 26), 4, 4, True), (x0 + 8, 26), (x0 + 12, 26),
                ((x0 + 16, 30), 4, 4, True), (x0 + 16, 34), (x0 + 13, 40),
            ])
        _path(self, 'fork', (4, 8), [(4, 10), ((12, 18), 8, 8, False), ((20, 10), 8, 8, False), (20, 8)])
        _path(self, 'fork-shaft', (12, 8), [(12, 18), (12, 26), (12, 34)])
        self.relate('connect', 'fork', 'fork-shaft')
        self.relate('connect', 'fork-shaft', 'left-fist')
        _path(self, 'knife', (36, 34), [(36, 26), (36, 18), (36, 8), ((28, 16), 8, 8, False), (28, 18), (36, 18)])
        self.relate('connect', 'knife', 'right-fist')
