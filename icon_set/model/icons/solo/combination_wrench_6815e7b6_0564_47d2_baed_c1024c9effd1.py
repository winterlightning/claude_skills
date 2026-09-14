"""A combination wrench with a closed ring end, open crescent jaw and diagonal shank; ring material represented by one outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6815e7b6-0564-47d2-baed-c1024c9effd1'
SOURCE_PATH = 'pictographic-primitives/tools/tools crescent double_6815e7b6-0564-47d2-baed-c1024c9effd1.svg'
AUTHOR = 'gpt-6'

class CombinationWrench(Solo48):
    icon_id = 'combination-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('wrench', 'combination wrench', 'spanner', 'ring', 'repair', 'mechanic', 'hardware', 'tool')

    def build(self) -> None:

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        # Ring and open crescent joined by two diagonal shank edges.
        circle('ring',33,15,9)
        self.add_arc('jaw-top',(6,32),(16,22),radius_x=10)
        self.add_arc('jaw-right',(16,22),(26,32),radius_x=10)
        self.add_arc('jaw-bottom',(26,32),(16,42),radius_x=10)
        self.add_line('jaw-tip',(16,42),(22,36))
        self.add_line('jaw-throat',(22,36),(12,26))
        self.add_line('jaw-mouth',(12,26),(6,32))
        self.add_contour('jaw','jaw-top','jaw-right','jaw-bottom','jaw-tip','jaw-throat','jaw-mouth',closed=True)
        self.add_line('shaft-left',(24,15),(16,22))
        self.add_line('shaft-right',(33,24),(26,32))
        for edge in ['shaft-left','shaft-right']:
            self.relate('connect',edge,'ring')
            self.relate('connect',edge,'jaw')
