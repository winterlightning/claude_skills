"""Independent 32px profile of comedy-mask.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e96d51a7-799a-4b44-bf43-4a82353969e1'
SOURCE_PATH = 'pictographic-primitives/symbol/comedy mask with curve line_e96d51a7-799a-4b44-bf43-4a82353969e1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e96d51a7-799a-4b44-bf43-4a82353969e1', 'pictographic-primitives/symbol/comedy mask with curve line_e96d51a7-799a-4b44-bf43-4a82353969e1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/comedy-mask',)
SOLO_SOURCE_ICON_IDS = ('comedy-mask',)
REFERENCE_EXPORT_SHA256 = '5efab0b6af4fc990c1bb8fc7ebb4734b401e2dd623a44fee9c8c18cd5d63de5a'

class Drawing(Sub32):
    icon_id = 'comedy-mask-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 2), (27, 2), radius_x=28, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p1-r1-2', (27, 2), (27, 19))
        self.add_arc('p1-r1-3', (27, 19), (16, 30), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 30), (5, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (5, 19), (5, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (12, 11), (12, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 11), (20, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (20, 20), (12, 20), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
