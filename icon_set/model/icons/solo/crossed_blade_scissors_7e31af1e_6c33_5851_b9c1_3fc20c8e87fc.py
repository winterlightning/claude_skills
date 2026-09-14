"""Straight crossed scissor blades with two circular finger loops; double blade edges and tiny pivot omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e31af1e-6c33-5851-b9c1-3fc20c8e87fc'
SOURCE_PATH = 'pictographic-primitives/tools/scissors_7e31af1e-6c33-5851-b9c1-3fc20c8e87fc.svg'
AUTHOR = 'gpt-6'

class CrossedBladeScissors(Solo48):
    icon_id = 'crossed-blade-scissors'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('scissors', 'cut', 'shears', 'blades', 'crossed', 'craft', 'office', 'tool')

    def build(self) -> None:

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        for n,x in [('left',13),('right',35)]:
            circle(n+'-loop',x,39,5)
        self.add_polyline('blade-a',(13,34),(24,22),(36,6))
        self.add_polyline('blade-b',(35,34),(24,22),(12,6))
        self.relate('connect','blade-a','left-loop')
        self.relate('connect','blade-b','right-loop')
        self.relate('connect','blade-a','blade-b')
