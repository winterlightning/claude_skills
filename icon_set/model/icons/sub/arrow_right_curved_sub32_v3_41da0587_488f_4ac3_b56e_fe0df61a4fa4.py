# Centerline repair: continuous intended straight runs and matched tangent directions.
# Variant of arrow-right-curved-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of arrow-right-curved.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '41da0587-488f-4ac3-b56e-fe0df61a4fa4'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow right curved_41da0587-488f-4ac3-b56e-fe0df61a4fa4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('41da0587-488f-4ac3-b56e-fe0df61a4fa4', 'pictographic-primitives/symbol/arrow right curved_41da0587-488f-4ac3-b56e-fe0df61a4fa4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-right-curved',)
SOLO_SOURCE_ICON_IDS = ('arrow-right-curved',)
REFERENCE_EXPORT_SHA256 = 'f5d1c89df5ef1fbafc53d5e84758640e00d4370fcdd44faf740218094f7839b2'

class DrawingVariant3(Sub32):
    icon_id = 'arrow-right-curved-sub32-v3'
    variant_of = 'arrow-right-curved-sub32-v2'
    variant_label = 'Continuous centerlines'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (22, short_low), (30, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (2, short_high), (18, 12), radius_x=16, radius_y=16, sweep=True)
        self.add_line('p2-r1-4', (18, 12), (30, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (22, 20), (30, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
