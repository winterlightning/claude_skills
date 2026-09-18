"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, arc-a, arc-b, arc-c.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'a004a57a-6eea-490b-8683-cc169050a26a'
SOURCE_PATH = 'pictographic-primitives/state/slice_a004a57a-6eea-490b-8683-cc169050a26a.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'broken-ring-v2'
    variant_of = 'broken-ring'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_arc('arc-a-0-0', (12, 12), (15, 10), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('arc-b-0-0', (22, 14), (22, 17), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('arc-c-0-0', (16, 22), (12, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
