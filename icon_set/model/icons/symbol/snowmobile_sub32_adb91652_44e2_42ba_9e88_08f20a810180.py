"""Independent 32px profile of snowmobile.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'adb91652-44e2-42ba-9e88-08f20a810180'
SOURCE_PATH = 'pictographic-primitives/symbol/snow scooter_adb91652-44e2-42ba-9e88-08f20a810180.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('adb91652-44e2-42ba-9e88-08f20a810180', 'pictographic-primitives/symbol/snow scooter_adb91652-44e2-42ba-9e88-08f20a810180.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowmobile',)
SOLO_SOURCE_ICON_IDS = ('snowmobile',)
REFERENCE_EXPORT_SHA256 = 'eaec920d3c5c3cebf76eaff3efce142868abda9a79a1dc762dac1bcbb8dc9232'

class Drawing(Sub32):
    icon_id = 'snowmobile-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 5), (15, 5))
        self.add_line('p1-r1-2', (15, 5), (19, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 20), (2, 17))
        self.add_arc('p2-r1-2', (2, 17), (5, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (5, 15), (12, 15))
        self.add_line('p2-r1-4', (12, 15), (13, 12))
        self.add_line('p2-r1-5', (13, 12), (19, 12))
        self.add_line('p2-r1-6', (19, 12), (23, 13))
        self.add_arc('p2-r1-7', (23, 13), (23, 20), radius_x=3, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-8', (23, 20), (22, 20))
        self.add_line('p2-r1-9', (22, 20), (16, 20))
        self.add_line('p2-r1-10', (16, 20), (13, 20))
        self.add_line('p2-r1-11', (13, 20), (5, 20))
        self.add_line('p2-r1-12', (5, 20), (2, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
        self.add_line('p3-r1-1', (22, 20), (22, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (17, 27), (22, 27))
        self.add_line('p4-r1-2', (22, 27), (26, 27))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (26, 27), (30, 23), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (2, 20), (13, 20), radius_x=6, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-5')
        self.relate('connect', 'p1-r1-2', 'p2-r1-6')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p2-r1-8', 'p3-r1-1')
        self.relate('connect', 'p2-r1-9', 'p3-r1-1')
        self.relate('connect', 'p2-r1-10', 'p6-r1-1')
        self.relate('connect', 'p2-r1-11', 'p6-r1-1')
        self.relate('connect', 'p2-r1-12', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
