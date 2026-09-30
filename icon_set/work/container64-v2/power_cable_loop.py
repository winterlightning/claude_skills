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

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (power-cable-loop CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class PowerCableLoopContainer(Container64):
    icon_id = 'power-cable-loop'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('circular-electrical-power-cable', 'cable-loop', 'plug-ring')
    keywords = ('cable', 'cables', 'plug', 'plugs', 'power', 'cord', 'lead', 'electrical', 'charger', 'loop', 'ring', 'coil')

    def build(self) -> None:
        self.add_arc('cable', (50, 28), (34, 18), radius_x=21, large_arc=True)
        self.add_line('plug-1', (42, 12), (34, 12))
        self.add_line('plug-2', (34, 12), (34, 18))
        self.add_line('plug-3', (34, 18), (34, 24))
        self.add_line('plug-4', (34, 24), (42, 24))
        self.add_contour('plug', 'plug-1', 'plug-2', 'plug-3', 'plug-4')
        self.relate('connect', 'cable', 'plug')
