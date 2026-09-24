"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, slash, upper, lower.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '01ec16aa-50ee-4ece-addd-2a4b27425d93'
SOURCE_PATH = 'pictographic-primitives/state/percent symbol circle_01ec16aa-50ee-4ece-addd-2a4b27425d93.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'percent-sign-v2'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('slash-0-0', (11, 22), (21, 10))
        self.add_line('upper-0-0', (11, 11), (11, 11))
        self.add_line('lower-0-0', (21, 21), (21, 21))
