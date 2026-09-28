from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2d6aea0f-956f-475c-983c-4883f1ff0ac5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__iterative-workflow-arrows/20260927T070909Z-thuan-mac-1/reference/workflow scrum_2d6aea0f-956f-475c-983c-4883f1ff0ac5.svg'
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
    icon_id = 'iterative-workflow-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('iterative', 'workflow', 'arrows')

    def build(self) -> None:
        # forward arrow along the bottom
        self.add_line("flow-a", (6, 38), (24, 38))
        self.add_line("flow-b", (24, 38), (42, 38))
        self.add_polyline("flow-head", (38, 34), (42, 38), (38, 42))
        self.relate("connect", "flow-a", "flow-b"); self.relate("connect", "flow-b", "flow-head")
        # iteration loop: rises from the arrow round an r8 loop, then curls over a second r8 loop above
        _path(self, "loop", (24, 38), [
            ((32, 30), 8, 8, False), ((24, 22), 8, 8, False),
            ((16, 14), 8, 8, True), ((24, 6), 8, 8, True), ((32, 14), 8, 8, True),
        ])
        self.relate("connect", "loop", "flow-a"); self.relate("connect", "loop", "flow-b")
