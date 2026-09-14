"""A boxy jigsaw with handle slot, vertical blade and trailing cord; housing seams omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc02504c-1fd9-4220-bb74-2ff809f58aba'
SOURCE_PATH = 'pictographic-primitives/tools/power tools wood cutter_dc02504c-1fd9-4220-bb74-2ff809f58aba.svg'
AUTHOR = 'gpt-6'

class JigsawPowerTool(Solo48):
    icon_id = 'jigsaw-power-tool'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('jigsaw', 'saw', 'power tool', 'cutting', 'woodworking', 'blade', 'electric', 'tool')

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

        box('body',8,8,28,24,7)
        self.add_line('slot',(18,18),(26,18))
        self.add_line('blade',(16,32),(16,40))
        self.relate('connect','blade','body')
        self.add_line('shoe',(4,40),(32,40))
        self.relate('connect','shoe','blade')
        self.add_line('cord-start',(36,24),(39,24))
        self.add_arc('cord-turn',(39,24),(39,34),radius_x=5)
        self.add_contour('cord','cord-start','cord-turn')
        self.relate('connect','cord','body')
