from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '99aca13e-621b-4224-a7d5-50e282c5a5ba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jasmine-logo/20260927T070909Z-thuan-mac-1/reference/jasmine logo_99aca13e-621b-4224-a7d5-50e282c5a5ba.svg'
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
    icon_id = 'jasmine-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('jasmine', 'testing', 'javascript', 'starburst', 'logo', 'brand', 'developer')

    def build(self) -> None:
        # ring r20 with a hollow starburst: four cardinal dashes (r6..r11) and four diagonal dots
        _circle(self, "ring", 24, 24, 20)
        for n, (dx, dy) in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
            self.add_line(f"ray-{n}", (24 + 6 * dx, 24 + 6 * dy), (24 + 11 * dx, 24 + 11 * dy))
        for n, (dx, dy) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
            self.add_dot(f"spark-{n}", (24 + 8 * dx, 24 + 8 * dy))
