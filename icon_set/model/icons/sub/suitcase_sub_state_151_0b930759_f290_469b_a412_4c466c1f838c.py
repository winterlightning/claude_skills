"""Suitcase: An upright suitcase has a broad body with rounded corners, a short rectangular handle above, and two short supports below. Its front remains completely blank.

Construction: A blank rounded suitcase retains its upper handle and two short bottom supports.
Keyshape: VRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0b930759-f290-469b-a412-4c466c1f838c'
SOURCE_PATH = 'pictographic-primitives/state/luggage_0b930759-f290-469b-a412-4c466c1f838c.svg'
AUTHOR = 'gpt-6'


class SuitcaseSubState151(Sub32):
    icon_id = 'suitcase-sub-state-151'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('suitcase', 'upright', 'broad', 'body', 'rounded', 'corners', 'short', 'rectangular')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('body',4,10,28,26,3)
        self.add_polyline('handle',(10,10),(10,2),(22,2),(22,10))
        self.relate('connect','body','handle')
        for x in (6,26):
            self.add_line(f'foot-{x}',(x,26),(x,30))
            self.relate('connect','body',f'foot-{x}')
