"""Independent 32px profile of coins.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5cabb173-08d9-478c-9912-5357cbf2ed85'
SOURCE_PATH = 'pictographic-primitives/money/coins_5cabb173-08d9-478c-9912-5357cbf2ed85.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5cabb173-08d9-478c-9912-5357cbf2ed85', 'pictographic-primitives/money/coins_5cabb173-08d9-478c-9912-5357cbf2ed85.svg'),)
PROFILE_SOURCE_KEYS = ('solo/coins',)
SOLO_SOURCE_ICON_IDS = ('coins',)
REFERENCE_EXPORT_SHA256 = 'e854f337b3c543c33ad1270a1e8e9c07bc89b4d44151b16c98832b1db2691547'

class Drawing(Sub32):
    icon_id = 'coins-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (8, 16), (24, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (24, 16), (8, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 15), (16, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
