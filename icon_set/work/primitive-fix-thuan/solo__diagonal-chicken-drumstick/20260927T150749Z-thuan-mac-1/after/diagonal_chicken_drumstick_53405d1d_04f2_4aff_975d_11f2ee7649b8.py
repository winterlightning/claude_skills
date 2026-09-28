"""Chicken drumstick: a tilted meat oval with a straight bone ending in a forked knob.

Revision of the disapproved drawing, whose bone was a squashed blob with a hole.
Plan (SQUARE, centerline (6,6)-(42,42)): the meat is a five-knot cubic oval fitted to a
45-degree ellipse (centre (30,18), semi-axes 14 and 9) with integer knots at its
bounding-box touch points and tip, axis-aligned handles there so the extremes (top 6,
right 42) are exact; the bone leaves the lower-left tip at (20,28) along the oval's axis to
(10,38), and the knob is a chevron (6,34)-(10,38)-(6,42). Lucide `drumstick`
informs the meat + bone + knob construction; the tilt is deliberate asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "53405d1d-04f2-4aff-975d-11f2ee7649b8"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diagonal-chicken-drumstick/20260927T150749Z-thuan-mac-1/reference/drumsticks_53405d1d-04f2-4aff-975d-11f2ee7649b8.svg"
AUTHOR = "claude-fable-5-1"


class DiagonalChickenDrumstick(Solo48):
    icon_id = "diagonal-chicken-drumstick"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("chicken leg", "drumstick")
    keywords = ("chicken", "drumstick", "meat", "bone", "poultry", "food", "leg")

    def build(self) -> None:
        self.add_bezier("meat-1", (42, 13), ((42.0, 20.79), (32.79, 30.0), (25, 30)))
        self.add_bezier("meat-2", (25, 30), ((22.95, 30.0), (21.22, 29.22), (20, 28)))
        self.add_bezier("meat-3", (20, 28), ((18.78, 26.78), (18.0, 25.05), (18, 23)))
        self.add_bezier("meat-4", (18, 23), ((18.0, 15.21), (27.21, 6.0), (35, 6)))
        self.add_bezier("meat-5", (35, 6), ((39.19, 6.0), (42.0, 8.81), (42, 13)))
        self.add_contour("meat", "meat-1", "meat-2", "meat-3", "meat-4", "meat-5", closed=True)
        self.add_line("bone", (20, 28), (10, 38))
        self.add_polyline("knob", (6, 34), (10, 38), (6, 42))
        self.relate("connect", "bone", "meat")
        self.relate("connect", "bone", "knob")
