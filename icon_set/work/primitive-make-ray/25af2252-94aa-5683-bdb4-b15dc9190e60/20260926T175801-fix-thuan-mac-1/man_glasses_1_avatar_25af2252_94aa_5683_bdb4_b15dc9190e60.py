from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '25af2252-94aa-5683-bdb4-b15dc9190e60'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-glasses-1-avatar/20260926T175624Z-thuan-mac-1/reference/man glasses_25af2252-94aa-5683-bdb4-b15dc9190e60.svg'
AUTHOR = "claude-opus-5-5"


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
    icon_id = 'man-glasses-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'glasses', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Man with round glasses: a broad bald dome (two cubics from the lens
        # rims to the crown) and a circular r11 jaw, joined through two r5
        # lenses that form the sides of the face at the temples (3-4-5 rim
        # points keep every join on the grid); a bridge joins the lenses and
        # the jaw touches a rounded bust.
        # Reference: human_ref/user.svg shoulders; supplied glasses drawing.
        for name, cx in (('lens-left', 16), ('lens-right', 32)):
            s = -1 if cx < 24 else 1
            _path(self, name, (cx, 12), [((cx + 3 * s, 13), 5, 5, s > 0), ((cx + 5 * s, 17), 5, 5, s > 0),
                                         ((cx + 3 * s, 21), 5, 5, s > 0), ((cx, 22), 5, 5, s > 0),
                                         ((cx - 5 * s, 17), 5, 5, s > 0), ((cx, 12), 5, 5, s > 0)], True)
        _path(self, 'crown', (13, 13), [('c', (13, 8), (18, 4), (24, 4)), ('c', (30, 4), (35, 8), (35, 13))])
        self.add_arc('jaw', (35, 21), (13, 21), radius_x=11, sweep=True)
        self.add_line('bridge', (21, 17), (27, 17))
        for part in ('crown', 'jaw', 'bridge'):
            self.relate('connect', part, 'lens-left')
            self.relate('connect', part, 'lens-right')
        _path(self, 'body', (8, 44), [((18, 36), 10, 8, True), (24, 36), (30, 36), ((40, 44), 10, 8, True)],
              ids={1: 'body-top', 2: 'body-top-right'})
        self.relate('connect', 'jaw', 'body')
