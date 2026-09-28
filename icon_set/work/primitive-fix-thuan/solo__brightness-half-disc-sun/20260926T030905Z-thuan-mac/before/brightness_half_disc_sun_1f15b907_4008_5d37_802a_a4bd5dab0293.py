"""A brightness sun with eight rays and a right-facing half disc. Circular envelope follows the radial subject. Lucide sun and contrast inform the circle, rays and half disc. Rays attach to the rim to make room for the defining half disc; all eight remain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f15b907-4008-5d37-802a-a4bd5dab0293'
SOURCE_PATH = 'pictographic-primitives/photography/photo adjust brightness_1f15b907-4008-5d37-802a-a4bd5dab0293.svg'
AUTHOR = 'gpt-6'

class BrightnessHalfDiscSun(Solo48):
    icon_id = 'brightness-half-disc-sun'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('brightness', 'contrast', 'sun', 'adjust', 'display', 'setting', 'photo', 'exposure')

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

        pts=[(24,9),(36,15),(39,24),(36,33),(24,39),(12,33),(9,24),(12,15)]
        ends=[(24,4),(40,12),(44,24),(40,36),(24,44),(8,36),(4,24),(8,12)]
        for j,p in enumerate(pts):arc('rim-'+str(j),p,pts[(j+1)%8],15)
        contour('rim',*[f'rim-{j}' for j in range(8)],closed=True)
        for j,p in enumerate(pts):line('ray-'+str(j),p,ends[j]);connect('ray-'+str(j),'rim')
        arc('half-disc',(22,18),(22,30),6)
        line('diameter',(22,30),(22,18));contour('contrast','half-disc','diameter',closed=True)
