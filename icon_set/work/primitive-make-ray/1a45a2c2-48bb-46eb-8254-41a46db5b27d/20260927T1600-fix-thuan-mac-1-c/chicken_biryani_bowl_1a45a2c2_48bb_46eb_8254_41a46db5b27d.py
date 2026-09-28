"""Chicken biryani bowl: a wide bowl with a rice mound and a drumstick standing in it.

Revision of the disapproved drawing: the bowl had no rim and the drumstick was an
unreadable balloon. Plan (SQUARE, centerline (6,6)-(42,42)): flat rim line at y=30
with a U bowl below it, a rice dome (r10 arc about (28,30)) rising from the rim, and a drumstick (a small
45-degree meat oval top-left, straight bone along its axis) whose bone lands on the
dome at the exact 6-8-10 circle point (22,22). Lucide `soup` informs the rim + bowl construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1a45a2c2-48bb-46eb-8254-41a46db5b27d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chicken-biryani-bowl/20260927T150749Z-thuan-mac-1/reference/chicken biryani muslim yellow rice with chicken_1a45a2c2-48bb-46eb-8254-41a46db5b27d.svg"
AUTHOR = "claude-fable-5-1"


class ChickenBiryaniBowl(Solo48):
    icon_id = "chicken-biryani-bowl"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("biryani", "rice bowl with chicken")
    keywords = ("biryani", "chicken", "rice", "bowl", "meal", "drumstick", "food")

    def build(self) -> None:
        # bowl: rim split at the dome feet, U body below
        self.add_line("rim-1", (6, 30), (18, 30))
        self.add_line("rim-2", (18, 30), (38, 30))
        self.add_line("rim-3", (38, 30), (42, 30))
        self.add_bezier("bowl-body", (42, 30), ((42, 46), (6, 46), (6, 30)))
        self.add_contour("bowl", "rim-1", "rim-2", "rim-3", "bowl-body", closed=True)
        # rice dome r10 about (28,30); the bone lands at (22,22) = centre + (-6,-8)
        self.add_arc("dome-left", (18, 30), (22, 22), radius_x=10)
        self.add_arc("dome-right", (22, 22), (38, 30), radius_x=10)
        self.add_contour("dome", "dome-left", "dome-right")
        self.relate("connect", "dome", "bowl")
        # drumstick meat: 45-degree ellipse about (11,11), semi-axes 6 and 3.74, integer
        # knots at its bbox touch points (left 6, top 6) and its tip (15,15)
        self.add_bezier("meat-1", (15, 15), ((14.51, 15.49), (13.84, 16.0), (13, 16)))
        self.add_bezier("meat-2", (13, 16), ((9.68, 16.0), (6.0, 12.32), (6, 9)))
        self.add_bezier("meat-3", (6, 9), ((6.0, 7.29), (7.29, 6.0), (9, 6)))
        self.add_bezier("meat-4", (9, 6), ((12.32, 6.0), (16.0, 9.68), (16, 13)))
        self.add_bezier("meat-5", (16, 13), ((16.0, 13.84), (15.49, 14.51), (15, 15)))
        self.add_contour("meat", "meat-1", "meat-2", "meat-3", "meat-4", "meat-5", closed=True)
        self.add_line("bone", (15, 15), (22, 22))
        self.relate("connect", "bone", "meat")
        self.relate("connect", "bone", "dome")
