from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6d77d3d0-6bee-4348-b189-fc45ae2e6768'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__finger-tapping-projected-panel/20260927T032037Z-thuan-mac-1/reference/virtual tap finger_6d77d3d0-6bee-4348-b189-fc45ae2e6768.svg'
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
    icon_id = 'finger-tapping-projected-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('tap', 'finger', 'hand', 'projection', 'virtual', 'touch', 'panel')

    def build(self) -> None:
        # Plan: projected panel arch (top y6, short sides to y14); a pointing
        # hand with an open wrist (index up, tip r4 at (22,19), one lower knuckle
        # bump, thumb out left); the projector is a base line y42 with an r4 lens
        # bump, 8+ below the wrist ends.
        _path(self, 'panel', (6, 14), [(6, 10), ((10, 6), 4, 4, True), (38, 6), ((42, 10), 4, 4, True), (42, 14)])
        _path(self, 'hand', (18, 31), [(18, 27), (18, 19), ((22, 15), 4, 4, True), ((26, 19), 4, 4, True),
                                       (26, 25), ((30, 21), 4, 4, True), ((34, 25), 4, 4, True), (34, 31)])
        self.add_line('thumb', (18, 27), (12, 21))
        self.relate('connect', 'thumb', 'hand')
        _path(self, 'projector', (10, 42), [(20, 42), ((24, 38), 4, 4, True), ((28, 42), 4, 4, True), (38, 42)])
