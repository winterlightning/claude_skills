"""Two diagonally overlapping desktop monitors. HRECT_L (4,8)-(44,40).
Rear screen is an open occluded contour; foreground screen owns its stand.
Lucide monitor contributes simple screen/stand construction. Omit bezel and
rear stand to preserve clearance; reference contributes diagonal pair layout.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "51794538-e0cd-4fd6-bb22-9d08f32d43d4"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/monitor transfer_51794538-e0cd-4fd6-bb22-9d08f32d43d4.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "two-overlapping-desktop-monitors"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ["Dual Computer Monitors"]
    keywords = ["monitors", "computer", "display", "screens", "desktop", "pair", "hardware"]
    def build(self):
        self.add_polyline("rear", (28,12),(28,8),(4,8),(4,24),(8,24))
        self.add_polyline("screen",(30,32),(16,32),(16,20),(44,20),(44,32),closed=True)
        self.add_line("stand",(30,32),(30,40))
        self.add_polyline("foot",(24,40),(30,40),(36,40))
        self.relate("connect","screen","stand")
        self.relate("connect","stand","foot")
