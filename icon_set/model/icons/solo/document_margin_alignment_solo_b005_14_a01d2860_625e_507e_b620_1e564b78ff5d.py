"""Document Margin Alignment.
Plan: Document alignment margin with two unequal content blocks sharing left boundary.
Centerline envelope: (8,4)-(40,44).
Final reduction/review: Lower block shares page baseline to preserve two bands and margin without undersized spacing.
Keyshape: VRECT_L; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide panels-top-left; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a01d2860-625e-507e-b620-1e564b78ff5d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/align to margin_a01d2860-625e-507e-b620-1e564b78ff5d.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-005/references/align to margin_a01d2860-625e-507e-b620-1e564b78ff5d.svg'
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
    icon_id = 'document-margin-alignment-solo-b005-14'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('document', 'margin', 'alignment')

    def build(self):
        s = self
        s.add_polyline('page',(8,4),(30,4),(40,14),(40,44),(16,44),(8,44),closed=True)
        s.add_polyline('margin',(16,4),(16,14),(16,24),(16,32),(16,44));join(s,'page','margin')
        s.add_polyline('block-top',(16,14),(28,14),(28,24),(16,24));join(s,'block-top','margin')
        s.add_polyline('block-bottom',(16,32),(32,32),(32,44));join(s,'block-bottom','margin');join(s,'block-bottom','page')
