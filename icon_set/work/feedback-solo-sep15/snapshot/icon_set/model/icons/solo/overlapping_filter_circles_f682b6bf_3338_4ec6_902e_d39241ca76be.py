"""Two circular filters overlap from upper left to lower right. Square envelope preserves the diagonal pair. Lucide blend informs equal circles and true intersection nodes. The two hatch marks are removed to retain an open overlap lens."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f682b6bf-3338-4ec6-902e-d39241ca76be'
SOURCE_PATH = 'pictographic-primitives/photography/photo changed filter_f682b6bf-3338-4ec6-902e-d39241ca76be.svg'
AUTHOR = 'gpt-6'

class OverlappingFilterCircles(Solo48):
    icon_id = 'overlapping-filter-circles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('filter', 'circles', 'overlap', 'blend', 'photo', 'effect', 'edit', 'color')

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

        circle('upper-filter',18,18,12)
        circle('lower-filter',30,30,12)
        connect('upper-filter','lower-filter')
