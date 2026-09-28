from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2313dc03-036c-434f-9815-674483c280e0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-beside-tree-under-cloud/20260927T061820Z-thuan-mac-1/reference/house nature_2313dc03-036c-434f-9815-674483c280e0.svg'
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
    icon_id = 'house-beside-tree-under-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'beside', 'tree', 'under', 'cloud')

    def build(self) -> None:
        # landscape on a ground line: a two-lobed cloud (r4 lobe about (8,14), r5 lobe about (13,13),
        # flat base) at the top left, a gabled house below it, and a tall teardrop tree (two-cubic
        # sides, pointed top) on a trunk at the right, as in the reference.
        _path(self, "cloud", (8, 18), [((4, 14), 4, 4, True), ((8, 10), 4, 4, True), (9, 10),
                                       ((13, 8), 5, 5, True), ((18, 13), 5, 5, True), ((13, 18), 5, 5, True), (8, 18)],
              closed=True)
        _path(self, "house", (4, 40), [(4, 34), (13, 27), (22, 34), (22, 40)])
        _path(self, "crown", (38, 8), [('c', (40, 12), (44, 18), (44, 24)), ('c', (44, 28), (41, 30), (38, 30)),
                                       ('c', (35, 30), (32, 28), (32, 24)), ('c', (32, 18), (36, 12), (38, 8))], closed=True)
        self.add_line("trunk", (38, 30), (38, 40))
        _path(self, "ground", (4, 40), [(22, 40), (38, 40), (44, 40)])
        for a, b in (("house", "ground"), ("trunk", "crown"), ("trunk", "ground")):
            self.relate("connect", a, b)
