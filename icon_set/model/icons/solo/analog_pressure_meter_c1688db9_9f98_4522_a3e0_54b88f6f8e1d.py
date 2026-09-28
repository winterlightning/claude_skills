"""An analog needle meter with a lower control dot; display border reduced to a divider to keep the needle legible."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1688db9-9f98-4522-a3e0-54b88f6f8e1d'
SOURCE_PATH = 'pictographic-primitives/tools/equipment pressure measure_c1688db9-9f98-4522-a3e0-54b88f6f8e1d.svg'
AUTHOR = 'gpt-6'

class AnalogPressureMeter(Solo48):
    icon_id = 'analog-pressure-meter'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('pressure', 'gauge', 'meter', 'measure', 'needle', 'instrument', 'equipment', 'device')

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

        box('case',8,4,32,40,4)
        self.add_line('display-base',(8,27),(40,27))
        self.relate('connect','display-base','case')
        self.add_line('needle',(24,27),(18,15))
        self.relate('connect','needle','display-base')
        self.add_dot('control',(24,35))
