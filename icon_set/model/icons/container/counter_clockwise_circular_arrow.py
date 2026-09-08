"""An open circular arrow used as an enclosing container.

User explicitly confirmed the container family for this batch reference.
CIRCLE: visible radius 32 about (32,32). The loop has radius 28 about
(34,32), reaching x=62 on its centerline, leaving room for the arrowhead
on the left. Its deliberate rightward offset balances that arrowhead.
Lucide rotate-ccw informed the coherent long circular sweep and attached
chevron; the source supplies the left/downward tip and lower-left opening.
Hosting (compose.py): check valid; plus and heart do not fit (arrowhead clearance).
No semantic detail was dropped. Geometry is authored directly on CONTAINER64.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class CounterClockwiseCircularArrow(Container64):
    icon_id = "counter-clockwise-circular-arrow"
    keyshape = Keyshape.CIRCLE
    aliases = ("counterclockwise-arrow-container", "circular-arrow-container")
    keywords = ("circular", "arrow", "counterclockwise", "ring", "refresh", "undo")

    def build(self) -> None:
        self.add_arc("loop", (34, 60), (6, 32), radius_x=28,
                     large_arc=True, sweep=False)
        self.add_polyline("arrowhead", (4, 22), (6, 32), (16, 27))
        self.relate("connect", "loop", "arrowhead")
