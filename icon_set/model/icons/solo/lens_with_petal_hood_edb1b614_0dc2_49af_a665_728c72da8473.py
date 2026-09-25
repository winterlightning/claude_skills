"""An upright camera lens with a flared petal hood and narrower bottom mount. Vertical envelope fits the stacked hood, barrel and mount. Lucide telescope informs the stepped barrel; no useful local petal-hood match was found. Dashed ring and multiple mount tiers are omitted; paired hood cutouts retain its identity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edb1b614-0dc2-49af-a665-728c72da8473'
SOURCE_PATH = 'pictographic-primitives/photography/lens shade 1_edb1b614-0dc2-49af-a665-728c72da8473.svg'
AUTHOR = 'gpt-6'

class LensWithPetalHood(Solo48):
    icon_id = 'lens-with-petal-hood'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    categories = ("photography", "primitives")
    aliases = ()
    keywords = ('lens', 'lens hood', 'petal hood', 'shade', 'camera lens', 'optics', 'photography', 'zoom')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def segments(n,*p):
            for j,(a,b) in enumerate(zip(p,p[1:]),1):line(n+'-'+str(j),a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)

        poly('hood',(8,8),(16,16),(20,4),(28,4),(32,16),(40,8),(36,24),(34,24),(14,24),(12,24),closed=True)
        poly('barrel',(14,24),(14,36),(18,36),(30,36),(34,36),(34,24));connect('barrel','hood')
        poly('mount',(18,36),(18,44),(30,44),(30,36));connect('mount','barrel')
