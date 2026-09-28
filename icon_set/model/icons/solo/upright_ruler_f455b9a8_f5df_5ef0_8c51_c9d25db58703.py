"""An upright ruler with four evenly spaced alternating graduations; one tick and numbers omitted to preserve end clearances."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f455b9a8-f5df-5ef0-8c51-c9d25db58703'
SOURCE_PATH = 'pictographic-primitives/tools/measure ruler_f455b9a8-f5df-5ef0-8c51-c9d25db58703.svg'
AUTHOR = 'gpt-6'

class UprightRuler(Solo48):
    icon_id = 'upright-ruler'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('ruler', 'measure', 'length', 'scale', 'straightedge', 'ticks', 'drafting', 'tool')

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

        box('ruler',8,4,32,40,4)
        for j,y in enumerate((12,20,28,36)):
            self.add_line('tick'+str(j),(8,y),(20 if j%2==0 else 16,y))
            self.relate('connect','tick'+str(j),'ruler')
