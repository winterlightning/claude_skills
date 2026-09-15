"""Gabled Outpost with Wide Door.

Symbol plan: Symmetric gabled building with roof overhang and a broad centered doorway. Omit trim and retain the shared ground.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide building-2: clear building walls and sparse openings; source supplies gable and wide doorway.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2a8a6932-7b48-4c6a-9ce2-bee1909a4df6'
SOURCE_PATH = 'pictographic-primitives/building/outpost_2a8a6932-7b48-4c6a-9ce2-bee1909a4df6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gabled-outpost-with-wide-door'
    keyshape = Keyshape.SQUARE
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

        path('roof',(6,18),(12,14),(24,6),(36,14),(42,18))
        line('wall-l',(12,14),(12,42));line('wall-r',(36,14),(36,42))
        connect('roof','wall-l');connect('roof','wall-r')
        line('ground-l',(6,42),(12,42));line('ground-r',(36,42),(42,42))
        path('door-l',(12,42),(20,42),(20,30))
        arc('door-tl',(20,30),(22,28),2);line('door-top',(22,28),(26,28));arc('door-tr',(26,28),(28,30),2)
        path('door-r',(28,30),(28,42),(36,42))
        join('door','door-l-1','door-l-2','door-tl','door-top','door-tr','door-r-1','door-r-2')
        self.contours=[c for c in self.contours if c.contour_id not in ('door-l','door-r')]
        connect('wall-l','door');connect('wall-r','door');connect('ground-l','door');connect('ground-r','door');connect('ground-l','wall-l');connect('ground-r','wall-r')
