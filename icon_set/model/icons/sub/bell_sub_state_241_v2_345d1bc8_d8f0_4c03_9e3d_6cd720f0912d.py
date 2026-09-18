"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: bell, clapper.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '345d1bc8-d8f0-4c03-9e3d-6cd720f0912d'
SOURCE_PATH = 'pictographic-primitives/state/ring_345d1bc8-d8f0-4c03-9e3d-6cd720f0912d.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'bell-sub-state-241-v2'
    variant_of = 'bell-sub-state-241'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_bezier('bell-0-0', (2, 22), ((6.0, 18.0), (6.0, 17.0), (6, 12)))
        self.add_bezier('bell-0-1', (6, 12), ((6.0, 6.0), (10.0, 2.0), (16, 2)))
        self.add_bezier('bell-0-2', (16, 2), ((22.0, 2.0), (26.0, 6.0), (26, 12)))
        self.add_bezier('bell-0-3', (26, 12), ((26.0, 17.0), (26.0, 18.0), (30, 22)))
        self.add_line('bell-0-4', (30, 22), (2, 22))
        self.add_contour('bell-0', 'bell-0-0', 'bell-0-1', 'bell-0-2', 'bell-0-3', 'bell-0-4', closed=True)
        self.add_line('clapper-0-0', (14, 30), (18, 30))
