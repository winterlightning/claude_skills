from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9fa77f79-8678-4042-bee6-8b1f446df614'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__grid-dot/20260927T055730Z-thuan-mac-1/reference/grid dot_9fa77f79-8678-4042-bee6-8b1f446df614.svg'
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
    icon_id = 'grid-dot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('grid', 'dot', 'design')

    def build(self) -> None:
        # rounded frame as four standalone edges joined by r4 corners (straight edges certify exact 8)
        _path(self, "frame", (10, 6), [
            (38, 6), ((42, 10), 4, 4, True), (42, 38), ((38, 42), 4, 4, True),
            (10, 42), ((6, 38), 4, 4, True), (6, 10), ((10, 6), 4, 4, True),
        ], closed=True)
        # 3x3 dot grid, 10 apart, 9 in from the frame edges
        for x in (15, 24, 33):
            for y in (15, 24, 33):
                self.add_dot(f"dot-{x}-{y}", (x, y))
