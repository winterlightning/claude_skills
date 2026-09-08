"""A circular aiming enclosure with outward cardinal ticks.

CIRCLE: visible radius 32; cardinal ink extremes 0 and 64. Lucide
crosshair supplies quarter-circle construction and radial attachments.
All four ticks retained, mirrored about both axes.
Batch 01 hosting measured with compose.py: plus, heart, check pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class PrecisionCrosshair(Container64):
    icon_id = 'precision-crosshair'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('circular-target-symbol', 'circular-precision-target-crosshair',)
    keywords = ('precision', 'crosshair')

    def build(self) -> None:
        self.add_arc("ring-0", (32, 6), (58, 32), radius_x=26)
        self.add_arc("ring-1", (58, 32), (32, 58), radius_x=26)
        self.add_arc("ring-2", (32, 58), (6, 32), radius_x=26)
        self.add_arc("ring-3", (6, 32), (32, 6), radius_x=26)
        self.add_contour("ring", "ring-0", "ring-1", "ring-2", "ring-3", closed=True)
        self.add_line("tick-0", (32, 6), (32, 2))
        self.relate("connect", "ring", "tick-0")
        self.add_line("tick-1", (58, 32), (62, 32))
        self.relate("connect", "ring", "tick-1")
        self.add_line("tick-2", (32, 58), (32, 62))
        self.relate("connect", "ring", "tick-2")
        self.add_line("tick-3", (6, 32), (2, 32))
        self.relate("connect", "ring", "tick-3")
