from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8c2721b6-de44-4f42-9cf3-339b3c542f59'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__soccer-player-avatar/20260926T180600Z-thuan-mac-1/reference/soccer player_8c2721b6-de44-4f42-9cf3-339b3c542f59.svg'
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
    icon_id = 'soccer-player-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('soccer', 'player', 'portrait', 'bust')

    def build(self) -> None:
        # Soccer player (reference): r10 head with swept fringe at upper right,
        # shoulders touching the chin, and a ball (r8 rim; the pentagon
        # pattern needs r18, so it is omitted) held in front of the torso at lower left; the torso side rises
        # from the ball's right edge.
        _path(self, 'head', (30, 24), [((20, 14), 10, 10, True), ((30, 4), 10, 10, True), ((36, 6), 10, 10, True),
                                       ((40, 14), 10, 10, True), ((30, 24), 10, 10, True)], True)
        self.add_bezier('fringe', (20, 14), ((26, 14), (33, 11), (36, 6)))
        self.relate('connect', 'head', 'fringe')
        _circle(self, 'ball', 16, 36, 8)
        _path(self, 'body', (24, 36), [(24, 32), ((28, 28), 4, 4, True), (30, 28), (32, 28), ((40, 36), 8, 8, True), (40, 44)])
        self.relate('connect', 'body', 'ball')
        self.relate('connect', 'body', 'head')
