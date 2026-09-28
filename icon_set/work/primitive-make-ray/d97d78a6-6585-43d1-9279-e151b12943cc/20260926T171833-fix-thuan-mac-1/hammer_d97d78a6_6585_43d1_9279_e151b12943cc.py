from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd97d78a6-6585-43d1-9279-e151b12943cc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hammer-interface-essential/20260926T171707Z-thuan-mac-1/reference/hammer_d97d78a6-6585-43d1-9279-e151b12943cc.svg'
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
    icon_id = 'hammer-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('hammer', 'interface-essential')

    def build(self) -> None:
        # Axis frame: the handle runs along v=(1,1); the head is a block across it, u=(1,-1).
        # Head centre P, half-length a along u, half-thickness b along v; the handle leaves
        # the middle of the lower face at a right angle and runs to the corner (42,42).
        px, py, a, b = 19, 19, 9, 4
        corner = lambda su, sv: (px + su * a + sv * b, py - su * a + sv * b)
        socket = (px + b, py + b)
        self.add_line('head-top', corner(-1, -1), corner(1, -1))
        self.add_line('head-right', corner(1, -1), corner(1, 1))
        self.add_line('head-face-upper', corner(1, 1), socket)
        self.add_line('head-face-lower', socket, corner(-1, 1))
        self.add_line('head-left', corner(-1, 1), corner(-1, -1))
        self.add_contour('head', 'head-top', 'head-right', 'head-face-upper', 'head-face-lower', 'head-left', closed=True)
        self.add_line('handle', socket, (42, 42))
        self.relate('connect', 'head', 'handle')
