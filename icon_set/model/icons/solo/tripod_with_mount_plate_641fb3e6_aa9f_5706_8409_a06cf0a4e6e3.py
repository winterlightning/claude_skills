"""A three-legged tripod with rectangular mounting plate and short column. Vertical envelope fits long legs. Lucide equipment construction informs simple joined supports; the source establishes the plate and three-way leg joint. Plate opening enlarged; mirrored legs share the centre node."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '641fb3e6-aa9f-5706-8409-a06cf0a4e6e3'
SOURCE_PATH = 'pictographic-primitives/photography/photography equipment tripod_641fb3e6-aa9f-5706-8409-a06cf0a4e6e3.svg'
AUTHOR = 'gpt-6'

class TripodWithMountPlate(Solo48):
    icon_id = 'tripod-with-mount-plate'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('tripod', 'stand', 'mount', 'camera', 'photography', 'legs', 'equipment', 'support')

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

        poly('plate',(16,4),(32,4),(32,12),(24,12),(16,12),closed=True)
        line('column',(24,12),(24,22));connect('column','plate')
        for j,x in enumerate((8,24,40)):
            line('leg-'+str(j),(24,22),(x,44));connect('leg-'+str(j),'column')
        for a,b in ((0,1),(1,2),(0,2)):connect('leg-'+str(a),'leg-'+str(b))
