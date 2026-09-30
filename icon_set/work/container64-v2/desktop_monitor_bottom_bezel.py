"""A desktop screen with a bezel stand or bezel.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide monitor: rounded screen and centered stand; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (desktop-monitor-bottom-bezel SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class DesktopMonitorBottomBezel(Container64):
    icon_id = 'desktop-monitor-bottom-bezel'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('desktop', 'monitor', 'bottom', 'bezel')

    def build(self) -> None:
        self.add_line('screen-0', (12, 6), (52, 6))
        self.add_arc('screen-1', (52, 6), (58, 12), radius_x=6)
        self.add_line('screen-2', (58, 12), (58, 44))
        self.add_arc('screen-3', (58, 44), (52, 50), radius_x=6)
        self.add_line('screen-4', (52, 50), (12, 50))
        self.add_arc('screen-5', (12, 50), (6, 44), radius_x=6)
        self.add_line('screen-6', (6, 44), (6, 12))
        self.add_arc('screen-7', (6, 12), (12, 6), radius_x=6)
        self.add_line('bezel', (6, 40), (58, 40))
        self.add_line('stand-left', (28, 50), (26, 58))
        self.add_line('stand-right', (36, 50), (38, 58))
        self.add_line('foot', (20, 58), (44, 58))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.relate('connect', 'bezel', 'screen')
        self.relate('connect', 'stand-left', 'screen')
        self.relate('connect', 'stand-right', 'screen')
        self.relate('connect', 'stand-left', 'foot')
        self.relate('connect', 'stand-right', 'foot')
