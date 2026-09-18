# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
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

class DrawingVariant2(Sub32):
    icon_id = 'arrow-right-curved-sub32-v2'
    variant_of = 'arrow-right-curved-sub32'
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
        self.add_line('p1-r1-1', (22, short_low), (30, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (2, short_high), ((2, short_high), (2, 26), (2, 26)))
        self.add_bezier('p2-r1-2', (2, 26), ((2, 21), (6, 15), (11, 13)))
        self.add_bezier('p2-r1-3', (11, 13), ((13, 12), (16, 12), (18, 12)))
        self.add_line('p2-r1-4', (18, 12), (30, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (22, 18), (30, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
