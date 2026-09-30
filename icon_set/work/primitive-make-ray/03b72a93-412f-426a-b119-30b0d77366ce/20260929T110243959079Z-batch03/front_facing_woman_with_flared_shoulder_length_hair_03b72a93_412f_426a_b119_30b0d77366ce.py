"""step daughter.
Symbol plan: SQUARE (6,6)-(42,42). Mirrored hair cap and flared ends; jaw radius9 centered24,21, bottom30 touches shoulder-top34 on ink. Shared shoulder and hair attachment nodes.
Shared human_ref/user.svg: circular jaw and broad smooth shoulders, with contract bust ink contact. Supplied reference controls the center part and flared hair.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '03b72a93-412f-426a-b119-30b0d77366ce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__front-facing-woman-with-flared-shoulder-length-hair/20260929T105554Z-thuan-mac/reference/step daughter_03b72a93-412f-426a-b119-30b0d77366ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-woman-with-flared-shoulder-length-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('front', 'facing', 'woman', 'with', 'flared', 'shoulder', 'length', 'hair')
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


        arc('jaw',(15,21),(33,21),9,s=False)
        bez('fringe-right',(33,21),((32,18),(27,18),(24,14)))
        bez('fringe-left',(24,14),((21,18),(16,18),(15,21)))
        contour('face','jaw','fringe-right','fringe-left',closed=True)
        line('shoulder-left-side',(6,42),(6,40))
        bez('shoulder-left',(6,40),((6,36),(11,34),(17,34)))
        line('shoulder-top',(17,34),(31,34))
        bez('shoulder-right',(31,34),((37,34),(42,36),(42,40)))
        line('shoulder-right-side',(42,40),(42,42))
        contour('shoulders','shoulder-left-side','shoulder-left','shoulder-top','shoulder-right','shoulder-right-side')
        connect('face','shoulders')
        bez('hair-left',(17,34),((7,34),(6,32),(8,27)),((10,22),(6,6),(24,6)))
        bez('hair-right',(24,6),((42,6),(38,22),(40,27)),((42,32),(41,34),(31,34)))
        contour('hair','hair-left','hair-right');connect('hair','shoulders')

