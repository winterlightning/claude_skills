"""Rounded battery case, separate right terminal, and central charging bolt."""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
from ._compact_reference_helpers import rounded_rect
SOURCE_ICON_ID = '638f0a9f-914c-4078-b32c-13c8ec4aacf6'
SOURCE_PATH = 'pictographic-primitives/other/battery 1_638f0a9f-914c-4078-b32c-13c8ec4aacf6.svg'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('rounded battery case', 'right terminal', 'lightning bolt')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 52
    icon_id = 'charging-battery-symbol-v2'
    variant_of = 'charging-battery-symbol'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/state'
    aliases = ('battery-charging',)
    keywords = ('battery', 'charge', 'power', 'bolt')

    def build(self):
        rounded_rect(self, 'battery', 2, 2, 50, 50, 8)
        self.add_line('terminal', (58, 18), (58, 34))
        self.add_polyline('bolt', (34, 12), (20, 30), (32, 28), (24, 42))
