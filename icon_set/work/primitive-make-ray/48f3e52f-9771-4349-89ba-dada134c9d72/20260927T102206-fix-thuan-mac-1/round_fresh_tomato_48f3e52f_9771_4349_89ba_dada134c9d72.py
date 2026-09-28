from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '48f3e52f-9771-4349-89ba-dada134c9d72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-fresh-tomato/20260927T101542Z-thuan-mac-1/reference/tomato_48f3e52f-9771-4349-89ba-dada134c9d72.svg'
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
    icon_id = 'round-fresh-tomato'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('round', 'fresh', 'tomato')

    def build(self) -> None:
        # Plan: wide round fruit (ellipse rx18 ry14 about (24,28)) with the calyx on
        # top: short stem plus two leaves curling out and down from the stem foot,
        # mirrored about x=24; a small shine arc inside the lower right.
        _path(self, "fruit", (24, 14), [((42, 28), 18, 14, True), ((24, 42), 18, 14, True),
                                        ((6, 28), 18, 14, True), ((24, 14), 18, 14, True)], True)
        self.add_line("stem", (24, 14), (24, 6))
        self.add_bezier("leaf-left", (24, 14), ((20, 9), (13, 7), (10, 11)))
        self.add_bezier("leaf-right", (24, 14), ((28, 9), (35, 7), (38, 11)))
        self.relate("connect", "stem", "fruit")
        self.relate("connect", "leaf-left", "fruit")
        self.relate("connect", "leaf-right", "fruit")
        self.relate("connect", "leaf-left", "stem")
        self.relate("connect", "leaf-right", "stem")
