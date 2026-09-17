"""Tied Money Sack.
Plan: Money pouch with tied mouth, wide rounded belly and small side tie; no currency text in source.
Centerline envelope: (8,4)-(40,44).
Final reduction/review: Money pouch with tied mouth, wide rounded belly and small side tie; no currency text in source.
Keyshape: VRECT_L; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide archive; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b374e57-1910-4c94-8ccf-5772b68aa865'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/container/pouch 1_7b374e57-1910-4c94-8ccf-5772b68aa865.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-004/references/pouch 1_7b374e57-1910-4c94-8ccf-5772b68aa865.svg'
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
    icon_id = 'tied-money-sack-solo-b004-10'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tied', 'money', 'sack')

    def build(self):
        s = self
        s.add_polyline('mouth',(18,14),(12,4),(36,4),(30,14),(18,14))
        s.add_arc('left',(18,14),(8,34),radius_x=30,sweep=False)
        s.add_arc('bottom',(8,34),(40,34),radius_x=16,radius_y=10,sweep=False)
        s.add_arc('right',(40,34),(30,14),radius_x=30,sweep=False)
        s.add_contour('bag','left','bottom','right');join(s,'bag','mouth')
        s.add_polyline('tie',(8,12),(18,14),(8,20));join(s,'tie','mouth');join(s,'tie','bag')
