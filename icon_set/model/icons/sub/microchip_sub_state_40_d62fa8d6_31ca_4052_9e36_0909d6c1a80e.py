"""Microchip: A rounded square chip has two short pins projecting from each of its four sides. The central body remains empty, and the evenly spaced pins form a balanced outline.

Construction: A rounded blank chip keeps two attached pins on every side, with shared spacing.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd62fa8d6-31ca-4052-9e36-0909d6c1a80e'
SOURCE_PATH = 'pictographic-primitives/state/chip_d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'
AUTHOR = 'gpt-6'


class MicrochipSubState40(Sub32):
    icon_id = 'microchip-sub-state-40'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('microchip', 'rounded', 'square', 'chip', 'short', 'pins', 'projecting', 'four')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('body',6,6,26,26,3)
        for v in (11,21):
            for name,a,b in ((f'top-{v}',(v,2),(v,6)),(f'bottom-{v}',(v,26),(v,30)),(f'left-{v}',(2,v),(6,v)),(f'right-{v}',(26,v),(30,v))):
                self.add_line(name,a,b)
                self.relate('connect','body',name)
