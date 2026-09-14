# Variant of desktop-hard-drive-enclosure; parent file remains unchanged.
"""A low hard-drive enclosure with a sloping lid, indicator and two feet.

HRECT_L extremes (2,8)-(46,40) fit a low case. Lucide hard-drive informs
the lid/front relationship and dot indicator. Source perspective is retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3f909303-878b-407a-8340-dbc1a2e3cfae'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/hard drive_3f909303-878b-407a-8340-dbc1a2e3cfae.svg'
AUTHOR = 'gpt-6'

class DesktopHardDriveEnclosureVariant2(Solo48):
    icon_id = 'desktop-hard-drive-enclosure-v2'
    variant_of = 'desktop-hard-drive-enclosure'
    variant_label = 'Correct width and full spacing review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('hard drive', 'hdd', 'enclosure', 'storage', 'server', 'disk', 'hardware', 'computer')

    def build(self) -> None:
        self.add_polyline('lid', (4, 19), (12, 8), (36, 8), (44, 19), closed=False)
        self.add_line('front-top', (4, 19), (44, 19))
        self.add_line('front-right', (44, 19), (44, 33))
        self.add_arc('front-se', (44, 33), (40, 37), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-right', (40, 37), (38, 37))
        self.add_line('base-middle', (38, 37), (10, 37))
        self.add_line('base-left', (10, 37), (8, 37))
        self.add_arc('front-sw', (8, 37), (4, 33), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('front-left', (4, 33), (4, 19))
        self.add_contour('front', 'front-top', 'front-right', 'front-se', 'base-right', 'base-middle', 'base-left', 'front-sw', 'front-left', closed=True)
        self.relate('connect', 'lid', 'front')
        self.add_dot('indicator', (14, 28))
        self.add_line('foot-left', (10, 37), (10, 40))
        self.relate('connect', 'front', 'foot-left')
        self.add_line('foot-right', (38, 37), (38, 40))
        self.relate('connect', 'front', 'foot-right')
