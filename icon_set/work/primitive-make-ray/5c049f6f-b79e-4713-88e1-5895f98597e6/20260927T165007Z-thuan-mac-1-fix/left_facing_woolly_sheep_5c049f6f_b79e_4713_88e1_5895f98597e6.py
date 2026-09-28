"""Left-facing woolly sheep.

Plan: round head (circle r10 about (14,18)) in front, woolly body behind it
with two soft top humps and a rounded rump, two single-stroke legs, and the
ram's curl as an arc hooked from the back of the head. Body contours end on
integer points of the head circle (3-4-5 offsets) so the occlusion joins are
exact. Keyshape HRECT_L: snout x=4, rump x=44, head top y=8, hooves y=40.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5c049f6f-b79e-4713-88e1-5895f98597e6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__left-facing-woolly-sheep/20260927T164623Z-thuan-mac-1/reference/mouton_5c049f6f-b79e-4713-88e1-5895f98597e6.svg"
AUTHOR = "claude-opus-5-5"


class LeftFacingWoollySheep(Solo48):
    icon_id = "left-facing-woolly-sheep"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('mouton', 'lamb')
    keywords = ('sheep', 'lamb', 'wool', 'farm', 'animal', 'mouton')

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

        self.path("head", (4, 18), [("A", (24, 18), 10, 10, True), ("A", (4, 18), 10, 10, True)], closed=True)
        self.path("body", (20, 10), [
            ("C", (30, 8), (23, 8), (26, 8)),          # wool line off the head
            ("C", (44, 21), (38, 8), (44, 12)),        # back and rump
            ("L", (44, 26)),
            ("C", (38, 34), (44, 31), (42, 34)),
            ("L", (23, 34)),
            ("C", (20, 26), (22.5, 31), (21, 28)),     # chest into the head
        ])
        self.relate("connect", "head", "body")
        for name, x in (("front", 23), ("back", 38)):
            self.add_line(f"leg-{name}", (x, 34), (x, 40))
            self.relate("connect", "body", f"leg-{name}")
