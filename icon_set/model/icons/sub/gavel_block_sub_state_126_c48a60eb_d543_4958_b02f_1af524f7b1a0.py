"""Gavel Block: A low, wide rectangular block has gently rounded corners and a blank front. It appears alone as a shallow horizontal slab, without a gavel or other surrounding object.

Construction: The source is a blank low rectangular block with slightly rounded corners.
Keyshape: HRECT_S; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c48a60eb-d543-4958-b02f-1af524f7b1a0'
SOURCE_PATH = 'pictographic-primitives/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.svg'
AUTHOR = 'gpt-6'


class GavelBlockSubState126(Sub32):
    icon_id = 'gavel-block-sub-state-126'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('gavel', 'block', 'low', 'wide', 'rectangular', 'gently', 'rounded', 'corners')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('block',2,10,30,22,2)
