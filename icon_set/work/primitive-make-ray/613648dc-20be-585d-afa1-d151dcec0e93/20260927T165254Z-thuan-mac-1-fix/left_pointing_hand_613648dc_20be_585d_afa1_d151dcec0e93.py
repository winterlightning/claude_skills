"""Hand pointing left with a long index finger.

Plan: index finger a capsule 8 tall (y 16-24) reaching the left edge; back of
hand rises in a smooth curve to a rounded top-right palm; two curled fingers
stacked below (8 each, y 24-40) with rounded knuckle bumps stepping right, and
two separator creases running into the palm. Curled-finger count reduced from
three to two to keep 8u spacing. Keyshape HRECT_L: fingertip x=4, palm x=44,
back y=8, base y=40.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "613648dc-20be-585d-afa1-d151dcec0e93"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__left-pointing-hand/20260927T164623Z-thuan-mac-1/reference/hand pointer left_613648dc-20be-585d-afa1-d151dcec0e93.svg"
AUTHOR = "claude-opus-5-5"


class LeftPointingHand(Solo48):
    icon_id = "left-pointing-hand"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('hand pointer left', 'point left')
    keywords = ('hand', 'pointer', 'point', 'left', 'direction', 'finger')

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
            ("L", (24, 16)),
            ("C", (32, 8), (24, 11), (27, 8)),          # back of hand
            ("L", (34, 8)),
            ("A", (44, 18), 10, 10, True),
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
