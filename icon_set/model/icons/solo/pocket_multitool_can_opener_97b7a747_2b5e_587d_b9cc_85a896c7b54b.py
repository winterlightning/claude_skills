"""A capsule pocket tool with a left-facing hooked opener; small cutting notch broadened."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97b7a747-2b5e-587d-b9cc-85a896c7b54b'
SOURCE_PATH = 'pictographic-primitives/tools/swiss army knife can opener_97b7a747-2b5e-587d-b9cc-85a896c7b54b.svg'
AUTHOR = 'gpt-6'

class PocketMultitoolCanOpener(Solo48):
    icon_id = 'pocket-multitool-can-opener'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('swiss army knife', 'multitool', 'can opener', 'pocket knife', 'camping', 'outdoor', 'opener', 'tool')

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

        self.add_line('back',(32,30),(26,14))
        self.add_arc('hook-back',(26,14),(18,6),radius_x=8,sweep=False)
        self.add_line('tip-1',(18, 6),(10, 12))
        self.add_line('tip-2',(10, 12),(18, 12))
        self.add_arc('hook-inner',(18,12),(22,18),radius_x=6)
        self.add_line('heel-1',(22, 18),(18, 22))
        self.add_line('heel-2',(18, 22),(24, 30))
        self.add_contour('opener','back','hook-back','tip-1','tip-2','hook-inner','heel-1','heel-2')
        self.relate('connect','opener','body')
