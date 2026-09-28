from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bbd247e8-7d52-4442-bf61-ae00b476644b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-in-exoskeleton-suit/20260927T084830Z-thuan-mac-1/reference/robot exo skeleton suit_bbd247e8-7d52-4442-bf61-ae00b476644b.svg'
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
    icon_id = 'person-in-exoskeleton-suit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('exoskeleton', 'suit', 'person', 'robotic', 'wearable', 'power-armor', 'assist')

    def build(self) -> None:
        # person standing inside an exoskeleton (reference): the suit's frame runs over the
        # shoulders and down both sides as mechanical arms/legs with round joint rings at hand
        # height, feet on the ground; the wearer's head, torso and legs inside. Before drew a
        # table-like bar with legs under a floating head.
        _circle(self, "head", 24, 10, 4)
        xs = (13, 24, 35)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"shoulder-{n}", (a, 22), (b, 22))
        self.relate("connect", "shoulder-0", "shoulder-1")
        self.add_line("torso", (24, 22), (24, 29))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.relate("connect", "torso", "shoulder-0"); self.relate("connect", "torso", "shoulder-1")
        self.add_line("leg-left", (24, 29), (18, 42)); self.add_line("leg-right", (24, 29), (30, 42))
        self.relate("connect", "torso", "leg-left"); self.relate("connect", "torso", "leg-right")
        self.relate("connect", "leg-left", "leg-right")
        for s, tag, sh in ((1, "left", "shoulder-0"), (-1, "right", "shoulder-1")):
            X = lambda x: 24 + s * (x - 24)
            _path(self, f"frame-{tag}-upper", (X(13), 22), [((X(9), 26), 4, 4, s < 0), (X(9), 27)])
            _circle(self, f"joint-{tag}", X(9), 30, 3)
            self.add_line(f"frame-{tag}-lower", (X(9), 33), (X(9), 42))
            self.relate("connect", f"frame-{tag}-upper", sh)
            self.relate("connect", f"frame-{tag}-upper", f"joint-{tag}")
            self.relate("connect", f"frame-{tag}-lower", f"joint-{tag}")
