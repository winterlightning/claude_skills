"""A sun with five rays only along its left half. Vertical envelope fits the asymmetrical ray distribution. Lucide sun informs circle and radial spacing; the circle shifts right to balance the missing right rays. All five rays retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4e98276-6765-5d3b-a94b-b30c48487419'
SOURCE_PATH = 'pictographic-primitives/photography/light mode bright_f4e98276-6765-5d3b-a94b-b30c48487419.svg'
AUTHOR = 'gpt-6'

class HalfRayedSun(Solo48):
    icon_id = 'half-rayed-sun'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('sun', 'brightness', 'low brightness', 'light', 'rays', 'display', 'setting', 'dim')

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

        circle('sun',30,24,10)
        line('top',(30,4),(30,5));line('bottom',(30,43),(30,44));line('left',(8,24),(11,24))
        line('upper-left',(13,7),(16,10));line('lower-left',(16,38),(13,41))
