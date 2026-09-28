"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, eye-left, eye-right, mouth.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '26f40b93-a3b7-419f-a55b-3b6e5693c80a'
SOURCE_PATH = 'pictographic-primitives/state/circle smiley face_26f40b93-a3b7-419f-a55b-3b6e5693c80a.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'smiling-face-sub-v2'
    variant_of = 'smiling-face-sub'
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
        self.add_line('eye-left-0-0', (11, 11), (11, 12))
        self.add_line('eye-right-0-0', (21, 11), (21, 12))
        self.add_bezier('mouth-0-0', (10, 20), ((13.0, 25.0), (19.0, 25.0), (22, 20)))
