# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of quotation-marks.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1'
SOURCE_PATH = 'pictographic-primitives/symbol/quotation_b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1', 'pictographic-primitives/symbol/quotation_b251c4a5-32cb-4f5c-a0d5-32ea0c61b0f1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/quotation-marks',)
SOLO_SOURCE_ICON_IDS = ('quotation-marks',)
REFERENCE_EXPORT_SHA256 = 'adaa7483df1701cdba3333d8a8a988feabc06489831545d5495d5d881015379a'

class DrawingVariant2(Sub32):
    icon_id = 'quotation-marks-sub32-v2'
    variant_of = 'quotation-marks-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_arc('p1-r1-1', (2, 23), (12, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 23), (2, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 23), (2, 17))
        self.add_arc('p2-r1-2', (2, 17), (12, short_low), radius_x=10, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (20, 23), (30, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 23), (20, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (20, 23), (20, 17))
        self.add_arc('p4-r1-2', (20, 17), (30, short_low), radius_x=10, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
