"""A folding knife with a horizontal rounded handle and raised pointed blade; small pivot dot omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '876a3ef0-1a0b-5bbc-b9ee-2b52166f106e'
SOURCE_PATH = 'pictographic-primitives/tools/folding pocket knife_876a3ef0-1a0b-5bbc-b9ee-2b52166f106e.svg'
AUTHOR = 'gpt-6'

class FoldingPocketKnife(Solo48):
    icon_id = 'folding-pocket-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('pocket knife', 'knife', 'folding', 'blade', 'penknife', 'camping', 'outdoor', 'tool')

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

        box('handle',6,30,36,12,6)
        self.add_line('blade-back',(36,30),(16,6))
        self.add_arc('blade-edge',(16,6),(20,22),radius_x=18,sweep=False)
        self.add_line('blade-heel',(20,22),(28,30))
        self.add_contour('blade','blade-back','blade-edge','blade-heel')
        self.relate('connect','blade','handle')
