"""Arrow Counterclockwise: A nearly circular arrow opens at the lower left and ends in a downward-pointing head at the left. Generate this component alone; exclude User Portrait.

Construction: The nearly circular source arrow retains its left downward head and lower-left opening; portrait excluded.
Keyshape: CIRCLE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '60e9babd-604c-4cb1-b70b-c30eaa2bec95'
SOURCE_PATH = 'pictographic-primitives/state/user sync_60e9babd-604c-4cb1-b70b-c30eaa2bec95.svg'
AUTHOR = 'gpt-6'


class ArrowCounterclockwiseState291(Sub32):
    icon_id = 'arrow-counterclockwise-state-291'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'counterclockwise', 'nearly', 'circular', 'opens', 'lower', 'left', 'ends')

    def build(self):
        cx, cy, radius = 18, 16, 10
        self.add_arc('lower',(cx,cy+radius),(cx+radius,cy),radius_x=radius,sweep=False)
        self.add_arc('upper',(cx+radius,cy),(cx-radius,cy),radius_x=radius,sweep=False)
        self.add_line('extension',(cx-radius,cy),(8,22))
        self.add_contour('sweep','lower','upper','extension')
        self.add_polyline('head',(2,16),(8,22),(14,16))
        self.relate('connect','sweep','head')
