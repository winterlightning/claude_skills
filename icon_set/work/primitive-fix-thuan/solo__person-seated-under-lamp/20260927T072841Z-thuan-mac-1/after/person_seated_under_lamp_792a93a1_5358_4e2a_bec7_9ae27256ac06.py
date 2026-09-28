from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '792a93a1-5358-4e2a-bec7-9ae27256ac06'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-seated-under-lamp/20260927T072841Z-thuan-mac-1/reference/waiting room lamp_792a93a1-5358-4e2a-bec7-9ae27256ac06.svg'
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
    icon_id = 'person-seated-under-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'seated', 'lamp', 'waiting', 'room', 'chair')

    def build(self) -> None:
        # pendant lamp: cord and dome with its rim
        self.add_line("cord", (36, 6), (36, 12))
        self.add_arc("dome", (30, 20), (42, 20), radius_x=6, radius_y=8)
        self.add_line("rim", (42, 20), (30, 20))
        self.relate("connect", "cord", "dome"); self.relate("connect", "dome", "rim")
        # reader seated in an armchair (human ref full_body_ref.png): r3 head 8 above the upright torso
        _circle(self, "head", 14, 16, 3)
        self.add_line("torso", (14, 27), (14, 35))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_polyline("leg", (14, 35), (24, 35), (24, 42))
        self.relate("connect", "torso", "leg")
        self.add_line("chair-back", (6, 24), (6, 42))
