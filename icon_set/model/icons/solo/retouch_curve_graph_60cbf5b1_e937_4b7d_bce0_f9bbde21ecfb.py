"""A rising retouch curve with two round control points and arrowed axes. Square envelope fits the graph. Lucide spline informs hollow control nodes with explicit curve endpoints. Curve segments are rebuilt from elliptical arcs and a connecting run; both control points and axis arrows remain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60cbf5b1-e937-4b7d-bce0-f9bbde21ecfb'
SOURCE_PATH = 'pictographic-primitives/photography/retouch graph_60cbf5b1-e937-4b7d-bce0-f9bbde21ecfb.svg'
AUTHOR = 'gpt-6'

class RetouchCurveGraph(Solo48):
    icon_id = 'retouch-curve-graph'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('curve', 'graph', 'retouch', 'adjust', 'edit', 'control points', 'chart', 'photo')

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

        poly('axes',(10,6),(10,38),(42,38))
        poly('vertical-arrow',(6,10),(10,6),(14,10));connect('vertical-arrow','axes')
        poly('horizontal-arrow',(38,34),(42,38),(38,42));connect('horizontal-arrow','axes')
        circle('control-lower',22,25,3);circle('control-upper',34,13,3)
        arc('curve-start',(10,38),(22,28),12,10,sweep=False);connect('curve-start','axes');connect('curve-start','control-lower')
        line('curve-middle',(22,22),(34,16));connect('curve-middle','control-lower');connect('curve-middle','control-upper')
        arc('curve-end',(37,13),(42,6),5,7);connect('curve-end','control-upper')
