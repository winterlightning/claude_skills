"""Unlocked Padlock: A rounded rectangular lock body supports an arched shackle attached on the left. The shackle curves over the body and ends freely above its upper-right edge.

Construction: Plain rounded lock body keeps its open curved shackle, with no keyhole invented.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4aa8fd4e-dd20-4ab4-9374-89370bfa9188'
SOURCE_PATH = 'pictographic-primitives/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.svg'
AUTHOR = 'gpt-6'


class UnlockedPadlockState288(Sub32):
    icon_id = 'unlocked-padlock-state-288'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('unlocked', 'padlock', 'rounded', 'rectangular', 'lock', 'body', 'supports', 'arched')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('body',6,16,26,30,3)
        self.add_line('shackle-side',(10,16),(10,9))
        self.add_arc('shackle-top',(10,9),(24,9),radius_x=7)
        self.add_contour('shackle','shackle-side','shackle-top')
        self.relate('connect','body','shackle')
