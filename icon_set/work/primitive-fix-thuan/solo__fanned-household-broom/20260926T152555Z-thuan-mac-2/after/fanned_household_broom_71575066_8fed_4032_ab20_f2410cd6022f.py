from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '71575066-8fed-4032-ab20-f2410cd6022f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fanned-household-broom/20260926T152555Z-thuan-mac-2/reference/broom sweep handle_71575066-8fed-4032-ab20-f2410cd6022f.svg'
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
    icon_id = 'fanned-household-broom'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: broom on a diagonal. Handle axis d=(2,-3) from the ferrule top K to the
        # upper-right corner (42,6). Band B1-B2 runs along n=(3,2), perpendicular to the
        # handle; the domed ferrule is two cubics B1 -> K -> B2 with tangents along n at K.
        # The outer strands continue the ferrule sides tangentially (one smooth fan
        # outline); a middle strand fans from the band centre C. 11 apart at roots/tips.
        K, B1, C, B2 = (28, 22), (15, 22), (24, 28), (33, 34)
        _path(self, 'ferrule', B1, [
            ('c', (17.6, 18.1), (22.9, 18.6), K),
            ('c', (33.1, 25.4), (34.3, 30.1), B2),
            C,
            B1,
        ], closed=True)
        self.add_line('handle', K, (42, 6))
        self.add_bezier('bristle-left', B1, ((12.4, 25.9), (9.5, 29.5), (6, 31)))
        self.add_bezier('bristle-middle', C, ((22, 32), (18, 36), (13, 39)))
        self.add_bezier('bristle-right', B2, ((32, 37), (29, 40.5), (24, 42)))
        self.relate('connect', 'ferrule', 'handle')
        for s in ('left', 'middle', 'right'):
            self.relate('connect', 'ferrule', 'bristle-' + s)
