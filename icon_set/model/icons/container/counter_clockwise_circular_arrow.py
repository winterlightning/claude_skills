"""An open circular arrow used as an enclosing container.

User explicitly confirmed the container family for this batch reference.
CIRCLE: visible radius 32 about (32,32). The loop has radius 24 about
(38,32), reaching x=62. A wider downward chevron extends visibly beyond
the left of the loop. Deliberate rightward offset leaves room for the head.
Lucide rotate-ccw informs the single circular sweep and attached chevron.
Hosting measured with compose.py: plus invalid, heart review, check invalid.
No semantic detail was dropped. Geometry is authored directly on CONTAINER64.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (counter-clockwise-circular-arrow CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: loop centred (38,32) r22 so it touches r28; arrowhead tip at r27.9.

v3 (2026-10-13): redrawn larger to host text labels and symbols, after reference faaa7d7c-6a73-4431-a100-a5eed3e2870a
(Twenty Four Hour Car Service; all 33 history / skip / rotation pairs share this container). Plan: one counter-
clockwise loop, centre (35,32) r25, from the bottom (35,57) round the right (60,32 = the CIRCLE envelope, r28 from
(32,32)) and the top to the left end (10,32); the gap stays at the lower left like the reference. One chevron
pointing down at the left end, arms 5 (the longest that keeps (5,27) inside the CIRCLE envelope). The room is the
loop centre (35,32): combos.json "center". The chevron is smaller than v2 (10 -> 5) so it no longer reaches into
the room; this lets two-digit labels sit at cap height 20-24 instead of 12. v2 is kept in
icon_set/work/container-combination64/originals/.
Lucide rotate-ccw informs the single sweep with the attached chevron. Hosting (combo.py --every): 9 text labels
fit (H 12 ZZZ, 20-24 digits), 24 symbols at 24 keep >= 6.7 px.
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
        cx, cy, r, arm = 35, 32, 25, 5  # loop centre and radius; chevron arm length
        self.add_arc('loop', (cx, cy + r), (cx - r, cy), radius_x=r, large_arc=True, sweep=False)
        self.add_polyline('arrowhead', (cx - r - arm, cy - arm), (cx - r, cy), (cx - r + arm, cy - arm))
        self.relate('connect', 'loop', 'arrowhead')
