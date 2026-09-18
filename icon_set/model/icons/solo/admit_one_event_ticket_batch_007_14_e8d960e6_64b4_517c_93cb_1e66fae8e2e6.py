"""Admit One Event Ticket.
Plan: Admission ticket with paired semicircular cutouts, tear-off line and one writing rule; no literal text in reference.
Visible-ink envelope: (2, 6, 46, 42); 4-unit stroke on the integer grid.
Construction: Lucide ticket; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8d960e6-64b4-517c-93cb-1e66fae8e2e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/entertainment/ticket_e8d960e6-64b4-517c-93cb-1e66fae8e2e6.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/ticket_e8d960e6-64b4-517c-93cb-1e66fae8e2e6.svg'

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
    icon_id = 'admit-one-event-ticket-batch-007-14'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'entertainment'
    aliases = ()
    keywords = ('admit', 'one', 'event', 'ticket')

    def build(self):
        run(self,'top',(4,18),(4,8),(29,8),(44,8),(44,18))
        self.add_arc('notch-right',(44,18),(44,30),radius_x=6,sweep=False)
        run(self,'bottom',(44,30),(44,40),(29,40),(4,40),(4,30))
        self.add_arc('notch-left',(4,30),(4,18),radius_x=6,sweep=False)
        self.add_contour('ticket','top-1','top-2','top-3','top-4','notch-right','bottom-1','bottom-2','bottom-3','bottom-4','notch-left',closed=True)
        self.add_line('tear',(29,8),(29,40));self.relate('connect','ticket','tear')
        self.add_line('writing',(19,24),(20,24))
