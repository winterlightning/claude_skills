"""An open circular power enclosure with a small ring above its opening.

SQUARE: centerline extremes (2,2)-(62,62). The user explicitly confirmed
container classification. Lucide power original and atomic-debug inform
an open circular sweep, but the supplied reference's small top circle is
retained instead of substituting Lucide's vertical bar. Mirrored about x=32;
no source-defining detail is dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (minimalist-power-button SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class MinimalistPowerButton(Container64):
    icon_id = 'minimalist-power-button'
    keyshape = Keyshape.SQUARE
    aliases = ('power-ring-container',)
    keywords = ('power', 'button', 'switch', 'circle')

    def build(self) -> None:
        self.add_arc('outer-ne', (48, 19), (58, 36), radius_x=26, radius_y=22)
        self.add_arc('outer-se', (58, 36), (32, 58), radius_x=26, radius_y=22)
        self.add_arc('outer-sw', (32, 58), (6, 36), radius_x=26, radius_y=22)
        self.add_arc('outer-nw', (6, 36), (16, 19), radius_x=26, radius_y=22)
        self.add_arc('button-upper', (22, 16), (42, 16), radius_x=10)
        self.add_arc('button-lower', (42, 16), (22, 16), radius_x=10)
        self.add_contour('outer', 'outer-ne', 'outer-se', 'outer-sw', 'outer-nw')
        self.add_contour('button', 'button-upper', 'button-lower', closed=True)
