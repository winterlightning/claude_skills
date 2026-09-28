from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7d5e1d4e-10c9-57b0-ba27-2edf8237c542'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bee-with-rounded-wings/20260926T182452Z-thuan-mac-1/reference/bee_7d5e1d4e-10c9-57b0-ba27-2edf8237c542.svg'
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
    icon_id = 'bee-with-rounded-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('bee', 'honeybee', 'insect', 'wings', 'stripes', 'honey', 'bug', 'symmetry')

    def build(self) -> None:
        # Bee (reference, top view): wide upright body (flat r2-cornered head
        # end, r6 round tail) with two stripes, semicircular wings off both
        # walls, and two antennae curling outward from the head corners.
        # Mirrored about x=24; wing and stripe ends are nodes on the body walls.
        _path(self, 'body', (20, 13), [(28, 13), ((30, 15), 2, 2, True), (30, 22), (30, 30), (30, 34), (30, 36),
                                       ((24, 42), 6, 6, True), ((18, 36), 6, 6, True),
                                       (18, 34), (18, 30), (18, 22), (18, 15),
                                       ((20, 13), 2, 2, True)], True)
        for y in (22, 30):
            self.add_line(f'stripe-{y}', (18, y), (30, y))
            self.relate('connect', 'body', f'stripe-{y}')
        _path(self, 'wing-right', (30, 22), [(36, 22), ((42, 28), 6, 6, True), ((36, 34), 6, 6, True), (30, 34)])
        _path(self, 'wing-left', (18, 22), [(12, 22), ((6, 28), 6, 6, False), ((12, 34), 6, 6, False), (18, 34)])
        self.add_bezier('antenna-left', (20, 13), ((19, 9), (17, 6), (13, 6)))
        self.add_bezier('antenna-right', (28, 13), ((29, 9), (31, 6), (35, 6)))
        for side in ('left', 'right'):
            self.relate('connect', 'body', f'antenna-{side}')
            self.relate('connect', 'body', f'wing-{side}')
