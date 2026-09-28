"""A camera on a tripod: a camera body with a viewfinder hump and a round lens, sitting on
a rounded tripod head from which three legs spread.

Symbol plan: mirrored about x=24. The body is one closed outline: a rounded rectangle
(r3) x 8..40, y 7..29 whose top edge rises into a trapezoid viewfinder hump (45-degree
shoulders, flat top y=4). The lens is an r3 circle of four quarter arcs centred (24,17)
under the hump, 9 above the base. The tripod head is a U mount 8 wide hanging from the
base (sides x 20 and 28, r4 bottom reaching y=37); the three legs leave its lowest point
(24,37), 8 below the body, the centre leg straight down and the side legs splayed.
Lucide construction: 'camera' - rounded body with a raised top and circular lens;
straight splayed legs as in 'easel' supports.
Keyshape VRECT_L: centerline x 8..40 (body sides), y 4..44 (hump top, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "54ea6b6a-9a44-52db-a388-ae80f56aa5ac"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-on-tripod/20260926T030905Z-thuan-mac/reference/camera tripod_54ea6b6a-9a44-52db-a388-ae80f56aa5ac.svg"
AUTHOR = "claude-opus-5-5"


class CameraOnTripod(Solo48):
    icon_id = "camera-on-tripod"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/equipment"
    aliases = ("camera-tripod", "tripod-camera", "camera-stand")
    keywords = ("camera", "tripod", "photo", "photography", "stand", "mount", "video", "equipment")

    def build(self) -> None:
        x0, x1, top, base, r = 8, 40, 7, 29, 3
        ml, mr = 20, 28
        self.add_line("body-top-left", (x0 + r, top), (17, top))
        self.add_line("hump-left", (17, top), (20, 4))
        self.add_line("hump-top", (20, 4), (28, 4))
        self.add_line("hump-right", (28, 4), (31, top))
        self.add_line("body-top-right", (31, top), (x1 - r, top))
        self.add_arc("corner-tr", (x1 - r, top), (x1, top + r), radius_x=r, sweep=True)
        self.add_line("body-right", (x1, top + r), (x1, base - r))
        self.add_arc("corner-br", (x1, base - r), (x1 - r, base), radius_x=r, sweep=True)
        self.add_line("body-base-right", (x1 - r, base), (mr, base))
        self.add_line("body-base-mid", (mr, base), (ml, base))
        self.add_line("body-base-left", (ml, base), (x0 + r, base))
        self.add_arc("corner-bl", (x0 + r, base), (x0, base - r), radius_x=r, sweep=True)
        self.add_line("body-left", (x0, base - r), (x0, top + r))
        self.add_arc("corner-tl", (x0, top + r), (x0 + r, top), radius_x=r, sweep=True)
        self.add_contour("body", "body-top-left", "hump-left", "hump-top", "hump-right", "body-top-right",
                         "corner-tr", "body-right", "corner-br", "body-base-right", "body-base-mid",
                         "body-base-left", "corner-bl", "body-left", "corner-tl", closed=True)
        cy, lr = 17, 3
        n, e, so, w = (24, cy - lr), (24 + lr, cy), (24, cy + lr), (24 - lr, cy)
        self.add_arc("lens-ne", n, e, radius_x=lr, sweep=True)
        self.add_arc("lens-se", e, so, radius_x=lr, sweep=True)
        self.add_arc("lens-sw", so, w, radius_x=lr, sweep=True)
        self.add_arc("lens-nw", w, n, radius_x=lr, sweep=True)
        self.add_contour("lens", "lens-ne", "lens-se", "lens-sw", "lens-nw", closed=True)
        # tripod head: U mount under the base
        J = (24, base + 8)
        self.add_line("mount-left", (ml, base), (ml, base + 4))
        self.add_arc("mount-bottom-left", (ml, base + 4), J, radius_x=4, sweep=False)
        self.add_arc("mount-bottom-right", J, (mr, base + 4), radius_x=4, sweep=False)
        self.add_line("mount-right", (mr, base + 4), (mr, base))
        self.add_contour("mount", "mount-left", "mount-bottom-left", "mount-bottom-right", "mount-right")
        self.relate("connect", "body", "mount")
        self.add_line("leg-centre", J, (24, 44))
        self.add_line("leg-left", J, (16, 44))
        self.add_line("leg-right", J, (32, 44))
        for leg in ("leg-centre", "leg-left", "leg-right"):
            self.relate("connect", "mount", leg)
        self.relate("connect", "leg-centre", "leg-left")
        self.relate("connect", "leg-centre", "leg-right")
        self.relate("connect", "leg-left", "leg-right")
