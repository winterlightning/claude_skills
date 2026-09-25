"""A circle inscribed in a square, touching all four sides and leaving open corners. Square envelope matches the image boundary. Lucide blend circle construction and the film frame inform coherent contours. All four contact nodes are explicit; corner curves are reduced to round stroke joins."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81677788-a51b-4be5-95c4-5d340e5b0517'
SOURCE_PATH = 'pictographic-primitives/photography/photo vignette_81677788-a51b-4be5-95c4-5d340e5b0517.svg'
AUTHOR = 'gpt-6'

class VignetteSquare(Solo48):
    icon_id = 'vignette-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ()
    keywords = ('vignette', 'circle', 'square', 'photo', 'effect', 'edit', 'filter', 'frame')

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
        circle('vignette',24,24,18);connect('vignette','frame')
