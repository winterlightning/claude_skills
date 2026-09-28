from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '16c6bf3d-a33d-570f-9e32-5cb3a500ac3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-falling-from-ledge/20260927T084830Z-thuan-mac-1/reference/safety danger cliff_16c6bf3d-a33d-570f-9e32-5cb3a500ac3a.svg'
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
    icon_id = 'person-falling-from-ledge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('falling', 'person', 'ledge', 'cliff', 'danger', 'safety')

    def build(self) -> None:
        # person tumbling off a ledge (reference): head at the top right, body pitching down-left,
        # one arm flung up-left and one down-right, legs splayed toward the ledge corner at the
        # bottom left. Before stretched the figure into one long diagonal with a tiny ledge.
        _circle(self, "head", 34, 10, 4)
        self.add_line("torso", (34, 22), (34, 24))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("torso-lean", (34, 24), (26, 30))
        self.add_line("arm-up", (34, 24), (18, 16)); self.add_line("arm-down", (34, 24), (42, 30))
        self.add_line("leg-back", (26, 30), (12, 24)); self.add_line("leg-down", (26, 30), (22, 42))
        for a, b in (("torso", "torso-lean"), ("torso", "arm-up"), ("torso", "arm-down"), ("torso-lean", "arm-up"),
                     ("torso-lean", "arm-down"), ("arm-up", "arm-down"), ("torso-lean", "leg-back"),
                     ("torso-lean", "leg-down"), ("leg-back", "leg-down")):
            self.relate("connect", a, b)
        self.add_polyline("ledge", (6, 34), (12, 34), (12, 42))
