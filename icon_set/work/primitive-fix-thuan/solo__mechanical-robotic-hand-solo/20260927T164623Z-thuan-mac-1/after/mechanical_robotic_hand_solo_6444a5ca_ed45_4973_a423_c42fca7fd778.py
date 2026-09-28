"""Mechanical robotic hand, palm up with the thumb raised.

Plan: the forearm enters open from the left; the palm's top and bottom edges
slope gently down to the right (1:6). The thumb rises on a 3:4 axis from
the crotch K=(29,20): its edges are 10 apart and it ends in an r5 cap about
(39,15) that touches the keyshape top and right. Mechanical joints as in the
reference: a curved wrist cuff near the left and a straight palm joint at
x=22. Keyshape HRECT_M: arm x=4, thumb x=44, y=10/38.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6444a5ca-ed45-4973-a423-c42fca7fd778"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mechanical-robotic-hand-solo/20260927T164623Z-thuan-mac-1/reference/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg"
AUTHOR = "claude-opus-5-5"


class MechanicalRoboticHand(Solo48):
    icon_id = "mechanical-robotic-hand-solo"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('hand robot', 'robot hand', 'bionic hand')
    keywords = ('robot', 'hand', 'mechanical', 'bionic', 'prosthetic', 'automation')

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

        self.path("hand", (4, 14), [
            ("L", (10, 15)),
            ("L", (22, 17)),
            ("C", (29, 20), (25, 17.5), (27.5, 18.5)), # knuckle into the thumb crotch
            ("L", (35, 12)),                           # thumb upper edge
            ("A", (43, 18), 5, 5, True),               # thumb tip
            ("L", (37, 26)),                           # thumb lower edge
            ("C", (28, 38), (35, 30), (32, 38)),       # heel of the hand
            ("L", (22, 37)),
            ("L", (10, 35)),
            ("L", (4, 34)),
        ])
        self.add_bezier("cuff", (10, 15), ((13, 21), (13, 29), (10, 35)))
        self.add_line("joint", (22, 17), (22, 37))
        self.relate("connect", "hand", "cuff")
        self.relate("connect", "hand", "joint")
