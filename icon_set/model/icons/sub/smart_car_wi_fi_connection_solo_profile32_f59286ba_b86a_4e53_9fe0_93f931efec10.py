"""Independent 32px profile of smart-car-wi-fi-connection-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f59286ba-b86a-4e53-9fe0-93f931efec10'
SOURCE_PATH = 'pictographic-primitives/other/car wifi_f59286ba-b86a-4e53-9fe0-93f931efec10.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f59286ba-b86a-4e53-9fe0-93f931efec10', 'pictographic-primitives/other/car wifi_f59286ba-b86a-4e53-9fe0-93f931efec10.svg'),)
PROFILE_SOURCE_KEYS = ('solo/smart-car-wi-fi-connection-solo',)
SOLO_SOURCE_ICON_IDS = ('smart-car-wi-fi-connection-solo',)
REFERENCE_EXPORT_SHA256 = '83330e909c95140182b492c4da83a49c167d67240f89ba29d0bc9c5c1f8618af'

class Drawing(Sub32):
    icon_id = 'smart-car-wi-fi-connection-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 6), ((8, 4), (12, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((20, 2), (24, 4), (27, 6)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (11, 12), ((12, 10), (14, 10), (16, 10)))
        self.add_bezier('p2-r1-2', (16, 10), ((18, 10), (20, 10), (21, 12)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (9, 23), (12, 17))
        self.add_line('p3-r1-2', (12, 17), (20, 17))
        self.add_line('p3-r1-3', (20, 17), (23, 23))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (8, 23), (24, 23))
        self.add_arc('p4-r1-2', (24, 23), (27, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p4-r1-3', (27, 26), (27, 27))
        self.add_arc('p4-r1-4', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p4-r1-5', (24, 30), (8, 30))
        self.add_arc('p4-r1-6', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p4-r1-7', (5, 27), (5, 26))
        self.add_arc('p4-r1-8', (5, 26), (8, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', closed=False)
