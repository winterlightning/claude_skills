"""Independent 32px profile of cake.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ffca9ae9-2486-4950-9183-fda6e50cd3ce'
SOURCE_PATH = 'pictographic-primitives/symbol/cake_ffca9ae9-2486-4950-9183-fda6e50cd3ce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ffca9ae9-2486-4950-9183-fda6e50cd3ce', 'pictographic-primitives/symbol/cake_ffca9ae9-2486-4950-9183-fda6e50cd3ce.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cake',)
SOLO_SOURCE_ICON_IDS = ('cake',)
REFERENCE_EXPORT_SHA256 = '921f03620541456e7f0f05d229e210e31f40004e3c6e13290aa26f9f0c708fc1'

class Drawing(Sub32):
    icon_id = 'cake-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Cake slice: curved top, sloped cut side, one layer line (cherry dropped: no 4-unit room).
        self.add_bezier('p1-r1-1', (2, 18), ((2, 11), (7, 6), (14, 6)))
        self.add_line('p1-r1-2', (14, 6), (30, 18))
        self.add_line('p1-r1-3', (30, 18), (30, 26))
        self.add_line('p1-r1-4', (30, 26), (2, 26))
        self.add_line('p1-r1-5', (2, 26), (2, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=True)
        self.add_line('p2-r1-1', (2, 18), (30, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
