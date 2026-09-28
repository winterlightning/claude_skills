from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '768a65f3-6f4f-518d-9a22-1dbd59a651ca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__human-upper-body-768a65f3/20260926T164653Z-thuan-mac/reference/massage map body_768a65f3-6f4f-518d-9a22-1dbd59a651ca.svg'
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
    icon_id = 'human-upper-body-768a65f3'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('human', 'upper', 'body')

    def build(self) -> None:
        # Plan: upper-body map as in the reference (human_ref/user.svg bust
        # vocabulary), on VRECT_L (x 8..40, y 4..44): a large r8 head (4..20)
        # exactly 8 above a flat shoulder top (y=28, a standalone line so the gap
        # certifies), r10 rounded shoulders into straight sides that run open to
        # the bottom edge, and the two arm-separation lines of the reference
        # (x 17/31, y 38..44), 9 clear of the shoulder curves. Mirrored about
        # x=24.
        _circle(self, 'head', 24, 12, 8)
        self.add_line('shoulder-top', (18, 28), (30, 28))
        _path(self, 'left-shoulder', (8, 44), [(8, 38), ((18, 28), 10, 10, True)])
        _path(self, 'right-shoulder', (30, 28), [((40, 38), 10, 10, True), (40, 44)])
        self.relate('connect', 'shoulder-top', 'left-shoulder')
        self.relate('connect', 'shoulder-top', 'right-shoulder')
        self.add_line('left-arm', (17, 38), (17, 44))
        self.add_line('right-arm', (31, 38), (31, 44))
