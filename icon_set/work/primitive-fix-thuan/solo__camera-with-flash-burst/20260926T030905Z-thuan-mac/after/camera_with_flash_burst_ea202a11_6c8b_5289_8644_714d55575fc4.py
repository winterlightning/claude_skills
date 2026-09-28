"""A camera firing its flash: a wide camera body with a viewfinder hump over the lens and a
star-shaped flash burst above its top-left corner.

Symbol plan: the body is one closed outline: a rounded rectangle (r3) x 8..40, y 24..44
whose top edge rises into a trapezoid hump (flat top y=20) centred over the lens at
x=28, as in the reference. The lens is an r3 circle of four quarter arcs centred (28,32),
9 from the hump top, the base and the shoulder corners. The flash burst is a five-spike
star (spikes of radius 5 from (13,9), tips rounded to the grid) in the free top-left
corner, 11 above the body; an eight-spike asterisk filled in to a blob at 48px and a
four-spike glint read as a plus sign.
Lucide construction: 'camera' - rounded body with a raised top and circular lens;
'sparkles' - radiating spikes for the burst.
Keyshape VRECT_L: centerline x 8..40 (body sides, glint), y 4..44 (glint tip, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ea202a11-6c8b-5289-8644-714d55575fc4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-with-flash-burst/20260926T030905Z-thuan-mac/reference/camera flash_ea202a11-6c8b-5289-8644-714d55575fc4.svg"
AUTHOR = "claude-opus-5-5"


class CameraWithFlashBurst(Solo48):
    icon_id = "camera-with-flash-burst"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/equipment"
    aliases = ("camera-flash", "flash-photo")
    keywords = ("camera", "flash", "burst", "photo", "photography", "light", "strobe", "shoot")

    def build(self) -> None:
        x0, x1, top, base, r = 8, 40, 24, 44, 3
        self.add_line("body-top-left", (x0 + r, top), (19, top))
        self.add_line("hump-left", (19, top), (22, 20))
        self.add_line("hump-top", (22, 20), (34, 20))
        self.add_line("hump-right", (34, 20), (37, top))
        self.add_line("body-top-right", (37, top), (x1 - r, top))
        self.add_arc("corner-tr", (x1 - r, top), (x1, top + r), radius_x=r, sweep=True)
        self.add_line("body-right", (x1, top + r), (x1, base - r))
        self.add_arc("corner-br", (x1, base - r), (x1 - r, base), radius_x=r, sweep=True)
        self.add_line("body-base", (x1 - r, base), (x0 + r, base))
        self.add_arc("corner-bl", (x0 + r, base), (x0, base - r), radius_x=r, sweep=True)
        self.add_line("body-left", (x0, base - r), (x0, top + r))
        self.add_arc("corner-tl", (x0, top + r), (x0 + r, top), radius_x=r, sweep=True)
        self.add_contour("body", "body-top-left", "hump-left", "hump-top", "hump-right", "body-top-right",
                         "corner-tr", "body-right", "corner-br", "body-base", "corner-bl", "body-left",
                         "corner-tl", closed=True)
        cx, cy, lr = 28, 32, 3
        n, e, so, w = (cx, cy - lr), (cx + lr, cy), (cx, cy + lr), (cx - lr, cy)
        self.add_arc("lens-ne", n, e, radius_x=lr, sweep=True)
        self.add_arc("lens-se", e, so, radius_x=lr, sweep=True)
        self.add_arc("lens-sw", so, w, radius_x=lr, sweep=True)
        self.add_arc("lens-nw", w, n, radius_x=lr, sweep=True)
        self.add_contour("lens", "lens-ne", "lens-se", "lens-sw", "lens-nw", closed=True)
        # flash burst: five spikes of a star around (13,9), tips on the grid near radius 5
        c = (13, 9)
        tips = ((13, 4), (18, 7), (16, 13), (10, 13), (8, 7))
        names = []
        for i, t in enumerate(tips):
            self.add_line(f"burst-spike-{i + 1}", c, t)
            names.append(f"burst-spike-{i + 1}")
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                self.relate("connect", a, b)
