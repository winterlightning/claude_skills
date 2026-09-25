"""Circular Arrow: A long curved arrow follows most of a clockwise circle and ends at the upper right. Its head has horizontal and vertical arms, and a gap separates the tip from the tail.

Construction: Three cardinal circle quadrants and a shortened upper-right quadrant; an angular arrowhead shares the end.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'pictographic-primitives/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.svg'
AUTHOR = 'gpt-6'


class CircularArrowSub(Sub32):
    icon_id = 'circular-arrow-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('circular', 'arrow', 'long', 'curved', 'follows', 'most', 'clockwise', 'circle')

    def build(self):
        self.add_arc("top",(2,16),(16,2),radius_x=14)
        self.add_arc("turn",(16,2),(30,16),radius_x=14)
        self.add_arc("bottom",(30,24),(16,30),radius_x=14,radius_y=6)
        self.add_arc("left",(16,30),(2,16),radius_x=14)
        self.add_contour("tail","bottom","left","top","turn")
        self.add_polyline("head",(22,16),(30,16),(30,8))
        self.relate("connect","tail","head")
