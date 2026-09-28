from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2cf7fe47-0bae-52b2-a6ad-0ac50b09764f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__delivery-person-with-open-box-solo-b003-05/20260927T091421Z-thuan-mac-1/reference/folding pocket knife_2cf7fe47-0bae-52b2-a6ad-0ac50b09764f.svg'
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
    icon_id = 'delivery-person-with-open-box-solo-b003-05'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('delivery', 'person', 'with', 'open', 'box')

    def build(self) -> None:
        # Delivery person holding an open parcel. Stick figure at the left: r5 head (touching the
        # SQUARE left) with a cap visor to the right, exactly 8 above a short vertical neck/torso
        # segment, straight torso, two legs to the floor, and an arm reaching forward to the parcel's
        # lower corner. The parcel (16x12) stands at the right with one flap swung open, a slanted lid hinged on
        # the box top whose top edge reaches the SQUARE top.
        _circle(self, "head", 11, 13, 5)
        self.add_line("visor", (15, 10), (20, 10))
        self.relate("connect", "head", "visor")
        self.add_line("torso", (11, 26), (11, 28))
        self.add_line("torso-lower", (11, 28), (11, 36))
        self.add_line("leg-back", (11, 36), (7, 42))
        self.add_line("leg-front", (11, 36), (15, 42))
        self.add_line("arm", (11, 28), (26, 34))
        for a, b in (("torso", "torso-lower"), ("torso-lower", "leg-back"), ("torso-lower", "leg-front"),
                     ("torso", "arm"), ("torso-lower", "arm")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        _path(self, "box", (26, 22), [(30, 22), (42, 22), (42, 34), (26, 34), (26, 22)], True)
        _path(self, "flap", (30, 22), [(29, 8), (38, 6), (42, 22)])
        self.relate("connect", "box", "flap")
        self.relate("connect", "box", "arm")
