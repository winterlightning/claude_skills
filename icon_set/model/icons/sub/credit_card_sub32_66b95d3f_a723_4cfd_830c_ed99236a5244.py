"""Independent 32px profile of credit-card.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '66b95d3f-a723-4cfd-830c-ed99236a5244'
SOURCE_PATH = 'pictographic-primitives/payments/credit card_66b95d3f-a723-4cfd-830c-ed99236a5244.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('66b95d3f-a723-4cfd-830c-ed99236a5244', 'pictographic-primitives/payments/credit card_66b95d3f-a723-4cfd-830c-ed99236a5244.svg'),)
PROFILE_SOURCE_KEYS = ('solo/credit-card',)
SOLO_SOURCE_ICON_IDS = ('credit-card',)
REFERENCE_EXPORT_SHA256 = '1fd402939e860a5b0b45fbcafa0d8a50ee5cff773c7938114a2df17bdcfcb04e'

class Drawing(Sub32):
    icon_id = 'credit-card-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'payments'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (30, 13))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 11), (2, 25))
        self.add_arc('p2-r1-2', (2, 25), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (4, 27), (28, 27))
        self.add_arc('p2-r1-4', (28, 27), (30, 25), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (30, 25), (30, 7))
        self.add_arc('p2-r1-6', (30, 7), (28, 5), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-7', (28, 5), (4, 5))
        self.add_line('p2-r1-8', (4, 5), (3, 6))
        self.add_line('p2-r1-9', (3, 6), (2, 8))
        self.add_line('p2-r1-10', (2, 8), (2, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_line('p3-r1-1', (24, 21), (24, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
