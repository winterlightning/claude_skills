"""Android Mascot Robot Icon.
Plan: Symmetric domed robot; seam, twin antennae and feet; no invented eyes.
Centerline envelope: (8,4)-(40,44).
Final reduction/review: Flattened dome shoulders provide exact mirrored antenna attachments; no eyes or arms invented.
Keyshape: VRECT_L; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide bot; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a895be7-0613-57bb-9e1f-038063cbd8b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-001/references/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
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
    icon_id = 'android-mascot-robot-icon-solo-b001-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('android', 'mascot', 'robot', 'icon')

    def build(self):
        s = self
        s.add_arc('dome-left',(8,20),(14,10),radius_x=6,radius_y=10)
        s.add_line('dome-top',(14,10),(34,10))
        s.add_arc('dome-right',(34,10),(40,20),radius_x=6,radius_y=10)
        s.add_contour('dome','dome-left','dome-top','dome-right')
        s.add_polyline('body',(40,20),(40,34),(32,34),(32,44),(24,44),(24,36),(16,36),(16,44),(8,44),(8,20))
        join(s,'dome','body');s.add_line('seam',(8,20),(40,20));join(s,'seam','body');join(s,'seam','dome')
        for side in (-1,1):
         x=24+side*10;s.add_line(f'antenna-{side}',(x,10),(x+side*4,4));join(s,f'antenna-{side}','dome')
