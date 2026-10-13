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
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 14), (10, 14))
        self.add_bezier('p1-r1-2', (10, 14), ((12, 12), (12, 8), (12, 6)))
        self.add_arc('p1-r1-3', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (20, 6), (20, 14))
        self.add_line('p1-r1-5', (20, 14), (26, 14))
        self.add_arc('p1-r1-6', (26, 14), (26, 30), radius_x=4, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (26, 30), (2, 30))
        self.add_line('p1-r1-8', (2, 30), (2, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
        self.add_line('p2-r1-1', (10, 14), (10, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
