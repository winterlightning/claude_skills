"""Waving Flag on Pole.
Plan: Waving fabric attached to pole; smooth repeated upper and lower waves with notched fly.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Waving fabric attached to pole; smooth repeated upper and lower waves with notched fly.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide flag; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '036d292c-063d-4d0e-96a6-7a21424e1c7e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/flag 3_036d292c-063d-4d0e-96a6-7a21424e1c7e.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-005/references/flag 3_036d292c-063d-4d0e-96a6-7a21424e1c7e.svg'
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
    icon_id = 'waving-flag-on-pole-solo-b005-03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('waving', 'flag', 'on', 'pole')

    def build(self):
        s = self
        s.add_polyline('pole',(6,9),(6,30),(6,42))
        s.add_arc('top-a',(6,9),(24,9),radius_x=9,radius_y=3,sweep=False)
        s.add_arc('top-b',(24,9),(42,9),radius_x=9,radius_y=3)
        s.add_line('fly-a',(42,9),(38,18));s.add_line('fly-b',(38,18),(42,30))
        s.add_arc('bottom-a',(42,30),(24,30),radius_x=9,radius_y=3,sweep=False)
        s.add_arc('bottom-b',(24,30),(6,30),radius_x=9,radius_y=3)
        s.add_contour('fabric','top-a','top-b','fly-a','fly-b','bottom-a','bottom-b');join(s,'pole','fabric')
