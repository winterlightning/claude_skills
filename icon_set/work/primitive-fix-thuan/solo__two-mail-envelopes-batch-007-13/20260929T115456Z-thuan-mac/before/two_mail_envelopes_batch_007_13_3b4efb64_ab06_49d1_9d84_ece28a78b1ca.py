"""Two Mail Envelopes.
Plan: Two overlapping closed envelopes; interrupted rear boundary communicates occlusion. Omit rear flap to avoid crowded overlap.
Visible-ink envelope: (4, 4, 44, 44); 4-unit stroke on the integer grid.
Construction: Lucide mail; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b4efb64-ab06-49d1-9d84-ece28a78b1ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/envelope back front_3b4efb64-ab06-49d1-9d84-ece28a78b1ca.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/envelope back front_3b4efb64-ab06-49d1-9d84-ece28a78b1ca.svg'

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
    icon_id = 'two-mail-envelopes-batch-007-13'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'emails'
    categories = ('emails', 'primitives')
    aliases = ()
    keywords = ('two', 'mail', 'envelopes')

    def build(self):
        self.add_polyline('rear',(6,30),(6,6),(32,6),(32,18))
        self.add_polyline('front',(16,18),(32,18),(42,18),(42,42),(16,42),closed=True)
        self.add_polyline('flap',(16,18),(29,30),(42,18))
        self.relate('connect','front','rear');self.relate('connect','front','flap')
