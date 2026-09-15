"""Money Hierarchy with Three Shapes.

Symbol plan: Dollar root with a branching connector and circle, square, triangle child nodes. Drop the root coin rim to preserve the monetary sign and three node shapes.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a835bb3a-ae87-57c1-854c-febe5a5a60bb'
SOURCE_PATH = 'pictographic-primitives/business/monetization structure_a835bb3a-ae87-57c1-854c-febe5a5a60bb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'money-hierarchy-with-three-shapes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('money', 'hierarchy', 'network', 'organization', 'connection', 'structure', 'branch', 'diagram', 'relationship')

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

        arc('dollar-top',(28,8),(24,8),2,s=False)
        arc('dollar-upper',(24,8),(24,16),4,s=False)
        arc('dollar-lower',(24,16),(24,24),4)
        line('dollar-bottom',(24,24),(20,24))
        join('dollar','dollar-top','dollar-upper','dollar-lower','dollar-bottom')
        line('stem',(24,8),(24,24));connect('dollar','stem')
        path('branch',(6,36),(6,24),(20,24),(24,24),(38,24),(38,28))
        line('middle-stem',(20,24),(20,32))
        connect('branch','middle-stem');connect('dollar','branch');connect('stem','branch')
        circle('round-node',6,38,2);connect('round-node','branch')
        box('square-node',16,32,8,8,1);connect('middle-stem','square-node')
        path('triangle-node',(32,40),(38,28),(44,40),(32,40),closed=True);connect('branch','triangle-node')
