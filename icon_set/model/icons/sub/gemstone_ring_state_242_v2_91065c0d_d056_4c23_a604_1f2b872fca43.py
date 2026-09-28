"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: ring, gem.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '91065c0d-d056-4c23-a604-1f2b872fca43'
SOURCE_PATH = 'pictographic-primitives/state/ring_91065c0d-d056-4c23-a604-1f2b872fca43.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'gemstone-ring-state-242-v2'
    variant_of = 'gemstone-ring-state-242'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_arc('ring-0-0', (6, 20), (26, 20), radius_x=10, radius_y=10, large_arc=True, sweep=True)
        self.add_arc('ring-0-1', (26, 20), (6, 20), radius_x=10, radius_y=10, large_arc=True, sweep=True)
        self.add_contour('ring-0', 'ring-0-0', 'ring-0-1', closed=True)
        self.add_line('gem-0-0', (10, 12), (8, 5))
        self.add_line('gem-0-1', (8, 5), (12, 2))
        self.add_line('gem-0-2', (12, 2), (20, 2))
        self.add_line('gem-0-3', (20, 2), (24, 5))
        self.add_line('gem-0-4', (24, 5), (22, 12))
        self.add_contour('gem-0', 'gem-0-0', 'gem-0-1', 'gem-0-2', 'gem-0-3', 'gem-0-4', closed=False)
        self.relate('connect', 'ring-0', 'gem-0')
