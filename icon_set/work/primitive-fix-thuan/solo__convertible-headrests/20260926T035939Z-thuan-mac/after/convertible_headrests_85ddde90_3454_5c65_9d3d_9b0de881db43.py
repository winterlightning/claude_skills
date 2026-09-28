"""A convertible car in side view, nose to the right: open top with a headrest and a raked
windshield.

Symbol plan: one closed body outline whose underside runs along the wheel centre line
(y=34) and rises over each wheel as that wheel's upper half (r4 arcs about (16,34) and
(32,34)), leaving 8-unit overhangs at tail and nose and 8 between the arches; each wheel is closed by its lower half arc. The top edge is flat at y=19 from
the rounded rear corner, carries an r4 headrest bump over the rear seat, and slopes into
the hood as a cubic to the nose at x=44. The windshield is one straight stroke raked back
from the hood base (26,19) to (21,10), 8+ clear of the headrest.
Lucide construction: 'car' - body outline sharing the wheel arcs, wheels as circles.
Keyshape HRECT_M: centerline x 4..44 (tail, nose), y 10..38 (windshield top, tyres).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "85ddde90-3454-5c65-9d3d-9b0de881db43"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__convertible-headrests/20260926T035939Z-thuan-mac/reference/car convertible_85ddde90-3454-5c65-9d3d-9b0de881db43.svg"
AUTHOR = "claude-opus-5-5"


class ConvertibleHeadrests(Solo48):
    icon_id = "convertible-headrests"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/cars"
    aliases = ("car-convertible", "convertible", "roadster", "cabriolet")
    keywords = ("car", "convertible", "roadster", "cabriolet", "open-top", "sports-car", "vehicle", "drive")

    def build(self) -> None:
        y, top, wr = 34, 19, 4
        rw, fw = 16, 32
        self.add_line("tail", (4, y), (4, top + 4))
        self.add_arc("tail-corner", (4, top + 4), (8, top), radius_x=4, sweep=True)
        self.add_arc("headrest", (8, top), (16, top), radius_x=4, sweep=True)
        self.add_line("deck", (16, top), (26, top))
        self.add_bezier("hood", (26, top), ((38, 19), (44, 21), (44, 27)))
        self.add_line("nose", (44, 27), (44, y))
        self.add_line("sill-front", (44, y), (fw + wr, y))
        self.add_arc("arch-front", (fw + wr, y), (fw - wr, y), radius_x=wr, sweep=False)
        self.add_line("sill-mid", (fw - wr, y), (rw + wr, y))
        self.add_arc("arch-rear", (rw + wr, y), (rw - wr, y), radius_x=wr, sweep=False)
        self.add_line("sill-rear", (rw - wr, y), (4, y))
        self.add_contour("body", "tail", "tail-corner", "headrest", "deck", "hood", "nose", "sill-front",
                         "arch-front", "sill-mid", "arch-rear", "sill-rear", closed=True)
        self.add_arc("wheel-front", (fw - wr, y), (fw + wr, y), radius_x=wr, sweep=False)
        self.add_arc("wheel-rear", (rw - wr, y), (rw + wr, y), radius_x=wr, sweep=False)
        self.add_line("windshield", (26, top), (21, 10))
        for part in ("wheel-front", "wheel-rear", "windshield"):
            self.relate("connect", "body", part)
