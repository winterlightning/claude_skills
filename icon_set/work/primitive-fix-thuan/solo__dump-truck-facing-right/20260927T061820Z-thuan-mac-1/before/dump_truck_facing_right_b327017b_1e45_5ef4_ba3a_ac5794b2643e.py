"""Dump Truck Facing Right.

Symbol plan: Right-facing tipper with angled rear bed, cab and two repeated circular wheels. Remove small window and bed trim.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: Lucide truck: equal circular wheels, one cab silhouette and shared chassis attachment.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b327017b-1e45-5ef4-ba3a-ac5794b2643e'
SOURCE_PATH = 'pictographic-primitives/construction/mortar truck_b327017b-1e45-5ef4-ba3a-ac5794b2643e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dump-truck-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('dump truck', 'tipper', 'truck', 'construction', 'vehicle', 'load', 'haulage', 'transport')

    def build(self) -> None:

        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)

        path('bed',(4,8),(28,8),(28,16),(28,24),(8,24),(4,8),closed=True)
        path('cab',(28,16),(36,16),(44,28),(44,32),(36,32),(12,32),(8,32),(8,24))
        connect('bed','cab')
        for j,x in enumerate((12,36)):
            circle('wheel-'+str(j),x,36,4);connect('wheel-'+str(j),'cab')
