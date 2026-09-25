"""A sunny-weather sun with eight detached rays. Circular envelope and Lucide sun radial construction. The disc is slightly smaller and cardinal rays slightly longer than the brightness sun, preserving the reference distinction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0db23651-38ae-59f8-bc20-16c574ea9de0'
SOURCE_PATH = 'pictographic-primitives/photography/light mode sunny_0db23651-38ae-59f8-bc20-16c574ea9de0.svg'
AUTHOR = 'gpt-6'

class SunnySun(Solo48):
    icon_id = 'sunny-sun'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('sun', 'sunny', 'weather', 'daylight', 'brightness', 'light', 'day', 'white balance')

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

        circle('sun',24,24,6)
        for j,(dx,dy) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
            line('axial-'+str(j),(24+dx*16,24+dy*16),(24+dx*20,24+dy*20))
        for j,(dx,dy) in enumerate(((1,1),(-1,1),(-1,-1),(1,-1))):
            line('diagonal-'+str(j),(24+dx*12,24+dy*12),(24+dx*14,24+dy*14))
