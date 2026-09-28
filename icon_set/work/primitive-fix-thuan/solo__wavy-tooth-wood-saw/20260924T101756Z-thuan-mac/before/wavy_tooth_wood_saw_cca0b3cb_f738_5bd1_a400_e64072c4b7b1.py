"""A wood saw with an open handle and two broad scalloped teeth; dense tooth waves removed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cca0b3cb-f738-5bd1-a400-e64072c4b7b1'
SOURCE_PATH = 'pictographic-primitives/tools/tools wood saw_cca0b3cb-f738-5bd1-a400-e64072c4b7b1.svg'
AUTHOR = 'gpt-6'

class WavyToothWoodSaw(Solo48):
    icon_id = 'wavy-tooth-wood-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('saw', 'wood saw', 'hand saw', 'cutting', 'carpentry', 'teeth', 'blade', 'tool')

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

        box('handle',6,24,16,18,6)
        self.add_line('blade-top',(16,24),(42,6))
        self.add_line('blade-end',(42,6),(42,22))
        self.add_arc('tooth-one',(42,22),(32,28),radius_x=7)
        self.add_arc('tooth-two',(32,28),(22,34),radius_x=7)
        self.add_contour('blade','blade-top','blade-end','tooth-one','tooth-two')
        self.relate('connect','blade','handle')
