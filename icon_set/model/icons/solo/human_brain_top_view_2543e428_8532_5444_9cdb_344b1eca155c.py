from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2543e428-8532-5444-9cdb-344b1eca155c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brain-with-central-fissure/20260927T032145Z-thuan-mac-1/reference/brain_2543e428-8532-5444-9cdb-344b1eca155c.svg'
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
    icon_id = 'human-brain-top-view'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('brain', 'with', 'central', 'fissure')

    def build(self) -> None:
        # top-view brain mirrored about the fissure x=24. Each hemisphere: four cubic lobes meeting at
        # inward notches (12,10), (12,24), (12,38). Equal control coordinates put each lobe's extreme
        # exactly on the keyshape edge: y = 10 - 0.75*(10 - 14/3) = 6, x = 12 - 0.75*8 = 6, y = 42.
        top_c, bottom_c = 14 / 3, 38 + 16 / 3
        for side, s in (("left", -1), ("right", 1)):
            x = lambda d: 24 + s * d
            _path(self, f"hemisphere-{side}", (24, 10), [
                ('c', (x(3), top_c), (x(9), top_c), (x(12), 10)),
                ('c', (x(20), 12), (x(20), 22), (x(12), 24)),
                ('c', (x(20), 26), (x(20), 36), (x(12), 38)),
                ('c', (x(9), bottom_c), (x(3), bottom_c), (24, 38)),
            ])
        # one fold per hemisphere from the side notch, curling up on the left and down on the right
        self.add_bezier("fold-left", (12, 24), ((14, 24), (15, 22), (15, 19)))
        self.add_bezier("fold-right", (36, 24), ((34, 24), (33, 26), (33, 29)))
        self.add_line("fissure", (24, 10), (24, 38))
        for a, b in (("hemisphere-left", "fold-left"), ("hemisphere-right", "fold-right"),
                     ("fissure", "hemisphere-left"), ("fissure", "hemisphere-right"),
                     ("hemisphere-left", "hemisphere-right")):
            self.relate("connect", a, b)
