from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6742b2e4-0a48-4b9c-a3b9-fddbfa96da87'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__invision-logo/20260927T070909Z-thuan-mac-1/reference/invision logo_6742b2e4-0a48-4b9c-a3b9-fddbfa96da87.svg'
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
    icon_id = 'invision-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('invision', 'design', 'prototype', 'in', 'logo', 'brand', 'collaboration')

    def build(self) -> None:
        # the script "in" wordmark: slanted strokes (6 over 22), dotted i, n with a round arch and a flick
        self.add_dot("i-dot", (12, 8))
        self.add_line("i", (10, 18), (4, 40))
        _path(self, "n", (14, 40), [
            (20, 18),
            ('c', (22, 10), (36, 10), (35, 20)),
            (32, 32),
            ('c', (31, 38), (37, 40), (44, 34)),
        ])
