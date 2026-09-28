"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, cross.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.
Source is a map pin with rounded crown and pointed base, not a circle or diamond.
"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '17182188-4f92-4523-a585-9c4533451c16'
SOURCE_PATH = 'pictographic-primitives/state/x pin_17182188-4f92-4523-a585-9c4533451c16.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'cross-mark-state-306-v2'
    variant_of = 'cross-mark-state-306'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_bezier('frame-0-0', (16, 30), ((11.0, 25.0), (6.0, 20.0), (6, 12)))
        self.add_bezier('frame-0-1', (6, 12), ((6.0, 6.0), (10.0, 2.0), (16, 2)))
        self.add_bezier('frame-0-2', (16, 2), ((22.0, 2.0), (26.0, 6.0), (26, 12)))
        self.add_bezier('frame-0-3', (26, 12), ((26.0, 20.0), (21.0, 25.0), (16, 30)))
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', closed=True)
        self.add_line('cross-0-0', (13, 10), (19, 16))
        self.add_line('cross-1-0', (19, 10), (13, 16))
        self.relate('connect', 'cross-0-0', 'cross-1-0')
