from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f9e55377-8da9-5927-845b-403bea7db251'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__croissant-batch-011-10/20260927T091424Z-thuan-mac-1/reference/breakfast croissant_f9e55377-8da9-5927-845b-403bea7db251.svg'
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
    icon_id = 'croissant-batch-011-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('croissant', 'pastry', 'bread', 'breakfast', 'food', 'bakery')

    def build(self) -> None:
        # Plan (Lucide croissant, integer 48 grid): mirrored about y=x.
        # Centre sector: rounded outer edge U(20,6)-V(6,20), sides to apex A(30,30)
        # on 5:12 lattice lines (split at the horn joins W). Each horn: outer edge
        # continuing from V, bottom seam, hanging tip bulb rising back to W.
        def m(p):
            return (p[1], p[0])

        self.add_bezier('sector-top', (20, 6), ((13, 6), (6, 13), (6, 20)))
        for side, f in (('l', lambda p: p), ('r', m)):
            V, W, A = f((6, 20)), f((18, 25)), (30, 30)
            self.add_line(f'side-{side}-1', V, W)
            self.add_line(f'side-{side}-2', W, A)
            sw = side == 'l'
            _path(self, f'horn-{side}', V, [
                ('c', f((6, 27)), f((6, 33)), f((8, 35))),
                f((10, 35)),
                (f((16, 42)), *((6, 7) if sw else (7, 6)), not sw),
                (f((20, 38)), 4, 4, not sw),
                f((20, 35)),
                ('c', f((20, 31)), f((19, 28)), W),
            ])
            self.add_line(f'seam-{side}', f((10, 35)), f((20, 35)))
            for a, b in (('sector-top', f'side-{side}-1'), ('sector-top', f'horn-{side}'),
                         (f'side-{side}-1', f'side-{side}-2'), (f'side-{side}-1', f'horn-{side}'),
                         (f'side-{side}-2', f'horn-{side}'), (f'seam-{side}', f'horn-{side}')):
                self.relate('connect', a, b)
        self.relate('connect', 'side-l-2', 'side-r-2')
