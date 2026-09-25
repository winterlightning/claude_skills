"""A woman with long hair holds a camera over the left side of her face. Vertical envelope fits the full portrait. Lucide camera and user-round inform geometric lens and shoulders. Fine hair strands and facial details are omitted; a long outer hair contour distinguishes this subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8c3aa49-8c17-4f3a-ad5a-a05cee6ca75e'
SOURCE_PATH = 'pictographic-primitives/photography/taking pictures woman_f8c3aa49-8c17-4f3a-ad5a-a05cee6ca75e.svg'
AUTHOR = 'gpt-6'

class WomanLongHairTakingPhoto(Solo48):
    icon_id = 'woman-long-hair-taking-photo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('woman', 'photographer', 'camera', 'taking pictures', 'photo', 'person', 'shooting', 'capture')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
            for j,p in enumerate(pts):arc(n+'-'+str(j),p,pts[(j+1)%4],r)
            contour(n,*[n+'-'+str(j) for j in range(4)],closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8]
                if j%2:arc(n+str(j),a,z,rad)
                else:line(n+str(j),a,z)
            contour(n,*[n+str(j) for j in range(8)],closed=True)

        poly('camera',(8,12),(20,12),(32,12),(32,28),(32,36),(16,36),(8,36),closed=True)
        circle('lens',20,24,3)
        arc('hair-left',(20,12),(28,4),8)
        arc('hair-crown',(28,4),(40,16),12)
        connect('hair-left','camera');connect('hair-left','hair-crown')
        poly('long-hair',(40,16),(40,28),(40,34),(32,36))
        connect('long-hair','hair-crown');connect('long-hair','camera')
        arc('shoulder-left',(16,36),(8,44),8,sweep=False)
        line('base',(8,44),(40,44))
        arc('shoulder-right',(40,44),(32,36),8,sweep=False)
        connect('shoulder-right','long-hair')
        connect('shoulder-left','camera');connect('shoulder-left','base');connect('shoulder-right','base');connect('shoulder-right','camera')
