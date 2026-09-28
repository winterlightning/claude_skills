"""Award: a rosette medal -- a round medallion over two notched ribbon tails.

Symbol plan: medallion circle centred on the axis x=24 (radius 10, integer
3-4-5 attachment points at (+-6, +8)). One ribbon polyline mirrored about the
axis: each tail leaves the medallion at its lower shoulder, runs down to a
V-notched end, and the two inner edges meet in a peak on the medallion's
bottom point, as in the reference. The medallion is split at the three
attachment points so every contact shares an endpoint. Lucide: `award`
(circle over ribbon tails).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4be122ae-6b9c-44a4-84d9-7652d7d7eac8"
SOURCE_PATH = "icon_set/work/todo-references/award_4be122ae-6b9c-44a4-84d9-7652d7d7eac8.svg"
AUTHOR = "claude-opus-5-5"

CX, CY, R = 24, 14, 10
SH_X, SH_Y = 6, 8         # 3-4-5 point on the medallion
FOOT_Y, NOTCH_Y = 40, 38
OUT_X, NOTCH_X, IN_X = 16, 13, 6   # offsets from CX at the tail end


class Award(Solo48):
    icon_id = "award"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/award"
    aliases = ("rosette", "medal", "prize ribbon")
    keywords = ("award", "medal", "rosette", "ribbon", "prize", "achievement")

    def build(self) -> None:
        sl, sr = (CX - SH_X, CY + SH_Y), (CX + SH_X, CY + SH_Y)
        bottom = (CX, CY + R)
        self.add_arc("medal-top", sl, sr, radius_x=R, radius_y=R, large_arc=True, sweep=True)
        self.add_arc("medal-lower-right", sr, bottom, radius_x=R, radius_y=R, sweep=True)
        self.add_arc("medal-lower-left", bottom, sl, radius_x=R, radius_y=R, sweep=True)
        self.add_contour("medal", "medal-top", "medal-lower-right", "medal-lower-left", closed=True)

        self.add_polyline(
            "ribbon",
            sl, (CX - OUT_X, FOOT_Y), (CX - NOTCH_X, NOTCH_Y), (CX - IN_X, 44), bottom,
            (CX + IN_X, 44), (CX + NOTCH_X, NOTCH_Y), (CX + OUT_X, FOOT_Y), sr,
        )
        self.relate("connect", "ribbon-1", "medal-top", "medal-lower-left")
        self.relate("connect", "ribbon-4", "ribbon-5", "medal-lower-left", "medal-lower-right")
        self.relate("connect", "ribbon-8", "medal-top", "medal-lower-right")
