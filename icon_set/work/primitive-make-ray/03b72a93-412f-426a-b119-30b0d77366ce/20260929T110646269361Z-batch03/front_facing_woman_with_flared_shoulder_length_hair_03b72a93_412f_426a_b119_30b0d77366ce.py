"""step daughter.
Symbol plan: SQUARE (6,6)-(42,42). Mirrored flared hair with radius16 crown centered24,22. Circular jaw radius7 at24,23 ends at30; shoulder top34 gives zero ink gap. Shared hair/shoulder nodes17,34 and31,34.
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


        arc('jaw',(17,23),(31,23),7,s=False)
        bez('fringe-right',(31,23),((30,18),(27,18),(24,14)))
        bez('fringe-left',(24,14),((21,18),(18,18),(17,23)))
        contour('face','jaw','fringe-right','fringe-left',closed=True)
        line('shoulder-left-side',(6,42),(6,40))
        bez('shoulder-left',(6,40),((6,36),(11,34),(17,34)))
        line('shoulder-top',(17,34),(31,34))
        bez('shoulder-right',(31,34),((37,34),(42,36),(42,40)))
        line('shoulder-right-side',(42,40),(42,42))
        contour('shoulders','shoulder-left-side','shoulder-left','shoulder-top','shoulder-right','shoulder-right-side')
        connect('face','shoulders')
        bez('hair-left',(17,34),((7,34),(6,32),(6,30)),((6,27),(8,26),(8,22)))
        arc('hair-cap',(8,22),(40,22),16)
        bez('hair-right',(40,22),((40,26),(42,27),(42,30)),((42,32),(41,34),(31,34)))
        contour('hair','hair-left','hair-cap','hair-right');connect('hair','shoulders')

