"""Padlock: body owns center dot; shackle is symmetric about x=24 and joins the body top.
Native SOLO48; VRECT_L envelope. Construction reference: lock.
Preserved the center dot and tall inverted-U shackle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52a489db-01e7-4af3-9fa0-bcb731eeb236'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lock_52a489db-01e7-4af3-9fa0-bcb731eeb236.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/lock_52a489db-01e7-4af3-9fa0-bcb731eeb236.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/lock_52a489db-01e7-4af3-9fa0-bcb731eeb236.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'closed-padlock-batch-019-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('closed', 'padlock')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def circle(n,x,y,r):
            arc(n+'-a',(x-r,y),(x+r,y),r)
            arc(n+'-b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b,k=4,cuts=()):
            pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
            members=[]
            for j in range(8):
                a,z=pts[j],pts[(j+1)%8]
                if j%2:
                    name=f'{n}-{j}';arc(name,a,z,k);members.append(name)
                else:
                    mids=[p for p in cuts if p not in (a,z) and
                          (z[0]-a[0])*(p[1]-a[1])==(z[1]-a[1])*(p[0]-a[0]) and
                          min(a[0],z[0])<=p[0]<=max(a[0],z[0]) and min(a[1],z[1])<=p[1]<=max(a[1],z[1])]
                    run=[a]+sorted(mids,key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)+[z]
                    for q,(u,v) in enumerate(zip(run,run[1:])):
                        name=f'{n}-{j}-{q}';line(name,u,v);members.append(name)
            self.add_contour(n,*members,closed=True)

        rect('body',8,22,40,44,4,cuts=((14,22),(34,22)))
        line('shackle-left',(14,22),(14,14))
        arc('shackle-top',(14,14),(34,14),10)
        line('shackle-right',(34,14),(34,22))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','body','shackle')
        self.add_dot('keyhole',(24,33))
