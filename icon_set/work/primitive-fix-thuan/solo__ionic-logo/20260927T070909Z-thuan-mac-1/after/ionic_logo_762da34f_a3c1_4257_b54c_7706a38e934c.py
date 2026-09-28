from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '762da34f-a3c1-4257-b54c-7706a38e934c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ionic-logo/20260927T070909Z-thuan-mac-1/reference/lonic logo_762da34f-a3c1-4257-b54c-7706a38e934c.svg'
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
    icon_id = 'ionic-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('ionic', 'framework', 'mobile', 'rings', 'logo', 'brand', 'developer')

    def build(self) -> None:
        # open ring r20 (gap in the upper right quarter), centre ring r5, small ring r3 in the gap
        self.add_arc("ring-a", (44, 24), (24, 44), radius_x=20)
        self.add_arc("ring-b", (24, 44), (4, 24), radius_x=20)
        self.add_arc("ring-c", (4, 24), (24, 4), radius_x=20)
        self.add_contour("ring", "ring-a", "ring-b", "ring-c")
        _circle(self, "centre", 24, 24, 5)
        _circle(self, "satellite", 36, 12, 3)
