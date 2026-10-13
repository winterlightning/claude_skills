"""Independent 32px profile of cargo-ship-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ab3ea798-6eb7-4962-94f0-08838f608e51'
SOURCE_PATH = 'pictographic-primitives/symbol/cargo ship_ab3ea798-6eb7-4962-94f0-08838f608e51.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ab3ea798-6eb7-4962-94f0-08838f608e51', 'pictographic-primitives/symbol/cargo ship_ab3ea798-6eb7-4962-94f0-08838f608e51.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cargo-ship-symbol',)
SOLO_SOURCE_ICON_IDS = ('cargo-ship-symbol',)
REFERENCE_EXPORT_SHA256 = '841b82a9ce0bc7260f373960445d8c092109fd89d7d6ebb1bb2243d0876d4d99'

class Drawing(Sub32):
    icon_id = 'cargo-ship-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 15), (7, 8))
        self.add_line('p1-r1-2', (7, 8), (12, 8))
        self.add_line('p1-r1-3', (12, 8), (12, 2))
        self.add_line('p1-r1-4', (12, 2), (20, 2))
        self.add_line('p1-r1-5', (20, 2), (20, 8))
        self.add_line('p1-r1-6', (20, 8), (25, 8))
        self.add_line('p1-r1-7', (25, 8), (25, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (5, 28), (2, 15))
        self.add_line('p2-r1-2', (2, 15), (7, 15))
        self.add_line('p2-r1-3', (7, 15), (25, 15))
        self.add_line('p2-r1-4', (25, 15), (30, 15))
        self.add_line('p2-r1-5', (30, 15), (27, 28))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 30), (5, 28))
        self.add_line('p3-r1-2', (5, 28), (11, 30))
        self.add_line('p3-r1-3', (11, 30), (16, 28))
        self.add_line('p3-r1-4', (16, 28), (21, 30))
        self.add_line('p3-r1-5', (21, 30), (27, 28))
        self.add_line('p3-r1-6', (27, 28), (30, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-7', 'p2-r1-3')
        self.relate('connect', 'p1-r1-7', 'p2-r1-4')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-5', 'p3-r1-5')
        self.relate('connect', 'p2-r1-5', 'p3-r1-6')
