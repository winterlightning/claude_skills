from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd95930dd-4c35-5a2d-ad85-faa5674be25f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-steamed-dumpling/20260927T080808Z-thuan-mac-1/reference/chef gear dumplings_d95930dd-4c35-5a2d-ad85-faa5674be25f.svg'
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
    icon_id = 'three-steamed-dumpling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('three', 'steamed', 'dumpling')

    def build(self) -> None:
        # Plan: pyramid of three steamed buns as in the reference. Front buns: r10 circle domes
        # about (16,32)/(32,32) with flattened cubic bottoms (base y42); they cross on the lattice
        # points (24,26) (circles) and (24,37) (shared bottom knot); the right bun is in front.
        # The back bun is a dome (r13 crown arc through (19,7)/(29,7), cubic flanks) hidden
        # behind the front domes at the lattice points (10,24)/(38,24); two curved pleat seams
        # hang from its crown knots as in the reference.
        _path(self, "bun-right", (32, 22), [((38, 24), 10, 10, True), ((42, 32), 10, 10, True),
                                            ('c', (42, 39), (39, 42), (32, 42)),
                                            ('c', (28, 42), (26, 39), (24, 37)),
                                            ('c', (23, 36), (22, 34), (22, 32)),
                                            ((24, 26), 10, 10, True), ((32, 22), 10, 10, True)], closed=True)
        _path(self, "bun-left", (24, 26), [((16, 22), 10, 10, False), ((10, 24), 10, 10, False),
                                           ((6, 32), 10, 10, False), ('c', (6, 39), (9, 42), (16, 42)),
                                           ('c', (20, 42), (22, 39), (24, 37))])
        _path(self, "bun-back", (10, 24), [('c', (10, 15), (14, 10), (19, 7)), ((24, 6), 13, 13, True),
                                           ((29, 7), 13, 13, True), ('c', (34, 10), (38, 15), (38, 24))])
        self.relate("connect", "bun-left-1", "bun-right-6", "bun-right-7")
        self.relate("connect", "bun-left-5", "bun-right-4", "bun-right-5")
        self.relate("connect", "bun-back-1", "bun-left-2", "bun-left-3")
        self.relate("connect", "bun-back-4", "bun-right-1", "bun-right-2")
        self.add_arc("pleat-left", (19, 7), (20, 15), radius_x=13, radius_y=13, sweep=False)
        self.add_arc("pleat-right", (29, 7), (28, 15), radius_x=13, radius_y=13, sweep=True)
        self.relate("connect", "pleat-left", "bun-back-1", "bun-back-2")
        self.relate("connect", "pleat-right", "bun-back-3", "bun-back-4")
