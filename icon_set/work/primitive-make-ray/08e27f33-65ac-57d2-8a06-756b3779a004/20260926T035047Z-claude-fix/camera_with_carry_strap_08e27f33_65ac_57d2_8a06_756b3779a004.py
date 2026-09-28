"""A camera hanging from its carry strap: a camera body with a round lens under a
triangular neck strap.

Symbol plan: mirrored about x=24. The strap is one cubic arch from the body's top
corners (9,18) and (39,18) up to its crest (24,6), bowing outward so it clears the
viewfinder hump; straight triangle runs as in the reference pass within 7 of the hump.
The body is a rounded rectangle (r3) x 6..42, y 18..42 whose top edge rises into a
trapezoid hump (flat top y=15); the lens is an r4 circle of four quarter arcs centred
(24,29) under the hump, 9 above the base.
Lucide construction: 'camera' - rounded body with a circular lens; the strap as a
smooth arch, as in 'handbag'/'briefcase' handles.
Keyshape SQUARE: centerline x 6..42 (body sides), y 6..42 (strap crest, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "08e27f33-65ac-57d2-8a06-756b3779a004"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-with-carry-strap/20260926T030905Z-thuan-mac/reference/camera carry_08e27f33-65ac-57d2-8a06-756b3779a004.svg"
AUTHOR = "claude-opus-5-5"


class CameraWithCarryStrap(Solo48):
    icon_id = "camera-with-carry-strap"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/equipment"
    aliases = ("camera-carry", "camera-strap", "hanging-camera")
    keywords = ("camera", "strap", "carry", "photo", "photography", "travel", "tourist", "neck-strap")

    def build(self) -> None:
        x0, x1, top, base, r = 6, 42, 18, 42, 3
        sl, sr = 9, 39
        self.add_line("body-top-left", (sl, top), (19, top))
        self.add_line("hump-left", (19, top), (21, 15))
        self.add_line("hump-top", (21, 15), (27, 15))
        self.add_line("hump-right", (27, 15), (29, top))
        self.add_line("body-top-right", (29, top), (sr, top))
        self.add_arc("corner-tr", (sr, top), (x1, top + r), radius_x=r, sweep=True)
        self.add_line("body-right", (x1, top + r), (x1, base - r))
        self.add_arc("corner-br", (x1, base - r), (x1 - r, base), radius_x=r, sweep=True)
        self.add_line("body-base", (x1 - r, base), (x0 + r, base))
        self.add_arc("corner-bl", (x0 + r, base), (x0, base - r), radius_x=r, sweep=True)
        self.add_line("body-left", (x0, base - r), (x0, top + r))
        self.add_arc("corner-tl", (x0, top + r), (sl, top), radius_x=r, sweep=True)
        self.add_contour("body", "body-top-left", "hump-left", "hump-top", "hump-right", "body-top-right",
                         "corner-tr", "body-right", "corner-br", "body-base", "corner-bl", "body-left",
                         "corner-tl", closed=True)
        cy, lr = 29, 4
        n, e, so, w = (24, cy - lr), (24 + lr, cy), (24, cy + lr), (24 - lr, cy)
        self.add_arc("lens-ne", n, e, radius_x=lr, sweep=True)
        self.add_arc("lens-se", e, so, radius_x=lr, sweep=True)
        self.add_arc("lens-sw", so, w, radius_x=lr, sweep=True)
        self.add_arc("lens-nw", w, n, radius_x=lr, sweep=True)
        self.add_contour("lens", "lens-ne", "lens-se", "lens-sw", "lens-nw", closed=True)
        self.add_bezier("strap", (sl, top), ((8.5, 11), (15, 6), (24, 6)), ((33, 6), (39.5, 11), (sr, top)))
        self.relate("connect", "body", "strap")
