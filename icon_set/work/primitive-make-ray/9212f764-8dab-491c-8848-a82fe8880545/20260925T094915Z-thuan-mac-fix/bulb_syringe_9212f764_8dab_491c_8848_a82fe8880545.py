"""Bulb syringe (enema): a round rubber bulb with a straight nozzle rising
diagonally to the upper right and a rounded tip.

Symbol plan: one closed contour on the 45-degree axis x+y=48. The bulb is a
radius-13 circle about (19,29); the nozzle sides leave it at its 5-12-13
points (24,17) and (31,24) and run parallel (9.9 apart) to a radius-5 tip
cap whose 3-4-5 end points (34,7) and (41,14) land exactly on the sides.
Keyshape SQUARE: bulb left x=6 and bottom y=42, tip top y=6 and right x=42.
Lucide construction: pipette / syringe (diagonal tube with rounded cap) and
circle for the bulb.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing had a
lumpy bulb and a squared, kinked nozzle; here the bulb is a true circle and
the nozzle a straight tube with a round tip.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9212f764-8dab-491c-8848-a82fe8880545"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bulb-syringe/20260925T092544Z-thuan-mac/reference/enema_9212f764-8dab-491c-8848-a82fe8880545.svg"
AUTHOR = "claude-opus-5-5"

BULB = (19, 29)
BULB_R = 13
TIP = (37, 11)
TIP_R = 5


class BulbSyringe(Solo48):
    icon_id = "bulb-syringe"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("enema", "rubber-bulb-syringe")
    keywords = ("enema", "bulb", "syringe", "medical", "rubber", "irrigation")

    def build(self) -> None:
        bx, by = BULB
        tx, ty = TIP
        neck_upper = (bx + 5, by - 12)       # 5-12-13 points on the bulb
        neck_lower = (bx + 12, by - 5)
        tip_upper = (tx - 3, ty - 4)         # 3-4-5 points on the tip cap
        tip_lower = (tx + 4, ty + 3)
        self.add_arc("bulb", neck_lower, neck_upper, radius_x=BULB_R, large_arc=True, sweep=True)
        self.add_line("nozzle-upper", neck_upper, tip_upper)
        self.add_arc("tip", tip_upper, tip_lower, radius_x=TIP_R, sweep=True)
        self.add_line("nozzle-lower", tip_lower, neck_lower)
        self.add_contour("syringe", "bulb", "nozzle-upper", "tip", "nozzle-lower", closed=True)
