from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'af634b87-e03b-46ea-80c0-7d215f7f1629'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reaching-up-toward-jagged-overhead-wire/20260927T072841Z-thuan-mac-1/reference/safety danger electricity_af634b87-e03b-46ea-80c0-7d215f7f1629.svg'
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
    icon_id = 'person-reaching-up-toward-jagged-overhead-wire'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    categories = ('electronics', 'primitives')
    aliases = ()
    keywords = ('person', 'electric', 'shock', 'hazard', 'wire', 'hand', 'danger', 'safety')

    def build(self) -> None:
        # overhead line with a broken wire hanging from it in a zigzag
        self.add_line("line-a", (6, 6), (30, 6))
        self.add_line("line-b", (30, 6), (42, 6))
        self.add_polyline("broken-wire", (30, 6), (24, 12), (31, 17), (25, 23))
        self.relate("connect", "line-a", "line-b"); self.relate("connect", "line-a", "broken-wire"); self.relate("connect", "line-b", "broken-wire")
        # person below reaching up toward it (human ref full_body_ref.png): r3 head 8 above the torso
        _circle(self, "head", 12, 24, 3)
        self.add_line("torso", (12, 35), (12, 42))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", (12, 37), (26, 31))
        self.relate("connect", "torso", "arm")
