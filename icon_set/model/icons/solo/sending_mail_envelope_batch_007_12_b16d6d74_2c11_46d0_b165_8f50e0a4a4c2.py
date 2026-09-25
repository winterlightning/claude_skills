"""Sending Mail Envelope.
Plan: Upright moving envelope with two horizontal speed strokes; equal stroke separation.
Visible-ink envelope: (2, 8, 46, 40); 4-unit stroke on the integer grid.
Construction: Lucide mail; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b16d6d74-2c11-46d0-b165-8f50e0a4a4c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/send email_b16d6d74-2c11-46d0-b165-8f50e0a4a4c2.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/send email_b16d6d74-2c11-46d0-b165-8f50e0a4a4c2.svg'

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
    icon_id = 'sending-mail-envelope-batch-007-12'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'emails'
    categories = ('emails', 'primitives')
    aliases = ()
    keywords = ('sending', 'mail', 'envelope')

    def build(self):
        self.add_polyline('mail',(20,10),(44,10),(44,38),(20,38),closed=True)
        self.add_polyline('flap',(20,10),(32,23),(44,10));self.relate('connect','mail','flap')
        self.add_line('speed-top',(4,19),(12,19))
        self.add_line('speed-bottom',(4,29),(9,29))
