"""Two ringed flare crosses on a diagonal, accompanied by two small plus sparkles. Square envelope fits the scattered light pattern. Lucide sparkles informs hierarchy and spacing. The two tiny dots are omitted; ring sizes differ deliberately."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '605c2d51-3eed-4af0-ba9c-f4df4ed4f110'
SOURCE_PATH = 'pictographic-primitives/photography/photo flares_605c2d51-3eed-4af0-ba9c-f4df4ed4f110.svg'
AUTHOR = 'gpt-6'

class LensFlareSparkles(Solo48):
    icon_id = 'lens-flare-sparkles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('flare', 'lens flare', 'sparkle', 'shine', 'glow', 'photo', 'effect', 'light')

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

        for j,(x,y,r,reach) in enumerate(((16,16,5,10),(34,34,3,8))):
            n='flare-'+str(j);circle(n,x,y,r)
            for k,(dx,dy) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
                ray=n+'-ray-'+str(k);line(ray,(x+dx*r,y+dy*r),(x+dx*reach,y+dy*reach));connect(ray,n)
        for j,(x,y) in enumerate(((36,10),(10,38))):
            poly('spark-h-'+str(j),(x-4,y),(x,y),(x+4,y))
            line('spark-v-'+str(j),(x,y-4),(x,y+4));connect('spark-h-'+str(j),'spark-v-'+str(j))
