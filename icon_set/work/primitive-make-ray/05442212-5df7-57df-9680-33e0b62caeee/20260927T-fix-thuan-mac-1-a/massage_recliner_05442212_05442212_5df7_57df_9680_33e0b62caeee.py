"""Massage chair with vibration waves.

Symbol plan: head = r4 ring in the top-left corner (10,10). Recliner = one
stroke: backrest (8,22)-(16,30) sloping down from under the head, seat
(16,30)-(32,30), leg rest (32,30)-(42,38). A pedestal drops from the seat
centre (24,30) to an r4 dome (20..28) standing on a floor line y=42. Two
identical horizontal S-waves (two cubics each, amplitude ~2) at y=9 and
y=18 fill the top right, 9 apart so the curved pair certifies.
Revision: the rejected drawing drew the waves as vertical "((" marks,
left out the head and set the chair on flat arcs; the reference has a head,
a reclined chair on a dome base and two horizontal massage waves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "05442212-5df7-57df-9680-33e0b62caeee"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__massage-recliner-05442212/20260927T153253Z-thuan-mac-1/reference/massage chair wave_05442212-5df7-57df-9680-33e0b62caeee.svg"
AUTHOR = "claude-opus-5-5"


class MassageRecliner(Solo48):
    icon_id = "massage-recliner-05442212"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("primitives", "health")
    aliases = ("massage chair", "massage chair wave")
    keywords = ("massage", "chair", "recliner", "spa", "relax", "vibration")

    def build(self) -> None:
        self.add_arc("head-1", (6, 10), (14, 10), radius_x=4, sweep=True)
        self.add_arc("head-2", (14, 10), (6, 10), radius_x=4, sweep=True)
        self.add_contour("head", "head-1", "head-2", closed=True)

        self.add_line("backrest", (8, 22), (16, 30))
        self.add_line("seat-left", (16, 30), (24, 30))
        self.add_line("seat-right", (24, 30), (32, 30))
        self.add_line("legrest", (32, 30), (42, 38))
        self.add_contour("chair", "backrest", "seat-left", "seat-right", "legrest")
        self.add_line("pedestal", (24, 30), (24, 38))
        self.add_arc("dome", (20, 42), (28, 42), radius_x=4, sweep=True)
        self.add_line("floor-left", (14, 42), (20, 42))
        self.add_line("floor-mid", (20, 42), (28, 42))
        self.add_line("floor-right", (28, 42), (34, 42))
        self.add_contour("floor", "floor-left", "floor-mid", "floor-right")
        self.relate("connect", "chair", "pedestal")
        self.relate("connect", "pedestal", "dome")
        self.relate("connect", "dome", "floor")

        for i, y in enumerate((9, 18)):
            self.add_bezier(f"wave-{i}", (22, y), ((25, y - 3), (29, y - 3), (32, y)),
                            ((35, y + 3), (39, y + 3), (42, y)))
