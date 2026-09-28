"""A rising S-shaped tone curve over a square grid. Square envelope retains the graph. Lucide chart-spline informs a coherent smooth curve, reconstructed with two tangent quarter circles. The three-by-three grid reduces to two-by-two so the curve leaves readable cells."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9857fa6-dd4a-4727-b239-360d879204e3'
SOURCE_PATH = 'pictographic-primitives/photography/photo histogram_d9857fa6-dd4a-4727-b239-360d879204e3.svg'
AUTHOR = 'gpt-6'

class ToneCurveGrid(Solo48):
    icon_id = 'tone-curve-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('curves', 'histogram', 'tone curve', 'grid', 'edit', 'adjust', 'photo', 'graph')

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

        poly('frame',(6,6),(24,6),(42,6),(42,24),(42,42),(24,42),(6,42),(6,24),closed=True)
        poly('vertical-grid',(24,6),(24,24),(24,42));connect('vertical-grid','frame')
        poly('horizontal-grid',(6,24),(24,24),(42,24));connect('horizontal-grid','frame');connect('vertical-grid','horizontal-grid')
        arc('curve-lower',(6,42),(24,24),18,sweep=False)
        arc('curve-upper',(24,24),(42,6),18)
        contour('tone-curve','curve-lower','curve-upper')
        for n in ('frame','vertical-grid','horizontal-grid'):connect('tone-curve',n)
