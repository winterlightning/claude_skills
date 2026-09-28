from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '14dea40b-c23a-4d0f-9235-bf861fd7d5ca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__icon-3d-box/20260926T164653Z-thuan-mac/reference/3d box_14dea40b-c23a-4d0f-9235-bf861fd7d5ca.svg'
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
    icon_id = 'icon-3d-box'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('3d', 'box', 'symbol')

    def build(self) -> None:
        # Plan: isometric cube as in the reference, on CIRCLE (radius 20 about
        # (24,24)): a near-regular pointy-top hexagon (24,4)/(41,14)/(41,34)/
        # (24,44)/(7,34)/(7,14) whose top and bottom vertices reach radius 20
        # (the side vertices sit at 19.7), with 10:17 (about 30 degree) edges,
        # and the three inner edges meeting at the near corner (24,24), parallel
        # to the outer ones. Mirrored about x=24.
        _path(self, 'cube', (24, 4), [(41, 14), (41, 34), (24, 44), (7, 34), (7, 14), (24, 4)], closed=True)
        _path(self, 'inner', (7, 14), [(24, 24), (41, 14)])
        self.add_line('near-edge', (24, 24), (24, 44))
        self.relate('connect', 'cube', 'inner')
        self.relate('connect', 'cube', 'near-edge')
        self.relate('connect', 'inner', 'near-edge')
