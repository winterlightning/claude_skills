"""travel map finger.
Symbol plan: SQUARE centerline (6,6)-(42,42). Long left route curve, upper destination cross, upright finger and projecting thumb with rounded palm.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4e54a956-814a-4581-8d3c-be1a087ebdba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__finger-selecting-map-destination/20260929T104744Z-thuan-mac/reference/travel map finger_4e54a956-814a-4581-8d3c-be1a087ebdba.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'finger-selecting-map-destination'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('finger', 'selecting', 'map', 'destination')
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


        bez('route',(6,42),((6,26),(6,15),(15,10)))
        path('cross-a',(26,6),(30,10),(34,14))
        path('cross-b',(34,6),(30,10),(26,14));connect('cross-a','cross-b')
        line('finger-left',(25,32),(25,24))
        arc('fingertip',(25,24),(33,24),4)
        line('finger-right',(33,24),(33,32))
        bez('palm',(33,32),((40,32),(42,34),(42,42)))
        contour('upper-hand','finger-left','fingertip','finger-right','palm')
        bez('thumb',(25,32),((21,26),(19,25),(17,28)),((14,31),(19,36),(23,42)))
        connect('thumb','upper-hand')

