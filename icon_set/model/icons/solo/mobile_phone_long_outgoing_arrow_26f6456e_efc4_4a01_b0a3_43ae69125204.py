"""A rounded phone with a long right-pointing forwarding arrow.

Symbol plan: the phone is an open rounded contour with a bottom bezel;
the long arrow passes through a broad right opening. Lucide smartphone
informed the device corners and arrow-right the diagonal head.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "26f6456e-efc4-4a01-b0a3-43ae69125204"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/mobile phone call forwarding outgoing 3_26f6456e-efc4-4a01-b0a3-43ae69125204.svg"
AUTHOR = "gpt-6"


class MobilePhoneLongOutgoingArrow(Solo48):
    icon_id = "mobile-phone-long-outgoing-arrow"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/mobile"
    aliases = ("phone call forwarding", "long outgoing call arrow")
    keywords = ("phone", "transfer", "forward", "right")

    def build(self) -> None:
        r = 4
        self.add_line("phone-right-upper", (25, 13), (25, 12))
        self.add_arc("phone-ne", (25, 12), (21, 8), radius_x=r, sweep=False)
        self.add_line("phone-top", (21, 8), (8, 8))
        self.add_arc("phone-nw", (8, 8), (4, 12), radius_x=r, sweep=False)
        self.add_line("phone-left", (4, 12), (4, 36))
        self.add_arc("phone-sw", (4, 36), (8, 40), radius_x=r, sweep=False)
        self.add_line("phone-bottom", (8, 40), (21, 40))
        self.add_arc("phone-se", (21, 40), (25, 36), radius_x=r, sweep=False)
        self.add_line("phone-right-lower", (25, 36), (25, 31))
        self.add_contour("phone-frame", "phone-right-upper", "phone-ne", "phone-top", "phone-nw", "phone-left", "phone-sw", "phone-bottom", "phone-se", "phone-right-lower")
        self.add_line("lower-bezel", (4, 31), (25, 31))
        self.relate("connect", "lower-bezel", "phone-left")
        self.relate("connect", "lower-bezel", "phone-right-lower")

        self.add_line("arrow-shaft", (13, 22), (44, 22))
        self.add_polyline("arrow-head", (37, 15), (44, 22), (37, 29))
        self.relate("connect", "arrow-shaft", "arrow-head-1")
        self.relate("connect", "arrow-shaft", "arrow-head-2")
