"""A wheel brace with a zigzag shaft, rounded lower grip and square upper socket; the tiny square bit is omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45297689-9ca7-417b-a96a-a28c28a90b6a'
SOURCE_PATH = 'pictographic-primitives/tools/tools wheel unscrew_45297689-9ca7-417b-a96a-a28c28a90b6a.svg'
AUTHOR = 'gpt-6'

class CrankWheelBrace(Solo48):
    icon_id = 'crank-wheel-brace'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('wheel brace', 'lug wrench', 'crank', 'unscrew', 'tire', 'car', 'socket', 'tool')

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

        box('grip',6,30,12,12,4)
        self.add_polyline('crank',(18,34),(22,34),(22,6),(30,6))
        box('socket',30,6,12,16,0)
        self.relate('connect','crank','grip')
        self.relate('connect','crank','socket')
