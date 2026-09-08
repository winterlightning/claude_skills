"""A low hard-drive enclosure with a sloping lid, indicator and two feet.

HRECT_L extremes (2,8)-(46,40) fit a low case. Lucide hard-drive informs
the lid/front relationship and dot indicator. Source perspective is retained.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f909303-878b-407a-8340-dbc1a2e3cfae'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/hard drive_3f909303-878b-407a-8340-dbc1a2e3cfae.svg'


class DesktopHardDriveEnclosure(Solo48):
    icon_id = 'desktop-hard-drive-enclosure'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('hard drive', 'hdd', 'enclosure', 'storage', 'server', 'disk', 'hardware', 'computer')

    def build(self) -> None:
        self.add_polyline('lid', (2, 21), (12, 8), (36, 8), (46, 21), closed=False)
        self.add_line('front-top', (2, 21), (46, 21))
        self.add_line('front-right', (46, 21), (46, 31))
        self.add_arc('front-se', (46, 31), (42, 35), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-right', (42, 35), (38, 35))
        self.add_line('base-middle', (38, 35), (10, 35))
        self.add_line('base-left', (10, 35), (6, 35))
        self.add_arc('front-sw', (6, 35), (2, 31), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('front-left', (2, 31), (2, 21))
        self.add_contour('front', 'front-top', 'front-right', 'front-se', 'base-right', 'base-middle', 'base-left', 'front-sw', 'front-left', closed=True)
        self.relate('connect', 'lid', 'front')
        self.add_dot('indicator', (12, 28))
        self.add_line('foot-left', (10, 35), (10, 40))
        self.relate('connect', 'front', 'foot-left')
        self.add_line('foot-right', (38, 35), (38, 40))
        self.relate('connect', 'front', 'foot-right')
