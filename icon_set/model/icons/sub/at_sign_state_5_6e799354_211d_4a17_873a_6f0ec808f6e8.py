"""At Sign: A rounded central bowl connects to a smaller return on its right within a sweeping outer loop. The outer stroke curls around the bowl and ends below it.

Construction: The bowl, returning hook and open outer loop retain the source at-sign.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6e799354-211d-4a17-873a-6f0ec808f6e8'
SOURCE_PATH = 'pictographic-primitives/state/@_6e799354-211d-4a17-873a-6f0ec808f6e8.svg'
AUTHOR = 'gpt-6'


class AtSignState5(Sub32):
    icon_id = 'at-sign-state-5'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sign', 'rounded', 'central', 'bowl', 'connects', 'smaller', 'return', 'right')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('bowl',16,16,6)
        self.add_line('join',(22,16),(26,20))
        self.add_arc('return',(26,20),(30,16),radius_x=4,sweep=False)
        self.add_arc('outer-upper',(30,16),(2,16),radius_x=14,sweep=False)
        self.add_arc('outer-lower',(2,16),(16,30),radius_x=14,sweep=False)
        self.add_contour('outer','join','return','outer-upper','outer-lower')
        self.relate('connect','bowl','outer')
