"""Dual camera smartphone back: a tall rounded phone body seen from behind, with two
camera lenses stacked in its top-left corner.

Symbol plan: one closed rounded rectangle x 10..38, y 4..44 with a shared corner
radius 6 (tangent quarter arcs). The two lenses are stroke-wide dots on one
vertical axis x=19, at y=13 and y=22: each 9 from the left and top walls (curved
contour, so 9 rather than 8) and 9 from each other.
Deliberate asymmetry: the lenses sit in the top-left corner as in the reference.
Revision: the rejected drawing used a wide VRECT_L body with near-central lens
rings whose holes closed up into blobs; this uses the reference's narrow phone
proportion and corner camera placement. Ring lenses of radius 3 were tried and
read as a speaker at 48 (they must sit 9 inside, which centres them).
Lucide construction: 'smartphone' - rounded body with a shared corner radius.
Keyshape VRECT_M: centerline x 10..38, y 4..44.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3fd36e29-728b-52a8-9cdc-ab4ac349f4b4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dual-camera-smartphone-back/20260926T055144Z-thuan-mac/reference/phone double camera_3fd36e29-728b-52a8-9cdc-ab4ac349f4b4.svg"
AUTHOR = "claude-opus-5-5"


class DualCameraSmartphoneBack(Solo48):
    icon_id = "dual-camera-smartphone-back"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "phones"
    aliases = ("phone-double-camera", "phone-back")
    keywords = ("smartphone", "camera", "dual", "lenses", "back", "phone", "mobile")

    def build(self) -> None:
        left, top, right, bottom, c = 10, 4, 38, 44, 6
        self.add_line("top", (left + c, top), (right - c, top))
        self.add_arc("corner-tr", (right - c, top), (right, top + c), radius_x=c)
        self.add_line("right", (right, top + c), (right, bottom - c))
        self.add_arc("corner-br", (right, bottom - c), (right - c, bottom), radius_x=c)
        self.add_line("bottom", (right - c, bottom), (left + c, bottom))
        self.add_arc("corner-bl", (left + c, bottom), (left, bottom - c), radius_x=c)
        self.add_line("left", (left, bottom - c), (left, top + c))
        self.add_arc("corner-tl", (left, top + c), (left + c, top), radius_x=c)
        self.add_contour("body", "top", "corner-tr", "right", "corner-br", "bottom",
                         "corner-bl", "left", "corner-tl", closed=True)
        lens_x = left + 9
        self.add_dot("lens-upper", (lens_x, top + 9))
        self.add_dot("lens-lower", (lens_x, top + 18))
