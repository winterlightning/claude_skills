"""Independent 32px profile of box-805cc175.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '805cc175-0660-4025-842b-55f4fa16a559'
SOURCE_PATH = 'pictographic-primitives/shipping/box_805cc175-0660-4025-842b-55f4fa16a559.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('805cc175-0660-4025-842b-55f4fa16a559', 'pictographic-primitives/shipping/box_805cc175-0660-4025-842b-55f4fa16a559.svg'),)
PROFILE_SOURCE_KEYS = ('solo/box-805cc175',)
SOLO_SOURCE_ICON_IDS = ('box-805cc175',)
REFERENCE_EXPORT_SHA256 = 'fceb65d0b3681d0dc19c00ef82aa2b12457a7b766fab8a4db3cd71726e6d24d6'

class Drawing(Sub32):
    icon_id = 'box-805cc175-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shipping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (16, 5))
        self.add_line('p1-r1-2', (16, 5), (27, 5))
        self.add_arc('p1-r1-3', (27, 5), (30, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (30, 8), (30, 12))
        self.add_line('p1-r1-5', (30, 12), (30, 23))
        self.add_arc('p1-r1-6', (30, 23), (26, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (26, 27), (6, 27))
        self.add_arc('p1-r1-8', (6, 27), (2, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 23), (2, 12))
        self.add_line('p1-r1-10', (2, 12), (2, 8))
        self.add_arc('p1-r1-11', (2, 8), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (2, 12), (16, 12))
        self.add_line('p2-r1-2', (16, 12), (30, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 5), (16, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
