"""Wireless Earbuds Charging Case.
Plan: Paired earbuds above charging case; lightning simplified to a charging dot.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Earbuds reduced to two stem capsules; lightning replaced by charging status dot.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide bot; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ae8162b-1fa3-4f3e-a7f2-5375c421b45f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/audio/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-001/references/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg'
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
    icon_id = 'wireless-earbuds-charging-case-solo-b001-15'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('wireless', 'earbuds', 'charging', 'case')

    def build(self):
        s = self
        box(s,'case',6,24,42,42,4,nodes=((10,24),(18,24),(30,24),(38,24)))
        for x in (14,34):
         s.add_arc(f'bud-{x}',(x-4,10),(x+4,10),radius_x=4)
         s.add_polyline(f'stem-{x}',(x+4,10),(x+4,24),(x-4,24),(x-4,10))
         join(s,f'bud-{x}',f'stem-{x}');join(s,'case',f'stem-{x}')
        s.add_dot('charge',(24,33))
