"""Independent 32px profile of square-with-lines-with-pen.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '87a60b78-ba59-46b6-98bc-5b60564657b5'
SOURCE_PATH = 'pictographic-primitives/symbol/square with lines with pen_87a60b78-ba59-46b6-98bc-5b60564657b5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('87a60b78-ba59-46b6-98bc-5b60564657b5', 'pictographic-primitives/symbol/square with lines with pen_87a60b78-ba59-46b6-98bc-5b60564657b5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/square-with-lines-with-pen',)
SOLO_SOURCE_ICON_IDS = ('square-with-lines-with-pen',)
REFERENCE_EXPORT_SHA256 = '3d8f4e8be2c4c0c69df896f4a3d2a260548fbf633e9a19ba4ef49535b1e9a2e6'

class Drawing(Sub32):
    icon_id = 'square-with-lines-with-pen-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (26, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (30, 7), (14, 22))
        self.add_arc('p2-r1-2', (14, 22), (2, 30), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (2, 30), (3, 27))
        self.add_arc('p2-r1-4', (3, 27), (4, 21), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (4, 21), (25, 2))
        self.add_line('p2-r1-6', (25, 2), (30, 7))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
