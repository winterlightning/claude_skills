"""Open Storage Drawer.
Plan: Wide open drawer; rear rim and converging sides, broad scooped front. Symmetric about x=24.
Visible-ink envelope: (2, 6, 46, 42); 4-unit stroke on the integer grid.
Construction: Lucide mail; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '244afd80-5d73-57d2-8e56-c06e1e49d855'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/drawer open_244afd80-5d73-57d2-8e56-c06e1e49d855.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/emails/drawer open_244afd80-5d73-57d2-8e56-c06e1e49d855.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/drawer open_244afd80-5d73-57d2-8e56-c06e1e49d855.svg'

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

def run(s,n,*points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        s.add_line(f'{n}-{i}',a,b)

class Result(Solo48):
    icon_id = 'open-storage-drawer-batch-007-07'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'emails'
    aliases = ()
    keywords = ('open', 'storage', 'drawer')

    def build(self):
        self.add_polyline('rear',(4,24),(10,8),(38,8),(44,24))
        run(self,'front-top-left',(4,24),(16,24))
        self.add_arc('scoop',(16,24),(32,24),radius_x=8,sweep=False)
        run(self,'front-rest',(32,24),(44,24),(44,40),(4,40),(4,24))
        self.add_contour('front','front-top-left-1','scoop','front-rest-1','front-rest-2','front-rest-3','front-rest-4',closed=True)
        self.relate('connect','rear','front')
