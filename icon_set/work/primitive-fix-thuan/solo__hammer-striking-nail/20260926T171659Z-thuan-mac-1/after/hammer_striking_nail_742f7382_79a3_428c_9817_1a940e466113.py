from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '742f7382-79a3-428c-9817-1a940e466113'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hammer-striking-nail/20260926T171659Z-thuan-mac-1/reference/hardware hammer nail hit_742f7382-79a3-428c-9817-1a940e466113.svg'
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
    icon_id = 'hammer-striking-nail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('hammer', 'nail', 'hit', 'strike', 'impact', 'hardware', 'construction', 'tool')

    def build(self) -> None:
        # Hammer striking a nail on SQUARE, mirrored about x=28 below the head:
        # an upright bullet-shaped head (22..34, rounded top r6 reaching y=6,
        # flat striking face at y=26); the handle is a tube 8 wide (y=14..22)
        # with an r4 butt at x=6, joining the head's left side.  The nail
        # (head at y=35, shank to 42) sits 9 below the face, flanked by two
        # impact streaks spraying down and out.
        _path(self, 'head', (22, 14), [(22, 12), ((34, 12), 6, 6, True), (34, 26), (22, 26), (22, 22)])
        _path(self, 'head-join', (22, 22), [(22, 14)])
        _path(self, 'handle', (22, 14), [(10, 14), ((10, 22), 4, 4, False), (22, 22)])
        self.relate('connect', 'head', 'head-join')
        self.relate('connect', 'handle', 'head-join')
        self.relate('connect', 'handle', 'head')
        self.add_line('nail-head', (24, 35), (32, 35))
        self.add_line('nail-shank', (28, 35), (28, 42))
        self.relate('connect', 'nail-head', 'nail-shank')
        self.add_line('impact-left', (14, 38), (18, 42))
        self.add_line('impact-right', (42, 38), (38, 42))
