from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '72f8da86-66ef-4f18-ac0b-44421c416a99'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-holding-flaming-bottle/20260927T084830Z-thuan-mac-1/reference/protest fire bottle_72f8da86-66ef-4f18-ac0b-44421c416a99.svg'
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
    icon_id = 'person-holding-flaming-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('person', 'holding', 'flaming', 'bottle')

    def build(self) -> None:
        # protester holding out a flaming bottle (reference): stick figure with legs apart, one arm
        # stretched right, the other reaching left to a bottle whose wick burns with a teardrop
        # flame curling at the tip. Before had a tiny bottle with an unreadable flame blob.
        _circle(self, "head", 28, 10, 4)
        self.add_line("torso", (28, 22), (28, 24))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("torso-lean", (28, 24), (28, 32))
        self.add_line("leg-left", (28, 32), (21, 42)); self.add_line("leg-right", (28, 32), (35, 42))
        self.add_line("arm-left", (28, 24), (14, 26)); self.add_line("arm-right", (28, 24), (42, 22))
        for a, b in (("torso", "torso-lean"), ("torso", "arm-left"), ("torso", "arm-right"), ("torso-lean", "arm-left"),
                     ("torso-lean", "arm-right"), ("arm-left", "arm-right"), ("torso-lean", "leg-left"),
                     ("torso-lean", "leg-right"), ("leg-left", "leg-right")):
            self.relate("connect", a, b)
        _path(self, "bottle", (14, 26), [(14, 34), (6, 34), (6, 24), (10, 20), (14, 24), (14, 26)], True)
        self.relate("connect", "bottle", "arm-left")
        self.add_line("wick", (10, 18), (10, 20))
        self.relate("connect", "wick", "bottle")
        _path(self, "flame", (13, 6), [('c', (8, 8), (6, 10), (6, 14)), ((10, 18), 4, 4, False), ((14, 14), 4, 4, False),
                                       ('c', (14, 11), (12, 9), (13, 6))], True)
        self.relate("connect", "wick", "flame")
