"""Independent 32px profile of institution.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2ee457ae-4157-4c6d-bafa-66a532de7822'
SOURCE_PATH = 'pictographic-primitives/symbol/institution_2ee457ae-4157-4c6d-bafa-66a532de7822.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ee457ae-4157-4c6d-bafa-66a532de7822', 'pictographic-primitives/symbol/institution_2ee457ae-4157-4c6d-bafa-66a532de7822.svg'),)
PROFILE_SOURCE_KEYS = ('solo/institution',)
SOLO_SOURCE_ICON_IDS = ('institution',)
REFERENCE_EXPORT_SHA256 = '189ef2fbb9dadc46a702f2f2f7809f177bcd758609ac6d0da0a09e785fd98271'

class Drawing(Sub32):
    icon_id = 'institution-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Institution: building base under a flat dome, a flag on a pole above, every gap 4 units.
        self.add_arc('dome', (4, 22), (28, 22), radius_x=12, radius_y=4, large_arc=False, sweep=True)
        self.add_polyline('base', (4, 22), (4, 30), (28, 30), (28, 22))
        self.add_polyline('flag', (16, 18), (16, 2), (26, 2), (26, 10), (16, 10))
        self.relate('connect', 'dome', 'base')
        self.relate('connect', 'dome', 'flag')
