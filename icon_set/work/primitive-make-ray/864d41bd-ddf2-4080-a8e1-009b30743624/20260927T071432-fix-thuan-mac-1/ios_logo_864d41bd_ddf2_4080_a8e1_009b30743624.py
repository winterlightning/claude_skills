from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '864d41bd-ddf2-4080-a8e1-009b30743624'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ios-logo/20260927T070909Z-thuan-mac-1/reference/ios logo_864d41bd-ddf2-4080-a8e1-009b30743624.svg'
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
    icon_id = 'ios-logo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('ios', 'apple', 'mobile', 'operating-system', 'logo', 'brand', 'iphone')

    def build(self) -> None:
        # "iOS": dotted i, a round O (not a narrow zero), and an S of two r4 bowls joined by its spine
        self.add_dot("i-dot", (4, 10))
        self.add_line("i-stem", (4, 18), (4, 38))
        self.add_arc("o-top", (13, 28), (27, 28), radius_x=7, radius_y=10)
        self.add_arc("o-bottom", (27, 28), (13, 28), radius_x=7, radius_y=10)
        self.add_contour("o", "o-top", "o-bottom", closed=True)
        _path(self, "s", (44, 22), [
            ((36, 22), 4, 4, False),
            ('c', (36, 27), (44, 29), (44, 34)),
            ((36, 34), 4, 4, True),
        ])
