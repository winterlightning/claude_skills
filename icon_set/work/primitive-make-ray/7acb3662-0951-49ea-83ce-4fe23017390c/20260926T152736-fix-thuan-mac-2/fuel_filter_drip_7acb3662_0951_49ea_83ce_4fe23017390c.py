from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7acb3662-0951-49ea-83ce-4fe23017390c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fuel-filter-drip/20260926T152555Z-thuan-mac-2/reference/fuel filter warning_7acb3662-0951-49ea-83ce-4fe23017390c.svg'
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
    icon_id = 'fuel-filter-drip'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('fuel filter', 'filter', 'fuel', 'drip', 'warning', 'diesel', 'dashboard', 'car')

    def build(self) -> None:
        # Plan: inline fuel filter on VRECT_L (8..40 x 4..44), mirrored about x=24.
        # Upper pipe y=8 runs in from both edges and rises into the raised cap
        # (12..36, top y=4). Lower pipe y=17 runs in from both edges into the filter
        # bowl: its top is three scallops (r5 arcs, 2 deep) hanging down with cusps
        # up, as the reference's fuel line; sides down to y=27 and a V bottom at
        # (24,33), deep enough to keep the scallops 8 clear. A short drip stroke
        # falls below (a teardrop outline needs ~11 units of height).
        _path(self, 'cap', (8, 8), [(12, 8), (12, 4), (36, 4), (36, 8), (40, 8)])
        self.add_line('pipe-left', (8, 17), (12, 17))
        self.add_line('pipe-right', (36, 17), (40, 17))
        _path(self, 'bowl', (12, 17), [
            ((20, 17), 5, 5, False), ((28, 17), 5, 5, False), ((36, 17), 5, 5, False),
            (36, 27), (24, 33), (12, 27), (12, 17),
        ], closed=True)
        self.add_line('drop', (24, 42), (24, 44))
        self.relate('connect', 'bowl', 'pipe-left')
        self.relate('connect', 'bowl', 'pipe-right')
