"""An open toolbox holds a wrench and hammer; latch notch and minor tool seams omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c81d578-87d9-40c2-9864-7e609646af17'
SOURCE_PATH = 'pictographic-primitives/tools/toolbox open_8c81d578-87d9-40c2-9864-7e609646af17.svg'
AUTHOR = 'gpt-6'

class OpenToolboxWithTools(Solo48):
    icon_id = 'open-toolbox-with-tools'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('toolbox', 'tools', 'wrench', 'hammer', 'repair', 'maintenance', 'kit', 'workshop')

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

        box('box',6,30,36,12,3)
        self.add_polyline('wrench',(10,6),(10,14),(22,14),(22,6))
        self.add_line('wrench-shaft',(16,14),(16,30))
        self.relate('connect','wrench','wrench-shaft')
        self.relate('connect','wrench-shaft','box')
        box('hammer-head',30,6,12,8)
        self.add_line('hammer-shaft',(36,14),(30,30))
        self.relate('connect','hammer-shaft','hammer-head')
        self.relate('connect','hammer-shaft','box')
