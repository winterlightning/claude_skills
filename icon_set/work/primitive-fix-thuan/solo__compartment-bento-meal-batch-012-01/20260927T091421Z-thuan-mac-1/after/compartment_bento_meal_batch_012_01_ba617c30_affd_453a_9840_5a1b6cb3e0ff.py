from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ba617c30-affd-453a-9840-5a1b6cb3e0ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__compartment-bento-meal-batch-012-01/20260927T091421Z-thuan-mac-1/reference/japanese launchbox bento ekiben_ba617c30-affd-453a-9840-5a1b6cb3e0ff.svg'
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
    icon_id = 'compartment-bento-meal-batch-012-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('bento', 'lunchbox', 'meal', 'food', 'compartment', 'japanese')

    def build(self) -> None:
        # Bento box laid out like the reference: a tall left compartment (x 6..24) with an umeboshi
        # dot on the rice, and a right side split in two. Broccoli florets (r5 + r4 lobes) heap over the
        # top-right edge and reach the SQUARE top; two r5 rice balls, meeting the walls at their upper
        # 3-4-5 points, form the top of the lower-right compartment.
        _path(self, "box", (24, 11), [(6, 11), (6, 42), (42, 42), (42, 11),
                                      ((38, 7), 4, 4, False), ((34, 11), 4, 4, False), ((29, 6), 5, 5, False),
                                      ((24, 11), 5, 5, False)], True)
        self.add_line("divider", (24, 11), (24, 42))
        _path(self, "rice-balls", (24, 24), [((28, 22), 5, 5, True), ((32, 24), 5, 5, True), (34, 24),
                                             ((38, 22), 5, 5, True), ((42, 24), 5, 5, True)])
        self.add_dot("plum", (15, 26))
        self.relate("connect", "box", "divider")
        self.relate("connect", "divider", "rice-balls")
        self.relate("connect", "box", "rice-balls")
