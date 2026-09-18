"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, arrow.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '05712fab-9325-43d9-b772-0f0ccf3bbfe6'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow down left_05712fab-9325-43d9-b772-0f0ccf3bbfe6.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'arrow-down-left-state-48-v2'
    variant_of = 'arrow-down-left-state-48'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('arrow-0-0', (21, 11), (11, 21))
        self.add_line('arrow-1-0', (11, 14), (11, 21))
        self.add_line('arrow-1-1', (11, 21), (18, 21))
        self.add_contour('arrow-1', 'arrow-1-0', 'arrow-1-1', closed=False)
        self.relate('connect', 'arrow-0-0', 'arrow-1')
