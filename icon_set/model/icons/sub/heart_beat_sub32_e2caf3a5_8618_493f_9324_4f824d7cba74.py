"""Independent 32px profile of heart-beat.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e2caf3a5-8618-493f-9324-4f824d7cba74'
SOURCE_PATH = 'pictographic-primitives/symbol/heart beat_e2caf3a5-8618-493f-9324-4f824d7cba74.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2caf3a5-8618-493f-9324-4f824d7cba74', 'pictographic-primitives/symbol/heart beat_e2caf3a5-8618-493f-9324-4f824d7cba74.svg'),)
PROFILE_SOURCE_KEYS = ('solo/heart-beat',)
SOLO_SOURCE_ICON_IDS = ('heart-beat',)
REFERENCE_EXPORT_SHA256 = 'f57a788fb11ed2a01a1c58e56ef2504db5fa0886b3f689015b149640173b6159'

class Drawing(Sub32):
    icon_id = 'heart-beat-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 17), (6, 17))
        self.add_line('p1-r1-2', (6, 17), (10, 5))
        self.add_line('p1-r1-3', (10, 5), (16, 27))
        self.add_line('p1-r1-4', (16, 27), (20, 9))
        self.add_line('p1-r1-5', (20, 9), (24, 17))
        self.add_line('p1-r1-6', (24, 17), (30, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
