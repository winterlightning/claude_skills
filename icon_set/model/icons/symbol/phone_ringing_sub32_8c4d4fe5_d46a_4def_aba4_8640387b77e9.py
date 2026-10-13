"""Independent 32px profile of phone-ringing.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8c4d4fe5-d46a-4def-aba4-8640387b77e9'
SOURCE_PATH = 'pictographic-primitives/symbol/phone with electric waves_8c4d4fe5-d46a-4def-aba4-8640387b77e9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8c4d4fe5-d46a-4def-aba4-8640387b77e9', 'pictographic-primitives/symbol/phone with electric waves_8c4d4fe5-d46a-4def-aba4-8640387b77e9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/phone-ringing',)
SOLO_SOURCE_ICON_IDS = ('phone-ringing',)
REFERENCE_EXPORT_SHA256 = '3b7766e3b86e7b001ef6e1e0ef549697afe6f882d99a2338aaa98cd99586005c'

class Drawing(Sub32):
    icon_id = 'phone-ringing-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (5, 2), (9, 2))
        self.add_arc('p1-r1-3', (9, 2), (12, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (12, 5), (12, 11))
        self.add_arc('p1-r1-5', (12, 11), (21, 20), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (21, 20), (27, 20))
        self.add_arc('p1-r1-7', (27, 20), (30, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (30, 23), (30, 27))
        self.add_arc('p1-r1-9', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-10', (27, 30), (2, 5), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_arc('p2-r1-1', (20, 2), (30, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
