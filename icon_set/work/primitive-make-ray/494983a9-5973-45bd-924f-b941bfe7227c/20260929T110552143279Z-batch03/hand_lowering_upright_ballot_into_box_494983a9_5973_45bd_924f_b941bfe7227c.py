"""election ballot box 3.
Symbol plan: SQUARE (6,6)-(42,42). Rounded box, upright paper with top edge occluded by a rounded thumb; curved upper hand.
Lucide hand and hand-fist inform smooth fingers; supplied original establishes upright ballot and broad box.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '494983a9-5973-45bd-924f-b941bfe7227c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-lowering-upright-ballot-into-box/20260929T105554Z-thuan-mac/reference/election ballot box 3_494983a9-5973-45bd-924f-b941bfe7227c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-lowering-upright-ballot-into-box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'lowering', 'upright', 'ballot', 'into', 'box')
    
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


        line('box-top',(10,28),(38,28));arc('box-tr',(38,28),(42,32),4)
        line('box-right',(42,32),(42,38));arc('box-br',(42,38),(38,42),4)
        line('box-bottom',(38,42),(10,42));arc('box-bl',(10,42),(6,38),4)
        line('box-left',(6,38),(6,32));arc('box-tl',(6,32),(10,28),4)
        contour('box','box-top','box-tr','box-right','box-br','box-bottom','box-bl','box-left','box-tl',closed=True)
        path('paper',(10,28),(10,10),(25,10));line('paper-right',(30,18),(30,28));connect('paper','box');connect('paper-right','box')
        bez('hand-top',(42,7),((38,6),(36,6),(34,6)),((30,6),(28,8),(25,10)))
        bez('thumb',(25,10),((18,10),(18,18),(25,18)))
        bez('hand-bottom',(25,18),((27,18),(28,18),(30,18)),((36,18),(37,14),(42,16)))
        contour('hand','hand-top','thumb','hand-bottom');connect('hand','paper');connect('hand','paper-right')

