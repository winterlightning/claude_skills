"""Postage Stamp With Face Profile.
Plan: Portrait stamp with one broad scalloped edge notch and continuous forehead, nose and neck; omit hat seam and repeated perforations. Profile asymmetry is intentional.
Visible-ink envelope: (4, 4, 44, 44); 4-unit stroke on the integer grid.
Construction: Lucide ticket; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7666422-a3f3-4822-a1b9-b8fa242e2e68'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/stamps famous_b7666422-a3f3-4822-a1b9-b8fa242e2e68.svg'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/stamps famous_b7666422-a3f3-4822-a1b9-b8fa242e2e68.svg'

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
    icon_id = 'postage-stamp-with-face-profile-batch-007-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'emails'
    aliases = ()
    keywords = ('postage', 'stamp', 'with', 'face', 'profile')

    def build(self):
        run(self,'frame',(6,6),(30,6),(42,6),(42,42),(30,42),(6,42),(6,30))
        self.add_arc('notch-lower',(6,30),(6,18),radius_x=6,sweep=False)
        self.add_line('left-top',(6,18),(6,6))
        self.add_contour('stamp','frame-1','frame-2','frame-3','frame-4','frame-5','frame-6','notch-lower','left-top',closed=True)
        self.add_polyline('profile',(30,6),(22,25),(30,25),(30,42))
        self.relate('connect','stamp','profile')
