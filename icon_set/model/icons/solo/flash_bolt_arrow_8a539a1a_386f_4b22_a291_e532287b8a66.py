"""A descending lightning bolt ending in an arrowhead. Vertical envelope preserves its directional silhouette. Lucide zap informs the coherent zigzag contour. Arrowhead enlarged for open space; its downward-left direction is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a539a1a-386f-4b22-a291-e532287b8a66'
SOURCE_PATH = 'pictographic-primitives/photography/light mode flash_8a539a1a-386f-4b22-a291-e532287b8a66.svg'
AUTHOR = 'gpt-6'

class FlashBoltArrow(Solo48):
    icon_id = 'flash-bolt-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('flash', 'lightning', 'bolt', 'camera flash', 'auto flash', 'electric', 'power', 'arrow')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'-top',(x-r,y),(x+r,y),r)
            arc(n+'-bottom',(x+r,y),(x-r,y),r)
            contour(n,n+'-top',n+'-bottom',closed=True)
        def box(n,l,t,r,b,rad=4):
            pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8]
                if j%2:arc(n+str(j),a,z,rad)
                else:line(n+str(j),a,z)
            contour(n,*[n+str(j) for j in range(8)],closed=True)

        poly('bolt',(28,4),(40,4),(28,18),(40,20),(24,36),(30,40),(10,44),(8,30),(14,34),(24,24),(12,24),closed=True)
