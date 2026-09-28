"""Complete reference redraw on SUB32; earlier incomplete variant preserved.
Source parts: outer, inner, headset.
Construction: native 32px layout, 4px strokes, integer nodes; complete source comparison.

"""
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '4b81caa3-7500-4d62-bd55-fb2f5c09c2bd'
SOURCE_PATH = 'pictographic-primitives/state/vr headset wifi_4b81caa3-7500-4d62-bd55-fb2f5c09c2bd.svg'
AUTHOR = 'gpt-6'
class CompleteReferenceRedraw(Sub32):
    icon_id = 'wireless-arcs-state-297-v2'
    variant_of = 'wireless-arcs-state-297'
    variant_label = 'Complete reference redraw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    def build(self):
        self.add_bezier('outer-0-0', (6, 5), ((12.0, 1.0), (20.0, 1.0), (26, 5)))
        self.add_bezier('inner-0-0', (12, 11), ((14.0, 9.0), (18.0, 9.0), (20, 11)))
        self.add_bezier('headset-0-0', (7, 20), ((12.0, 18.0), (20.0, 18.0), (25, 20)))
        self.add_bezier('headset-0-1', (25, 20), ((28.0, 21.0), (30.0, 23.0), (30, 26)))
        self.add_bezier('headset-0-2', (30, 26), ((30.0, 29.0), (28.0, 30.0), (26, 30)))
        self.add_bezier('headset-0-3', (26, 30), ((22.0, 30.0), (21.0, 25.0), (16, 25)))
        self.add_bezier('headset-0-4', (16, 25), ((11.0, 25.0), (10.0, 30.0), (6, 30)))
        self.add_bezier('headset-0-5', (6, 30), ((4.0, 30.0), (2.0, 29.0), (2, 26)))
        self.add_bezier('headset-0-6', (2, 26), ((2.0, 23.0), (4.0, 21.0), (7, 20)))
        self.add_contour('headset-0', 'headset-0-0', 'headset-0-1', 'headset-0-2', 'headset-0-3', 'headset-0-4', 'headset-0-5', 'headset-0-6', closed=True)
