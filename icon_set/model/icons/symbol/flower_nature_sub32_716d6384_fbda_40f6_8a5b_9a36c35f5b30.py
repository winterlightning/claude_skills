"""Independent 32px profile of flower-nature.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '716d6384-fbda-40f6-8a5b-9a36c35f5b30'
SOURCE_PATH = 'pictographic-primitives/nature/flower_716d6384-fbda-40f6-8a5b-9a36c35f5b30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('716d6384-fbda-40f6-8a5b-9a36c35f5b30', 'pictographic-primitives/nature/flower_716d6384-fbda-40f6-8a5b-9a36c35f5b30.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flower-nature',)
SOLO_SOURCE_ICON_IDS = ('flower-nature',)
REFERENCE_EXPORT_SHA256 = 'aae1a9ae3673dc034ab5f8a8008f8d3f26a090b59e23587a55a7f9ae6ff07f51'

class Drawing(Sub32):
    icon_id = 'flower-nature-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    categories = ('nature', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 5), ((20, 5), (22, 7), (22, 10)))
        self.add_bezier('p1-r1-2', (22, 10), ((22, 9), (23, 9), (24, 9)))
        self.add_bezier('p1-r1-3', (24, 9), ((27, 9), (30, 12), (30, 15)))
        self.add_bezier('p1-r1-4', (30, 15), ((30, 18), (26, 20), (24, 20)))
        self.add_bezier('p1-r1-5', (24, 20), ((24, 21), (25, 22), (25, 23)))
        self.add_bezier('p1-r1-6', (25, 23), ((25, 26), (23, 27), (20, 27)))
        self.add_bezier('p1-r1-7', (20, 27), ((18, 27), (17, 27), (16, 25)))
        self.add_bezier('p1-r1-8', (16, 25), ((15, 26), (14, 27), (12, 27)))
        self.add_bezier('p1-r1-9', (12, 27), ((9, 27), (7, 26), (7, 23)))
        self.add_bezier('p1-r1-10', (7, 23), ((7, 22), (8, 21), (8, 20)))
        self.add_bezier('p1-r1-11', (8, 20), ((6, 20), (2, 18), (2, 15)))
        self.add_bezier('p1-r1-12', (2, 15), ((2, 12), (5, 9), (8, 9)))
        self.add_bezier('p1-r1-13', (8, 9), ((9, 9), (10, 9), (10, 10)))
        self.add_bezier('p1-r1-14', (10, 10), ((10, 7), (13, 5), (16, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
        self.add_arc('p2-r1-1', (13, 16), (19, 16), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (19, 16), (13, 16), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
