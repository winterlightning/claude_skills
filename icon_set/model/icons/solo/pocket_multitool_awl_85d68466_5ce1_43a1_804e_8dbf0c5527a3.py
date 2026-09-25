"""A capsule pocket tool with an upright pointed awl; body hardware omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85d68466-5ce1-43a1-804e-8dbf0c5527a3'
SOURCE_PATH = 'pictographic-primitives/tools/swiss army knife awl_85d68466-5ce1-43a1-804e-8dbf0c5527a3.svg'
AUTHOR = 'gpt-6'

class PocketMultitoolAwl(Solo48):
    icon_id = 'pocket-multitool-awl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('swiss army knife', 'multitool', 'awl', 'pocket knife', 'camping', 'outdoor', 'punch', 'tool')

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

        self.add_polyline('awl',(20,30),(20,16),(24,6),(28,16),(28,30))
        self.relate('connect','awl','body')
