"""Circular Arrow: A long curved arrow follows most of a clockwise circle and ends at the upper right. Its head has horizontal and vertical arms, and a gap separates the tip from the tail.

Construction: A radius-10 circular sweep, centered slightly lower and left, flows into a tangent extension. A broad arrowhead has clear space above the smaller sweep.
Keyshape: CIRCLE; the arrowhead supplies the outer radial extent while the circle remains smaller.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'pictographic-primitives/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.svg'
AUTHOR = 'gpt-6'

class CircularArrowSubVariant3ContainerSymbol(Sub32):
    icon_id = 'circular-arrow-sub-v3-symbol'
    related_origin_icon_id = 'circular-arrow-sub-v3'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circular-arrow-sub-v3'
    counterpart_icon_id = 'circular-arrow-sub-v3'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('circular', 'arrow', 'long', 'curved', 'follows', 'most', 'clockwise', 'circle')

    def build(self):
        cx, cy, radius = (14, 18, 10)
        shoulder, tip = ((cx + 6, cy - 8), (28, 16))
        self.add_arc('lower-left', (cx, cy + radius), (cx - radius, cy), radius_x=radius)
        self.add_arc('upper-left', (cx - radius, cy), (cx, cy - radius), radius_x=radius)
        self.add_arc('upper-right', (cx, cy - radius), shoulder, radius_x=radius)
        self.add_line('extension', shoulder, tip)
        self.add_contour('sweep', 'lower-left', 'upper-left', 'upper-right', 'extension')
        self.add_polyline('head', (20, 16), tip, (28, 9))
        self.relate('connect', 'sweep', 'head')
