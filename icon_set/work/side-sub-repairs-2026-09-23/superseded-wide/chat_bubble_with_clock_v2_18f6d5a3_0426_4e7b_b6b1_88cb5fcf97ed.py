"""Rounded chat bubble with lower-left tail and centered clock."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import circle
SOURCE_ICON_ID = '18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed'
SOURCE_PATH = 'pictographic-primitives/symbol/chat time clock_18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('speech bubble and lower-left tail', 'clock circle', 'two clock hands')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'chat-bubble-with-clock-v2'
    variant_of = 'chat-bubble-with-clock'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/symbol'
    aliases = ('message-time', 'chat-time')
    keywords = ('chat', 'message', 'clock', 'time')

    def build(self):
        self.add_line('top', (12, 2), (48, 2))
        self.add_arc('top-right', (48, 2), (58, 12), radius_x=10)
        self.add_line('right', (58, 12), (58, 40))
        self.add_arc('bottom-right', (58, 40), (48, 50), radius_x=10)
        self.add_line('bottom', (48, 50), (30, 50))
        self.add_line('tail-upper', (30, 50), (16, 58))
        self.add_line('tail-lower', (16, 58), (16, 50))
        self.add_line('bottom-left-run', (16, 50), (12, 50))
        self.add_arc('bottom-left', (12, 50), (2, 40), radius_x=10)
        self.add_line('left', (2, 40), (2, 12))
        self.add_arc('top-left', (2, 12), (12, 2), radius_x=10)
        self.add_contour('bubble', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'tail-upper', 'tail-lower', 'bottom-left-run', 'bottom-left', 'left', 'top-left', closed=True)
        circle(self, 'clock', 30, 26, 14)
        self.add_polyline('hands', (30, 16), (30, 26), (40, 26))
        self.relate('connect', 'clock', 'hands')
