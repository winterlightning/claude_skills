"""An open circular arrow used as an enclosing container.

User explicitly confirmed the container family for this batch reference.
CIRCLE: visible radius 32 about (32,32). The loop has radius 24 about
(38,32), reaching x=62. A wider downward chevron extends visibly beyond
the left of the loop. Deliberate rightward offset leaves room for the head.
Lucide rotate-ccw informs the single circular sweep and attached chevron.
Hosting measured with compose.py: plus invalid, heart review, check invalid.
No semantic detail was dropped. Geometry is authored directly on CONTAINER64.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (counter-clockwise-circular-arrow CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: loop centred (38,32) r22 so it touches r28; arrowhead tip at r27.9.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class CounterClockwiseCircularArrow(Container64):
    icon_id = 'counter-clockwise-circular-arrow'
    keyshape = Keyshape.CIRCLE
    aliases = ('counterclockwise-arrow-container', 'circular-arrow-container')
    keywords = ('circular', 'arrow', 'counterclockwise', 'ring', 'refresh', 'undo')

    def build(self) -> None:
        self.add_arc('loop', (38, 54), (16, 32), radius_x=22, large_arc=True, sweep=False)
        self.add_polyline('arrowhead', (6, 22), (16, 32), (26, 22))
        self.relate('connect', 'loop', 'arrowhead')
