"""Leopard standing, facing right.

Plan: one closed silhouette traced clockwise: rounded rump, level back, a
round ear (r4) on the crown, sloping forehead to a squared muzzle, jaw and
chest curving into the front leg, an arched belly, and the back leg curving
up into the rump. Legs are 8 wide with an 8 gap. Keyshape HRECT_M for a long,
low cat body: rump x=4, nose x=44, ear y=10, paws y=38.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4ff1165f-25a1-4654-a51e-73e523879edc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__leopard/20260927T164623Z-thuan-mac-1/reference/leopard 1_4ff1165f-25a1-4654-a51e-73e523879edc.svg"
AUTHOR = "claude-opus-5-5"


class Leopard(Solo48):
    icon_id = "leopard"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('big cat', 'panther', 'jaguar')
    keywords = ('leopard', 'cat', 'wild', 'animal', 'safari', 'feline')

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

        self.path("body", (12, 14), [
            ("L", (28, 14)),                           # back
            ("A", (36, 14), 4, 4, True),               # ear
            ("C", (44, 19), (40, 14), (44, 16)),       # rounded forehead to nose
            ("L", (44, 21)),
            ("C", (37, 26), (44, 24), (40, 25)),       # jaw
            ("C", (32, 30), (34, 27), (32, 28)),       # chest
            ("L", (32, 38)),                           # front leg
            ("L", (24, 38)),
            ("L", (24, 30)),
            ("C", (14, 30), (22, 25), (16, 25)),       # belly arch
            ("L", (14, 38)),                           # back leg
            ("L", (6, 38)),
            ("C", (4, 26), (5, 34), (4, 30)),          # thigh
            ("C", (12, 14), (4, 18), (8, 14)),         # rump
        ], closed=True)
