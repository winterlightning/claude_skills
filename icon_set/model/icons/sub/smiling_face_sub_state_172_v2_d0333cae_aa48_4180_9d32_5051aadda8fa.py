"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, eye-left, eye-right, mouth.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'd0333cae-aa48-4180-9d32-5051aadda8fa'
SOURCE_PATH = 'pictographic-primitives/state/messages bubble round smile_d0333cae-aa48-4180-9d32-5051aadda8fa.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'smiling-face-sub-state-172-v2'
    variant_of = 'smiling-face-sub-state-172'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_bezier('frame-0-0', (16, 2), ((8.0, 2.0), (2.0, 6.0), (2, 14)))
        self.add_bezier('frame-0-1', (2, 14), ((2.0, 18.0), (3.0, 21.0), (6, 23)))
        self.add_line('frame-0-2', (6, 23), (3, 30))
        self.add_line('frame-0-3', (3, 30), (12, 26))
        self.add_bezier('frame-0-4', (12, 26), ((23.0, 28.0), (30.0, 23.0), (30, 14)))
        self.add_bezier('frame-0-5', (30, 14), ((30.0, 6.0), (24.0, 2.0), (16, 2)))
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', 'frame-0-2', 'frame-0-3', 'frame-0-4', 'frame-0-5', closed=True)
        self.add_line('eye-left-0-0', (11, 10), (11, 11))
        self.add_line('eye-right-0-0', (21, 10), (21, 11))
        self.add_bezier('mouth-0-0', (11, 18), ((14.0, 20.0), (18.0, 20.0), (21, 18)))
