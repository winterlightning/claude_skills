# Variant of desktop-monitor-bottom-bezel; parent file remains unchanged.
"""A desktop screen with a bezel stand or bezel.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide monitor: rounded screen and centered stand; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class DesktopMonitorBottomBezelVariant2(Container64):
    icon_id = 'desktop-monitor-bottom-bezel-v2'
    variant_of = 'desktop-monitor-bottom-bezel'
    variant_label = 'More interior space'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('desktop', 'monitor', 'bottom', 'bezel')

    def build(self) -> None:
        self.add_line('screen-0', (8, 2), (56, 2))
        self.add_arc('screen-1', (56, 2), (62, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-2', (62, 8), (62, 48))
        self.add_arc('screen-3', (62, 48), (56, 54), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-4', (56, 54), (8, 54))
        self.add_arc('screen-5', (8, 54), (2, 48), radius_x=6, radius_y=6, sweep=True)
        self.add_line('screen-6', (2, 48), (2, 8))
        self.add_arc('screen-7', (2, 8), (8, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.add_line('bezel', (2, 44), (62, 44))
        self.relate('connect', 'bezel', 'screen')
        self.add_line('stand-left', (26, 54), (24, 62))
        self.add_line('stand-right', (38, 54), (40, 62))
        self.add_line('foot', (18, 62), (46, 62))
        self.relate('connect', 'stand-left', 'screen')
        self.relate('connect', 'stand-right', 'screen')
        self.relate('connect', 'stand-left', 'foot')
        self.relate('connect', 'stand-right', 'foot')
