"""global colaboration handshake.
Symbol plan: HRECT_L (4,8)-(44,40). Left cuff, upper right-entering hand, oblique clasp and two broad rounded finger ends; intentional asymmetric anatomy.
Lucide handshake original and atomic-debug: continuous rounded thumb and repeated knuckle arcs. Supplied original controls horizontal wrists.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0788c931-6c1a-4eae-bd4d-d84eeef4e11a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-handshake-with-cuff/20260929T105554Z-thuan-mac/reference/global colaboration handshake_0788c931-6c1a-4eae-bd4d-d84eeef4e11a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-handshake-with-cuff'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('horizontal', 'handshake', 'with', 'cuff')
    
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


        path('cuff',(4,14),(12,14),(12,30),(4,30))
        line('left-hand-top',(12,14),(20,14))
        bez('hand-top',(20,14),((24,8),(26,8),(30,8)),((35,8),(38,14),(44,14)))
        line('right-wrist',(44,29),(39,29))
        bez('grip',(39,29),((43,33),(37,39),(33,35)),((37,39),(31,43),(27,37)),((24,42),(21,39),(19,37)),((16,34),(14,32),(12,30)))
        bez('thumb',(20,14),((14,19),(18,25),(23,20)),((24,19),(24,18),(25,18)))
        line('thumb-palm',(25,18),(39,29))
        contour('thumb-contour','thumb','thumb-palm')
        for a,b in [('cuff','left-hand-top'),('left-hand-top','hand-top'),('left-hand-top','thumb-contour'),('hand-top','thumb-contour'),('thumb-contour','grip'),('grip','right-wrist'),('cuff','grip')]:connect(a,b)

