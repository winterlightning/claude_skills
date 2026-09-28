from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c2a943ba-cacb-5a74-a64e-f06eba88f8ee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__front-loading-washing-machine-c2a943ba/20260926T152555Z-thuan-mac-2/reference/laundry machine_c2a943ba-cacb-5a74-a64e-f06eba88f8ee.svg'
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
    icon_id = 'front-loading-washing-machine-c2a943ba'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('front', 'loading', 'washing', 'machine', 'c2a943ba')

    def build(self) -> None:
        # Plan: front-loading washer on VRECT_L (8..40 x 4..44). Body = box with square
        # centerline corners (round joins paint the ink corners), so every inner mark
        # can sit exactly 8 from a wall straight-to-straight. Control panel: a short
        # line top-left and a knob dot top-right, 8 from the top and side walls.
        # Porthole: an r7 circle on the axis x=24, 9 clear of the walls.
        self.add_polyline('body', (8, 4), (40, 4), (40, 44), (8, 44), closed=True)
        self.add_line('panel', (16, 12), (20, 12))
        self.add_dot('knob', (32, 12))
        _circle(self, 'door', 24, 28, 7)
