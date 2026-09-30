"""business contract give.
Symbol plan: VRECT_L extremes (8,4)-(40,44). Rounded upright paper with lower-right edge occluded by one coherent hand contour.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1996803f-fb1a-423a-9fd2-78b1fe8a9c74'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-gripping-blank-upright-document/20260929T104744Z-thuan-mac/reference/business contract give_1996803f-fb1a-423a-9fd2-78b1fe8a9c74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-gripping-blank-upright-document'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'gripping', 'blank', 'upright', 'document')
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


        line('paper-top',(12,4),(28,4));arc('paper-corner',(28,4),(32,8),4)
        line('paper-right',(32,8),(32,22))
        line('paper-left',(8,34),(8,8));arc('paper-topleft',(8,8),(12,4),4)
        arc('paper-bottomleft',(12,38),(8,34),4);line('paper-bottom',(22,38),(12,38))
        contour('paper','paper-bottom','paper-bottomleft','paper-left','paper-topleft','paper-top','paper-corner','paper-right')
        bez('hand-back',(32,22),((38,27),(40,28),(40,33)),((40,39),(39,40),(40,44)))
        bez('thumb',(34,34),((31,31),(27,27),(25,27)),((21,27),(20,31),(23,34)),((25,37),(27,40),(28,44)))
        connect('paper-right','hand-back')

