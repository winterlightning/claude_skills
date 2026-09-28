"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, trend.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'a10ca9c7-11ee-4f85-a018-73f458ce70c0'
SOURCE_PATH = 'pictographic-primitives/state/circle arrow_a10ca9c7-11ee-4f85-a018-73f458ce70c0.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'arrow-trend-up-left-v2'
    variant_of = 'arrow-trend-up-left'
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
        self.add_line('trend-0-0', (22, 12), (17, 18))
        self.add_line('trend-0-1', (17, 18), (10, 11))
        self.add_contour('trend-0', 'trend-0-0', 'trend-0-1', closed=False)
        self.add_line('trend-1-0', (10, 18), (10, 11))
        self.add_line('trend-1-1', (10, 11), (17, 11))
        self.add_contour('trend-1', 'trend-1-0', 'trend-1-1', closed=False)
        self.relate('connect', 'trend-0', 'trend-1')
