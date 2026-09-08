"""A rounded speech enclosure with a triangular tail at the lower left.
The tail is intentionally asymmetric and all source features are retained.

Keyshape SQUARE; centerline extremes recorded in build below.
Lucide message-square informs the single contour and deliberate tail corners. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class RoundedChatMessageBubble(Container64):
    icon_id = 'rounded-chat-message-bubble'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('rounded', 'chat', 'message', 'bubble')

    def build(self) -> None:
        # Centerline extremes (2,2)-(62,62); body floor at y=49.
        self.add_line("top", (10, 2), (54, 2))
        self.add_arc("ne", (54, 2), (62, 10), radius_x=8)
        self.add_line("right", (62, 10), (62, 41))
        self.add_arc("se", (62, 41), (54, 49), radius_x=8)
        self.add_line("floor", (54, 49), (29, 49))
        self.add_line("tail-outer", (29, 49), (15, 62))
        self.add_line("tail-inner", (15, 62), (15, 49))
        self.add_line("floor-left", (15, 49), (10, 49))
        self.add_arc("sw", (10, 49), (2, 41), radius_x=8)
        self.add_line("left", (2, 41), (2, 10))
        self.add_arc("nw", (2, 10), (10, 2), radius_x=8)
        self.add_contour("outline", "top", "ne", "right", "se", "floor", "tail-outer", "tail-inner", "floor-left", "sw", "left", "nw", closed=True)
