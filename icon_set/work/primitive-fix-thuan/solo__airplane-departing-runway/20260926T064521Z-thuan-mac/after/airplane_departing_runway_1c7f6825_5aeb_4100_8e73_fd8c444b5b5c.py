"""An airliner climbing away from a runway: a side-view plane rising up-right above a
runway drawn in perspective.

Symbol plan: the plane is drawn in strokes, climbing along (2, -1). The fuselage is one
straight stroke from the tail (10, 22) to the nose (42, 6), split where the other parts
join. The near wing sweeps down and back from (30, 12) to (26, 24); the far wing rises back
from (26, 14) to (18, 6); the tail fin rises from (14, 20) to (10, 12). The tips keep 8+
from each other and from the fuselage. The runway is a closed perspective trapezoid, top
(12, 34)-(36, 34), bottom (6, 42)-(42, 42), 10 below the wing tip. An outlined fuselage
(attempts/v1-outlined-fuselage.svg) was too short and fat and read as a check mark. The
reference's runway dashes are dropped: a dashed runway needs 16 units of height, and the
plane needs the rest.
Lucide construction: 'plane-takeoff' (climbing plane over a runway); round nose from a
3-4-5 integer cap.
Keyshape SQUARE: centerline x 6..42 (runway base, nose), y 6..42 (nose and far wing, runway base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1c7f6825-5aeb-4100-8e73-fd8c444b5b5c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__airplane-departing-runway/20260926T064521Z-thuan-mac/reference/optimization plane_1c7f6825-5aeb-4100-8e73-fd8c444b5b5c.svg"
AUTHOR = "claude-opus-5-5"


class AirplaneDepartingRunway(Solo48):
    icon_id = "airplane-departing-runway"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transport"
    aliases = ("optimization plane", "plane takeoff", "departure")
    keywords = ("airplane", "takeoff", "departure", "runway", "flight", "airport", "travel", "plane")

    def build(self) -> None:
        tail, fin_root, far_root, near_root, nose = (10, 22), (14, 20), (26, 14), (30, 12), (42, 6)
        self.add_polyline("fuselage", tail, fin_root, far_root, near_root, nose)
        self.add_line("wing-near", near_root, (26, 24))
        self.add_line("wing-far", far_root, (18, 6))
        self.add_line("tail-fin", fin_root, (10, 12))
        for part in ("wing-near", "wing-far", "tail-fin"):
            self.relate("connect", "fuselage", part)
        self.add_polyline("runway", (12, 34), (36, 34), (42, 42), (6, 42), closed=True)
