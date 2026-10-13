"""Independent 32px profile of diagonal-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8ec3a613-7e1f-4f25-b24f-78c45957aa3b'
SOURCE_PATH = 'pictographic-primitives/symbol/diagonal arrow_8ec3a613-7e1f-4f25-b24f-78c45957aa3b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ec3a613-7e1f-4f25-b24f-78c45957aa3b', 'pictographic-primitives/symbol/diagonal arrow_8ec3a613-7e1f-4f25-b24f-78c45957aa3b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diagonal-arrow',)
SOLO_SOURCE_ICON_IDS = ('diagonal-arrow',)
REFERENCE_EXPORT_SHA256 = 'aeca72c69659752d1d880eea31d32fda56b4a7173d5cc31bab1220388cc2b80b'

class DrawingVariant2(Sub32):
    icon_id = 'diagonal-arrow-sub32-v2'
    related_origin_icon_id = 'diagonal-arrow-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_line('p1-r1-1', (8, 4), (2, 10))
        self.add_line('p3-r1-1', (2, 10), (30, 10))
        self.add_line('p5-r1-1', (30, 22), (2, 22))
        self.add_line('p6-r1-1', (30, 22), (24, 28))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
