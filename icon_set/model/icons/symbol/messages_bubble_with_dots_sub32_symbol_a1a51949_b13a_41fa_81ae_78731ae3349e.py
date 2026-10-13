"""Independent 32px profile of messages-bubble-with-dots.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a1a51949-b13a-41fa-81ae-78731ae3349e'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a1a51949-b13a-41fa-81ae-78731ae3349e', 'pictographic-primitives/symbol/messages bubble with dots_a1a51949-b13a-41fa-81ae-78731ae3349e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/messages-bubble-with-dots',)
SOLO_SOURCE_ICON_IDS = ('messages-bubble-with-dots',)
REFERENCE_EXPORT_SHA256 = '39f8291b05f35e684ddf67feec2714d56e71bdfd75efac63617f290be00c2909'

class DrawingContainerSymbol(Sub32):
    icon_id = 'messages-bubble-with-dots-sub32-symbol'
    related_origin_icon_id = 'messages-bubble-with-dots-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/messages-bubble-with-dots-sub32'
    counterpart_icon_id = 'messages-bubble-with-dots-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Message bubble with dots: rounded bubble, tail at the bottom left, two dots 8 units apart.
        self.add_line('b-1', (6, 4), (26, 4))
        self.add_arc('b-2', (26, 4), (30, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('b-3', (30, 8), (30, 18))
        self.add_arc('b-4', (30, 18), (26, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('b-5', (26, 22), (14, 22))
        self.add_line('b-6', (14, 22), (8, 28))
        self.add_line('b-7', (8, 28), (8, 22))
        self.add_line('b-8', (8, 22), (6, 22))
        self.add_arc('b-9', (6, 22), (2, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('b-10', (2, 18), (2, 8))
        self.add_arc('b-11', (2, 8), (6, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('bubble', 'b-1', 'b-2', 'b-3', 'b-4', 'b-5', 'b-6', 'b-7', 'b-8', 'b-9', 'b-10', 'b-11', closed=True)
        self.add_dot('dot-1', (12, 13))
        self.add_dot('dot-2', (20, 13))
