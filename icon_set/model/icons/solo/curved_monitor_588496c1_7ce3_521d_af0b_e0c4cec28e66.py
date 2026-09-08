"""A bowed widescreen monitor with a splayed stand and floor bar.

HRECT_L extremes (2,5)-(46,40) suit the wide display. Lucide monitor
informs a simple stand. Matched shallow end arcs flow into a level centre.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '588496c1-7ce3-521d-af0b-e0c4cec28e66'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/screen curved_588496c1-7ce3-521d-af0b-e0c4cec28e66.svg'


class CurvedMonitor(Solo48):
    icon_id = 'curved-monitor'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('monitor', 'curved', 'screen', 'display', 'widescreen', 'gaming', 'computer', 'ultrawide')

    def build(self) -> None:
        self.add_arc('top-left', (2, 5), (14, 7), radius_x=37, radius_y=37, sweep=False, large_arc=False)
        self.add_line('top-middle', (14, 7), (34, 7))
        self.add_arc('top-right', (34, 7), (46, 5), radius_x=37, radius_y=37, sweep=False, large_arc=False)
        self.add_line('side-right', (46, 5), (46, 35))
        self.add_arc('bottom-right', (46, 35), (34, 33), radius_x=37, radius_y=37, sweep=False, large_arc=False)
        self.add_line('bottom-middle-1', (34, 33), (28, 33))
        self.add_line('bottom-middle-2', (28, 33), (20, 33))
        self.add_line('bottom-middle-3', (20, 33), (14, 33))
        self.add_arc('bottom-left', (14, 33), (2, 35), radius_x=37, radius_y=37, sweep=False, large_arc=False)
        self.add_line('side-left', (2, 35), (2, 5))
        self.add_contour('screen', 'top-left', 'top-middle', 'top-right', 'side-right', 'bottom-right', 'bottom-middle-1', 'bottom-middle-2', 'bottom-middle-3', 'bottom-left', 'side-left', closed=True)
        self.add_polyline('stand', (20, 33), (17, 43), (31, 43), (28, 33), closed=False)
        self.relate('connect', 'screen', 'stand')
        self.add_line('base-left', (12, 43), (17, 43))
        self.add_line('base-right', (31, 43), (36, 43))
        self.relate('connect', 'stand', 'base-left')
        self.relate('connect', 'stand', 'base-right')
