from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47e29b00-ec8e-42e0-8793-0a437d3fa02a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-holding-megaphone/20260927T084830Z-thuan-mac-1/reference/election campaign 3_47e29b00-ec8e-42e0-8793-0a437d3fa02a.svg'
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
    icon_id = 'person-holding-megaphone'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('person', 'megaphone', 'campaign', 'speaker', 'announcement', 'rally')

    def build(self) -> None:
        # campaigner shouting through a megaphone (reference): head at the left, arm/shoulder
        # rising from the bottom to the handle under the cone, cone opening to the right with
        # three sound lines fanning past the mouth. Before drew a head beside a loose squiggle
        # and a triangle with no handle or sound lines.
        _circle(self, "head", 8, 20, 4)
        _path(self, "cone", (21, 17), [(31, 12), (31, 28), (23, 24), (21, 23), (21, 17)], True)
        self.add_line("handle", (23, 24), (23, 30))
        self.relate("connect", "handle", "cone")
        self.add_bezier("back", (23, 30), ((17, 31), (8, 34), (4, 40)))
        self.add_bezier("front", (23, 30), ((22, 34), (20, 37), (19, 40)))
        for a, b in (("back", "front"), ("back", "handle"), ("front", "handle")):
            self.relate("connect", a, b)
        self.add_line("sound-up", (39, 12), (43, 8))
        self.add_line("sound-mid", (39, 20), (44, 20))
        self.add_line("sound-down", (39, 28), (43, 32))
