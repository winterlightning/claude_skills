"""Advertisement Flyer with Tear-Off Tabs.
Plan: Flyer printed headline and tear-off tabs, one missing tab; simplify image to horizontal mark.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Printed image and text reduced to headline; missing tear-off tab retained.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide newspaper; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '08adb1ca-a993-46ae-966a-fe5da84cc041'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/flyer taken_08adb1ca-a993-46ae-966a-fe5da84cc041.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-002/references/flyer taken_08adb1ca-a993-46ae-966a-fe5da84cc041.svg'
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
    icon_id = 'advertisement-flyer-with-tear-off-tabs-solo-b002-06'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('advertisement', 'flyer', 'with', 'tear-off', 'tabs')

    def build(self):
        s = self
        s.add_polyline('paper',(6,42),(6,6),(42,6),(42,30),(33,26),(24,30),(15,26),(6,30))
        s.add_line('headline',(16,16),(32,16))
        for x,y in ((15,26),(24,30)):
         s.add_line(f'tab-{x}',(x,y),(x,42));join(s,'paper',f'tab-{x}')
