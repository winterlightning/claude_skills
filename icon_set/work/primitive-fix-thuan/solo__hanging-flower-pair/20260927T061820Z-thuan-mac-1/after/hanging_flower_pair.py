from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '76e15d0e-0c43-40b6-ba38-ae2903117c14'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hanging-flower-pair/20260927T061820Z-thuan-mac-1/reference/hanging flowers_76e15d0e-0c43-40b6-ba38-ae2903117c14.svg'
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
    icon_id = 'hanging-flower-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('flower', 'hanging', 'petals', 'stem', 'leaf', 'botanical', 'decor')

    def build(self) -> None:
        # two stems hanging from the top edge. Left: a long stem with a pointed leaf (two-cubic lens)
        # branching down-left where the stem bends right and continues to the bottom. Right: a short
        # stem ending in a hanging tulip bell -- r8 dome, straight sides, two r4 petals opening down.
        self.add_line("stem-left", (14, 6), (14, 26))
        _path(self, "stem-left-low", (14, 26), [('c', (14, 30), (18, 30), (18, 36)), (18, 42)])
        _path(self, "leaf", (14, 26), [('c', (8, 26), (6, 30), (6, 38)), ('c', (12, 38), (14, 32), (14, 26))], closed=True)
        self.relate("connect", "stem-left", "stem-left-low")
        self.relate("connect", "leaf", "stem-left"); self.relate("connect", "leaf", "stem-left-low")
        self.add_line("stem-right", (34, 6), (34, 18))
        _path(self, "bell", (26, 32), [(26, 26), ((34, 18), 8, 8, True), ((42, 26), 8, 8, True), (42, 32),
                                       ((34, 32), 4, 4, True), ((26, 32), 4, 4, True)], closed=True)
        self.relate("connect", "stem-right", "bell")
