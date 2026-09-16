"""Banknote Falling into Basket.

Symbol plan: Banknote with a central denomination mark above an open ribbed basket. Remove corner microprinting and straighten the note for clear spacing.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b3619943-75ef-45de-907e-af930db20bab'
SOURCE_PATH = 'pictographic-primitives/business/money basket_b3619943-75ef-45de-907e-af930db20bab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'banknote-falling-into-basket'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('banknote', 'basket', 'money', 'payment', 'cash', 'collection', 'deposit', 'finance')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)

        box('note',10,4,28,18,2)
        self.add_dot('denomination',(24,13))
        path('basket',(8,32),(24,32),(40,32),(36,44),(24,44),(12,44),(8,32),closed=True)
        line('rib',(24,32),(24,44));connect('rib','basket')
