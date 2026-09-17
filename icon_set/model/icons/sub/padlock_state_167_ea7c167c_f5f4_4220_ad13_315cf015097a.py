"""Padlock: A rounded rectangular lock body supports a tall arched shackle, with a tiny keyhole dot centred on the body. Generate this component alone; exclude Speech Bubble.

Construction: The source closed padlock keeps its arched shackle, rounded body and tiny central keyhole dot.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ea7c167c-f5f4-4220-ad13-315cf015097a'
SOURCE_PATH = 'pictographic-primitives/state/message lock_ea7c167c-f5f4-4220-ad13-315cf015097a.svg'
AUTHOR = 'gpt-6'


class PadlockState167(Sub32):
    icon_id = 'padlock-state-167'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('padlock', 'rounded', 'rectangular', 'lock', 'body', 'supports', 'tall', 'arched')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('body',6,14,26,30,3)
        self.add_line('shackle-left',(10,14),(10,8))
        self.add_arc('shackle-top',(10,8),(22,8),radius_x=6)
        self.add_line('shackle-right',(22,8),(22,14))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','body','shackle')
        self.add_dot('keyhole',(16,22))
