"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, heart.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '29604065-1175-4732-a32c-afa455c4c9ab'
SOURCE_PATH = 'pictographic-primitives/state/circle heart_29604065-1175-4732-a32c-afa455c4c9ab.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'heart-state-63-v2'
    variant_of = 'heart-state-63'
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
        self.add_bezier('heart-0-0', (16, 13), ((11.0, 7.0), (7.0, 13.0), (11, 18)))
        self.add_line('heart-0-1', (11, 18), (16, 22))
        self.add_line('heart-0-2', (16, 22), (21, 18))
        self.add_bezier('heart-0-3', (21, 18), ((25.0, 13.0), (21.0, 7.0), (16, 13)))
        self.add_contour('heart-0', 'heart-0-0', 'heart-0-1', 'heart-0-2', 'heart-0-3', closed=True)
