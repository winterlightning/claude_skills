from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '74cd9635-1138-4c98-8a6c-b379d6f39c3c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-drinking-from-fountain/20260927T084830Z-thuan-mac-1/reference/water fountain drink_74cd9635-1138-4c98-8a6c-b379d6f39c3c.svg'
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
    icon_id = 'person-drinking-from-fountain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'drinking', 'fountain', 'water', 'basin', 'hydration')

    def build(self) -> None:
        # person bending to drink from a wall fountain (reference): legs apart, rounded back rising
        # to the shoulders, head leaning forward over the water jet, arm reaching down, and a wall
        # basin at the right. Before zig-zagged the body into an unreadable squiggle.
        _circle(self, "head", 28, 11, 5)
        self.add_line("torso", (15, 11), (12, 11))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_bezier("back", (12, 11), ((10, 11), (8, 15), (8, 22)))
        self.add_line("leg-back", (8, 22), (6, 42))
        self.add_line("leg-front", (8, 22), (16, 42))
        self.add_line("arm", (12, 11), (20, 24))
        for a, b in (("torso", "back"), ("torso", "arm"), ("back", "arm"), ("back", "leg-back"), ("back", "leg-front"),
                     ("leg-back", "leg-front")):
            self.relate("connect", a, b)
        _path(self, "basin", (28, 33), [(42, 33), (42, 41), (36, 41), ((28, 33), 8, 8, True)], True)
        self.add_line("wall", (42, 41), (42, 42))
        self.relate("connect", "basin", "wall")
        self.add_arc("jet", (36, 24), (42, 24), radius_x=3, radius_y=3, sweep=True)
