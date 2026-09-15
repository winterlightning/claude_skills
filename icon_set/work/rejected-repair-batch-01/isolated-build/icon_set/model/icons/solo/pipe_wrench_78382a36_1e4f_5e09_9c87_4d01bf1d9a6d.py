"""An adjustable pipe wrench with hooked upper jaw, lower opposing jaw and long broad handle; screw ridges omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78382a36-1e4f-5e09-9c87-4d01bf1d9a6d'
SOURCE_PATH = 'pictographic-primitives/tools/tools vice grip_78382a36-1e4f-5e09-9c87-4d01bf1d9a6d.svg'
AUTHOR = 'gpt-6'

class PipeWrench(Solo48):
    icon_id = 'pipe-wrench'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('pipe wrench', 'wrench', 'vice grip', 'plumbing', 'adjustable', 'pipe', 'hardware', 'tool')

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

        self.add_polyline('upper-jaw',(8,20),(8,4),(40,4),(40,12))
        self.add_polyline('lower-jaw',(8,28),(32,28),(40,20))
        box('handle',8,28,12,16,0)
        self.add_line('spine',(8,20),(8,28))
        self.relate('connect','spine','upper-jaw')
        self.relate('connect','spine','lower-jaw')
        self.relate('connect','lower-jaw','handle')
        self.relate('connect','spine','handle')
