"""Two concentric circular outlines form a double-ring enclosure.

Keyshape CIRCLE: visible bounds (0, 0, 64, 64).
Lucide circle informs exact shared-center arcs. Both source ring references map
to this concept; their different ring gaps are unified at nine centerline units.
Outer centerline radius 30, inner radius 21; all four outer extrema are 2 and 62.
Hosting measured with compose.py: plus passes, heart does not pass, check does not pass.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class DoubleConcentricCircles(Container64):
    icon_id = 'double-concentric-circles'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('two-concentric-circles', 'double-concentric-ring-symbol', 'double-ring', 'target-bullseye-symbol')
    keywords = ('circle', 'ring', 'concentric', 'target')

    def build(self) -> None:
        self.add_arc('outer-ring-top', (2, 32), (62, 32), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('outer-ring-bottom', (62, 32), (2, 32), radius_x=30, radius_y=30, sweep=True)
        self.add_contour('outer-ring', 'outer-ring-top', 'outer-ring-bottom', closed=True)
        self.add_arc('inner-ring-top', (11, 32), (53, 32), radius_x=21, radius_y=21, sweep=True)
        self.add_arc('inner-ring-bottom', (53, 32), (11, 32), radius_x=21, radius_y=21, sweep=True)
        self.add_contour('inner-ring', 'inner-ring-top', 'inner-ring-bottom', closed=True)
