from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a2ad7637-7eca-4441-9689-f3b3c74e0207'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-one-logo/20260926T171651Z-thuan-mac-1/reference/google one logo_a2ad7637-7eca-4441-9689-f3b3c74e0207.svg'
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
    icon_id = 'google-one-logo'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google', 'one', 'logo', 'logos')

    def build(self) -> None:
        # Plan: the Google One mark, an outlined rounded "1", on VRECT_M
        # (x 10..38, y 4..44). One closed contour: a 12-wide stem with an r6
        # quarter cap at the top right and an r6 semicircle at the bottom,
        # and the flag arm (10 wide, 3-4-5 slope) running down-left from the
        # top to a round r5 knob whose 3-4-5 tangent points keep both arm
        # edges tangent. A cubic eases the arm's upper edge into the top.
        _path(self, 'one', (32, 4), [((38, 10), 6, 6, True), (38, 38), ((26, 38), 6, 6, True, True), (26, 18), (18, 24),
                                     ((12, 16), 5, 5, True, True), (24, 7), ('c', (27.2, 4.6), (30, 4), (32, 4))], True)
