"""Independent 32px profile of personal-hotspot-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f'
SOURCE_PATH = 'pictographic-primitives/symbol/personal hotspot_c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f', 'pictographic-primitives/symbol/personal hotspot_c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/personal-hotspot-symbol',)
SOLO_SOURCE_ICON_IDS = ('personal-hotspot-symbol',)
REFERENCE_EXPORT_SHA256 = '6b807b0b866d81159ae09ae242167260eea0adca3f12adfcc612443fea02d978'

class Drawing(Sub32):
    icon_id = 'personal-hotspot-symbol-sub32'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Personal hotspot: a chain link, two open ends joined by a bar.
        self.add_line('l-1', (12, 8), (10, 8))
        self.add_arc('l-2', (10, 8), (10, 24), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('l-3', (10, 24), (12, 24))
        self.add_contour('link-l', 'l-1', 'l-2', 'l-3')
        self.add_line('r-1', (20, 8), (22, 8))
        self.add_arc('r-2', (22, 8), (22, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('r-3', (22, 24), (20, 24))
        self.add_contour('link-r', 'r-1', 'r-2', 'r-3')
        self.add_line('bar', (10, 16), (22, 16))
