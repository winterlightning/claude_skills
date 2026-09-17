"""Arrow Counterclockwise: A nearly circular open arrow ends at the left in a downward-pointing angular head. Generate this component alone; exclude Leaf.

Construction: A radius-10 circular sweep and short extension end in an open downward head at the left, preserving the lower-left opening.
Keyshape: CIRCLE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '34cfa58d-681e-489e-ad61-e32cc51234d7'
SOURCE_PATH = 'pictographic-primitives/state/recycle leaf_34cfa58d-681e-489e-ad61-e32cc51234d7.svg'
AUTHOR = 'gpt-6'


class ArrowCounterclockwise(Sub32):
    icon_id = 'arrow-counterclockwise'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'counterclockwise', 'nearly', 'circular', 'open', 'ends', 'left', 'downward')

    def build(self):
        cx, cy, radius = 18, 16, 10
        self.add_arc('lower',(cx,cy+radius),(cx+radius,cy),radius_x=radius,sweep=False)
        self.add_arc('upper',(cx+radius,cy),(cx-radius,cy),radius_x=radius,sweep=False)
        self.add_line('extension',(cx-radius,cy),(8,22))
        self.add_contour('sweep','lower','upper','extension')
        self.add_polyline('head',(2,16),(8,22),(14,16))
        self.relate('connect','sweep','head')
