"""Two left-facing clamp jaws on an upright bar with a lower screw; dense threads omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77cd1486-6f65-42a4-ba97-fa119288dc79'
SOURCE_PATH = 'pictographic-primitives/tools/jackclamp_77cd1486-6f65-42a4-ba97-fa119288dc79.svg'
AUTHOR = 'gpt-6'

class BarClamp(Solo48):
    icon_id = 'bar-clamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('clamp', 'bar clamp', 'quick clamp', 'hold', 'woodworking', 'workshop', 'jaws', 'tool')

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

        box('upper-jaw',6,6,26,8,4)
        box('lower-jaw',6,26,26,8,4)
        self.add_line('bar',(32,10),(32,42))
        self.relate('connect','bar','upper-jaw')
        self.relate('connect','bar','lower-jaw')
        self.add_line('screw',(32,42),(42,42))
        self.add_line('knob',(42,36),(42,42))
        self.relate('connect','screw','bar')
        self.relate('connect','screw','knob')
