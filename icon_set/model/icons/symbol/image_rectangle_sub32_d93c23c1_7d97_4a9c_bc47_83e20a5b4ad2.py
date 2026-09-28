"""Independent 32px profile of image-rectangle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd93c23c1-7d97-4a9c-bc47-83e20a5b4ad2'
SOURCE_PATH = 'pictographic-primitives/symbol/image rectangle_d93c23c1-7d97-4a9c-bc47-83e20a5b4ad2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d93c23c1-7d97-4a9c-bc47-83e20a5b4ad2', 'pictographic-primitives/symbol/image rectangle_d93c23c1-7d97-4a9c-bc47-83e20a5b4ad2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/image-rectangle',)
SOLO_SOURCE_ICON_IDS = ('image-rectangle',)
REFERENCE_EXPORT_SHA256 = 'fec32f04b3b93db86202d8c4b13eb9fbb21d3a2b632a874e2b9f13855b2436ca'

class Drawing(Sub32):
    icon_id = 'image-rectangle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (30, 30))
        self.add_line('p1-r1-2', (30, 30), (22, 16))
        self.add_line('p1-r1-3', (22, 16), (16, 24))
        self.add_line('p1-r1-4', (16, 24), (12, 20))
        self.add_line('p1-r1-5', (12, 20), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (2, 7), ((2, 4), (4, 2), (7, 2)))
        self.add_bezier('p2-r1-2', (7, 2), ((10, 2), (13, 4), (13, 7)))
        self.add_arc('p2-r1-3', (13, 7), (2, 7), radius_x=5.5, radius_y=5.5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
