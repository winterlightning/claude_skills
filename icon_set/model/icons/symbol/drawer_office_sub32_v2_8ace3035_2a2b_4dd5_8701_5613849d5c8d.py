"""Independent 32px profile of drawer-office.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8ace3035-2a2b-4dd5-8701-5613849d5c8d'
SOURCE_PATH = 'pictographic-primitives/office/drawer_8ace3035-2a2b-4dd5-8701-5613849d5c8d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ace3035-2a2b-4dd5-8701-5613849d5c8d', 'pictographic-primitives/office/drawer_8ace3035-2a2b-4dd5-8701-5613849d5c8d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/drawer-office',)
SOLO_SOURCE_ICON_IDS = ('drawer-office',)
REFERENCE_EXPORT_SHA256 = '80d93175eacdba45d3584b62e7674abfe23010ef31367ddb9f307337e4f7fc71'

class DrawingVariant2(Sub32):
    icon_id = 'drawer-office-sub32-v2'
    related_origin_icon_id = 'drawer-office-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'office'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (28, 15), (4, 15))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (28, short_high), (28, short_low))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (28, 24), (4, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (4, short_low), (4, short_high))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, short_low), (2, short_low))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 15), (16, short_low))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
