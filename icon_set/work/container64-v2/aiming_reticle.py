"""A circular aiming enclosure with inward cardinal ticks.

CIRCLE: visible radius 32; cardinal ink extremes 0 and 64. Lucide
crosshair supplies quarter-circle construction and radial attachments.
All four ticks retained, mirrored about both axes.
Batch 01 hosting measured with compose.py: plus, heart, check pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (aiming-reticle CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class AimingReticle(Container64):
    icon_id = 'aiming-reticle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('circular-target-reticle', 'circular-aiming-reticle')
    keywords = ('aiming', 'reticle')

    def build(self) -> None:
        self.add_arc('ring-0', (32, 4), (60, 32), radius_x=28)
        self.add_arc('ring-1', (60, 32), (32, 60), radius_x=28)
        self.add_arc('ring-2', (32, 60), (4, 32), radius_x=28)
        self.add_arc('ring-3', (4, 32), (32, 4), radius_x=28)
        self.add_line('tick-0', (32, 4), (32, 12))
        self.add_line('tick-1', (60, 32), (52, 32))
        self.add_line('tick-2', (32, 60), (32, 52))
        self.add_line('tick-3', (4, 32), (12, 32))
        self.add_contour('ring', 'ring-0', 'ring-1', 'ring-2', 'ring-3', closed=True)
        self.relate('connect', 'ring', 'tick-0')
        self.relate('connect', 'ring', 'tick-1')
        self.relate('connect', 'ring', 'tick-2')
        self.relate('connect', 'ring', 'tick-3')
