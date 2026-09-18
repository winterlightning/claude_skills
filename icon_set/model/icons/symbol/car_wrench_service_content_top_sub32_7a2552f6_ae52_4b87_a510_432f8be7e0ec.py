"""Independent 32px profile of car-wrench-service-content-top.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7a2552f6-ae52-4b87-a510-432f8be7e0ec'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/7a2552f6-ae52-4b87-a510-432f8be7e0ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7a2552f6-ae52-4b87-a510-432f8be7e0ec', 'icon_set/dist/gallery/combination-originals/7a2552f6-ae52-4b87-a510-432f8be7e0ec.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-wrench-service-content-top',)
SOLO_SOURCE_ICON_IDS = ('car-wrench-service-content-top',)
REFERENCE_EXPORT_SHA256 = 'c42bc196a5645c7b7303b6af7e2ccc09ae6f353fa9dd1fa7ce452cd258d40049'

class Drawing(Sub32):
    icon_id = 'car-wrench-service-content-top-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 24), (5, 20))
        self.add_line('p1-r1-2', (5, 20), (8, 17))
        self.add_line('p1-r1-3', (8, 17), (24, 17))
        self.add_line('p1-r1-4', (24, 17), (27, 20))
        self.add_line('p1-r1-5', (27, 20), (27, 24))
        self.add_line('p1-r1-6', (27, 24), (5, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 24), (8, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 24), (24, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (2, 5), (2, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (30, 12), (30, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (6, 8), (27, 8))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
