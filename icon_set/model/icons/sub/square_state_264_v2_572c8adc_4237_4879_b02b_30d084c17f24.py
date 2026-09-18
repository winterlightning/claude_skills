"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, square.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '572c8adc-4237-4879-b02b-30d084c17f24'
SOURCE_PATH = 'pictographic-primitives/state/square circle_572c8adc-4237-4879-b02b-30d084c17f24.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'square-state-264-v2'
    variant_of = 'square-state-264'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('square-0-0', (11, 11), (21, 11))
        self.add_line('square-0-1', (21, 11), (21, 21))
        self.add_line('square-0-2', (21, 21), (11, 21))
        self.add_line('square-0-3', (11, 21), (11, 11))
        self.add_contour('square-0', 'square-0-0', 'square-0-1', 'square-0-2', 'square-0-3', closed=True)
