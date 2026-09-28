"""A camera on a slim tripod: a camera body with a viewfinder hump and a round lens,
standing on a single post that splits into three legs.

Symbol plan: mirrored about x=24. The body is one closed outline: a rounded rectangle
(r3) x 8..40, y 7..29 whose top edge rises into a trapezoid viewfinder hump (45-degree
shoulders, flat top y=4). The lens is an r3 circle of four quarter arcs centred (24,17)
under the hump, 9 above the base and 9 from the hump shoulders on centerlines. A
slim post drops 8 from the base centre to the leg junction (24,37), so the legs stay 8
clear of the body; the centre leg continues straight down and the side legs splay.
Lucide construction: 'camera' - rounded body with a raised top and circular lens;
straight splayed legs as in 'tent'/'easel' supports.
Keyshape VRECT_L: centerline x 8..40 (body sides), y 4..44 (hump top, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a2604ba0-efa4-511a-a7be-31bd8355058a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-on-slim-tripod/20260926T030905Z-thuan-mac/reference/camera tripod_a2604ba0-efa4-511a-a7be-31bd8355058a.svg"
AUTHOR = "claude-opus-5-5"


class CameraOnSlimTripod(Solo48):
    icon_id = "camera-on-slim-tripod"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/equipment"
    aliases = ("camera-tripod", "tripod-camera")
    keywords = ("camera", "tripod", "photo", "photography", "stand", "video", "shoot", "equipment")

    def build(self) -> None:
        x0, x1, top, base, r = 8, 40, 7, 29, 3
        pts = dict(hl=(17, top), htl=(20, 4), htr=(28, 4), hr=(31, top))
        self.add_line("body-top-left", (x0 + r, top), pts["hl"])
        self.add_line("hump-left", pts["hl"], pts["htl"])
        self.add_line("hump-top", pts["htl"], pts["htr"])
        self.add_line("hump-right", pts["htr"], pts["hr"])
        self.add_line("body-top-right", pts["hr"], (x1 - r, top))
        self.add_arc("corner-tr", (x1 - r, top), (x1, top + r), radius_x=r, sweep=True)
        self.add_line("body-right", (x1, top + r), (x1, base - r))
        self.add_arc("corner-br", (x1, base - r), (x1 - r, base), radius_x=r, sweep=True)
        self.add_line("body-base-right", (x1 - r, base), (24, base))
        self.add_line("body-base-left", (24, base), (x0 + r, base))
        self.add_arc("corner-bl", (x0 + r, base), (x0, base - r), radius_x=r, sweep=True)
        self.add_line("body-left", (x0, base - r), (x0, top + r))
        self.add_arc("corner-tl", (x0, top + r), (x0 + r, top), radius_x=r, sweep=True)
        self.add_contour("body", "body-top-left", "hump-left", "hump-top", "hump-right", "body-top-right",
                         "corner-tr", "body-right", "corner-br", "body-base-right", "body-base-left",
                         "corner-bl", "body-left", "corner-tl", closed=True)
        cy, lr = 17, 3
        n, e, so, w = (24, cy - lr), (24 + lr, cy), (24, cy + lr), (24 - lr, cy)
        self.add_arc("lens-ne", n, e, radius_x=lr, sweep=True)
        self.add_arc("lens-se", e, so, radius_x=lr, sweep=True)
        self.add_arc("lens-sw", so, w, radius_x=lr, sweep=True)
        self.add_arc("lens-nw", w, n, radius_x=lr, sweep=True)
        self.add_contour("lens", "lens-ne", "lens-se", "lens-sw", "lens-nw", closed=True)
        # tripod
        J = (24, base + 8)
        self.add_line("post", (24, base), J)
        self.add_line("leg-centre", J, (24, 44))
        self.add_line("leg-left", J, (16, 44))
        self.add_line("leg-right", J, (32, 44))
        self.relate("connect", "body", "post")
        for leg in ("leg-centre", "leg-left", "leg-right"):
            self.relate("connect", "post", leg)
        self.relate("connect", "leg-centre", "leg-left")
        self.relate("connect", "leg-centre", "leg-right")
        self.relate("connect", "leg-left", "leg-right")
