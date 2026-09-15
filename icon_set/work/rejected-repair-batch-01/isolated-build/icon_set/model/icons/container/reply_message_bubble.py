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
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class ReplyMessageBubbleContainer(Container64):
    icon_id = "reply-message-bubble"
    keyshape = Keyshape.SQUARE
    aliases = ("message-reply", "reply-bubble", "speech-bubble-reply")
    keywords = (
        "reply", "respond", "message", "bubble", "speech", "comment",
        "chat", "conversation", "discourse", "return", "back",
    )

    def build(self) -> None:
        # SQUARE-64 is (0, 0)-(64, 64) visible, (2, 2)-(62, 62) centerline. The
        # trace reports aspect 0.959 and painted bounds (3.0,1.8)-(61.0,62.2),
        # so the square is the fit; the four extremes are the bubble's left
        # side (x 6), its right side (x 58), the chevron's upper arm (y 6)
        # and the tail tip (y 58).
        #
        # Vertical rhythm, taken from the reference and rescaled to the 52
        # units between those extremes: chevron apex 6, top edge 13, floor
        # 48, tail tip 58 -- 7 / 35 / 10 against the reference's 7.0 / 39.8 /
        # 11.2 out of 58.

        # The chevron. Two straight arms meeting at (25, 10), on the top edge
        # and 8 clear of the stub that edge resumes from on the left. Kept
        # arc-free and in its own contour: that 8 is the CONTAINER64
        # minimum, and a straight-to-straight pair is the only kind the
        # spacing engine measures exactly. Legs of 7 at 45 degrees put the
        # upper arm on y 6 -- the keyshape's top -- and the lower arm at
        # y 20, matching the reference's head, which is a shade taller than
        # it is wide.
        self.add_line("head-upper", (33, 2), (25, 10))
        self.add_line("head-lower", (25, 10), (33, 18))
        self.add_contour("head", "head-upper", "head-lower")

        # The shaft: the arrow's tail and the bubble's top edge are the same
        # line. Its own path for the same exactness reason, sharing (25, 10)
        # with the chevron and (53, 10) with the north-east corner.
        self.add_line("top-edge", (25, 10), (53, 10))

        # What is left of the top edge west of the break, likewise its own
        # straight path, sharing (11, 10) with the north-west corner.
        self.add_line("top-stub", (11, 10), (16, 10))

        # The frame, one contour from the break's right end round to its
        # left. Every corner is a quarter circle of radius 8 whose centre is
        # on the grid, so each meets its neighbours at a shared axis extreme
        # and no join kinks. The floor stops at 28 for the tail, which drops
        # to the tip at (11, 62) and returns up the vertical the south-west
        # corner hands it -- the reference has no floor to the left of the
        # tail either.
        self.add_arc("corner-ne", (53, 10), (62, 19), radius_x=9)
        self.add_line("side-right", (62, 19), (62, 41))
        self.add_arc("corner-se", (62, 41), (53, 50), radius_x=9)
        self.add_line("floor", (53, 50), (27, 50))
        self.add_line("tail-outer", (27, 50), (11, 62))
        self.add_line("tail-inner", (11, 62), (11, 50))
        self.add_arc("corner-sw", (11, 50), (2, 41), radius_x=9)
        self.add_line("side-left", (2, 41), (2, 19))
        self.add_arc("corner-nw", (2, 19), (11, 10), radius_x=9)
        self.add_contour(
            "frame",
            "corner-ne", "side-right", "corner-se", "floor", "tail-outer",
            "tail-inner", "corner-sw", "side-left", "corner-nw",
        )

        self.relate("connect", "head", "top-edge")
        self.relate("connect", "top-edge", "frame")
        self.relate("connect", "frame", "top-stub")
