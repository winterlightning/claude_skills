# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of pine-tree.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3f0937d0-e60c-4dfb-805d-b75941386342'
SOURCE_PATH = 'pictographic-primitives/nature/tree_3f0937d0-e60c-4dfb-805d-b75941386342.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3f0937d0-e60c-4dfb-805d-b75941386342', 'pictographic-primitives/nature/tree_3f0937d0-e60c-4dfb-805d-b75941386342.svg'), ('66e32e15-544c-4dc8-bd51-99f96d8c78b2', 'pictographic-primitives/nature/tree_66e32e15-544c-4dc8-bd51-99f96d8c78b2.svg'))
PROFILE_SOURCE_KEYS = ('solo/pine-tree', 'solo/pine-tree-upright')
SOLO_SOURCE_ICON_IDS = ('pine-tree', 'pine-tree-upright')
REFERENCE_EXPORT_SHA256 = '56bfdcf80722d513f8aac4db4730696f0fd5090438a6301800207449153ec469'

class DrawingVariant2(Sub32):
    icon_id = 'pine-tree-sub32-v2'
    variant_of = 'pine-tree-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature/batch-03'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, 2), (short_low, 13))
        self.add_line('p1-r1-2', (short_low, 13), (13, 13))
        self.add_line('p1-r1-3', (13, 13), (short_low, 24))
        self.add_line('p1-r1-4', (short_low, 24), (16, 24))
        self.add_line('p1-r1-5', (16, 24), (short_high, 24))
        self.add_line('p1-r1-6', (short_high, 24), (19, 13))
        self.add_line('p1-r1-7', (19, 13), (short_high, 13))
        self.add_line('p1-r1-8', (short_high, 13), (16, 2))
        self.add_line('p1-r1-9', (16, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (16, 24), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
