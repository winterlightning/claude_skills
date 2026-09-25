"""Bubbles: A large circular bubble touches a smaller circle at its upper-right edge. Both interiors are empty, and the two rounded outlines meet without a separate action or status mark.

Construction: Two round bubbles with unequal radii; a clear gap replaces the source overlap.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725'
SOURCE_PATH = 'pictographic-primitives/state/bubble_4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725.svg'
AUTHOR = 'gpt-6'


class Bubbles(Sub32):
    icon_id = 'bubbles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives-generate', 'state')
    aliases = ()
    keywords = ('bubbles', 'large', 'circular', 'bubble', 'touches', 'smaller', 'circle', 'upper')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle("large",12,20,10)
        circle("small",27,5,3)
