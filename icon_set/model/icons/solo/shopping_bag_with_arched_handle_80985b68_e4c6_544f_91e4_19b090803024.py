"""Flared carrier bag with arched handle. Lucide shopping-bag informs simple rounded base construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80985b68-e4c6-544f-91e4-19b090803024'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.svg'
AUTHOR = 'astra-chatgpt'

class ShoppingBagWithArchedHandle(Solo48):
    icon_id = 'shopping-bag-with-arched-handle'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('shopping', 'bag', 'with', 'arched', 'handle')

    def build(self) -> None:
        # Centerline extremes (5,2)-(43,46).
        self.add_line("rim-1", (8,16), (14,16))
        self.add_line("rim-2", (14,16), (34,16))
        self.add_line("rim-3", (34,16), (40,16))
        self.add_line("side-right", (40,16), (43,40))
        self.add_arc("corner-right", (43,40), (37,46), radius_x=6)
        self.add_line("base", (37,46), (11,46))
        self.add_arc("corner-left", (11,46), (5,40), radius_x=6)
        self.add_line("side-left", (5,40), (8,16))
        self.add_contour("body", "rim-1", "rim-2", "rim-3", "side-right", "corner-right", "base", "corner-left", "side-left", closed=True)
        self.add_line("handle-left", (14,16), (14,12))
        self.add_arc("handle-arch", (14,12), (34,12), radius_x=10)
        self.add_line("handle-right", (34,12), (34,16))
        self.add_contour("handle", "handle-left", "handle-arch", "handle-right")
        self.relate("connect", "body", "handle")
