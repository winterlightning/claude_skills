"""Chicken drumstick: a tilted meat oval with a straight bone ending in a forked knob.

Revision of the disapproved drawing, whose bone was a squashed blob with a hole.
Plan (SQUARE, centerline (6,6)-(42,42)): the meat is a five-knot cubic oval with
axis-aligned knots at its bounding-box touch points so the extremes (top 6, right 42)
are exact; the bone leaves the lower-left tip at (20,28) along the oval's axis to
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
        T, R, B, P, L = (35, 6), (42, 13), (25, 30), (20, 28), (18, 23)
        self.add_bezier("meat-1", T, ((39, 6), (42, 9), R))
        self.add_bezier("meat-2", R, ((42, 22), (34, 30), B))
        self.add_bezier("meat-3", B, ((23, 30), (22, 30), P))
        self.add_bezier("meat-4", P, ((19, 27), (18, 25), L))
        self.add_bezier("meat-5", L, ((18, 16), (26, 6), T))
        self.add_contour("meat", "meat-1", "meat-2", "meat-3", "meat-4", "meat-5", closed=True)
        self.add_line("bone", P, (10, 38))
        self.add_polyline("knob", (6, 34), (10, 38), (6, 42))
        self.relate("connect", "bone", "meat")
        self.relate("connect", "bone", "knob")
