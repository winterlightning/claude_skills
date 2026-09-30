"""A desktop screen with a post stand or bezel.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide monitor: rounded screen and centered stand; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check does not fit.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (desktop-monitor SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class DesktopMonitor(Container64):
    icon_id = 'desktop-monitor'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('desktop', 'monitor')

    def build(self) -> None:
        self.add_line('screen-0', (12, 6), (52, 6))
        self.add_arc('screen-1', (52, 6), (58, 12), radius_x=6)
        self.add_line('screen-2', (58, 12), (58, 38))
        self.add_arc('screen-3', (58, 38), (52, 44), radius_x=6)
        self.add_line('screen-4', (52, 44), (12, 44))
        self.add_arc('screen-5', (12, 44), (6, 38), radius_x=6)
        self.add_line('screen-6', (6, 38), (6, 12))
        self.add_arc('screen-7', (6, 12), (12, 6), radius_x=6)
        self.add_line('stem', (32, 44), (32, 58))
        self.add_line('foot', (22, 58), (42, 58))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.relate('connect', 'stem', 'screen')
        self.relate('connect', 'stem', 'foot')
