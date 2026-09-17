"""Person Wearing Explosive Vest.
Plan: Figure with paired vest panels, extended arm and hanging loop; preserve visible apparatus without inventing controls.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Vest panels and hanging loop retained; lower leg outlines omitted. Head r4 center(16,10), torso start(16,22): gap8 / ink4.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide contact; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '152f8e57-b879-40b3-9e9a-155338f12ac6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/crime/suicide bombing_152f8e57-b879-40b3-9e9a-155338f12ac6.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-005/references/suicide bombing_152f8e57-b879-40b3-9e9a-155338f12ac6.svg'
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
    icon_id = 'person-wearing-explosive-vest-solo-b005-07'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('person', 'wearing', 'explosive', 'vest')

    def build(self):
        s = self
        circle(s,'head',16,10,4)
        s.add_line('torso',(16,22),(16,32));s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        s.add_polyline('arm',(6,32),(6,22),(16,22),(42,22));join(s,'arm','torso')
        s.add_polyline('vest',(6,32),(16,32),(26,32),(26,42),(6,42),closed=True);join(s,'vest','arm');join(s,'vest','torso')
        s.add_line('panel',(16,32),(16,42));join(s,'panel','vest');join(s,'panel','torso')
        s.add_polyline('loop',(34,22),(34,38),(42,38),(42,22));join(s,'loop','arm')
