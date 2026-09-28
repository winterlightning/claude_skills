from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '045520ca-f23a-531a-b54e-ce7bc4cbf52e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-heart/20260927T055730Z-thuan-mac-1/reference/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg'
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
    icon_id = 'hand-holding-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('hand', 'heart', 'holding', 'care', 'love', 'romance')

    def build(self) -> None:
        # heart resting in the hand: two r5 lobes about (19,13) and (29,13) meeting in a cusp at (24,13);
        # the sides leave the lobes tangentially at the 3-4-5 points (15,16)/(33,16) and run on the
        # (3,4) direction down to the thumb, where the point is hidden behind it
        _path(self, "heart", (21, 24), [
            (15, 16),
            ((24, 13), 5, 5, True, True),
            ((33, 16), 5, 5, True, True),
            (27, 24),
        ])
        # palm-up hand (kept from the approved construction): palm arc, flat thumb, r4 thumb tip,
        # r6 fingertips, palm base and wrist
        self.add_arc("palm-upper", (4, 28), (20, 24), radius_x=16, radius_y=8)
        xs = (20, 21, 27, 28)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"thumb-top-{n}", (a, 24), (b, 24))
        self.add_arc("thumb-tip-upper", (28, 24), (32, 28), radius_x=4)
        self.add_arc("thumb-tip-lower", (32, 28), (28, 32), radius_x=4)
        self.add_line("thumb-bottom", (28, 32), (18, 32))
        self.add_contour("thumb", "palm-upper", "thumb-top-0", "thumb-top-1", "thumb-top-2",
                         "thumb-tip-upper", "thumb-tip-lower", "thumb-bottom")
        self.relate("connect", "heart", "thumb")
        self.add_line("fingers-upper", (32, 28), (38, 28))
        self.add_arc("fingertips", (38, 28), (44, 32), radius_x=6)
        self.add_line("fingers-lower", (44, 32), (34, 40))
        self.add_line("palm-base", (34, 40), (12, 40))
        self.add_line("wrist-lower", (12, 40), (4, 38))
        self.add_contour("hand", "fingers-upper", "fingertips", "fingers-lower", "palm-base", "wrist-lower")
        self.relate("connect", "thumb", "hand")
