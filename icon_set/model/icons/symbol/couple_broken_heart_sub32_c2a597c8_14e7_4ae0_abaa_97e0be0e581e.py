"""Independent 32px profile of couple-broken-heart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c2a597c8-14e7-4ae0-abaa-97e0be0e581e'
SOURCE_PATH = 'pictographic-primitives/symbol/two persons with broken heart_c2a597c8-14e7-4ae0-abaa-97e0be0e581e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c2a597c8-14e7-4ae0-abaa-97e0be0e581e', 'pictographic-primitives/symbol/two persons with broken heart_c2a597c8-14e7-4ae0-abaa-97e0be0e581e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/couple-broken-heart',)
SOLO_SOURCE_ICON_IDS = ('couple-broken-heart',)
REFERENCE_EXPORT_SHA256 = 'bd2e2fb634d35d181914c7d49a118897eb55601842bda6d6cf8a9d4349c7b8f6'

class Drawing(Sub32):
    icon_id = 'couple-broken-heart-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Couple: two heads above a heart split into two halves.
        self.add_arc('head-l-1', (7, 4), (11, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-l-2', (11, 4), (7, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-l', 'head-l-1', 'head-l-2', closed=True)
        self.add_arc('head-r-1', (21, 4), (25, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-r-2', (25, 4), (21, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-r', 'head-r-1', 'head-r-2', closed=True)
        self.add_arc('half-l-1', (2, 19), (12, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('half-l-2', (12, 19), (12, 30))
        self.add_line('half-l-3', (12, 30), (2, 19))
        self.add_contour('half-l', 'half-l-1', 'half-l-2', 'half-l-3', closed=True)
        self.add_arc('half-r-1', (20, 19), (30, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('half-r-2', (30, 19), (20, 30))
        self.add_line('half-r-3', (20, 30), (20, 19))
        self.add_contour('half-r', 'half-r-1', 'half-r-2', 'half-r-3', closed=True)
