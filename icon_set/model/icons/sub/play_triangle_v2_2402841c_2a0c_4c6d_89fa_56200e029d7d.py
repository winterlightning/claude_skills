"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, play.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '2402841c-2a0c-4c6d-89fa-56200e029d7d'
SOURCE_PATH = 'pictographic-primitives/state/circle play connect_2402841c-2a0c-4c6d-89fa-56200e029d7d.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'play-triangle-v2'
    variant_of = 'play-triangle'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_bezier('frame-0-0', (24, 27), ((22.0, 29.0), (19.0, 30.0), (16, 30)))
        self.add_arc('frame-0-1', (16, 30), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=False)
        self.add_line('play-0-0', (12, 10), (23, 16))
        self.add_line('play-0-1', (23, 16), (12, 22))
        self.add_line('play-0-2', (12, 22), (12, 10))
        self.add_contour('play-0', 'play-0-0', 'play-0-1', 'play-0-2', closed=True)
