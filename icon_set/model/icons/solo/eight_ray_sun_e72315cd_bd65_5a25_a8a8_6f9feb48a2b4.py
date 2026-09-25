"""A circular sun with eight detached rays. Circular envelope follows radial construction. Lucide sun informs opposed ray pairs. The short cardinal rays sit slightly farther out than diagonal rays; all eight are retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e72315cd-bd65-5a25-a8a8-6f9feb48a2b4'
SOURCE_PATH = 'pictographic-primitives/photography/light mode brightness_e72315cd-bd65-5a25-a8a8-6f9feb48a2b4.svg'
AUTHOR = 'gpt-6'

class EightRaySun(Solo48):
    icon_id = 'eight-ray-sun'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('sun', 'brightness', 'light', 'rays', 'day', 'display', 'setting', 'bright')

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

        circle('sun',24,24,7)
        for j,(dx,dy) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
            line('axial-'+str(j),(24+dx*17,24+dy*17),(24+dx*20,24+dy*20))
        for j,(dx,dy) in enumerate(((1,1),(-1,1),(-1,-1),(1,-1))):
            line('diagonal-'+str(j),(24+dx*12,24+dy*12),(24+dx*14,24+dy*14))
