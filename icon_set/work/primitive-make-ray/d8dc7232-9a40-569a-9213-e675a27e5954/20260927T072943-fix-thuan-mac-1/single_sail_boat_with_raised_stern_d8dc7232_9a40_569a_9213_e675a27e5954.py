from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd8dc7232-9a40-569a-9213-e675a27e5954'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__single-sail-boat-with-raised-stern/20260927T072849Z-thuan-mac-1/reference/piracy ship_d8dc7232-9a40-569a-9213-e675a27e5954.svg'
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
    icon_id = 'single-sail-boat-with-raised-stern'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('boat', 'sailing', 'sail', 'mast', 'hull', 'nautical', 'vessel', 'ship')

    def build(self) -> None:
        # Square sail between two yards, both edges bellying left as in the
        # reference; the mast rises from the waist deck to the lower yard.
        _path(self, 'sail', (16, 6), [(34, 6), ('c', (30, 10), (30, 16), (34, 20)), (16, 20),
                                      ('c', (12, 16), (12, 10), (16, 6))], True)
        self.add_line('yard-top-l', (12, 6), (16, 6))
        self.add_line('yard-top-r', (34, 6), (38, 6))
        self.add_line('yard-bot-r', (34, 20), (38, 20))
        for n in ('yard-top-l', 'yard-top-r', 'yard-bot-r'):
            self.relate('connect', n, 'sail')
        self.add_line('mast', (24, 20), (24, 32))
        # Hull: sweeping bow at the left, low deck, raised stern castle.
        _path(self, 'hull', (6, 28), [(12, 32), (24, 32), (32, 32), (34, 28), (42, 28), (42, 34),
                                      ('c', (42, 38), (40, 42), (36, 42)), (20, 42), ('c', (12, 42), (8, 36), (6, 28))], True)
        self.relate('connect', 'mast', 'sail')
        self.relate('connect', 'mast', 'hull')
