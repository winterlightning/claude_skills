# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of menu-state.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3eeabb37-3df8-43ae-bf08-f1a3235c1435'
SOURCE_PATH = 'pictographic-primitives/state/menu_3eeabb37-3df8-43ae-bf08-f1a3235c1435.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3eeabb37-3df8-43ae-bf08-f1a3235c1435', 'pictographic-primitives/state/menu_3eeabb37-3df8-43ae-bf08-f1a3235c1435.svg'), ('9021d3df-1ef4-4e3d-94c6-469ac6bd996d', 'pictographic-primitives/symbol/menu_9021d3df-1ef4-4e3d-94c6-469ac6bd996d.svg'), ('48ceef16-bc0f-47db-9f92-d1bfe04d9743', 'pictographic-primitives/symbol/three lines horizontal_48ceef16-bc0f-47db-9f92-d1bfe04d9743.svg'))
PROFILE_SOURCE_KEYS = ('solo/menu-state', 'solo/menu-symbol', 'solo/three-lines-horizontal')
SOLO_SOURCE_ICON_IDS = ('menu-state', 'menu-symbol', 'three-lines-horizontal')
REFERENCE_EXPORT_SHA256 = 'd772b155f792221ee99b0173269a9a9e3eb991340dd6b70ab343e8cf2117259b'

class DrawingVariant2(Sub32):
    icon_id = 'menu-state-sub32-v2'
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
        self.add_line('p1-r1-1', (2, short_low), (30, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, short_high), (30, short_high))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
