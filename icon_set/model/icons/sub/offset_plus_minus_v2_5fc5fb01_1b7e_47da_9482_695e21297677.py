"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, plus, minus.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '5fc5fb01-1b7e-47da-9482-695e21297677'
SOURCE_PATH = 'pictographic-primitives/state/circle plus minus 1_5fc5fb01-1b7e-47da-9482-695e21297677.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'offset-plus-minus-v2'
    variant_of = 'offset-plus-minus'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('plus-0-0', (10, 13), (18, 13))
        self.add_line('plus-1-0', (14, 9), (14, 17))
        self.add_line('minus-0-0', (18, 22), (21, 22))
        self.relate('connect', 'plus-0-0', 'plus-1-0')
