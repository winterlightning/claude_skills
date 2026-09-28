from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7a06c938-aa06-5aee-b5c4-6a27a848e3b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hanging-ball-cat-toy/20260926T162509Z-thuan-mac/reference/cat toy_7a06c938-aa06-5aee-b5c4-6a27a848e3b5.svg'
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
    icon_id = 'hanging-ball-cat-toy'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('cat-toy', 'ball', 'string', 'hanging', 'feather', 'play', 'pet')

    def build(self) -> None:
        # Plan: cat toy ball hanging from a string, as in the reference, on
        # VRECT_M (x 10..38, y 4..44). An r10 ball about (20,28); a small
        # rounded cap (8x8, r3 corners) rests on the ball's top point; the string
        # rises from the cap to y=4. A tassel hangs from the ball's lower right:
        # its inner edge drops from the rim bottom (20,38) and sweeps along y=44,
        # its outer edge leaves the rim at the 6-8-10 point (28,34), and both
        # meet at the tip (38,44).
        _path(self, 'ball', (20, 18), [
            ((30, 28), 10, 10, True), ((28, 34), 10, 10, True), ((20, 38), 10, 10, True),
            ((10, 28), 10, 10, True), ((20, 18), 10, 10, True),
        ], closed=True)
        _path(self, 'cap', (20, 18), [
            (24, 18), (24, 13), ((21, 10), 3, 3, False), (20, 10), (19, 10), ((16, 13), 3, 3, False), (16, 18), (20, 18),
        ], closed=True)
        self.add_line('string', (20, 10), (20, 4))
        _path(self, 'tassel', (20, 38), [
            ('c', (20, 42), (22, 44), (26, 44)), (38, 44), ('c', (33, 42), (29, 39), (28, 34)),
        ])
        for a, b in (('ball', 'cap'), ('cap', 'string'), ('ball', 'tassel')):
            self.relate('connect', a, b)
