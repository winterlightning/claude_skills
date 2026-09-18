"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, arrow.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '90afee1d-c8d3-4450-9484-ad9b41908249'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow right_90afee1d-c8d3-4450-9484-ad9b41908249.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'arrow-right-state-49-v2'
    variant_of = 'arrow-right-state-49'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('arrow-0-0', (10, 16), (22, 16))
        self.add_line('arrow-1-0', (17, 11), (22, 16))
        self.add_line('arrow-1-1', (22, 16), (17, 21))
        self.add_contour('arrow-1', 'arrow-1-0', 'arrow-1-1', closed=False)
        self.relate('connect', 'arrow-0-0', 'arrow-1')
