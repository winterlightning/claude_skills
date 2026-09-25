"""Square Repeating Loop Arrows.
Plan: Opposing rounded bent arrows share corner radii and rotational symmetry.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Opposing rounded bent arrows share corner radii and rotational symmetry.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide repeat-2; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca612233-0073-4bac-8e1e-0eb28541ca7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/arrow square_ca612233-0073-4bac-8e1e-0eb28541ca7f.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-004/references/arrow square_ca612233-0073-4bac-8e1e-0eb28541ca7f.svg'
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
    icon_id = 'square-repeating-loop-arrows-solo-b004-07'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('square', 'repeating', 'loop', 'arrows')

    def build(self):
        s = self
        for j in range(2):
         p=lambda x,y:(x,y) if j==0 else (48-x,48-y)
         s.add_line(f'side-{j}',p(6,28),p(6,16))
         s.add_arc(f'corner-{j}',p(6,16),p(12,10),radius_x=6)
         s.add_line(f'run-{j}',p(12,10),p(38,10))
         s.add_contour(f'arrow-{j}',f'side-{j}',f'corner-{j}',f'run-{j}')
         s.add_polyline(f'tip-{j}',p(34,6),p(38,10),p(34,14));join(s,f'arrow-{j}',f'tip-{j}')
