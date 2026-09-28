"""A side-view salon chair with a sloping back, arm, pedestal, and footrest.

Symbol plan: continuous back and seat, a raised arm with one seat attachment,
central pedestal and base, and a separate projecting footrest. Lucide armchair
informed the compact arm construction; the source's side profile is retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d057f678-f39c-50d4-9554-598acaf09010"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__salon-chair-with-footrest/20260927T091420Z-thuan-mac-1/reference/hair dress chair_d057f678-f39c-50d4-9554-598acaf09010.svg"
AUTHOR = "gpt-6"


class SalonChairWithFootrest(Solo48):
    icon_id = "salon-chair-with-footrest"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "beauty"
    aliases = ()
    keywords = ("salon", "chair", "footrest", "hairdresser")

    def build(self) -> None:
        self.add_line("back", (4,8), (9,24))
        self.add_arc("back-turn", (9,24), (15,30), radius_x=6, sweep=False)
        self.add_line("seat", (15,30), (34,30))
        self.add_contour("chair", "back", "back-turn", "seat")

        self.add_line("arm-top", (18,18), (26,18))
        self.add_arc("arm-turn", (26,18), (28,20), radius_x=2, sweep=True)
        self.add_line("arm-front", (28,20), (28,30))
        self.add_contour("arm", "arm-top", "arm-turn", "arm-front")
        self.relate("connect", "arm", "chair")

        self.add_line("pedestal", (23,30), (23,40))
        self.add_line("base", (12,40), (30,40))
        self.relate("connect", "pedestal", "chair")
        self.relate("connect", "pedestal", "base")

        self.add_polyline("footrest", (34,30), (39,38), (44,38))
        self.relate("connect", "chair", "footrest")
