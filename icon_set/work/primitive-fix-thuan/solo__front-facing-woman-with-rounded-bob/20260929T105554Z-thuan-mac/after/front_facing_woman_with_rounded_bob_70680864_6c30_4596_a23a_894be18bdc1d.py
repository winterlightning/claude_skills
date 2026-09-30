"""step aunt.
Symbol plan: SQUARE (6,6)-(42,42). Rounded bob with radius18 cap centered24,24 and deliberate asymmetric fringe. Circular jaw radius8 at24,22 ends at30; shoulder top34 gives zero ink gap.
Shared human_ref/user.svg: circular jaw, broad shoulders, touching bust ink. Supplied original for rounded bob and side part.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '70680864-6c30-4596-a23a-894be18bdc1d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__front-facing-woman-with-rounded-bob/20260929T105554Z-thuan-mac/reference/step aunt_70680864-6c30-4596-a23a-894be18bdc1d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-woman-with-rounded-bob'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('front', 'facing', 'woman', 'with', 'rounded', 'bob')
    human_construction = "bust"
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


        arc('jaw',(16,22),(32,22),8,s=False)
        bez('fringe-right',(32,22),((32,18),(25,18),(23,14)))
        bez('fringe-left',(23,14),((21,18),(16,18),(16,22)))
        contour('face','jaw','fringe-right','fringe-left',closed=True)
        line('shoulder-left-side',(6,42),(6,40))
        bez('shoulder-left',(6,40),((6,36),(11,34),(17,34)))
        line('shoulder-top',(17,34),(31,34))
        bez('shoulder-right',(31,34),((37,34),(42,36),(42,40)))
        line('shoulder-right-side',(42,40),(42,42))
        contour('shoulders','shoulder-left-side','shoulder-left','shoulder-top','shoulder-right','shoulder-right-side');connect('face','shoulders')
        bez('hair-left',(17,34),((6,34),(6,32),(6,28)))
        line('hair-side-left',(6,28),(6,24))
        arc('hair-cap',(6,24),(42,24),18)
        line('hair-side-right',(42,24),(42,28))
        bez('hair-right',(42,28),((42,32),(42,34),(31,34)))
        contour('hair','hair-left','hair-side-left','hair-cap','hair-side-right','hair-right');connect('hair','shoulders')

