"""Independent 32px profile of barrier.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '80d907cf-11f8-4104-a791-525bc0837b34'
SOURCE_PATH = 'pictographic-primitives/symbol/barrier_80d907cf-11f8-4104-a791-525bc0837b34.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('80d907cf-11f8-4104-a791-525bc0837b34', 'pictographic-primitives/symbol/barrier_80d907cf-11f8-4104-a791-525bc0837b34.svg'),)
PROFILE_SOURCE_KEYS = ('solo/barrier',)
SOLO_SOURCE_ICON_IDS = ('barrier',)
REFERENCE_EXPORT_SHA256 = '63cca0edac0230c1c02a36348fe6f7b1c4df27747b6e33850a5315fb5e5b6e56'

class Drawing(Sub32):
    icon_id = 'barrier-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (13, 5))
        self.add_line('p1-r1-2', (13, 5), (24, 5))
        self.add_line('p1-r1-3', (24, 5), (30, 5))
        self.add_line('p1-r1-4', (30, 5), (30, 16))
        self.add_line('p1-r1-5', (30, 16), (24, 16))
        self.add_line('p1-r1-6', (24, 16), (13, 16))
        self.add_line('p1-r1-7', (13, 16), (8, 16))
        self.add_line('p1-r1-8', (8, 16), (2, 16))
        self.add_line('p1-r1-9', (2, 16), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (2, 16), (13, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 16), (24, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (8, 16), (8, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 16), (24, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p5-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p5-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
