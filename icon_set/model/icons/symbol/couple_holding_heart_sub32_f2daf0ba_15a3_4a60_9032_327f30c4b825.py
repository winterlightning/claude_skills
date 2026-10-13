"""Independent 32px profile of couple-holding-heart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f2daf0ba-15a3-4a60-9032-327f30c4b825'
SOURCE_PATH = 'pictographic-primitives/symbol/two persons with heart_f2daf0ba-15a3-4a60-9032-327f30c4b825.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f2daf0ba-15a3-4a60-9032-327f30c4b825', 'pictographic-primitives/symbol/two persons with heart_f2daf0ba-15a3-4a60-9032-327f30c4b825.svg'),)
PROFILE_SOURCE_KEYS = ('solo/couple-holding-heart',)
SOLO_SOURCE_ICON_IDS = ('couple-holding-heart',)
REFERENCE_EXPORT_SHA256 = '611df6872449de3df8942b9a711e470d427c9bf24cf5279a979dc544598dc0f2'

class Drawing(Sub32):
    icon_id = 'couple-holding-heart-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Couple: two heads above one shared heart (the heart's lobes are their shoulders).
        self.add_arc('head-l-1', (7, 4), (11, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-l-2', (11, 4), (7, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-l', 'head-l-1', 'head-l-2', closed=True)
        self.add_arc('head-r-1', (21, 4), (25, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-r-2', (25, 4), (21, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head-r', 'head-r-1', 'head-r-2', closed=True)
        self.add_arc('heart-1', (2, 19), (16, 19), radius_x=7, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('heart-2', (16, 19), (30, 19), radius_x=7, radius_y=5, large_arc=False, sweep=True)
        self.add_line('heart-3', (30, 19), (16, 30))
        self.add_line('heart-4', (16, 30), (2, 19))
        self.add_contour('heart', 'heart-1', 'heart-2', 'heart-3', 'heart-4', closed=True)
