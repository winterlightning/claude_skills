"""Broken Speech Bubble.
Plan: Speech bubble with open zigzag break in its top edge and bottom-left tail.
Centerline envelope: (6,6)-(42,42).
Final reduction/review: Wider open zigzag crack; rounded outline reduced to geometric corners.
Keyshape: SQUARE; all geometry authored at SOLO48, never scaled.
Construction reference: Lucide panel-left; rounded contours and shared attachment nodes.
Human construction reference where applicable: icon_set/references/human_ref/.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9390f65a-a76b-451f-b66d-2d0bd6fbda66'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/chat/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-003/references/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
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
    icon_id = 'broken-speech-bubble-solo-b003-03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    categories = ('primitives', 'chat')
    aliases = ()
    keywords = ('broken', 'speech', 'bubble')

    def build(self):
        s = self
        s.add_polyline('bubble',(18,6),(6,6),(6,34),(14,34),(14,42),(24,34),(42,34),(42,6),(32,6),(34,16),(30,24))
        s.add_polyline('crack',(18,6),(24,14),(16,22))
        join(s,'bubble','crack')
