"""A camera with a raised shutter button: a wide body with a viewfinder hump over a round
lens and a low shutter-button bump on the top-left.

Symbol plan: the body is one closed outline: a rounded rectangle (r3) x 4..44, y 14..40.
Its top edge rises twice, as in the reference: a low flat-topped shutter bump (base
x 7..15, top x 9..13 at y=11) right after the top-left corner, then, 8 along the top edge,
the larger trapezoid viewfinder hump (base x 23..37, flat top y=8) right of centre. The
lens is an r5 circle of four quarter arcs centred (30,26) under the hump, 9 above the
base and 9 from the body's right side.
Lucide construction: 'camera' - rounded body with a raised trapezoid top and circular
lens.
Keyshape HRECT_L: centerline x 4..44 (body sides), y 8..40 (hump top, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b79f701b-ae96-59f9-981f-600ef6cff58f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-with-raised-shutter-button/20260926T030905Z-thuan-mac/reference/camera 1_b79f701b-ae96-59f9-981f-600ef6cff58f.svg"
AUTHOR = "claude-opus-5-5"


class CameraWithRaisedShutterButton(Solo48):
    icon_id = "camera-with-raised-shutter-button"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/equipment"
    aliases = ("camera-1", "camera", "photo-camera")
    keywords = ("camera", "photo", "photography", "shutter", "button", "lens", "snapshot", "picture")

    def build(self) -> None:
        x0, x1, top, base, r = 4, 44, 14, 40, 3
        pts = [(x0 + r, top), (9, 11), (13, 11), (15, top), (23, top), (26, 8), (34, 8), (37, top), (x1 - r, top)]
        for i in range(1, len(pts)):
            self.add_line(f"top-edge-{i}", pts[i - 1], pts[i])
        self.add_arc("corner-tr", (x1 - r, top), (x1, top + r), radius_x=r, sweep=True)
        self.add_line("body-right", (x1, top + r), (x1, base - r))
        self.add_arc("corner-br", (x1, base - r), (x1 - r, base), radius_x=r, sweep=True)
        self.add_line("body-base", (x1 - r, base), (x0 + r, base))
        self.add_arc("corner-bl", (x0 + r, base), (x0, base - r), radius_x=r, sweep=True)
        self.add_line("body-left", (x0, base - r), (x0, top + r))
        self.add_arc("corner-tl", (x0, top + r), (x0 + r, top), radius_x=r, sweep=True)
        self.add_contour("body", *[f"top-edge-{i}" for i in range(1, 9)], "corner-tr", "body-right",
                         "corner-br", "body-base", "corner-bl", "body-left", "corner-tl", closed=True)
        cx, cy, lr = 30, 26, 5
        n, e, so, w = (cx, cy - lr), (cx + lr, cy), (cx, cy + lr), (cx - lr, cy)
        self.add_arc("lens-ne", n, e, radius_x=lr, sweep=True)
        self.add_arc("lens-se", e, so, radius_x=lr, sweep=True)
        self.add_arc("lens-sw", so, w, radius_x=lr, sweep=True)
        self.add_arc("lens-nw", w, n, radius_x=lr, sweep=True)
        self.add_contour("lens", "lens-ne", "lens-se", "lens-sw", "lens-nw", closed=True)
