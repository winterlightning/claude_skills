"""Hand pointing left with the thumb raised.

Plan: index finger a capsule 8 tall (y 16-24) reaching the left edge; raised thumb
capsule (x 22-30) tops the hand at y=8 and the back slopes to the palm; two curled fingers
stacked below (8 each, y 24-40) with rounded knuckle bumps stepping right, and
two separator creases running into the palm. Curled-finger count reduced from
three to two to keep 8u spacing. Keyshape HRECT_L: fingertip x=4, palm x=44,
back y=8, base y=40.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ea54b202-0f96-50db-97dc-1884a36b2fb9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__left-pointing-hand-with-raised-thumb/20260927T164623Z-thuan-mac-1/reference/hand pointer left_ea54b202-0f96-50db-97dc-1884a36b2fb9.svg"
AUTHOR = "claude-opus-5-5"


class LeftPointingHandWithRaisedThumb(Solo48):
    icon_id = "left-pointing-hand-with-raised-thumb"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('hand pointer left', 'thumb up pointer')
    keywords = ('hand', 'pointer', 'point', 'left', 'direction', 'finger', 'thumb')

    def path(self, name, start, steps, closed=False):
        here, members = start, []
        for j, (kind, end, *args) in enumerate(steps):
            member = f"{name}-{j}"
            if kind == "L":
                self.add_line(member, here, end)
            elif kind == "A":
                self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2],
                             large_arc=args[3] if len(args) > 3 else False)
            else:
                self.add_bezier(member, here, (args[0], args[1], end))
            here = end
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:

        self.path("hand", (8, 16), [
            ("L", (22, 16)),
            ("L", (22, 12)),
            ("A", (30, 12), 4, 4, True),                # raised thumb tip
            ("C", (44, 26), (30, 16), (43, 17)),        # back of hand, tangent off the thumb
            ("L", (44, 32)),
            ("A", (36, 40), 8, 8, True),
            ("L", (18, 40)),
            ("A", (18, 32), 4, 4, True),                # little curled finger
            ("L", (16, 32)),
            ("A", (16, 24), 4, 4, True),                # middle curled finger
            ("L", (8, 24)),
            ("A", (8, 16), 4, 4, True),                 # fingertip
        ], closed=True)
        self.add_line("crease-index", (16, 24), (26, 24))
        self.add_line("crease-middle", (18, 32), (26, 32))
        self.relate("connect", "hand", "crease-index")
        self.relate("connect", "hand", "crease-middle")
