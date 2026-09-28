"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, handle, top, lower.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '95ce7206-163d-407b-992a-15a039d71489'
SOURCE_PATH = 'pictographic-primitives/state/magnify glass 1_95ce7206-163d-407b-992a-15a039d71489.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'two-text-lines-v2'
    variant_of = 'two-text-lines'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_arc('frame-0-0', (2, 14), (26, 14), radius_x=12, radius_y=12, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (26, 14), (2, 14), radius_x=12, radius_y=12, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('handle-0-0', (22, 22), (30, 30))
        self.add_line('top-0-0', (10, 10), (18, 10))
        self.add_line('lower-0-0', (11, 18), (16, 18))
        self.relate('connect', 'frame-0', 'handle-0-0')
