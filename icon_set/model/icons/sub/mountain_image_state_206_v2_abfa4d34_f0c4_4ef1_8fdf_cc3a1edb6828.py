"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, mountain, sun.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828'
SOURCE_PATH = 'pictographic-primitives/state/photo_abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'mountain-image-state-206-v2'
    variant_of = 'mountain-image-state-206'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_line('frame-0-0', (5, 2), (27, 2))
        self.add_arc('frame-0-1', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-2', (30, 5), (30, 27))
        self.add_arc('frame-0-3', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-4', (27, 30), (5, 30))
        self.add_arc('frame-0-5', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-6', (2, 27), (2, 5))
        self.add_arc('frame-0-7', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', closed=True)
        self.add_line('mountain-0-0', (9, 23), (13, 18))
        self.add_line('mountain-0-1', (13, 18), (17, 22))
        self.add_line('mountain-0-2', (17, 22), (21, 14))
        self.add_line('mountain-0-3', (21, 14), (23, 18))
        self.add_contour('mountain-0', 'mountain-0-0', 'mountain-0-1', 'mountain-0-2', 'mountain-0-3', closed=False)
        self.add_line('sun-0-0', (10, 10), (10, 10))
