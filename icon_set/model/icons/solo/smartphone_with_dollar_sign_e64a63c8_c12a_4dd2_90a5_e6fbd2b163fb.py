"""monetization tablet: standalone repair of supplied reference.

Plan: Tall phone containing dollar sign. Keyshape VRECT_L.
Reduction: Omitted bottom control strip and home dash; open S with terminal ticks prevents tiny holes.
Construction references: local Lucide originals and atomic-debug: smartphone, dollar-sign.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

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
        # Roomier open dollar stroke; secondary bottom strip omitted.
        self.add_bezier("dollar-upper-end", (29,18), ((28,16),(26,16),(24,16)))
        self.add_bezier("dollar-upper-bowl", (24,16), ((16,16),(16,23),(24,24)))
        self.add_bezier("dollar-lower-bowl", (24,24), ((32,25),(32,32),(24,32)))
        self.add_bezier("dollar-lower-end", (24,32), ((22,32),(20,32),(19,30)))
        self.add_contour("dollar-s", "dollar-upper-end", "dollar-upper-bowl", "dollar-lower-bowl", "dollar-lower-end")
        self.add_line("dollar-upper-tick", (24,13),(24,16))
        self.add_line("dollar-lower-tick", (24,32),(24,35))
        self.relate("connect", "dollar-upper-tick", "dollar-upper-end")
        self.relate("connect", "dollar-upper-tick", "dollar-upper-bowl")
        self.relate("connect", "dollar-lower-tick", "dollar-lower-bowl")
        self.relate("connect", "dollar-lower-tick", "dollar-lower-end")
