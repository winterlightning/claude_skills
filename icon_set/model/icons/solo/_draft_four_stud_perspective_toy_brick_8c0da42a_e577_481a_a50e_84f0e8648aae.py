"""Four studs arranged on a perspective toy brick. Retains count, diamond top and two side faces; Lucide toy-brick informs protruding studs. HRECT_L wide perspective.
Redraw authorized 2026-09-22. Source interpretation follows visible composition.
Earlier draft, if any, is preserved. Shared parameters own repeated geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8c0da42a-e577-481a-a50e-84f0e8648aae'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'four-stud-perspective-toy-brick'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = "Uncategorized"
    aliases = ('Four Stud Toy Building Brick',)
    keywords = ('four', 'stud', 'perspective', 'toy', 'brick')
    def build(self):
        def curve(n,start,*segments): self.add_bezier(n,start,*segments)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def join(*n): self.relate('connect',*n)
        poly('body',(4,22),(24,12),(44,22),(44,32),(24,40),(4,32),(4,22))
        poly('top-front',(4,22),(24,30),(44,22))
        line('corner',(24,30),(24,40))
        join('body-1','body-6','top-front-1');join('body-2','body-3','top-front-2');join('top-front-1','top-front-2','corner');join('corner','body-4','body-5')
        for i,(x,y) in enumerate(((24,10),(14,18),(34,18),(24,21))): circle('stud-'+str(i),x,y,2)
