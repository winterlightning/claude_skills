# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of double-arrow-right-state.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7099ca2e-6b54-40e6-a460-b7c2704abd1f'
SOURCE_PATH = 'pictographic-primitives/state/double arrow right_7099ca2e-6b54-40e6-a460-b7c2704abd1f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7099ca2e-6b54-40e6-a460-b7c2704abd1f', 'pictographic-primitives/state/double arrow right_7099ca2e-6b54-40e6-a460-b7c2704abd1f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/double-arrow-right-state',)
SOLO_SOURCE_ICON_IDS = ('double-arrow-right-state',)
REFERENCE_EXPORT_SHA256 = '58dae22be44d1dee606ec328cf7518ad6df7bfb269891912593c7b7da3ec3321'

class DrawingVariant2(Sub32):
    icon_id = 'double-arrow-right-state-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (20, short_low), (30, 16))
        self.add_line('p1-r1-2', (30, 16), (20, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (20, 16), (2, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 16), (9, short_high))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 16), (9, short_low))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
