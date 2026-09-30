"""A circular target ring with four ticks crossing its perimeter.

Keyshape CIRCLE: visible radius 32 about (32,32).
Reference: batch_16 supplied renders; Lucide crosshair: circular ring and cardinal ticks.
All four crossing ticks retained, mirrored on both axes.
Hosting (compose.py): plus does not fit, heart does not fit, check does not fit.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (target-crosshair-symbol CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class TargetCrosshairSymbol(Container64):
    icon_id = 'target-crosshair-symbol'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('target', 'crosshair', 'symbol')

    def build(self) -> None:
        self.add_arc('ring-0', (10, 32), (54, 32), radius_x=22)
        self.add_arc('ring-1', (54, 32), (10, 32), radius_x=22)
        self.add_line('top', (32, 4), (32, 17))
        self.add_line('right', (60, 32), (47, 32))
        self.add_line('bottom', (32, 60), (32, 47))
        self.add_line('left', (4, 32), (17, 32))
        self.add_contour('ring', 'ring-0', 'ring-1', closed=True)
        self.relate('connect', 'top', 'ring')
        self.relate('connect', 'right', 'ring')
        self.relate('connect', 'bottom', 'ring')
        self.relate('connect', 'left', 'ring')
