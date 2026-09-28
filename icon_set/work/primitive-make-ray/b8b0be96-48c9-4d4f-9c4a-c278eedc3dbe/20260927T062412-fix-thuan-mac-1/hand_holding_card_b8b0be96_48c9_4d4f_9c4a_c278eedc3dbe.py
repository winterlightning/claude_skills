from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b8b0be96-48c9-4d4f-9c4a-c278eedc3dbe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-card/20260927T055730Z-thuan-mac-1/reference/credit card scan_b8b0be96-48c9-4d4f-9c4a-c278eedc3dbe.svg'
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
    icon_id = 'hand-holding-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'payments'
    categories = ('primitives', 'payments')
    aliases = ()
    keywords = ('credit-card', 'card', 'hand', 'holding', 'scan', 'payment', 'pay', 'purchase')

    def build(self) -> None:
        # card held upright in the hand: landscape card with a magnetic stripe; its lower edge is hidden
        # behind the thumb (left side lands on the thumb top) and the fingers (right side lands on them)
        self.add_polyline("card", (16, 24), (16, 8), (40, 8), (40, 28))
        self.add_line("stripe", (16, 16), (40, 16))
        self.relate("connect", "card", "stripe")
        # palm-up hand (library construction): palm arc, flat thumb top, r4 thumb tip, fingers, r4 tips
        self.add_arc("palm-upper", (4, 28), (14, 24), radius_x=10, radius_y=4)
        self.add_line("thumb-top-0", (14, 24), (16, 24))
        self.add_line("thumb-top-1", (16, 24), (28, 24))
        self.add_arc("thumb-tip-upper", (28, 24), (32, 28), radius_x=4)
        self.add_arc("thumb-tip-lower", (32, 28), (28, 32), radius_x=4)
        self.add_line("thumb-bottom", (28, 32), (18, 32))
        self.add_contour("thumb", "palm-upper", "thumb-top-0", "thumb-top-1", "thumb-tip-upper",
                         "thumb-tip-lower", "thumb-bottom")
        self.add_line("fingers-upper-0", (32, 28), (40, 28))
        self.add_arc("fingertips", (40, 28), (44, 32), radius_x=4)
        self.add_line("fingers-lower", (44, 32), (36, 40))
        self.add_line("palm-base", (36, 40), (12, 40))
        self.add_line("wrist-lower", (12, 40), (4, 38))
        self.add_contour("hand", "fingers-upper-0", "fingertips", "fingers-lower", "palm-base", "wrist-lower")
        for a, b in (("thumb", "hand"), ("card", "thumb"), ("card", "hand")):
            self.relate("connect", a, b)
