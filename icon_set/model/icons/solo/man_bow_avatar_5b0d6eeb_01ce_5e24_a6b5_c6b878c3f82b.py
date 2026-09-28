from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b0d6eeb-01ce-5e24-a6b5-c6b878c3f82b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-bow-avatar/20260926T175624Z-thuan-mac-1/reference/man bow_5b0d6eeb-01ce-5e24-a6b5-c6b878c3f82b.svg'
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
    icon_id = 'man-bow-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'bow', 'portrait', 'bust')

    def build(self) -> None:
        # Tall rounded head (r4 crown corners, r8 circular jaw) crossed by a
        # full-width hat-band line, touching a flat collar line whose ends are
        # the corners of a wide bow tie (two triangles crossing at a knot); the
        # rounded shoulders leave from the same corners.
        # Reference: human_ref/user.svg bust; supplied man-bow drawing.
        _path(self, 'head', (16, 13), [(16, 8), ((20, 4), 4, 4, True), (28, 4), ((32, 8), 4, 4, True),
                                      (32, 13), (32, 16), ((16, 16), 8, 8, True), (16, 13)], True)
        _path(self, 'band', (8, 13), [(16, 13), (32, 13), (40, 13)])
        self.relate('connect', 'head', 'band')
        _path(self, 'body', (8, 44), [('c', (8, 36), (9, 30), (12, 28)), (24, 28), (36, 28),
                                      ('c', (39, 30), (40, 36), (40, 44))],
              ids={1: 'body-top', 2: 'body-top-right'})
        self.relate('connect', 'head', 'body')
        _path(self, 'bow', (12, 28), [(24, 35), (36, 28), (32, 40), (24, 35), (16, 40), (12, 28)])
        self.relate('connect', 'bow', 'body')
