"""Euro Sign: A large C-shaped currency curve is crossed by a single horizontal bar extending left of its stem. The curve remains open on the right, with rounded upper and lower ends.

Construction: Four tangent quarter ellipses form an open C; the bar meets the leftmost midpoint.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f98fd830-ab70-4a21-8f49-67aa7e50b273'
SOURCE_PATH = 'pictographic-primitives/state/euro sign_f98fd830-ab70-4a21-8f49-67aa7e50b273.svg'
AUTHOR = 'gpt-6'


class EuroSignSub(Sub32):
    icon_id = 'euro-sign-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('euro', 'sign', 'large', 'c', 'shaped', 'currency', 'curve', 'crossed')

    def build(self):
        self.add_arc("top-right",(30,8),(16,2),radius_x=14,radius_y=6,sweep=False)
        self.add_arc("top-left",(16,2),(4,16),radius_x=12,radius_y=14,sweep=False)
        self.add_arc("bottom-left",(4,16),(16,30),radius_x=12,radius_y=14,sweep=False)
        self.add_arc("bottom-right",(16,30),(30,24),radius_x=14,radius_y=6,sweep=False)
        self.add_contour("c","top-right","top-left","bottom-left","bottom-right")
        self.add_line("bar",(2,16),(20,16))
        self.relate("connect","c","bar")
