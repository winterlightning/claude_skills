"""Independent 32px profile of thumb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1748248c-ea64-40ed-bc18-c40c4a97032b'
SOURCE_PATH = 'pictographic-primitives/state/thumb_1748248c-ea64-40ed-bc18-c40c4a97032b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1748248c-ea64-40ed-bc18-c40c4a97032b', 'pictographic-primitives/state/thumb_1748248c-ea64-40ed-bc18-c40c4a97032b.svg'), ('c5652a88-5c11-499a-8e2e-486a9b3a75d1', 'pictographic-primitives/symbol/thumb_c5652a88-5c11-499a-8e2e-486a9b3a75d1.svg'))
PROFILE_SOURCE_KEYS = ('solo/thumb', 'solo/thumb-symbol')
SOLO_SOURCE_ICON_IDS = ('thumb', 'thumb-symbol')
REFERENCE_EXPORT_SHA256 = 'd0ba68115546736ca9894c4ac6f3e5459fbf3145a63a8a908393719577d98d78'

class DrawingContainerSymbol(Sub32):
    icon_id = 'thumb-sub32-symbol'
    related_origin_icon_id = 'thumb-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/thumb-sub32'
    counterpart_icon_id = 'thumb-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 15), ((8, 15), (10, 14), (11, 12)))
        self.add_bezier('p1-r1-2', (11, 12), ((12, 9), (12, 2), (15, 2)))
        self.add_bezier('p1-r1-3', (15, 2), ((19, 2), (21, 3), (21, 6)))
        self.add_line('p1-r1-4', (21, 6), (20, 14))
        self.add_line('p1-r1-5', (20, 14), (24, 15))
        self.add_bezier('p1-r1-6', (24, 15), ((27, 15), (27, 16), (27, 17)))
        self.add_line('p1-r1-7', (27, 17), (24, 27))
        self.add_bezier('p1-r1-8', (24, 27), ((24, 29), (22, 30), (20, 30)))
        self.add_line('p1-r1-9', (20, 30), (13, 30))
        self.add_bezier('p1-r1-10', (13, 30), ((10, 30), (10, 27), (8, 27)))
        self.add_line('p1-r1-11', (8, 27), (5, 27))
        self.add_line('p1-r1-12', (5, 27), (5, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
