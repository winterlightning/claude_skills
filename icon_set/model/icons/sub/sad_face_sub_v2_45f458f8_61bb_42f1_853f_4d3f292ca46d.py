"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, eye-left, eye-right, mouth.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '45f458f8-61bb-42f1-853f-4d3f292ca46d'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble square sad_45f458f8-61bb-42f1-853f-4d3f292ca46d.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'sad-face-sub-v2'
    variant_of = 'sad-face-sub'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_line('frame-0-0', (5, 2), (27, 2))
        self.add_arc('frame-0-1', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-2', (30, 5), (30, 21))
        self.add_arc('frame-0-3', (30, 21), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-4', (27, 24), (23, 24))
        self.add_line('frame-0-5', (23, 24), (23, 30))
        self.add_line('frame-0-6', (23, 30), (16, 24))
        self.add_line('frame-0-7', (16, 24), (5, 24))
        self.add_arc('frame-0-8', (5, 24), (2, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-9', (2, 21), (2, 5))
        self.add_arc('frame-0-10', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', 'frame-0-8', 'frame-0-9', 'frame-0-10', closed=True)
        self.add_line('eye-left-0-0', (11, 9), (11, 10))
        self.add_line('eye-right-0-0', (21, 9), (21, 10))
        self.add_bezier('mouth-0-0', (11, 17), ((14.0, 15.0), (18.0, 15.0), (21, 17)))
