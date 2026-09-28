"""An open head-and-shoulders outline with a broad head and narrow neck. Vertical envelope fits the silhouette. Lucide user-round informs paired shoulder curves, while the source establishes the connected neck. Tiny ear bumps are omitted for smooth sides; the bottom remains open."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fabe2871-28e2-4de0-93c6-579984309329'
SOURCE_PATH = 'pictographic-primitives/photography/man_fabe2871-28e2-4de0-93c6-579984309329.svg'
AUTHOR = 'gpt-6'

class ManHeadShouldersOutline(Solo48):
    icon_id = 'man-head-shoulders-outline'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('man', 'person', 'silhouette', 'portrait', 'profile', 'user', 'avatar', 'head')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8]
                if j%2:arc(n+str(j),a,z,rad)
                else:line(n+str(j),a,z)
            contour(n,*[n+str(j) for j in range(8)],closed=True)

        line('crown',(20,4),(28,4))
        arc('head-right',(28,4),(34,10),6)
        poly('jaw-right',(34,10),(34,18),(28,28),(28,32),(36,36))
        arc('shoulder-right',(36,36),(40,44),10)
        arc('shoulder-left',(8,44),(12,36),10)
        poly('jaw-left',(12,36),(20,32),(20,28),(14,18),(14,10))
        arc('head-left',(14,10),(20,4),6)
        connect('crown','head-left');connect('crown','head-right');connect('head-right','jaw-right');connect('head-left','jaw-left');connect('shoulder-right','jaw-right');connect('shoulder-left','jaw-left')
