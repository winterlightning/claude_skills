from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0f991193-97ec-4f8a-8e42-4f4bca8b2446'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-clown-1-avatar/20260926T175624Z-thuan-mac-1/reference/man clown_0f991193-97ec-4f8a-8e42-4f4bca8b2446.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False, ids=None):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = (ids or {}).get(i, f"{name}-{i + 1}")
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
    icon_id = 'man-clown-1-avatar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'clown', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Clown head (no body, as in the reference): a small rounded top hat on a
        # hair line, one big puff of hair on each side (rx8 ry9 half-ellipses),
        # a two-scallop fringe and a circular r10 jaw, plus a round nose.
        _path(self, 'hat', (18, 14), [(18, 9), ((21, 6), 3, 3, True), (27, 6), ((30, 9), 3, 3, True), (30, 14)])
        _path(self, 'hairline', (14, 14), [(18, 14), (30, 14), (34, 14)])
        self.relate('connect', 'hat', 'hairline')
        _path(self, 'face', (14, 22), [(14, 32), ((34, 32), 10, 10, False), (34, 22)])
        _path(self, 'puff-left', (14, 14), [((14, 32), 8, 9, False)])
        _path(self, 'puff-right', (34, 14), [((34, 32), 8, 9, True)])
        _path(self, 'fringe', (14, 22), [((24, 22), 5, 3, False), ((34, 22), 5, 3, False)])
        for a, b in (('hairline', 'puff-left'), ('hairline', 'puff-right'), ('puff-left', 'face'),
                     ('puff-right', 'face'), ('fringe', 'face')):
            self.relate('connect', a, b)
        self.add_dot('nose', (24, 33))
