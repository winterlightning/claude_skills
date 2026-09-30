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
        self.add_line('head-upper', (33, 6), (25, 14))
        self.add_line('head-lower', (25, 14), (33, 22))
        self.add_line('top-edge', (25, 14), (51, 14))
        self.add_line('top-stub', (13, 14), (18, 14))
        self.add_arc('corner-ne', (51, 14), (58, 23), radius_x=7, radius_y=9)
        self.add_line('side-right', (58, 23), (58, 37))
        self.add_arc('corner-se', (58, 37), (51, 46), radius_x=7, radius_y=9)
        self.add_line('floor', (51, 46), (27, 46))
        self.add_line('tail-outer', (27, 46), (13, 58))
        self.add_line('tail-inner', (13, 58), (13, 46))
        self.add_arc('corner-sw', (13, 46), (6, 37), radius_x=7, radius_y=9)
        self.add_line('side-left', (6, 37), (6, 23))
        self.add_arc('corner-nw', (6, 23), (13, 14), radius_x=7, radius_y=9)
        self.add_contour('head', 'head-upper', 'head-lower')
        self.add_contour('frame', 'corner-ne', 'side-right', 'corner-se', 'floor', 'tail-outer', 'tail-inner', 'corner-sw', 'side-left', 'corner-nw')
        self.relate('connect', 'head', 'top-edge')
        self.relate('connect', 'top-edge', 'frame')
        self.relate('connect', 'frame', 'top-stub')
