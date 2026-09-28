"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, arrow.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '398ecdf7-5386-489c-ac93-0b8eaf1c441f'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow back_398ecdf7-5386-489c-ac93-0b8eaf1c441f.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'arrow-bend-left-v2'
    variant_of = 'arrow-bend-left'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_bezier('arrow-0-0', (21, 21), ((21.0, 15.0), (17.0, 12.0), (10, 12)))
        self.add_line('arrow-1-0', (15, 9), (10, 12))
        self.add_line('arrow-1-1', (10, 12), (15, 17))
        self.add_contour('arrow-1', 'arrow-1-0', 'arrow-1-1', closed=False)
        self.relate('connect', 'arrow-0-0', 'arrow-1')
