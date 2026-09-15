"""A broken outer circle around an inner ring and centre dot. Circular envelope follows the recording symbol. Lucide circle-dashed informs separated arcs. Eight outer dashes reduce to four to preserve gap clearance; inner ring and dot remain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e288c21f-0d5e-4f0d-9565-237add36debd'
SOURCE_PATH = 'pictographic-primitives/photography/live photos_e288c21f-0d5e-4f0d-9565-237add36debd.svg'
AUTHOR = 'gpt-6'

class LivePhotoRings(Solo48):
    icon_id = 'live-photo-rings'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('live photo', 'live', 'rings', 'motion', 'capture', 'camera', 'target', 'photo')

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

        for j,(a,b) in enumerate((((18,5),(30,5)),((43,18),(43,30)),((30,43),(18,43)),((5,30),(5,18)))):arc('dash-'+str(j),a,b,20)
        circle('ring',24,24,10)
        self.add_dot('centre',(24,24))
