"""Independent 32px profile of building-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a6adecf4-5959-4f91-a3a7-5bdffc5bac69'
SOURCE_PATH = 'pictographic-primitives/building/building 1_a6adecf4-5959-4f91-a3a7-5bdffc5bac69.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a6adecf4-5959-4f91-a3a7-5bdffc5bac69', 'pictographic-primitives/building/building 1_a6adecf4-5959-4f91-a3a7-5bdffc5bac69.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-1',)
SOLO_SOURCE_ICON_IDS = ('building-1',)
REFERENCE_EXPORT_SHA256 = '519ccd77a4e3268a3a032ee8173d71c0af662aeea4929dff227dd0f07677ff94'

class DrawingVariant2(Sub32):
    icon_id = 'building-1-sub32-v2'
    related_origin_icon_id = 'building-1-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'building'
    categories = ('building', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 30), (short_low, 2))
        self.add_line('p1-r1-2', (short_low, 2), (short_high, 15))
        self.add_line('p1-r1-3', (short_high, 15), (short_high, 30))
        self.add_line('p1-r1-4', (short_high, 30), (short_low, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (13, 19), (18, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
