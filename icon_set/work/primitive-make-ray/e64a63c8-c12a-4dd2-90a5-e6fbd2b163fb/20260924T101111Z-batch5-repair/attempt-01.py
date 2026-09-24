"""An upright smartphone displays a hand-authored dollar sign.

Symbol plan: a rounded phone enclosure and bottom divider frame one
continuous dollar stroke whose upper and lower stems attach to an S curve.
Lucide smartphone informed the device; badge-dollar-sign informed the S.
The tiny home dash is omitted because the bottom strip cannot fit it legally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e64a63c8-c12a-4dd2-90a5-e6fbd2b163fb"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/monetization tablet_e64a63c8-c12a-4dd2-90a5-e6fbd2b163fb.svg"
AUTHOR = "gpt-6"


class SmartphoneWithDollarSign(Solo48):
    icon_id = "smartphone-with-dollar-sign"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance/mobile"
    aliases = ("monetization tablet", "phone payment")
    keywords = ("dollar", "money", "smartphone", "earning")

    def build(self) -> None:
        r = 4
        self.add_line("phone-top", (12, 4), (36, 4))
        self.add_arc("phone-ne", (36, 4), (40, 8), radius_x=r, sweep=True)
        self.add_line("phone-right", (40, 8), (40, 40))
        self.add_arc("phone-se", (40, 40), (36, 44), radius_x=r, sweep=True)
        self.add_line("phone-bottom", (36, 44), (12, 44))
        self.add_arc("phone-sw", (12, 44), (8, 40), radius_x=r, sweep=True)
        self.add_line("phone-left", (8, 40), (8, 8))
        self.add_arc("phone-nw", (8, 8), (12, 4), radius_x=r, sweep=True)
        self.add_contour("phone", "phone-top", "phone-ne", "phone-right", "phone-se", "phone-bottom", "phone-sw", "phone-left", "phone-nw", closed=True)
        self.add_line("control-divider", (8, 35), (40, 35))
        self.relate("connect", "control-divider", "phone-left")
        self.relate("connect", "control-divider", "phone-right")

        # Open S with attached terminal ticks, without closed micro-counters.
        self.add_bezier("dollar-s", (29,15), ((17,11),(16,20),(24,21)), ((32,22),(31,29),(19,26)))
        self.add_line("dollar-upper-tick", (24,12),(24,14))
        self.add_line("dollar-lower-tick", (24,28),(24,30))
