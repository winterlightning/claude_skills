"""A standalone double-bordered rectangular shape with evenly separated rounded outlines. Wide envelope follows the requested geometric symbol. Lucide rectangle-horizontal informs tangent quarter-circle corners. The gap is expanded to nine units; no border is removed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e03da5ac-6e03-49c3-b898-a69eff035b31'
SOURCE_PATH = 'pictographic-primitives/photography/symbol non specific_e03da5ac-6e03-49c3-b898-a69eff035b31.svg'
AUTHOR = 'gpt-6'

class DoubleBorderedRectangle(Solo48):
    icon_id = 'double-bordered-rectangle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('rectangle', 'frame', 'border', 'symbol', 'shape', 'screen', 'placeholder', 'generic')

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

        box('outer',4,8,44,40,4)
        box('inner',13,17,35,31,3)
