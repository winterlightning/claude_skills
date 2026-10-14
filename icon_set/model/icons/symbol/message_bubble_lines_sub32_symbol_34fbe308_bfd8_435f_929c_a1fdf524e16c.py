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
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Speech bubble with rounded corners, a tail at the bottom left and two text lines.
        self.add_line('b-1', (6, 2), (26, 2))
        self.add_arc('b-2', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('b-3', (30, 6), (30, 22))
        self.add_arc('b-4', (30, 22), (26, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('b-5', (26, 26), (16, 26))
        self.add_line('b-6', (16, 26), (10, 30))
        self.add_line('b-7', (10, 30), (10, 26))
        self.add_line('b-8', (10, 26), (6, 26))
        self.add_arc('b-9', (6, 26), (2, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('b-10', (2, 22), (2, 6))
        self.add_arc('b-11', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('bubble', 'b-1', 'b-2', 'b-3', 'b-4', 'b-5', 'b-6', 'b-7', 'b-8', 'b-9', 'b-10', 'b-11', closed=True)
        self.add_line('text-1', (10, 10), (22, 10))
        self.add_line('text-2', (10, 18), (18, 18))
