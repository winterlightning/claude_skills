"""A desktop screen with a flared stand or bezel.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide monitor: rounded screen and centered stand; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check does not fit.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class DesktopMonitorFlaredStand(Container64):
    icon_id = 'desktop-monitor-flared-stand'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('desktop', 'monitor', 'flared', 'stand')

    def build(self) -> None:
        self.add_line('screen-0', (8, 2), (56, 2))
        self.add_arc('screen-1', (56, 2), (62, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-2', (62, 8), (62, 40))
        self.add_arc('screen-3', (62, 40), (56, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-4', (56, 46), (8, 46))
        self.add_arc('screen-5', (8, 46), (2, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-6', (2, 40), (2, 8))
        self.add_arc('screen-7', (2, 8), (8, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.add_arc('stand-left', (26, 46), (14, 58), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('foot-left', (14, 58), (14, 62), radius_x=2, radius_y=2, sweep=False)
        self.add_line('foot', (14, 62), (50, 62))
        self.add_arc('foot-right', (50, 62), (50, 58), radius_x=2, radius_y=2, sweep=False)
        self.add_arc('stand-right', (50, 58), (38, 46), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('stand', 'stand-left', 'foot-left', 'foot', 'foot-right', 'stand-right', closed=False)
        self.relate("connect", 'stand', 'screen')
