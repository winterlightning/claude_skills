from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9aef2fa3-a180-440e-8f69-2d6f71b6f2b3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gpon-splitter-1/20260926T160438Z-thuan-mac-2/reference/gpon splitter 1_9aef2fa3-a180-440e-8f69-2d6f71b6f2b3.svg'
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
    icon_id = 'gpon-splitter-1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'networks'
    categories = ('primitives', 'networks')
    aliases = ()
    keywords = ('gpon', 'splitter', 'networks')

    def build(self) -> None:
        # Plan: GPON splitter on SQUARE, mirrored about y=24. The input line enters
        # from the left edge into the splitter hub (r5 ring about (20,24)). Three
        # outputs leave the hub from its grid points: two diagonals to the top-right
        # and bottom-right corners, each ending in an open right-angle arrowhead
        # along the edges (7-long arms), and a horizontal output to the right edge
        # ending in an open chevron. Arrowheads stay 8+ apart.
        _path(self, 'hub', (20, 19), [
            ((24, 21), 5, 5, True), ((25, 24), 5, 5, True), ((24, 27), 5, 5, True),
            ((20, 29), 5, 5, True), ((15, 24), 5, 5, True), ((20, 19), 5, 5, True),
        ], closed=True)
        self.add_line('input', (6, 24), (15, 24))
        self.add_line('out-up', (24, 21), (42, 6))
        self.add_line('out-mid', (25, 24), (42, 24))
        self.add_line('out-down', (24, 27), (42, 42))
        _path(self, 'head-up', (35, 6), [(42, 6), (42, 13)])
        _path(self, 'head-mid', (38, 20), [(42, 24), (38, 28)])
        _path(self, 'head-down', (35, 42), [(42, 42), (42, 35)])
        for o, h in (('out-up', 'head-up'), ('out-mid', 'head-mid'), ('out-down', 'head-down')):
            self.relate('connect', 'hub', o)
            self.relate('connect', o, h)
        self.relate('connect', 'hub', 'input')
