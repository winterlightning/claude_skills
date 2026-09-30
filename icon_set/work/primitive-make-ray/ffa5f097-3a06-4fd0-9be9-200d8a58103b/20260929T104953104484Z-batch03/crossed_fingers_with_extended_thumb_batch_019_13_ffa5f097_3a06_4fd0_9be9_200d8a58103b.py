"""finger crossed.
Symbol plan: VRECT_L extremes (8,4)-(40,44). Two crossing raised fingers above the palm, separate back finger attached at shared outline nodes; extended left thumb.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ffa5f097-3a06-4fd0-9be9-200d8a58103b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crossed-fingers-with-extended-thumb-batch-019-13/20260929T104523Z-thuan-mac/reference/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-fingers-with-extended-thumb-batch-019-13'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crossed', 'fingers', 'with', 'extended', 'thumb', 'batch', '019', '13')
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


        bez('front-finger',(16,28),((16,22),(18,19),(20,16)),((22,13),(23,11),(24,10)),((26,4),(30,4),(32,7)),((34,10),(33,12),(31,15)),((28,20),(25,23),(24,27)))
        bez('curled-fingers',(24,27),((27,23),(31,24),(32,30)),((36,25),(40,26),(40,32)))
        bez('palm',(40,32),((40,39),(35,44),(26,44)),((19,44),(15,40),(11,34)),((8,30),(8,28),(8,26)),((8,22),(12,22),(16,26)))
        line('thumb',(16,26),(21,31))
        contour('skin','front-finger','curled-fingers','palm','thumb')
        bez('rear-finger',(20,16),((16,12),(12,8),(12,6)),((12,4),(14,4),(16,4)),((20,4),(22,7),(24,10)))
        connect('rear-finger','skin')

