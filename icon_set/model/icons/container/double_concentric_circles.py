"""Two concentric circular outlines form a double-ring enclosure.

Keyshape CIRCLE: visible bounds (0, 0, 64, 64).
Lucide circle informs exact shared-center arcs. Both source ring references map
to this concept; their different ring gaps are unified at nine centerline units.
Outer centerline radius 30, inner radius 21; all four outer extrema are 2 and 62.
Hosting measured with compose.py: plus passes, heart does not pass, check does not pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (double-concentric-circles CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class DoubleConcentricCircles(Container64):
    icon_id = 'double-concentric-circles'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('two-concentric-circles', 'double-concentric-ring-symbol', 'double-ring', 'target-bullseye-symbol')
    keywords = ('circle', 'ring', 'concentric', 'target')

    def build(self) -> None:
        self.add_arc('outer-ring-top', (4, 32), (60, 32), radius_x=28)
        self.add_arc('outer-ring-bottom', (60, 32), (4, 32), radius_x=28)
        self.add_arc('inner-ring-top', (12, 32), (52, 32), radius_x=20)
        self.add_arc('inner-ring-bottom', (52, 32), (12, 32), radius_x=20)
        self.add_contour('outer-ring', 'outer-ring-top', 'outer-ring-bottom', closed=True)
        self.add_contour('inner-ring', 'inner-ring-top', 'inner-ring-bottom', closed=True)
