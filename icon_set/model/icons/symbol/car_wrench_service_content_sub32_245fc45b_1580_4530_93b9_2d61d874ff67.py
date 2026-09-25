"""Independent 32px profile of car-wrench-service-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '245fc45b-1580-4530-93b9-2d61d874ff67'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/245fc45b-1580-4530-93b9-2d61d874ff67.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('245fc45b-1580-4530-93b9-2d61d874ff67', 'icon_set/dist/gallery/combination-originals/245fc45b-1580-4530-93b9-2d61d874ff67.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-wrench-service-content',)
SOLO_SOURCE_ICON_IDS = ('car-wrench-service-content',)
REFERENCE_EXPORT_SHA256 = 'b20300aae8d2ead0165537d0c99dcd33867cd6e19fab1a027330f5637576058f'

class Drawing(Sub32):
    icon_id = 'car-wrench-service-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 13), (5, 8))
        self.add_line('p1-r1-2', (5, 8), (8, 5))
        self.add_line('p1-r1-3', (8, 5), (24, 5))
        self.add_line('p1-r1-4', (24, 5), (27, 8))
        self.add_line('p1-r1-5', (27, 8), (27, 13))
        self.add_line('p1-r1-6', (27, 13), (5, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 13), (8, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 13), (24, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (2, 20), (2, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (30, 27), (30, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (6, 24), (27, 24))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
