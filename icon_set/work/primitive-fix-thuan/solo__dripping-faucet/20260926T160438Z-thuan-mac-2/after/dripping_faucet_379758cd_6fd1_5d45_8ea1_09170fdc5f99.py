from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '379758cd-6fd1-5d45-8ea1-09170fdc5f99'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dripping-faucet/20260926T160438Z-thuan-mac-2/reference/water fountain sink_379758cd-6fd1-5d45-8ea1-09170fdc5f99.svg'
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
    icon_id = 'dripping-faucet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('dripping', 'faucet')

    def build(self) -> None:
        # Plan: water fountain faucet on VRECT_L (8..40 x 4..44). The pipe is an
        # inverted U drawn as a tube of two walls 8 apart: it rises at the right
        # (walls x=32/40), runs left along the top (y=4/12, r4 corners) and ends in a
        # downward spout 8 wide (x 10..18, mouth at y=16). A teardrop (r4 bulb)
        # falls 9 below the spout; the base is one stroke along the bottom edge
        # that also closes the pipe foot.
        _path(self, 'pipe', (32, 44), [
            (32, 16), ((28, 12), 4, 4, False), (18, 12), (18, 16), (10, 16), (10, 8),
            ((14, 4), 4, 4, True), (36, 4), ((40, 8), 4, 4, True), (40, 44),
        ])
        self.add_polyline('base', (8, 44), (32, 44), (40, 44))
        _path(self, 'drop', (14, 25), [
            ('c', (16, 27), (18, 29), (18, 31)),
            ((14, 35), 4, 4, True), ((10, 31), 4, 4, True),
            ('c', (10, 29), (12, 27), (14, 25)),
        ], closed=True)
        self.relate('connect', 'pipe', 'base')
