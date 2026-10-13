"""Independent 32px profile of peercoin.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e015513e-29e5-48ae-ad99-806d5a1b0b1e'
SOURCE_PATH = 'pictographic-primitives/symbol/peercoin_e015513e-29e5-48ae-ad99-806d5a1b0b1e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e015513e-29e5-48ae-ad99-806d5a1b0b1e', 'pictographic-primitives/symbol/peercoin_e015513e-29e5-48ae-ad99-806d5a1b0b1e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/peercoin',)
SOLO_SOURCE_ICON_IDS = ('peercoin',)
REFERENCE_EXPORT_SHA256 = '817f18f3164ef9d9d84d593091943a6395d58a5903034738ff0eca23b509e659'

class Drawing(Sub32):
    icon_id = 'peercoin-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 30), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (21, 2))
        self.add_arc('p1-r1-3', (21, 2), (21, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (21, 16), (10, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (4, 24), (20, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
