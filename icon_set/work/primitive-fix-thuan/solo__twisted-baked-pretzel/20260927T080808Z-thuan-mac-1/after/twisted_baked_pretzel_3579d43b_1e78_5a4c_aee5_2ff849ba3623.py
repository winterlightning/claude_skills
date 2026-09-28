from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3579d43b-1e78-5a4c-aee5-2ff849ba3623'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__twisted-baked-pretzel/20260927T080808Z-thuan-mac-1/reference/pretzel_3579d43b-1e78-5a4c-aee5-2ff849ba3623.svg'
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
    icon_id = 'twisted-baked-pretzel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('twisted', 'baked', 'pretzel')

    def build(self) -> None:
        # Pretzel (reference, double twist) as one rope, mirrored about x=24:
        # the outer loop runs from the top dip Y over the r8 humps, down
        # full sides and round a broad bottom; the arms cross at Y at 90
        # degrees, form a 9-wide lens, cross again at X (24,26) and fold
        # down at 45 degrees as tails resting on the loop at (13,37) /
        # (35,37), meeting it square.
        Y, X = (24, 14), (24, 26)
        _path(self, 'loop', Y, [('c', (21, 11), (18, 6), (14, 6)), ((6, 14), 8, 8, False),
                                ('c', (6, 27), (9, 33), (13, 37)), ('c', (16, 40), (19, 42), (24, 42)),
                                ('c', (29, 42), (32, 40), (35, 37)), ('c', (39, 33), (42, 27), (42, 14)),
                                ((34, 6), 8, 8, False), ('c', (30, 6), (27, 11), Y)], True)
        _path(self, 'lens-right', X, [('c', (30, 20), (30, 20), Y)])
        _path(self, 'lens-left', Y, [('c', (18, 20), (18, 20), X)])
        self.add_line('tail-left', (13, 37), X)
        self.add_line('tail-right', X, (35, 37))
        for part in ('lens-right', 'lens-left', 'tail-left', 'tail-right'):
            self.relate('connect', part, 'loop')
        for a, b in (('lens-right', 'lens-left'), ('tail-left', 'lens-right'), ('tail-left', 'lens-left'),
                     ('tail-right', 'lens-right'), ('tail-right', 'lens-left'), ('tail-left', 'tail-right')):
            self.relate('connect', a, b)
