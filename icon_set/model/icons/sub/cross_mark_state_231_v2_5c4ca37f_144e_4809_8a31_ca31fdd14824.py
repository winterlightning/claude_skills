"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, cross.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '5c4ca37f-144e-4809-8a31-ca31fdd14824'
SOURCE_PATH = 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'cross-mark-state-231-v2'
    variant_of = 'cross-mark-state-231'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_line('frame-0-0', (4, 6), (28, 6))
        self.add_arc('frame-0-1', (28, 6), (30, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('frame-0-2', (30, 8), (30, 24))
        self.add_arc('frame-0-3', (30, 24), (28, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('frame-0-4', (28, 26), (4, 26))
        self.add_arc('frame-0-5', (4, 26), (2, 24), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('frame-0-6', (2, 24), (2, 8))
        self.add_arc('frame-0-7', (2, 8), (4, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', 'frame-0-6', 'frame-0-7', closed=True)
        self.add_line('cross-0-0', (13, 13), (19, 19))
        self.add_line('cross-1-0', (19, 13), (13, 19))
        self.relate('connect', 'cross-0-0', 'cross-1-0')
