"""A rounded speech enclosure with a triangular tail at the lower left.
The tail is intentionally asymmetric and all source features are retained.

Keyshape SQUARE; centerline extremes recorded in build below.
Lucide message-square informs the single contour and deliberate tail corners. Rebuilt on CONTAINER64 with integer geometry.
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (rounded-chat-message-bubble SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class RoundedChatMessageBubble(Container64):
    icon_id = 'rounded-chat-message-bubble'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('rounded', 'chat', 'message', 'bubble')

    def build(self) -> None:
        self.add_line('top', (14, 6), (50, 6))
        self.add_arc('ne', (50, 6), (58, 14), radius_x=8)
        self.add_line('right', (58, 14), (58, 37))
        self.add_arc('se', (58, 37), (50, 45), radius_x=8)
        self.add_line('floor', (50, 45), (29, 45))
        self.add_line('tail-outer', (29, 45), (19, 58))
        self.add_line('tail-inner', (19, 58), (19, 45))
        self.add_line('floor-left', (19, 45), (14, 45))
        self.add_arc('sw', (14, 45), (6, 37), radius_x=8)
        self.add_line('left', (6, 37), (6, 14))
        self.add_arc('nw', (6, 14), (14, 6), radius_x=8)
        self.add_contour('outline', 'top', 'ne', 'right', 'se', 'floor', 'tail-outer', 'tail-inner', 'floor-left', 'sw', 'left', 'nw', closed=True)
