"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: arrow, landing.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '22b19b8b-2dbf-4961-8544-e875b0c1ab8a'
SOURCE_PATH = 'pictographic-primitives/state/minimize 1_22b19b8b-2dbf-4961-8544-e875b0c1ab8a.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'arrow-down-right-state-175-v2'
    variant_of = 'arrow-down-right-state-175'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_line('arrow-0-0', (2, 2), (16, 16))
        self.add_line('arrow-1-0', (8, 16), (16, 16))
        self.add_line('arrow-1-1', (16, 16), (16, 8))
        self.add_contour('arrow-1', 'arrow-1-0', 'arrow-1-1', closed=False)
        self.add_line('landing-0-0', (17, 22), (29, 22))
        self.add_arc('landing-0-1', (29, 22), (30, 23), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('landing-0-2', (30, 23), (30, 29))
        self.add_arc('landing-0-3', (30, 29), (29, 30), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('landing-0-4', (29, 30), (17, 30))
        self.add_arc('landing-0-5', (17, 30), (16, 29), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('landing-0-6', (16, 29), (16, 23))
        self.add_arc('landing-0-7', (16, 23), (17, 22), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('landing-0', 'landing-0-0', 'landing-0-1', 'landing-0-2', 'landing-0-3', 'landing-0-4', 'landing-0-5', 'landing-0-6', 'landing-0-7', closed=True)
        self.relate('connect', 'arrow-0-0', 'arrow-1')
