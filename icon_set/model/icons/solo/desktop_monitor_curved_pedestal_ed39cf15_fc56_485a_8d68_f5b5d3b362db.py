"""A desktop monitor supported by a splayed curved pedestal.

HRECT_XL extremes (2,5)-(46,43) fit screen and stand. Lucide monitor
informs rounded screen corners; the mirrored waisted stand follows the source.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed39cf15-fc56-485a-8d68-f5b5d3b362db'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/monitor_ed39cf15-fc56-485a-8d68-f5b5d3b362db.svg'
AUTHOR = 'astra-chatgpt'


class DesktopMonitorCurvedPedestal(Solo48):
    icon_id = 'desktop-monitor-curved-pedestal'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('monitor', 'display', 'screen', 'desktop', 'computer', 'stand', 'pedestal', 'device')

    def build(self) -> None:
        self.add_line('screen-top', (6, 5), (42, 5))
        self.add_arc('screen-ne', (42, 5), (46, 9), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen-right', (46, 9), (46, 27))
        self.add_arc('screen-se', (46, 27), (42, 31), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen-bottom-0', (42, 31), (28, 31))
        self.add_line('screen-bottom-1', (28, 31), (20, 31))
        self.add_line('screen-bottom-2', (20, 31), (6, 31))
        self.add_arc('screen-sw', (6, 31), (2, 27), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('screen-left', (2, 27), (2, 9))
        self.add_arc('screen-nw', (2, 9), (6, 5), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('screen', 'screen-top', 'screen-ne', 'screen-right', 'screen-se', 'screen-bottom-0', 'screen-bottom-1', 'screen-bottom-2', 'screen-sw', 'screen-left', 'screen-nw', closed=True)
        self.add_arc('stand-left', (20, 31), (12, 43), radius_x=8, radius_y=12, sweep=True, large_arc=False)
        self.add_line('stand-base', (12, 43), (36, 43))
        self.add_arc('stand-right', (36, 43), (28, 31), radius_x=8, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('stand', 'stand-left', 'stand-base', 'stand-right', closed=False)
        self.relate('connect', 'screen', 'stand')
