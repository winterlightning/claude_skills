"""Independent 32px profile of message-bubble-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '34fbe308-bfd8-435f-929c-a1fdf524e16c'
SOURCE_PATH = 'pictographic-primitives/symbol/message lines_34fbe308-bfd8-435f-929c-a1fdf524e16c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('34fbe308-bfd8-435f-929c-a1fdf524e16c', 'pictographic-primitives/symbol/message lines_34fbe308-bfd8-435f-929c-a1fdf524e16c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/message-bubble-lines',)
SOLO_SOURCE_ICON_IDS = ('message-bubble-lines',)
REFERENCE_EXPORT_SHA256 = '4cba4c38ccf41d2b8d3d4a508e1d401bcd0443c6f091fe1d5d6440bb24eab9c5'

class DrawingContainerSymbol(Sub32):
    icon_id = 'message-bubble-lines-sub32-symbol'
    related_origin_icon_id = 'message-bubble-lines-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/message-bubble-lines-sub32'
    counterpart_icon_id = 'message-bubble-lines-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (3, 5), (29, 5))
        self.add_bezier('p1-r1-2', (29, 5), ((29, 5), (30, 6), (30, 8)))
        self.add_line('p1-r1-3', (30, 8), (30, 20))
        self.add_bezier('p1-r1-4', (30, 20), ((30, 21), (29, 22), (29, 23)))
        self.add_line('p1-r1-5', (29, 23), (15, 23))
        self.add_line('p1-r1-6', (15, 23), (8, 27))
        self.add_line('p1-r1-7', (8, 27), (8, 23))
        self.add_line('p1-r1-8', (8, 23), (3, 23))
        self.add_bezier('p1-r1-9', (3, 23), ((3, 22), (2, 21), (2, 20)))
        self.add_line('p1-r1-10', (2, 20), (2, 8))
        self.add_bezier('p1-r1-11', (2, 8), ((2, 6), (3, 5), (3, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (9, 11), (23, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 17), (23, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
