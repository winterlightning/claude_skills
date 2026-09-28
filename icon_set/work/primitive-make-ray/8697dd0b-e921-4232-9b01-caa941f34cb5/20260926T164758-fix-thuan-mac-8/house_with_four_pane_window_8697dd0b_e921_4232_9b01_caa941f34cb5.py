from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8697dd0b-e921-4232-9b01-caa941f34cb5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-with-four-pane-window/20260926T164653Z-thuan-mac/reference/work from home office_8697dd0b-e921-4232-9b01-caa941f34cb5.svg'
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
    icon_id = 'house-with-four-pane-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: house with a four-pane window as in the reference, on SQUARE
        # (6..42): a 1:2 gable roof from the eaves (6,15)/(42,15) up to the apex
        # (24,6), overhanging walls at x 8/40 down to a floor on y=42; a short
        # chimney stroke rising from the right roof slope at x=34; a 16x16
        # window (x 16..32, y 18..34, r3 corners so it clears the roof by 8)
        # split by a cross into four 8x8 panes. The window's straight sides are
        # their own contours (corners separate) so the exact 8 gaps to the walls
        # and floor certify. Mirrored about x=24 except the chimney.
        _path(self, 'roof', (6, 15), [(8, 14), (24, 6), (34, 11), (40, 14), (42, 15)])
        self.add_line('left-wall', (8, 14), (8, 42))
        self.add_line('floor', (8, 42), (40, 42))
        self.add_line('right-wall', (40, 42), (40, 14))
        for a, b in (('roof', 'left-wall'), ('left-wall', 'floor'), ('floor', 'right-wall'), ('right-wall', 'roof')):
            self.relate('connect', a, b)
        self.add_line('chimney', (34, 11), (34, 6))
        self.relate('connect', 'roof', 'chimney')
        _path(self, 'win-top', (19, 18), [(24, 18), (29, 18)])
        _path(self, 'win-right', (32, 21), [(32, 26), (32, 31)])
        _path(self, 'win-bottom', (29, 34), [(24, 34), (19, 34)])
        _path(self, 'win-left', (16, 31), [(16, 26), (16, 21)])
        _path(self, 'corner-tr', (29, 18), [((32, 21), 3, 3, True)])
        _path(self, 'corner-br', (32, 31), [((29, 34), 3, 3, True)])
        _path(self, 'corner-bl', (19, 34), [((16, 31), 3, 3, True)])
        _path(self, 'corner-tl', (16, 21), [((19, 18), 3, 3, True)])
        ring = ('win-top', 'corner-tr', 'win-right', 'corner-br', 'win-bottom', 'corner-bl', 'win-left', 'corner-tl')
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate('connect', a, b)
        self.add_line('mullion', (24, 18), (24, 34))
        self.add_line('transom', (16, 26), (32, 26))
        for side in ('win-top', 'win-bottom'):
            self.relate('connect', 'mullion', side)
        for side in ('win-left', 'win-right'):
            self.relate('connect', 'transom', side)
        self.relate('connect', 'mullion', 'transom')
