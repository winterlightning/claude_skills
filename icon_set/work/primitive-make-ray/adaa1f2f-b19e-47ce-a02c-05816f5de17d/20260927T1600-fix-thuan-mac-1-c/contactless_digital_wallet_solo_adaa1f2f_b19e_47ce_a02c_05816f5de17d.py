"""Contactless digital wallet: a bifold wallet with a front flap under two signal arcs.

Revision of the disapproved drawing, whose signal arcs dwarfed a small wallet. Plan
(SQUARE, centerline (6,6)-(42,42)): wallet body (6,27)-(42,42) with r3 corners and a
flap whose top edge runs from the top edge node (12,27) to (24,34) and then straight
down to the bottom edge node (24,42); two nested signal cubics above, outer apex at 6
(exact: endpoints 12, controls 4), inner apex at 15, endpoints at y=18 keeping 9 units
above the wallet. Lucide `wallet` and `wifi` inform the construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "adaa1f2f-b19e-47ce-a02c-05816f5de17d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__contactless-digital-wallet-solo/20260927T150749Z-thuan-mac-1/reference/wallet wifi_adaa1f2f-b19e-47ce-a02c-05816f5de17d.svg"
AUTHOR = "claude-fable-5-1"


class ContactlessDigitalWallet(Solo48):
    icon_id = "contactless-digital-wallet-solo"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ("wallet wifi", "tap to pay wallet", "nfc wallet")
    keywords = ("wallet", "contactless", "wifi", "signal", "payment", "nfc", "digital")

    def build(self) -> None:
        self.add_bezier("signal-outer", (8, 12), ((16, 4), (32, 4), (40, 12)))
        self.add_bezier("signal-inner", (14, 18), ((19, 14), (29, 14), (34, 18)))
        r = 3
        self.add_line("w-top-1", (9, 27), (12, 27))
        self.add_line("w-top-2", (12, 27), (39, 27))
        self.add_arc("w-tr", (39, 27), (42, 30), radius_x=r)
        self.add_line("w-right", (42, 30), (42, 39))
        self.add_arc("w-br", (42, 39), (39, 42), radius_x=r)
        self.add_line("w-bottom-1", (39, 42), (24, 42))
        self.add_line("w-bottom-2", (24, 42), (9, 42))
        self.add_arc("w-bl", (9, 42), (6, 39), radius_x=r)
        self.add_line("w-left", (6, 39), (6, 30))
        self.add_arc("w-tl", (6, 30), (9, 27), radius_x=r)
        self.add_contour("wallet", "w-top-1", "w-top-2", "w-tr", "w-right", "w-br",
                         "w-bottom-1", "w-bottom-2", "w-bl", "w-left", "w-tl", closed=True)
        self.add_polyline("flap", (12, 27), (24, 34), (24, 42))
        self.relate("connect", "flap", "wallet")
