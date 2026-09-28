from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47659966-6bcc-4338-8851-46f26e9cca27'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-axe/20260927T055730Z-thuan-mac-1/reference/tools axe hold_47659966-6bcc-4338-8851-46f26e9cca27.svg'
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
    icon_id = 'hand-holding-axe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('axe', 'hand', 'holding', 'grip', 'chop', 'lumberjack', 'wood', 'tool')

    def build(self) -> None:
        # 45-degree axis frame along the handle: ab(a, b) = (18 + a + b, 30 - a + b);
        # a runs up the handle toward the head, b runs across it toward the wrist (down-right)
        ab = lambda a, b: (18 + a + b, 30 - a + b)
        # fist: two r6 knuckles on the upper-left side, flat top and bottom, arm leaving down-right
        _path(self, "hand", ab(-6, 6), [          # (18,42): lower arm edge at the bottom
            ab(-6, 4),                          # (16,40)
            ab(-6, -6),                         # (6,30) bottom of the fist
            (ab(0, -6), 6, 6, True),            # (12,24) knuckle (r6: leftmost point is the endpoint)
            (ab(6, -6), 6, 6, True),            # (18,18) knuckle
            ab(6, 4),                           # (28,28) top of the fist
            ab(6, 18),                          # (42,42) upper arm edge
        ])
        # the handle passes behind the fist: it shows below and above it
        self.add_line("handle-low", ab(-6, 0), ab(-10, 0))      # (12,36) -> (8,40)
        self.add_line("handle-high", ab(6, 0), ab(13, 0))       # (24,24) -> (31,17)
        self.relate("connect", "hand", "handle-low"); self.relate("connect", "hand", "handle-high")
        # axe head: back on the handle (8.5) flaring to a 14-long cutting edge 8.5 away
        self.add_polyline("head", (28, 14), (32, 6), (42, 16), (34, 20), (31, 17), closed=True)
        self.relate("connect", "head", "handle-high")
