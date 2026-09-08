"""A desktop screen with a post stand or bezel.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide monitor: rounded screen and centered stand; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check does not fit.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class DesktopMonitor(Container64):
    icon_id = 'desktop-monitor'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('desktop', 'monitor')

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
        self.add_line('stem', (32, 46), (32, 62))
        self.add_line('foot', (20, 62), (44, 62))
        self.relate("connect", 'stem', 'screen')
        self.relate("connect", 'stem', 'foot')
