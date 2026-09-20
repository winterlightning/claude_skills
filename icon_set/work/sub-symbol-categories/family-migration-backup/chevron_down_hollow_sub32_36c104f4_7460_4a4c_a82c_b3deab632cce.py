"""Independent 32px profile of chevron-down-hollow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '36c104f4-7460-4a4c-a82c-b3deab632cce'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow down button_36c104f4-7460-4a4c-a82c-b3deab632cce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('36c104f4-7460-4a4c-a82c-b3deab632cce', 'pictographic-primitives/symbol/arrow down button_36c104f4-7460-4a4c-a82c-b3deab632cce.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chevron-down-hollow',)
SOLO_SOURCE_ICON_IDS = ('chevron-down-hollow',)
REFERENCE_EXPORT_SHA256 = 'c709c1a3bc2cd4287d43c22d1b5c584a5363473dc718adc76ba9a52b8c970f1d'

class Drawing(Sub32):
    icon_id = 'chevron-down-hollow-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (16, 19))
        self.add_line('p1-r1-2', (16, 19), (30, 5))
        self.add_line('p1-r1-3', (30, 5), (30, 13))
        self.add_line('p1-r1-4', (30, 13), (16, 27))
        self.add_line('p1-r1-5', (16, 27), (2, 13))
        self.add_line('p1-r1-6', (2, 13), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
