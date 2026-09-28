from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '293432b3-59da-44f7-9810-43c9f99bcef0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fuel-gauge-empty/20260926T152555Z-thuan-mac-2/reference/car dashboard e_293432b3-59da-44f7-9810-43c9f99bcef0.svg'
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
    icon_id = 'fuel-gauge-empty'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('fuel gauge', 'empty', 'fuel', 'gauge', 'dashboard', 'car', 'petrol', 'low fuel')

    def build(self) -> None:
        # Plan: fuel gauge on CIRCLE. Dial rim r20; everything inside stays within
        # radius ~11.3 of the centre (8.7+ clear of the rim). The "E" (empty) mark:
        # spine x=16 with three arms 8 apart (y=16,24,32) out to x=22. The needle
        # rises from its pivot (30,32) at lower left to the tip (35,21), 8+ clear of
        # the E, as in the reference.
        _circle(self, 'rim', 24, 24, 20)
        _path(self, 'letter-e', (22, 16), [(16, 16), (16, 24), (16, 32), (22, 32)])
        self.add_line('letter-e-arm', (16, 24), (22, 24))
        self.add_line('needle', (30, 32), (35, 21))
        self.relate('connect', 'letter-e', 'letter-e-arm')
