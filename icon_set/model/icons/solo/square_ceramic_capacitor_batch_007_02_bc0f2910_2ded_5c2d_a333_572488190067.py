"""Square Ceramic Capacitor.
Plan: Rounded ceramic body with paired leads at shared bottom nodes; blank face retained.
Visible-ink envelope: (6, 2, 42, 46); 4-unit stroke on the integer grid.
Construction: Lucide cable; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc0f2910-2ded-5c2d-a333-572488190067'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/electronics/capacitor_bc0f2910-2ded-5c2d-a333-572488190067.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/capacitor_bc0f2910-2ded-5c2d-a333-572488190067.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/capacitor_bc0f2910-2ded-5c2d-a333-572488190067.svg'

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
    icon_id = 'square-ceramic-capacitor-batch-007-02'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    aliases = ()
    keywords = ('square', 'ceramic', 'capacitor')

    def build(self):
        box(self,'body',8,4,40,28,4,nodes=((16,28),(32,28)))
        for i,x in enumerate((16,32)):
            self.add_line(f'lead-{i}',(x,28),(x,44));self.relate('connect','body',f'lead-{i}')
