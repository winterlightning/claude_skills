"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: frame, play.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '19c25b61-6678-43f8-aae6-dc07a9ea8291'
SOURCE_PATH = 'pictographic-primitives/state/circle play_19c25b61-6678-43f8-aae6-dc07a9ea8291.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'play-triangle-state-74-v2'
    variant_of = 'play-triangle-state-74'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_arc('frame-0-0', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('frame-0-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('frame-0', 'frame-0-0', 'frame-0-1', closed=True)
        self.add_line('play-0-0', (12, 10), (23, 16))
        self.add_line('play-0-1', (23, 16), (12, 22))
        self.add_line('play-0-2', (12, 22), (12, 10))
        self.add_contour('play-0', 'play-0-0', 'play-0-1', 'play-0-2', closed=True)
