"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: outline, vein.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '8024309f-c48a-48ee-abd1-6650423aefd7'
SOURCE_PATH = 'pictographic-primitives/state/leaf horizontal_8024309f-c48a-48ee-abd1-6650423aefd7.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'leaf-v2'
    variant_of = 'leaf'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    def build(self):
        self.add_bezier('outline-0-0', (6, 24), ((2.0, 12.0), (10.0, 6.0), (17, 6)))
        self.add_bezier('outline-0-1', (17, 6), ((22.0, 6.0), (24.0, 10.0), (30, 10)))
        self.add_bezier('outline-0-2', (30, 10), ((26.0, 19.0), (23.0, 26.0), (16, 26)))
        self.add_bezier('outline-0-3', (16, 26), ((12.0, 26.0), (9.0, 25.0), (6, 24)))
        self.add_contour('outline-0', 'outline-0-0', 'outline-0-1', 'outline-0-2', 'outline-0-3', closed=True)
        self.add_bezier('vein-0-0', (2, 26), ((8.0, 21.0), (14.0, 18.0), (20, 18)))
        self.relate('connect', 'outline-0', 'vein-0-0')
