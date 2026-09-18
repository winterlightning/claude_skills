"""SD Memory Storage Card.
Plan: Clipped upright SD card; evenly spaced contacts and orientation chevron. Left locking notch omitted and four contacts reduced to three for clearance.
Visible-ink envelope: (6, 2, 42, 46); 4-unit stroke on the integer grid.
Construction: Lucide cable; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '415842e2-9e42-4cd1-8038-df3362e7ac71'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/electronics/sd card_415842e2-9e42-4cd1-8038-df3362e7ac71.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/sd card_415842e2-9e42-4cd1-8038-df3362e7ac71.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/sd card_415842e2-9e42-4cd1-8038-df3362e7ac71.svg'

def circle(s,n,x,y,r):
    s.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
    s.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
    s.add_contour(n,n+'a',n+'b',closed=True)

def box(s,n,l,t,r,b,k=3,nodes=()):
    pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k),(l+k,t)]
    members=[]
    for i,(a,z) in enumerate(zip(pts,pts[1:])):
        if a==z: continue
        if i%2:
            p=f'{n}-{i}';s.add_arc(p,a,z,radius_x=k);members.append(p)
        else:
            dx,dy=z[0]-a[0],z[1]-a[1]
            mid=[p for p in nodes if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            mid.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy)
            q=[a]+mid+[z]
            for j,(v,w) in enumerate(zip(q,q[1:])):
                p=f'{n}-{i}-{j}';s.add_line(p,v,w);members.append(p)
    s.add_contour(n,*members,closed=True)

class Result(Solo48):
    icon_id = 'sd-memory-storage-card-batch-007-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    aliases = ()
    keywords = ('sd', 'memory', 'storage', 'card')

    def build(self):
        self.add_polyline('card',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        for i,x in enumerate(range(16,33,8)):
            self.add_line(f'contact-{i}',(x,18),(x,23))
        self.add_polyline('orientation',(20,36),(24,32),(28,36))
