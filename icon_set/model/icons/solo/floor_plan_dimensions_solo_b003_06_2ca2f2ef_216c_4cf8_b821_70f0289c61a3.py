"""Floor Plan Dimensions.
Plan: Plan with unequal partitions plus top and left dimension arrows.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Partitions reduced to three unequal rooms; dimension arrows retained.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide panels-top-left; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ca2f2ef-216c-4cf8-b821-70f0289c61a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/construction/real estate dimensions block_2ca2f2ef-216c-4cf8-b821-70f0289c61a3.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-003/references/real estate dimensions block_2ca2f2ef-216c-4cf8-b821-70f0289c61a3.svg'
AUTHOR = 'gpt-6'

def circle(s,n,x,y,r):
    s.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
    s.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
    s.add_contour(n,n+'-a',n+'-b',closed=True)

def box(s,n,l,t,r,b,k=3,nodes=()):
    pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k),(l+k,t)]
    members=[]
    for i,(a,z) in enumerate(zip(pts,pts[1:])):
        if a==z: continue
        if i%2:
            q=f'{n}-{i}';s.add_arc(q,a,z,radius_x=k);members.append(q)
        else:
            dx,dy=z[0]-a[0],z[1]-a[1]
            cuts=sorted([p for p in nodes if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy],key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy)
            seq=[a]+cuts+[z]
            for j,(u,v) in enumerate(zip(seq,seq[1:])):
                q=f'{n}-{i}-{j}';s.add_line(q,u,v);members.append(q)
    s.add_contour(n,*members,closed=True)

def join(s,a,b):
    s.relate('connect',a,b)

def arrow(s,n,a,z,w=7):
    s.add_line(n+'-shaft',a,z)
    dx,dy=z[0]-a[0],z[1]-a[1]
    if dy==0: pts=((z[0]-(w if dx>0 else -w),z[1]-w),z,(z[0]-(w if dx>0 else -w),z[1]+w))
    elif dx==0: pts=((z[0]-w,z[1]-(w if dy>0 else -w)),z,(z[0]+w,z[1]-(w if dy>0 else -w)))
    else: pts=((z[0]-(w if dx>0 else -w),z[1]),z,(z[0],z[1]-(w if dy>0 else -w)))
    s.add_polyline(n+'-tip',*pts);join(s,n+'-shaft',n+'-tip')

class GeneratedSolo(Solo48):
    icon_id = 'floor-plan-dimensions-solo-b003-06'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('floor', 'plan', 'dimensions')

    def build(self):
        s = self
        box(s,'plan',20,20,42,42,2,nodes=((30,20),(30,42),(20,30),(30,30)))
        s.add_polyline('partition',(30,20),(30,30),(30,42));join(s,'partition','plan')
        s.add_line('room',(20,30),(30,30));join(s,'room','plan');join(s,'room','partition')
        arrow(s,'width',(20,9),(42,9),3);s.add_polyline('width-start',(23,6),(20,9),(23,12));join(s,'width-start','width-shaft')
        arrow(s,'height',(9,20),(9,42),3);s.add_polyline('height-start',(6,23),(9,20),(12,23));join(s,'height-start','height-shaft')
