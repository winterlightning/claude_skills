"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: handset, inner-wave, outer-wave.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'cd4e700a-5d5e-4752-8cea-1bc976043740'
SOURCE_PATH = 'pictographic-primitives/state/airpod wave forward_cd4e700a-5d5e-4752-8cea-1bc976043740.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'sound-waves-v2'
    variant_of = 'sound-waves'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_line('handset-0-0', (8, 2), (10, 2))
        self.add_arc('handset-0-1', (10, 2), (12, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('handset-0-2', (12, 4), (12, 14))
        self.add_line('handset-0-3', (12, 14), (10, 14))
        self.add_line('handset-0-4', (10, 14), (10, 28))
        self.add_arc('handset-0-5', (10, 28), (8, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('handset-0-6', (8, 30), (4, 30))
        self.add_arc('handset-0-7', (4, 30), (2, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('handset-0-8', (2, 28), (2, 8))
        self.add_arc('handset-0-9', (2, 8), (8, 2), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('handset-0', 'handset-0-0', 'handset-0-1', 'handset-0-2', 'handset-0-3', 'handset-0-4', 'handset-0-5', 'handset-0-6', 'handset-0-7', 'handset-0-8', 'handset-0-9', closed=True)
        self.add_bezier('inner-wave-0-0', (19, 10), ((22.0, 13.0), (22.0, 19.0), (19, 22)))
        self.add_bezier('outer-wave-0-0', (25, 4), ((28.0, 7.0), (30.0, 12.0), (30, 16)))
        self.add_bezier('outer-wave-0-1', (30, 16), ((30.0, 20.0), (28.0, 25.0), (25, 28)))
        self.add_contour('outer-wave-0', 'outer-wave-0-0', 'outer-wave-0-1', closed=False)
