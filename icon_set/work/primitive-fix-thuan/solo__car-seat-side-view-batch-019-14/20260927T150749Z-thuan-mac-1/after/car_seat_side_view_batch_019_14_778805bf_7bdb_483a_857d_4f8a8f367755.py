"""Car seat in side view: a padded backrest curving down into a seat cushion.

Revision of the disapproved drawing, an angular cut-corner polygon. Plan (SQUARE,
centerline (6,6)-(42,42)): one smooth outline. Rounded backrest top (r4 cap about
(10,10)), an inner cubic from (15,10) sweeping down into the cushion top at (26,30),
a r6 rounded cushion end about (36,36), a flat bottom and a r10 outer corner about
(16,32), then the straight back edge at x=6. Interior widths stay at 9/12 units.
No useful Lucide subject match; `armchair` informs the rounded-cushion construction.
The backrest/cushion asymmetry is the subject's own.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "778805bf-7bdb-483a-857d-4f8a8f367755"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__car-seat-side-view-batch-019-14/20260927T150749Z-thuan-mac-1/reference/seat car_778805bf-7bdb-483a-857d-4f8a8f367755.svg"
AUTHOR = "claude-fable-5-1"


class CarSeatSideView(Solo48):
    icon_id = "car-seat-side-view-batch-019-14"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ("seat car", "vehicle seat")
    keywords = ("seat", "car", "chair", "cushion", "backrest", "vehicle", "interior", "seating")

    def build(self) -> None:
        self.add_arc("cap-left", (6, 10), (10, 6), radius_x=4)
        self.add_arc("cap-right", (10, 6), (15, 10), radius_x=5, radius_y=4)
        self.add_bezier("inner", (15, 10), ((15, 22), (20, 30), (26, 30)))
        self.add_line("cushion-top", (26, 30), (36, 30))
        self.add_arc("end-top", (36, 30), (42, 36), radius_x=6)
        self.add_arc("end-bottom", (42, 36), (36, 42), radius_x=6)
        self.add_line("bottom", (36, 42), (16, 42))
        self.add_arc("corner", (16, 42), (6, 32), radius_x=10)
        self.add_line("back", (6, 32), (6, 10))
        self.add_contour("seat", "cap-left", "cap-right", "inner", "cushion-top", "end-top",
                         "end-bottom", "bottom", "corner", "back", closed=True)
