"""Independent 32px profile of bag-photography.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1342f536-c927-4566-8887-d52e83745630'
SOURCE_PATH = 'pictographic-primitives/photography/bag_1342f536-c927-4566-8887-d52e83745630.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1342f536-c927-4566-8887-d52e83745630', 'pictographic-primitives/photography/bag_1342f536-c927-4566-8887-d52e83745630.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bag-photography',)
SOLO_SOURCE_ICON_IDS = ('bag-photography',)
REFERENCE_EXPORT_SHA256 = '7ff31929be22397b73923723917f01cad39286b6ea9c7199944b177063c95000'

class Drawing(Sub32):
    icon_id = 'bag-photography-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'photography'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 10), (22, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (5, 10), (10, 10))
        self.add_line('p2-r1-2', (10, 10), (22, 10))
        self.add_line('p2-r1-3', (22, 10), (27, 10))
        self.add_arc('p2-r1-4', (27, 10), (30, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (30, 13), (30, 16))
        self.add_line('p2-r1-6', (30, 16), (30, 24))
        self.add_arc('p2-r1-7', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-8', (27, 27), (5, 27))
        self.add_arc('p2-r1-9', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-10', (2, 24), (2, 16))
        self.add_line('p2-r1-11', (2, 16), (2, 13))
        self.add_arc('p2-r1-12', (2, 13), (5, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
        self.add_bezier('p3-r1-1', (2, 16), ((6, 19), (11, 20), (16, 20)))
        self.add_bezier('p3-r1-2', (16, 20), ((21, 20), (26, 19), (30, 16)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p2-r1-5', 'p3-r1-2')
        self.relate("connect", 'p2-r1-6', 'p3-r1-2')
        self.relate("connect", 'p2-r1-10', 'p3-r1-1')
        self.relate("connect", 'p2-r1-11', 'p3-r1-1')
