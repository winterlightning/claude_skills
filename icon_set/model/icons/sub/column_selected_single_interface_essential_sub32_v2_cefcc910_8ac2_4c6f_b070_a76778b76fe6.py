# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of column-selected-single-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'cefcc910-8ac2-4c6f-b070-a76778b76fe6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/column selected single_cefcc910-8ac2-4c6f-b070-a76778b76fe6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cefcc910-8ac2-4c6f-b070-a76778b76fe6', 'pictographic-primitives/interface-essential/column selected single_cefcc910-8ac2-4c6f-b070-a76778b76fe6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/column-selected-single-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('column-selected-single-interface-essential',)
REFERENCE_EXPORT_SHA256 = '32a292c8cccc1ef4db26c5b8ec4414f3d97974dc0bbc03d65100fa3d60d57c54'

class DrawingVariant2(Sub32):
    icon_id = 'column-selected-single-interface-essential-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 20), (short_high, 20))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (short_low, 20), (short_low, 30))
        self.add_line('p2-r1-2', (short_low, 30), (short_high, 30))
        self.add_line('p2-r1-3', (short_high, 30), (short_high, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (short_low, 20), (short_low, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (short_high, 20), (short_high, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (short_low, 12), (short_high, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (short_low, 12), (short_low, 2))
        self.add_line('p6-r1-2', (short_low, 2), (short_high, 2))
        self.add_line('p6-r1-3', (short_high, 2), (short_high, 12))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-3')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-3')
