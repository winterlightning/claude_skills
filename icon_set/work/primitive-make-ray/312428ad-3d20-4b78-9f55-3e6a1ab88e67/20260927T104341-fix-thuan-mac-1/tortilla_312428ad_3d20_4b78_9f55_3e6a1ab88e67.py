from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '312428ad-3d20-4b78-9f55-3e6a1ab88e67'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tortilla/20260927T104205Z-thuan-mac-1/reference/tortilla_312428ad-3d20-4b78-9f55-3e6a1ab88e67.svg'
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
    icon_id = 'tortilla'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tortilla', '_uncategorized')

    def build(self) -> None:
        # Plan: flat round tortilla (r20 disc outline) with irregular toasted spots:
        # char marks of different lengths and angles scattered inside radius 12,
        # deliberately not in a grid so the disc does not read as a button.
        _circle(self, "tortilla", 24, 24, 20)
        self.add_dot("spot-1", (16, 22))
        self.add_line("spot-2", (23, 14), (27, 15))
        self.add_line("spot-3", (27, 26), (32, 28))
        self.add_dot("spot-4", (20, 31))
