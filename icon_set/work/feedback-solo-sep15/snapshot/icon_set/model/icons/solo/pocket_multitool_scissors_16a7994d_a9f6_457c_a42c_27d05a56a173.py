"""A capsule pocket tool with deployed crossed scissors; tiny loops and doubled blade edges omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16a7994d-a9f6-457c-a42c-27d05a56a173'
SOURCE_PATH = 'pictographic-primitives/tools/swiss army knife scissors_16a7994d-a9f6-457c-a42c-27d05a56a173.svg'
AUTHOR = 'gpt-6'

class PocketMultitoolScissors(Solo48):
    icon_id = 'pocket-multitool-scissors'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('swiss army knife', 'multitool', 'scissors', 'pocket knife', 'camping', 'outdoor', 'blade', 'tool')

    def build(self) -> None:

        def box(n,x,y,w,h,r=0):
            if not r:
                self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                a,b=pts[j],pts[(j+1)%8]
                if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
                else:self.add_line(n+str(j),a,b)
            self.add_contour(n,*[n+str(j) for j in range(8)],closed=True)

        box('body',6,30,36,12,6)

        self.add_polyline('scissor-a',(16,30),(24,18),(34,6))
        self.add_polyline('scissor-b',(32,30),(24,18),(14,6))
        self.relate('connect','scissor-a','scissor-b')
        self.relate('connect','scissor-a','body')
        self.relate('connect','scissor-b','body')
