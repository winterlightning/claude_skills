# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of arrow-up-down.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '21dd4ec9-3d12-4039-88ab-b49577388c2d'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow up down_21dd4ec9-3d12-4039-88ab-b49577388c2d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('21dd4ec9-3d12-4039-88ab-b49577388c2d', 'pictographic-primitives/symbol/arrow up down_21dd4ec9-3d12-4039-88ab-b49577388c2d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-up-down',)
SOLO_SOURCE_ICON_IDS = ('arrow-up-down',)
REFERENCE_EXPORT_SHA256 = '1fa68481dc45886aae893cf601b316748c6a66cf1f1bf477a46fe7442018df11'

class DrawingVariant2(Sub32):
    icon_id = 'arrow-up-down-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 10), (8, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (8, short_low), (8, short_high))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, short_low), (13, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, short_low), (24, short_high))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (19, 22), (24, short_high))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (30, 22), (24, short_high))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
