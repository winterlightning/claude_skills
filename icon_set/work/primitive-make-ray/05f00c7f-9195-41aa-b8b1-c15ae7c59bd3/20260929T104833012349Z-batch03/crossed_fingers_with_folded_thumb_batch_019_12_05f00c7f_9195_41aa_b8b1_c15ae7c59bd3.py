"""finger crossed 1.
Symbol plan: VRECT_L extremes (8,4)-(40,44). Broad palm with horizontal folded thumb; two crossing fingers, rounded fingertips and restrained curled knuckle detail.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '05f00c7f-9195-41aa-b8b1-c15ae7c59bd3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crossed-fingers-with-folded-thumb-batch-019-12/20260929T104523Z-thuan-mac/reference/finger crossed 1_05f00c7f-9195-41aa-b8b1-c15ae7c59bd3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-fingers-with-folded-thumb-batch-019-12'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crossed', 'fingers', 'with', 'folded', 'thumb', 'batch', '019', '12')
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


        bez('front-finger',(8,32),((8,26),(15,20),(18,16)),((22,10),(24,6),(27,6)),((31,4),(35,8),(32,13)),((30,17),(27,22),(25,26)))
        bez('curled-fingers',(25,26),((25,21),(33,21),(33,28)),((33,23),(40,23),(40,30)))
        bez('palm',(40,30),((40,40),(34,44),(24,44)),((15,44),(8,41),(8,32)))
        contour('skin','front-finger','curled-fingers','palm',closed=True)
        bez('rear-finger',(16,19),((13,15),(10,10),(10,8)),((10,2),(16,3),(18,6)),((20,8),(20,10),(22,12)))
        connect('rear-finger','skin')
        bez('thumb',(8,32),((12,30),(18,30),(25,30)),((32,30),(32,38),(25,38)),((22,38),(20,38),(18,38)))
        connect('thumb','skin')

