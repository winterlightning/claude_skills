"""Independent 32px profile of account-profile-card.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a2029a15-66fa-482d-a28c-001d915dd91d'
SOURCE_PATH = 'pictographic-primitives/symbol/account page_a2029a15-66fa-482d-a28c-001d915dd91d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a2029a15-66fa-482d-a28c-001d915dd91d', 'pictographic-primitives/symbol/account page_a2029a15-66fa-482d-a28c-001d915dd91d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/account-profile-card',)
SOLO_SOURCE_ICON_IDS = ('account-profile-card',)
REFERENCE_EXPORT_SHA256 = '2328328d7aeeaaa37a617cf03b374cba6b827589873a15c3673d2df4f2df401d'

class Drawing(Sub32):
    icon_id = 'account-profile-card-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 5), (9, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 13), (9, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 27), (9, 19), radius_x=7, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (9, 19), (16, 27), radius_x=7, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (23, 6), (30, 6))
        self.add_line('p3-r1-2', (30, 6), (30, 15))
        self.add_line('p3-r1-3', (30, 15), (23, 15))
        self.add_line('p3-r1-4', (23, 15), (23, 6))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (23, 23), (30, 23))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
