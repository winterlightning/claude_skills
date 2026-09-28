from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f875f41c-ce24-4c42-b39e-be3923b31ffa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-swimmer-avatar/20260926T175624Z-thuan-mac-1/reference/man swimmer_f875f41c-ce24-4c42-b39e-be3923b31ffa.svg'
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
    icon_id = 'man-swimmer-avatar-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'swimmer', 'portrait', 'bust')

    def build(self) -> None:
        # Swimmer: an r13 head bobbing in water.  A swim-cap line crosses the
        # head at its 12-5-13 points; goggle lenses hang from it, closed by the
        # head outline and two inner cubics down to the lower 12-5-13 points.
        # The circular jaw touches the flat crest of the water line (the body
        # contact), which rolls away in one wave on each side.
        # Reference: human_ref/user.svg head/contact rule; supplied swimmer.
        _path(self, 'head', (12, 16), [((24, 8), 13, 13, True), ((36, 16), 13, 13, True), ((37, 21), 13, 13, True),
                                      ((36, 26), 13, 13, True), ((12, 26), 13, 13, True), ((11, 21), 13, 13, True),
                                      ((12, 16), 13, 13, True)], True)
        self.add_line('cap', (12, 16), (36, 16))
        _path(self, 'lens-left', (20, 16), [('c', (20, 21), (17, 25), (12, 26))])
        _path(self, 'lens-right', (28, 16), [('c', (28, 21), (31, 25), (36, 26))])
        for part in ('cap', 'lens-left', 'lens-right'):
            self.relate('connect', 'head', part)
        self.relate('connect', 'cap', 'lens-left')
        self.relate('connect', 'cap', 'lens-right')
        _path(self, 'water', (4, 40), [('c', (6, 40), (7, 38), (9, 38)), ('c', (11, 38), (12, 40), (14, 40)),
                                       ('c', (16, 40), (16, 38), (18, 38)), (24, 38), (30, 38),
                                       ('c', (32, 38), (32, 40), (34, 40)), ('c', (36, 40), (37, 38), (39, 38)),
                                       ('c', (41, 38), (42, 40), (44, 40))], ids={3: 'body-top', 4: 'body-top-right'})
        self.relate('connect', 'head', 'water')
