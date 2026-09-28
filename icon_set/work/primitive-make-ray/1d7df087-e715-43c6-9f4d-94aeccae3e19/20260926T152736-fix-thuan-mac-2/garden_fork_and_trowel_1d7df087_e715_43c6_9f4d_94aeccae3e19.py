from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1d7df087-e715-43c6-9f4d-94aeccae3e19'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__garden-fork-and-trowel/20260926T152555Z-thuan-mac-2/reference/gardening tools_1d7df087-e715-43c6-9f4d-94aeccae3e19.svg'
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
    icon_id = 'garden-fork-and-trowel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('garden', 'fork', 'and', 'trowel')

    def build(self) -> None:
        # Plan: garden fork (left) and trowel (right) side by side on SQUARE, as in
        # the reference. Each tool: head on top, an 8-long neck, and a capsule handle
        # (8 wide, r4 caps) from y=28 to the bottom edge.
        # Fork: outer tines x=6/22 run into an r8 U (bottom y=20); the middle tine
        # x=14 runs straight down through the U into the neck. Tines 8 apart.
        # Trowel: pointed blade 12 wide (two cubics to the apex (36,6)) over a
        # flat base y=20, 8+ clear of the fork.
        def handle(name, cx):
            _path(self, name, (cx, 28), [
                ((cx + 4, 32), 4, 4, True), (cx + 4, 38), ((cx, 42), 4, 4, True),
                ((cx - 4, 38), 4, 4, True), (cx - 4, 32), ((cx, 28), 4, 4, True),
            ], closed=True)
        _path(self, 'fork-u', (6, 6), [(6, 12), ((14, 20), 8, 8, False), ((22, 12), 8, 8, False), (22, 6)])
        _path(self, 'fork-shaft', (14, 6), [(14, 20), (14, 28)])
        handle('fork-handle', 14)
        _path(self, 'trowel-blade', (30, 20), [
            ('c', (30, 13), (32.5, 8), (36, 6)),
            ('c', (39.5, 8), (42, 13), (42, 20)),
            (36, 20), (30, 20),
        ], closed=True)
        self.add_line('trowel-neck', (36, 20), (36, 28))
        handle('trowel-handle', 36)
        self.relate('connect', 'fork-u', 'fork-shaft')
        self.relate('connect', 'fork-shaft', 'fork-handle')
        self.relate('connect', 'trowel-blade', 'trowel-neck')
        self.relate('connect', 'trowel-neck', 'trowel-handle')
