"""Hand Stealing Identity Card.
Plan: Hand holds identity card; preserve complete interaction and portrait.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Portrait head r2 center(16,24), shoulder y34: gap8 / ink4; hand and card kept together.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide contact; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ba267b5-9ca9-4999-a24d-b73d45e0c937'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/crime/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-005/references/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg'
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
    icon_id = 'hand-stealing-identity-card-solo-b005-06'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hand', 'stealing', 'identity', 'card')

    def build(self):
        s = self
        s.add_polyline('card',(28,14),(6,14),(6,42),(34,42),(34,24))
        s.add_polyline('hand-upper',(18,14),(26,6),(34,6),(42,6));join(s,'hand-upper','card')
        s.add_polyline('hand-lower',(42,16),(34,24),(28,24));join(s,'hand-lower','card')
        circle(s,'portrait',16,24,2)
        s.add_line('shoulders',(14,34),(20,34))
