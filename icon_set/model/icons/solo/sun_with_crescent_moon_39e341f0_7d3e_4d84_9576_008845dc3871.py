"""A sun disc with an overlapping crescent and eight attached rays. Circular envelope fits the day/night symbol. Lucide sun and sun-moon inform radial rays and crescent curves. Rays attach at shared rim nodes; the crescent remains deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39e341f0-7d3e-4d84-9576-008845dc3871'
SOURCE_PATH = 'pictographic-primitives/photography/light mode dark light_39e341f0-7d3e-4d84-9576-008845dc3871.svg'
AUTHOR = 'gpt-6'

class SunWithCrescentMoon(Solo48):
    icon_id = 'sun-with-crescent-moon'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('sun', 'moon', 'day', 'night', 'dark mode', 'light mode', 'theme', 'toggle')

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

        pts=[(24,14),(32,18),(34,24),(32,30),(24,34),(16,30),(14,24),(16,18)]
        for j,p in enumerate(pts):arc('rim-'+str(j),p,pts[(j+1)%8],10)
        contour('disc',*[f'rim-{j}' for j in range(8)],closed=True)
        ends=[(24,4),(40,12),(44,24),(40,36),(24,44),(8,36),(4,24),(8,12)]
        for j,p in enumerate(pts):line('ray-'+str(j),p,ends[j]);connect('ray-'+str(j),'disc')
        arc('crescent',(24,14),(24,34),16,sweep=True);connect('crescent','disc')
