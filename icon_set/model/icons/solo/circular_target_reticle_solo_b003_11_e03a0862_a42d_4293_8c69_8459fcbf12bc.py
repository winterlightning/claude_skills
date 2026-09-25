"""Circular Target Reticle.
Plan: Cardinal reticle ring and four radial ticks; shared radius and axis.
Centerline envelope: center (24,24), radius 20; cardinal extrema (4,24),(24,4),(44,24),(24,44).
Final reduction/review: Cardinal reticle ring and four radial ticks; shared radius and axis.
Keyshape: CIRCLE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide crosshair; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e03a0862-a42d-4293-8c69-8459fcbf12bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/circle clock_e03a0862-a42d-4293-8c69-8459fcbf12bc.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-003/references/circle clock_e03a0862-a42d-4293-8c69-8459fcbf12bc.svg'
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
    icon_id = 'circular-target-reticle-solo-b003-11'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    aliases = ()
    keywords = ('circular', 'target', 'reticle')

    def build(self):
        s = self
        axis=24;r=20
        pts=[(axis,axis-r),(axis+r,axis),(axis,axis+r),(axis-r,axis)]
        for j in range(4):
         s.add_arc(f'ring-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        s.add_contour('ring',*(f'ring-{j}' for j in range(4)),closed=True)
        for j,(a,z) in enumerate([((24,24-r),(24,24-14)),((24+r,24),(24+14,24)),((24,24+r),(24,24+14)),((24-r,24),(24-14,24))]):
         s.add_line(f'tick-{j}',a,z);join(s,'ring',f'tick-{j}')
