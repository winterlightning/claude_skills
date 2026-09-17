"""Three-Leaf Clover: Three heart-shaped leaves meet at a shared central junction, pointing upward, left, and right. A narrow curved stem descends from the junction beneath the spreading leaves.

Construction: A single trefoil outline has three rounded lobes and a separate curved stem sharing its base.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '15eae920-a828-4e82-80ae-2bcb9cd7a2f2'
SOURCE_PATH = 'pictographic-primitives/state/clover_15eae920-a828-4e82-80ae-2bcb9cd7a2f2.svg'
AUTHOR = 'gpt-6'


class ThreeLeafClover(Sub32):
    icon_id = 'three-leaf-clover'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('leaf', 'clover', 'heart', 'shaped', 'leaves', 'meet', 'shared', 'central')

    def build(self):
        self.add_line("neck-left",(10,14),(10,8))
        self.add_arc("top",(10,8),(22,8),radius_x=6)
        self.add_line("neck-right",(22,8),(22,14))
        self.add_arc("right-top",(22,14),(30,20),radius_x=8,radius_y=6)
        self.add_arc("right-bottom",(30,20),(22,26),radius_x=8,radius_y=6)
        self.add_line("base-1",(22,26),(16,22))
        self.add_line("base-2",(16,22),(10,26))
        self.add_arc("left-bottom",(10,26),(2,20),radius_x=8,radius_y=6)
        self.add_arc("left-top",(2,20),(10,14),radius_x=8,radius_y=6)
        self.add_contour("leaves","neck-left","top","neck-right","right-top","right-bottom","base-1","base-2","left-bottom","left-top",closed=True)
        self.add_line("stem",(16,22),(14,30))
        self.relate("connect","leaves","stem")
