"""Independent 32px profile of colon-currency-sign.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a48b3aac-95e9-403d-8bce-d467fba83570'
SOURCE_PATH = 'pictographic-primitives/symbol/colon sign_a48b3aac-95e9-403d-8bce-d467fba83570.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a48b3aac-95e9-403d-8bce-d467fba83570', 'pictographic-primitives/symbol/colon sign_a48b3aac-95e9-403d-8bce-d467fba83570.svg'),)
PROFILE_SOURCE_KEYS = ('solo/colon-currency-sign',)
SOLO_SOURCE_ICON_IDS = ('colon-currency-sign',)
REFERENCE_EXPORT_SHA256 = '55553f9643fca1a1b0933a4998f228cd78df2855077bb38ecf12744031e524db'

class Drawing(Sub32):
    icon_id = 'colon-currency-sign-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (19, 2))
        self.add_arc('p1-r1-2', (19, 2), (5, 16), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (5, 16), (8, 24), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (8, 24), (19, 30), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (19, 30), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 27), (8, 24))
        self.add_line('p2-r1-2', (8, 24), (27, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
