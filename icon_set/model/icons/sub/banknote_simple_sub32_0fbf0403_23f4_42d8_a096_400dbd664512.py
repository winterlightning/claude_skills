"""Independent 32px profile of banknote-simple.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0fbf0403-23f4-42d8-a096-400dbd664512'
SOURCE_PATH = 'pictographic-primitives/symbol/money bill_0fbf0403-23f4-42d8-a096-400dbd664512.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fbf0403-23f4-42d8-a096-400dbd664512', 'pictographic-primitives/symbol/money bill_0fbf0403-23f4-42d8-a096-400dbd664512.svg'), ('76664091-6ef6-44a2-8c4c-a2b2e41d7461', 'pictographic-primitives/symbol/cash card_76664091-6ef6-44a2-8c4c-a2b2e41d7461.svg'))
PROFILE_SOURCE_KEYS = ('solo/banknote-simple', 'solo/banknote-coin-mark')
SOLO_SOURCE_ICON_IDS = ('banknote-simple', 'banknote-coin-mark')
REFERENCE_EXPORT_SHA256 = '5d9498d5dfd55a394a8885d47b51d1c493a2d045e1141eaea4167a7c66c7162a'

class Drawing(Sub32):
    icon_id = 'banknote-simple-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (30, 5))
        self.add_line('p1-r1-2', (30, 5), (30, 27))
        self.add_line('p1-r1-3', (30, 27), (2, 27))
        self.add_line('p1-r1-4', (2, 27), (2, 5))
        self.add_line('p1-r1-5', (2, 5), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (11, 16), (21, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (21, 16), (11, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
