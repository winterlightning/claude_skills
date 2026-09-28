# Variant of euro-sign-sub; parent file remains unchanged.
"""Euro Sign: A large C-shaped currency curve is crossed by a single horizontal bar extending left of its stem. The curve remains open on the right, with rounded upper and lower ends.

Construction: A vertically mirrored half ellipse flows tangentially into short horizontal terminals. A single source-faithful crossbar projects left of the curve.
Keyshape: VRECT_L; centerline extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f98fd830-ab70-4a21-8f49-67aa7e50b273'
SOURCE_PATH = 'pictographic-primitives/state/euro sign_f98fd830-ab70-4a21-8f49-67aa7e50b273.svg'
AUTHOR = 'gpt-6'

class EuroSignSubVariant2(Sub32):
    icon_id = 'euro-sign-sub-v2'
    variant_of = 'euro-sign-sub'
    variant_label = 'Balanced euro curve'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('primitives-generate', 'state')
    aliases = ()
    keywords = ('euro', 'sign', 'large', 'c', 'shaped', 'currency', 'curve', 'crossed')

    def build(self):
        cx, cy, rx, ry = 20, 16, 12, 14
        top, left, bottom = (cx, cy - ry), (cx - rx, cy), (cx, cy + ry)
        self.add_line('upper-terminal', (26, top[1]), top)
        self.add_arc('upper-curve', top, left, radius_x=rx, radius_y=ry, sweep=False)
        self.add_arc('lower-curve', left, bottom, radius_x=rx, radius_y=ry, sweep=False)
        self.add_line('lower-terminal', bottom, (26, bottom[1]))
        self.add_contour('curve', 'upper-terminal', 'upper-curve', 'lower-curve', 'lower-terminal')
        self.add_line('bar', (6, cy), (22, cy))
        self.relate('connect', 'curve', 'bar')
