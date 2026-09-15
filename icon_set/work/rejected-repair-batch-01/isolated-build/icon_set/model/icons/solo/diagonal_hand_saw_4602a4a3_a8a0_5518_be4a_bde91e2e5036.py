"""A hand saw with a squared D-shaped handle and two broad blade teeth; tiny serrations are removed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4602a4a3-a8a0-5518-be4a-bde91e2e5036'
SOURCE_PATH = 'pictographic-primitives/tools/tools saw_4602a4a3-a8a0-5518-be4a-bde91e2e5036.svg'
AUTHOR = 'gpt-6'

class DiagonalHandSaw(Solo48):
    icon_id = 'diagonal-hand-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('saw', 'hand saw', 'wood', 'cutting', 'carpentry', 'teeth', 'blade', 'tool')

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

        box('handle',26,24,16,18,6)
        self.add_polyline('blade',(32,24),(6,6),(6,22),(12,20),(14,30),(20,28),(26,36))
        self.relate('connect','blade','handle')
