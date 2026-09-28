from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f303a1ac-9387-43d7-9138-b3796c7f22b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__imgur-logo/20260927T070905Z-thuan-mac-1/reference/imgur logo_f303a1ac-9387-43d7-9138-b3796c7f22b5.svg'
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
    icon_id = 'imgur-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('imgur', 'images', 'sharing', 'arrow', 'logo', 'brand', 'upload')

    def build(self) -> None:
        # Imgur logo as in the reference: a square badge with the top-left and bottom-right corners
        # cut at 45 degrees and r4 rounded top-right/bottom-left corners, holding an OUTLINED arrow
        # pointing up-right. Arrow axis x+y=48, tip (33,15); shaft sides x+y=41/55 (9.9 apart);
        # r5 tail cap with a 3-4-5 chord (7,7) about (20,28).
        _path(self, "badge", (17, 6), [(38, 6), ((42, 10), 4, 4, True), (42, 31), (31, 42), (10, 42),
                                       ((6, 38), 4, 4, True), (6, 17), (17, 6)], closed=True)
        _path(self, "arrow", (20, 15), [(33, 15), (33, 28), (30, 25), (24, 31), ((17, 24), 5, 5, True),
                                        (23, 18), (20, 15)], closed=True)
