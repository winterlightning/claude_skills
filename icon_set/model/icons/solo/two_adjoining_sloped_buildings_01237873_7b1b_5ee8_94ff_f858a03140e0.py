"""Two Adjoining Sloped Buildings.

Symbol plan: Two adjoining blocks share one vertical wall and a level base; retain unequal sloped roofs.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: Lucide building-2: connected building masses with minimal facade detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '01237873-7b1b-5ee8-94ff-f858a03140e0'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture_01237873-7b1b-5ee8-94ff-f858a03140e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-adjoining-sloped-buildings'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building', 'architecture', 'structure', 'roof', 'property', 'exterior', 'construction', 'urban')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)

        path('outline',(4,40),(4,8),(24,20),(24,28),(44,22),(44,40),(24,40),(4,40),closed=True)
        line('shared-wall',(24,28),(24,40));connect('shared-wall','outline')
