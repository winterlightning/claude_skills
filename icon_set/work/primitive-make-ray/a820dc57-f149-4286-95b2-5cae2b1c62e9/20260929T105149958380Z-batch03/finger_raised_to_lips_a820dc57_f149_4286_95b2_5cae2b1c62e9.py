"""allowances silence.
Symbol plan: VRECT_L bounds (8,4)-(40,44). Two separate contours: a left-facing profile and an oblique index finger above a compact palm.
Lucide hand and hand-fist: rounded fingertips, coherent palm contours. Shared human references inspected; detached-head spacing does not apply to hands.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a820dc57-f149-4286-95b2-5cae2b1c62e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__finger-raised-to-lips/20260929T104744Z-thuan-mac/reference/allowances silence_a820dc57-f149-4286-95b2-5cae2b1c62e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'finger-raised-to-lips'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('finger', 'raised', 'to', 'lips')
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


        bez('forehead',(40,4),((35,4),(33,8),(33,13)))
        line('nose-a',(33,13),(30,22));line('nose-b',(30,22),(37,22))
        bez('chin',(37,22),((36,31),(36,34),(40,34)))
        line('neck',(40,34),(40,44))
        contour('face','forehead','nose-a','nose-b','chin','neck')
        bez('palm',(8,44),((8,36),(10,33),(17,36)))
        line('index-left',(17,36),(14,24))
        bez('tip',(14,24),((12,18),(20,16),(22,23)))
        line('index-right',(22,23),(28,44))
        contour('hand','palm','index-left','tip','index-right')

