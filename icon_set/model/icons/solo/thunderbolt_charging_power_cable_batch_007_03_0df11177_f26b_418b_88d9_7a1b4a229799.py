"""Thunderbolt Charging Power Cable.
Plan: Unequal plugs joined by a continuous two-bend loop; omit miniature pin sleeves and diagonal markings. Intentional left/right height asymmetry.
Visible-ink envelope: (4, 4, 44, 44); 4-unit stroke on the integer grid.
Construction: Lucide cable; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0df11177-f26b-418b-88d9-7a1b4a229799'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/electronics/thunderbolt cable_0df11177-f26b-418b-88d9-7a1b4a229799.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/thunderbolt cable_0df11177-f26b-418b-88d9-7a1b4a229799.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/thunderbolt cable_0df11177-f26b-418b-88d9-7a1b4a229799.svg'

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
    icon_id = 'thunderbolt-charging-power-cable-batch-007-03'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'electronics'
    aliases = ()
    keywords = ('thunderbolt', 'charging', 'power', 'cable')

    def build(self):
        box(self,'plug-left',6,6,14,22,2,nodes=((10,22),))
        box(self,'plug-right',34,30,42,42,2,nodes=((38,30),))
        self.add_line('cord-a',(10,22),(10,35))
        self.add_arc('cord-b',(10,35),(24,35),radius_x=7,sweep=False)
        self.add_line('cord-c',(24,35),(24,13))
        self.add_arc('cord-d',(24,13),(38,13),radius_x=7)
        self.add_line('cord-e',(38,13),(38,30))
        self.add_contour('cord','cord-a','cord-b','cord-c','cord-d','cord-e')
        self.relate('connect','cord','plug-left');self.relate('connect','cord','plug-right')
