"""Delivery Truck with Export Arrow.
Plan: Export truck with rising arrow on cargo, cab and paired wheels; minimal cab detail.
Centerline envelope: (4,8)-(44,40).
Final reduction/review: Export truck with rising arrow on cargo, cab and paired wheels; minimal cab detail.
Keyshape: HRECT_L; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide truck; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2886b11f-72f8-5830-839e-a7881e8e2fbe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/delivery/delivery truck_2886b11f-72f8-5830-839e-a7881e8e2fbe.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-005/references/delivery truck_2886b11f-72f8-5830-839e-a7881e8e2fbe.svg'
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
    icon_id = 'delivery-truck-with-export-arrow-solo-b005-08'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('delivery', 'truck', 'with', 'export', 'arrow')

    def build(self):
        s = self
        s.add_polyline('cargo',(4,32),(4,8),(28,8),(28,32))
        s.add_polyline('cab',(28,16),(36,16),(44,26),(44,32),(36,32));join(s,'cargo','cab')
        circle(s,'wheel-left',12,36,4);circle(s,'wheel-right',36,36,4)
        s.add_polyline('chassis',(4,32),(12,32),(28,32),(36,32))
        join(s,'chassis','cargo');join(s,'chassis','cab');join(s,'chassis','wheel-left');join(s,'chassis','wheel-right');join(s,'cab','wheel-right')
        arrow(s,'export',(13,24),(20,16),5)
