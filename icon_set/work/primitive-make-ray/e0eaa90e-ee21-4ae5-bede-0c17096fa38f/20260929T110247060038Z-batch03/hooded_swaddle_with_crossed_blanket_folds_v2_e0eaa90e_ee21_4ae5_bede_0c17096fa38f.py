"""baby newborn.
Symbol plan: VRECT_L (8,4)-(40,44). Hood radius16; circular face r7 at24,20; rounded lower blanket and two curved folds meet at24,36. Head enclosed in cloth, no detached body.
Shared human_ref/user.svg for circular face; supplied original for hood and overlapping blanket folds.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e0eaa90e-ee21-4ae5-bede-0c17096fa38f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hooded-swaddle-with-crossed-blanket-folds-v2/20260929T105554Z-thuan-mac/reference/baby newborn_e0eaa90e-ee21-4ae5-bede-0c17096fa38f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hooded-swaddle-with-crossed-blanket-folds-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hooded', 'swaddle', 'with', 'crossed', 'blanket', 'folds', 'v2')
    
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


        arc('hood-top',(8,20),(40,20),16)
        line('side-right-1',(40,20),(40,28));line('side-right-2',(40,28),(40,38))
        arc('foot-right',(40,38),(34,44),6)
        line('foot',(34,44),(14,44));arc('foot-left',(14,44),(8,38),6)
        line('side-left-1',(8,38),(8,30));line('side-left-2',(8,30),(8,20))
        contour('blanket','hood-top','side-right-1','side-right-2','foot-right','foot','foot-left','side-left-1','side-left-2',closed=True)
        circle('face',24,20,7)
        bez('fold-main',(8,30),((12,35),(17,36),(24,36)),((29,36),(35,37),(40,38)))
        bez('fold-upper',(40,28),((40,32),(33,36),(24,36)))
        connect('fold-main','blanket');connect('fold-upper','blanket');connect('fold-main','fold-upper')

