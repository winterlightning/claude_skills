"""hand fist bump.
Symbol plan: Horizontal fist, centerline extremes (4,8)-(44,40). Three broad knuckle lobes replace four cramped divisions; the palm and oblique thumb share their top junction.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9cc745f-989b-5241-9fd0-090475a8c137'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clenched-fist-solo-b018/20260929T104523Z-thuan-mac/reference/hand fist bump_f9cc745f-989b-5241-9fd0-090475a8c137.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clenched-fist-solo-b018'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('clenched', 'fist', 'solo', 'b018')
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


        bez('wrist-top',(4,16),((12,16),(12,8),(24,8)))
        line('top',(24,8),(36,8))
        for i,y in enumerate((8,19,30)):
            h = 11 if i < 2 else 10
            bez('knuckle-'+str(i),(36,y),((42,y),(44,y+1),(44,y+5)),((44,y+h-1),(42,y+h),(36,y+h)))
        line('bottom',(36,40),(24,40))
        bez('wrist-bottom',(24,40),((14,40),(14,34),(4,34)))
        contour('outline','wrist-top','top',*[f'knuckle-{i}' for i in range(3)],'bottom','wrist-bottom')
        bez('thumb',(28,8),((29,12),(31,16),(32,20)),((33,24),(27,26),(24,24)),((22,23),(21,21),(20,18)),((19,23),(16,26),(12,27)))
        connect('thumb','outline')
        

