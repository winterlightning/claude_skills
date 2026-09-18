# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of column-selected-single-1-state.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'dfeadfd1-5e80-4042-9a90-d17374c480dc'
SOURCE_PATH = 'pictographic-primitives/state/column selected single 1_dfeadfd1-5e80-4042-9a90-d17374c480dc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dfeadfd1-5e80-4042-9a90-d17374c480dc', 'pictographic-primitives/state/column selected single 1_dfeadfd1-5e80-4042-9a90-d17374c480dc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/column-selected-single-1-state',)
SOLO_SOURCE_ICON_IDS = ('column-selected-single-1-state',)
REFERENCE_EXPORT_SHA256 = '8991d993511a9cd378234419e8d6682d8e404d6c3ee01c45dd87f9633ac65eae'

class DrawingVariant2(Sub32):
    icon_id = 'column-selected-single-1-state-sub32-v2'
    variant_of = 'column-selected-single-1-state-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (20, short_low), (20, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (12, short_low), (12, short_high))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, short_low), (30, short_high))
        self.add_line('p3-r1-2', (30, short_high), (2, short_high))
        self.add_line('p3-r1-3', (2, short_high), (2, short_low))
        self.add_line('p3-r1-4', (2, short_low), (30, short_low))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
