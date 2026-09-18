"""Mailbox with Envelope.
Plan: Mail envelope rests across domed mailbox; single post and simplified dome replace front divider.
Visible-ink envelope: (6, 2, 42, 46); 4-unit stroke on the integer grid.
Construction: Lucide mail; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '433a84d0-4b9d-5ce3-bc13-30591f7fdce8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/mailbox in_433a84d0-4b9d-5ce3-bc13-30591f7fdce8.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/emails/mailbox in_433a84d0-4b9d-5ce3-bc13-30591f7fdce8.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/mailbox in_433a84d0-4b9d-5ce3-bc13-30591f7fdce8.svg'

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
    icon_id = 'mailbox-with-envelope-batch-007-06'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'emails'
    aliases = ()
    keywords = ('mailbox', 'with', 'envelope')

    def build(self):
        self.add_polyline('letter',(14,4),(34,4),(34,20),(14,20),closed=True)
        self.add_polyline('flap',(14,4),(24,12),(34,4));self.relate('connect','letter','flap')
        self.add_arc('dome-left',(8,28),(14,20),radius_x=6,radius_y=8)
        self.add_arc('dome-right',(34,20),(40,28),radius_x=6,radius_y=8)
        run(self,'box-base',(40,28),(40,34),(24,34),(8,34),(8,28))
        self.add_contour('mailbox','dome-right','box-base-1','box-base-2','box-base-3','box-base-4','dome-left')
        self.relate('connect','mailbox','letter')
        self.add_line('post',(24,34),(24,44));self.relate('connect','post','mailbox')
