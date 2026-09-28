"""A toothed half-blade hangs over a separate plank; grain line and rail curls omitted to preserve separation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4799612-88be-4269-9614-a36785b96c6c'
SOURCE_PATH = 'pictographic-primitives/tools/power tools wood cutter_c4799612-88be-4269-9614-a36785b96c6c.svg'
AUTHOR = 'gpt-6'

class SawBladeOverPlank(Solo48):
    icon_id = 'saw-blade-over-plank'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('saw', 'blade', 'wood', 'plank', 'cutter', 'planer', 'woodworking', 'power tool')

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

        self.add_line('rail',(6,8),(42,8))
        self.add_polyline('blade',(12,8),(12,16),(18,16),(18,22),(24,20),(30,22),(30,16),(36,16),(36,8))
        self.relate('connect','blade','rail')
        box('plank',4,32,40,8)
