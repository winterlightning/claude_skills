from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '66cf9f40-4254-4619-ba1e-7b78e0914552'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__intellij-idea-logo-square/20260927T070909Z-thuan-mac-1/reference/intellij idea logo_66cf9f40-4254-4619-ba1e-7b78e0914552.svg'
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
    icon_id = 'intellij-idea-logo-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('intellij-idea', 'jetbrains', 'ide', 'logo', 'brand', 'developer', 'java')

    def build(self) -> None:
        # square badge; "IJ" set in the upper left and the underscore bar in the lower left, as in the logo
        self.add_polyline("frame", (6, 6), (42, 6), (42, 42), (6, 42), closed=True)
        self.add_line("i", (14, 15), (14, 25))
        _path(self, "j", (30, 15), [(30, 21), ((22, 21), 4, 4, True)])
        self.add_line("bar", (14, 34), (26, 34))
