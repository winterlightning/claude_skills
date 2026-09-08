"""A circular aiming enclosure with inward cardinal ticks.

CIRCLE: visible radius 32; cardinal ink extremes 0 and 64. Lucide
crosshair supplies quarter-circle construction and radial attachments.
All four ticks retained, mirrored about both axes.
Batch 01 hosting measured with compose.py: plus, heart, check pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class AimingReticle(Container64):
    icon_id = 'aiming-reticle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('circular-target-reticle', 'circular-aiming-reticle',)
    keywords = ('aiming', 'reticle')

    def build(self) -> None:
        self.add_arc("ring-0", (32, 2), (62, 32), radius_x=30)
        self.add_arc("ring-1", (62, 32), (32, 62), radius_x=30)
        self.add_arc("ring-2", (32, 62), (2, 32), radius_x=30)
        self.add_arc("ring-3", (2, 32), (32, 2), radius_x=30)
        self.add_contour("ring", "ring-0", "ring-1", "ring-2", "ring-3", closed=True)
        self.add_line("tick-0", (32, 2), (32, 10))
        self.relate("connect", "ring", "tick-0")
        self.add_line("tick-1", (62, 32), (54, 32))
        self.relate("connect", "ring", "tick-1")
        self.add_line("tick-2", (32, 62), (32, 54))
        self.relate("connect", "ring", "tick-2")
        self.add_line("tick-3", (2, 32), (10, 32))
        self.relate("connect", "ring", "tick-3")
