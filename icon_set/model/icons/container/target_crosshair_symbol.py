"""A circular target ring with four ticks crossing its perimeter.

Keyshape CIRCLE: visible radius 32 about (32,32).
Reference: batch_16 supplied renders; Lucide crosshair: circular ring and cardinal ticks.
All four crossing ticks retained, mirrored on both axes.
Hosting (compose.py): plus does not fit, heart does not fit, check does not fit.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class TargetCrosshairSymbol(Container64):
    icon_id = 'target-crosshair-symbol'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('target', 'crosshair', 'symbol')

    def build(self) -> None:
        self.add_arc('ring-0', (8, 32), (56, 32), radius_x=24, radius_y=24, sweep=True)
        self.add_arc('ring-1', (56, 32), (8, 32), radius_x=24, radius_y=24, sweep=True)
        self.add_contour('ring', 'ring-0', 'ring-1', closed=True)
        self.add_line('top', (32, 2), (32, 15))
        self.relate("connect", 'top', 'ring')
        self.add_line('right', (62, 32), (49, 32))
        self.relate("connect", 'right', 'ring')
        self.add_line('bottom', (32, 62), (32, 49))
        self.relate("connect", 'bottom', 'ring')
        self.add_line('left', (2, 32), (15, 32))
        self.relate("connect", 'left', 'ring')
