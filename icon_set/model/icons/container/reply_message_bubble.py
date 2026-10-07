"""Reply message bubble: a speech bubble whose top edge is broken by a
left-pointing arrow.

Reconstructed from the reference render. The identity is the break: the
bubble's top edge stops short of the north-west corner, and the arrow's
vertex takes over from there, so the shaft the arrow points away from *is*
the top edge. Drawn as two separate marks stacked above the frame it reads
as an annotation; drawn as one interrupted line it reads as a reply.

Lucide message-square-reply informed the rounded enclosure and clear arrow
join; the supplied source keeps the arrow integrated into the top edge.

Everything the reference carries survives at 64 -- outline, break, chevron,
tail. Nothing else was there to drop.

Hosting: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (reply-message-bubble SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class ReplyMessageBubbleContainer(Container64):
    icon_id = 'reply-message-bubble'
    keyshape = Keyshape.SQUARE
    aliases = ('message-reply', 'reply-bubble', 'speech-bubble-reply')
    keywords = ('reply', 'respond', 'message', 'bubble', 'speech', 'comment', 'chat', 'conversation', 'discourse', 'return', 'back')

    def build(self) -> None:
        # Bubble 6..58 x 10..50 (was 14..46) with a smaller reply arrow on its top edge, so it holds a symbol of 24
        # with a 4 px gap (was 14.5).
        self.add_line('head-upper', (29, 6), (25, 10))
        self.add_line('head-lower', (25, 10), (29, 14))
        self.add_line('top-edge', (25, 10), (51, 10))
        self.add_line('top-stub', (13, 10), (18, 10))
        self.add_arc('corner-ne', (51, 10), (58, 18), radius_x=7, radius_y=8)
        self.add_line('side-right', (58, 18), (58, 42))
        self.add_arc('corner-se', (58, 42), (51, 50), radius_x=7, radius_y=8)
        self.add_line('floor', (51, 50), (25, 50))
        self.add_line('tail-outer', (25, 50), (13, 58))
        self.add_line('tail-inner', (13, 58), (13, 50))
        self.add_arc('corner-sw', (13, 50), (6, 42), radius_x=7, radius_y=8)
        self.add_line('side-left', (6, 42), (6, 18))
        self.add_arc('corner-nw', (6, 18), (13, 10), radius_x=7, radius_y=8)
        self.add_contour('head', 'head-upper', 'head-lower')
        self.add_contour('frame', 'corner-ne', 'side-right', 'corner-se', 'floor', 'tail-outer', 'tail-inner', 'corner-sw', 'side-left', 'corner-nw')
        self.relate('connect', 'head', 'top-edge')
        self.relate('connect', 'top-edge', 'frame')
        self.relate('connect', 'top-stub', 'frame')
