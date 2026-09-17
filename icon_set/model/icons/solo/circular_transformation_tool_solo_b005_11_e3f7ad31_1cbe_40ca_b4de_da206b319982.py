"""Circular Transformation Tool.
Plan: Open transformation disc with radial handle and diagonal arrow plus outside rotation cues.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: INCOMPLETE: rebalanced disc, handle, diagonal arrow and outer arrows remain crowded; hole, pinch and spacing failures retained.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide repeat-2; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3f7ad31-1cbe-40ca-b4de-da206b319982'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/transform shrink_e3f7ad31-1cbe-40ca-b4de-da206b319982.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-005/references/transform shrink_e3f7ad31-1cbe-40ca-b4de-da206b319982.svg'
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
    icon_id = 'circular-transformation-tool-solo-b005-11'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('circular', 'transformation', 'tool')

    def build(self):
        s = self
        s.add_arc('disc-a',(30,24),(14,24),radius_x=8)
        s.add_arc('disc-b',(14,24),(22,32),radius_x=8,sweep=False)
        s.add_contour('disc','disc-a','disc-b')
        s.add_polyline('radial',(30,24),(22,24),(30,34));join(s,'disc','radial')
        s.add_polyline('tip',(24,34),(30,34),(30,28));join(s,'radial','tip')
        circle(s,'handle',40,24,2)
        s.add_polyline('top',(22,6),(34,6),(42,14))
        s.add_polyline('top-tip',(34,14),(34,6),(42,6));join(s,'top','top-tip')
        s.add_polyline('bottom',(6,32),(10,42),(18,42))
        s.add_polyline('bottom-tip',(12,36),(18,42),(10,42));join(s,'bottom','bottom-tip')
