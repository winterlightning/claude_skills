"""car sensor 3.
Symbol plan: HRECT_L (4,8)-(44,40). Symmetric compact front car, short wheels, two lateral sensing arcs. One wave per side and no tiny lamps fit the48 canvas.
Lucide car-front original and atomic-debug: rounded front body, sloped roof and short wheel ends. Supplied original: bilateral sensing waves.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3c675853-e649-4029-b679-cef625fb977e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__front-view-car-with-sensor-waves/20260929T105554Z-thuan-mac/reference/car sensor 3_3c675853-e649-4029-b679-cef625fb977e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-view-car-with-sensor-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('front', 'view', 'car', 'with', 'sensor', 'waves')
    
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


        bez('roof',(13,23),((15,15),(16,8),(20,8)),((22,8),(26,8),(28,8)),((32,8),(33,15),(35,23)))
        line('windshield',(35,23),(13,23));contour('roof-outline','roof','windshield',closed=True)
        line('body-left',(13,23),(13,32));arc('corner-left',(13,32),(17,36),4,s=False)
        line('body-bottom-1',(17,36),(19,36));line('body-bottom-2',(19,36),(29,36));line('body-bottom-3',(29,36),(31,36))
        arc('corner-right',(31,36),(35,32),4,s=False);line('body-right',(35,32),(35,23))
        contour('body','body-left','corner-left','body-bottom-1','body-bottom-2','body-bottom-3','corner-right','body-right');connect('body','roof-outline')
        line('wheel-left',(19,36),(19,40));line('wheel-right',(29,36),(29,40));connect('wheel-left','body');connect('wheel-right','body')
        bez('wave-left',(5,18),((4,20),(4,22),(4,26)),((4,30),(4,32),(5,34)))
        bez('wave-right',(43,18),((44,20),(44,22),(44,26)),((44,30),(44,32),(43,34)))

