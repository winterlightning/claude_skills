"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: upper, lower.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '22ebeb63-e3c2-4cdd-a779-46135c16e412'
SOURCE_PATH = 'pictographic-primitives/state/wind_22ebeb63-e3c2-4cdd-a779-46135c16e412.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'wind-gusts-sub-v2'
    variant_of = 'wind-gusts-sub'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_line('upper-0-0', (2, 14), (24, 14))
        self.add_arc('upper-0-1', (24, 14), (18, 8), radius_x=6, radius_y=6, large_arc=True, sweep=False)
        self.add_contour('upper-0', 'upper-0-0', 'upper-0-1', closed=False)
        self.add_line('lower-0-0', (2, 22), (18, 22))
        self.add_arc('lower-0-1', (18, 22), (14, 26), radius_x=4, radius_y=4, large_arc=True, sweep=True)
        self.add_contour('lower-0', 'lower-0-0', 'lower-0-1', closed=False)
