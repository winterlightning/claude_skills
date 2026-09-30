"""begging cup give coin.
Symbol plan: SQUARE (6,6)-(42,42). Left-entering hand; smooth pinch touches coin at its upper extreme; trapezoidal cup below with clear separation.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b756b0fb-ba2c-4349-bad0-de1ee11adb74'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-lowering-a-coin-toward-a-cup/20260929T104744Z-thuan-mac/reference/begging cup give coin_b756b0fb-ba2c-4349-bad0-de1ee11adb74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-lowering-a-coin-toward-a-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'lowering', 'a', 'coin', 'toward', 'a', 'cup')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def path(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def contour(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)


        bez('hand-top',(6,6),((11,6),(17,6),(20,6)),((26,6),(29,9),(30,14)))
        bez('pinch',(30,14),((27,14),(25,15),(24,18)),((19,18),(12,17),(6,14)))
        contour('hand','hand-top','pinch')
        arc('coin-top',(24,20),(36,20),6)
        arc('coin-bottom',(36,20),(24,20),6)
        contour('coin','coin-top','coin-bottom',closed=True)
        connect('coin','hand')
        path('cup',(20,34),(42,34),(38,42),(24,42),closed=True)

