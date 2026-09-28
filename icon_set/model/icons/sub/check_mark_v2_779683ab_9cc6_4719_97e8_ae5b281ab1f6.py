"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, check.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '779683ab-9cc6-4719-97e8-ae5b281ab1f6'
SOURCE_PATH = 'pictographic-primitives/state/file check_779683ab-9cc6-4719-97e8-ae5b281ab1f6.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'check-mark-v2'
    variant_of = 'check-mark'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_line('frame-0-0', (6, 2), (21, 2))
        self.add_line('frame-0-1', (21, 2), (28, 9))
        self.add_line('frame-0-2', (28, 9), (28, 27))
        self.add_arc('frame-0-3', (28, 27), (25, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-4', (25, 30), (7, 30))
        self.add_arc('frame-0-5', (7, 30), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-6', (4, 27), (4, 5))
        self.add_arc('frame-0-7', (4, 5), (7, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('frame-0-8', (7, 2), (6, 2))
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', 'frame-0-8', closed=True)
        self.add_line('check-0-0', (11, 17), (15, 21))
        self.add_line('check-0-1', (15, 21), (21, 14))
        self.add_contour('check-0', 'check-0-0', 'check-0-1', closed=False)
