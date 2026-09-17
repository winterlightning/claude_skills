"""Key: A large circular key bow sits at the upper right of a diagonal shaft extending down-left. Two short teeth project from one side near the shaft's lower end.

Construction: Diagonal key keeps its large empty upper-right bow and two lower-right-facing teeth along the shaft.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '83975ae2-2084-4cd7-9672-1f60ee985535'
SOURCE_PATH = 'pictographic-primitives/state/key 3_83975ae2-2084-4cd7-9672-1f60ee985535.svg'
AUTHOR = 'gpt-6'


class KeyState142(Sub32):
    icon_id = 'key-state-142'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('key', 'large', 'circular', 'bow', 'sits', 'upper', 'right', 'diagonal')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('bow',20,12,10)
        self.add_line('shaft',(2,30),(14,20))
        self.relate('connect','bow','shaft')
        for n,a,b in [('first',(2,30),(6,30)),('second',(8,25),(12,29))]:
            self.add_line(n,a,b)
            self.relate('connect','shaft',n)
