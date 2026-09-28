from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0c8f7f81-3b5e-4964-a6bc-5955f81d4007'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-bar-battery/20260927T080808Z-thuan-mac-1/reference/charging battery two bars_0c8f7f81-3b5e-4964-a6bc-5955f81d4007.svg'
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
    icon_id = 'two-bar-battery'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'mobile'
    categories = ('mobile', 'primitives')
    aliases = ()
    keywords = ('battery', 'two-bars', 'charge', 'power', 'energy', 'level', 'indicator')

    def build(self) -> None:
        # Plan: wide battery body (4..40 x 10..38, r4 corners) with the terminal as a
        # 4-deep bump in the right wall (y18..30), two charge bars on the left (9 clear of the
        # rounded body, 8 apart), right half left empty for the uncharged part.
        _path(self, "body", (8, 10), [(36, 10), ((40, 14), 4, 4, True), (40, 18), (44, 18), (44, 30),
                                      (40, 30), (40, 34), ((36, 38), 4, 4, True), (8, 38),
                                      ((4, 34), 4, 4, True), (4, 14), ((8, 10), 4, 4, True)], closed=True)
        self.add_line("bar-1", (13, 19), (13, 29))
        self.add_line("bar-2", (21, 19), (21, 29))
