"""Power cable coiled into a ring, ending in a two-pin plug at the top.

Reconstructed from the reference render. The subject is a cable looped into an
almost-closed circle: the loop is the container, the break at the upper right
is what makes it a cable rather than a ring, and the plug at the top is the
only thing that says *power*.

The loop is deliberately off-centre -- radius 25 about (32,37) rather than the
concentric radius 30 -- because the plug rides on it tangentially at twelve
o'clock and has to fit inside the CIRCLE envelope with it. Dropping the loop
five units buys the plug its band above the ring; the loop's own six o'clock
point then reaches radius 30, which is what touches the envelope. The
reference's loop sits low in the same way, for the same reason.

The plug is reduced to its back and its two pins. A closed body with pins
emerging from its face cannot be drawn here: the pins need 8 between
centrelines from each other *and* from the body's own top and bottom edges,
which puts the body at 24 units tall -- more than a third of the canvas, for a
detail. Back-plus-pins keeps the two pins the full 12 apart with nothing
crowded, and the cable entering the middle of the back is what reads it as a
plug rather than a bracket.

The cable meets the back at its midpoint, perpendicular to it, and that shared
vertex is the one declared contact. Everything else is measured: the loose end
at (52,22) clears the lower pin by 8.94 on centrelines -- almost five units of
white -- which is what fixes the pins at 12 long: at 14 the loose end would
have to move round to 74 degrees and the break would stop reading as a break.

Local Lucide plug informed the review of the two pins and cable attachment.
The loop retains its deliberate vertical offset and upper-right opening.

Batch 01 hosting measured with compose.py: plus pass. heart, check do not pass (including uncertified review).
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class PowerCableLoopContainer(Container64):
    icon_id = "power-cable-loop"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ("circular-electrical-power-cable", "cable-loop", "plug-ring")
    keywords = (
        "cable", "cables", "plug", "plugs", "power", "cord", "lead",
        "electrical", "charger", "loop", "ring", "coil",
    )

    def build(self) -> None:
        # CIRCLE-64 is visible radius 32 about (32,32), centreline radius 30.
        #
        # The loop: one 306.9-degree arc of radius 25 about (32,37), running
        # clockwise from the loose end at (52,22) -- 53 degrees round from the
        # top, the break the reference shows -- through three, six and nine
        # o'clock and up to the plug at (32,12). Six o'clock lands at (32,62),
        # radius 30 from the canvas centre, so the artwork touches its
        # envelope there and nowhere overruns it: the loop's farthest point
        # from (32,32) is exactly its own centre offset plus its radius.
        self.add_arc(
            "cable", (52, 22), (32, 12), radius_x=25, large_arc=True, sweep=True,
        )

        # The plug, drawn back-first: upper pin, back down through the point
        # the cable arrives at, lower pin. The two pins are 12 apart, half
        # again the minimum, and the back's midpoint (32,12) is the loop's
        # twelve o'clock, where its tangent is horizontal -- so the cable
        # enters the back square-on and leaves the pins pointing the way the
        # loop was travelling.
        self.add_polyline(
            "plug",
            (44, 6), (32, 6), (32, 12), (32, 18), (44, 18),
        )
        self.relate("connect", "cable", "plug")
