from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c7617317-0663-433d-b73d-2bfd2f6407c8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dumbbell-sports/20260927T061820Z-thuan-mac-1/reference/dumbbell_c7617317-0663-433d-b73d-2bfd2f6407c8.svg'
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
    icon_id = 'dumbbell-sports'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('dumbbell', 'sports')

    def build(self) -> None:
        # side-view dumbbell: two 8x16 plates, a bar between them and short collar stubs outside
        # CIRCLE: only the stub tips reach r20 at (4,24)/(44,24)
        for side, s in (("left", -1), ("right", 1)):
            x = lambda d: 24 + s * d
            _path(self, f"plate-{side}", (x(8), 24), [(x(8), 16), (x(16), 16), (x(16), 32), (x(8), 32), (x(8), 24)], closed=True)
            self.add_line(f"stub-{side}", (x(16), 24), (x(20), 24))
            self.relate("connect", f"stub-{side}", f"plate-{side}")
        self.add_line("bar", (16, 24), (32, 24))
        self.relate("connect", "bar", "plate-left"); self.relate("connect", "bar", "plate-right")
