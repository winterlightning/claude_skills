"""A ceiling-mounted dome security camera: a wide mounting plate with a dome hanging
beneath it and a round lens in the dome.

Symbol plan: symmetric about x = 24. The mounting plate is a closed trapezoid, 8 tall:
top (6, 6)-(42, 6), bottom (8, 14)-(40, 14). The dome is an open contour hanging from the
plate bottom: short verticals at x 9 and 39 from y 14 to 17, then an r17 arc about
(24, 25) (8-15-17 end points (9, 17) and (39, 17)) sweeping down through the bottom
(24, 42). The lens is an r4 ring about (24, 29), 9 inside the dome and 11 below the plate.
The reference's inner arch around the lens is dropped: an arch 8 from both the lens and
the dome leaves no room at 48 px.
Lucide construction: 'cctv'-style mount plate with Lucide's circle lens; dome from an
integer-point (8-15-17) circle.
Keyshape SQUARE: centerline x 6..42 (plate top), y 6..42 (plate top, dome bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "649db65c-32e2-45a2-9b75-61ac786da97c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dome-security-camera/20260926T055140Z-thuan-mac/reference/surveillance camera_649db65c-32e2-45a2-9b75-61ac786da97c.svg"
AUTHOR = "claude-opus-5-5"


class DomeSecurityCamera(Solo48):
    icon_id = "dome-security-camera"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("surveillance camera", "cctv", "dome camera")
    keywords = ("camera", "security", "surveillance", "cctv", "dome", "monitoring", "ceiling", "video")

    def build(self) -> None:
        self.add_line("plate-top", (6, 6), (42, 6))
        self.add_line("plate-right", (42, 6), (40, 14))
        self.add_line("plate-bottom-right", (40, 14), (39, 14))
        self.add_line("plate-bottom", (39, 14), (9, 14))
        self.add_line("plate-bottom-left", (9, 14), (8, 14))
        self.add_line("plate-left", (8, 14), (6, 6))
        self.add_contour("plate", "plate-top", "plate-right", "plate-bottom-right", "plate-bottom",
                         "plate-bottom-left", "plate-left", closed=True)
        self.add_line("dome-left", (9, 14), (9, 17))
        self.add_arc("dome-bottom-left", (9, 17), (24, 42), radius_x=17, sweep=False)
        self.add_arc("dome-bottom-right", (24, 42), (39, 17), radius_x=17, sweep=False)
        self.add_line("dome-right", (39, 17), (39, 14))
        self.add_contour("dome", "dome-left", "dome-bottom-left", "dome-bottom-right", "dome-right")
        self.relate("connect", "plate", "dome")
        cx, cy, r = 24, 29, 4
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = ("lens-nw", "lens-ne", "lens-se", "lens-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("lens", *names, closed=True)
