"""A tall mobile phone frame with an arrow exiting its right-side gap.

Symbol plan: one open rounded phone contour, a lower bezel bar, and a
three-part right arrow share a vertical center. Lucide smartphone informed
the device corners; arrow-right informed the open head. The arrow direction
is intentional asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "bc63b0a1-e317-45a2-a96b-d545b39f1c83"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/mobile phone call forwarding outgoing 1_bc63b0a1-e317-45a2-a96b-d545b39f1c83.svg"
AUTHOR = "gpt-6"


class MobilePhoneOutgoingArrow(Solo48):
    icon_id = "mobile-phone-outgoing-arrow"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("phone forwarding out", "mobile call outgoing")
    keywords = ("phone", "transfer", "send", "right")

    def build(self) -> None:
        r = 4
        self.add_line("phone-right-upper", (24, 15), (24, 8))
        self.add_arc("phone-ne", (24, 8), (20, 4), radius_x=r, sweep=False)
        self.add_line("phone-top", (20, 4), (12, 4))
        self.add_arc("phone-nw", (12, 4), (8, 8), radius_x=r, sweep=False)
        self.add_line("phone-left", (8, 8), (8, 40))
        self.add_arc("phone-sw", (8, 40), (12, 44), radius_x=r, sweep=False)
        self.add_line("phone-bottom", (12, 44), (20, 44))
        self.add_arc("phone-se", (20, 44), (24, 40), radius_x=r, sweep=False)
        self.add_line("phone-right-lower", (24, 40), (24, 33))
        self.add_contour("phone-frame", "phone-right-upper", "phone-ne", "phone-top", "phone-nw", "phone-left", "phone-sw", "phone-bottom", "phone-se", "phone-right-lower")
        self.add_line("lower-bezel", (8, 35), (24, 35))
        self.relate("connect", "lower-bezel", "phone-left")
        self.relate("connect", "lower-bezel", "phone-right-lower")

        self.add_line("arrow-shaft", (18, 24), (40, 24))
        self.add_polyline("arrow-head", (34, 18), (40, 24), (34, 30))
        self.relate("connect", "arrow-shaft", "arrow-head-1")
        self.relate("connect", "arrow-shaft", "arrow-head-2")
