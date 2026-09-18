"""Crossword: seven equal 9-unit cells, four across and four down, shared second cell.
Native SOLO48; SQUARE envelope. Construction reference: none; equal-cell grid construction.
All seven blank cells retained; off-center crossing intentionally preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b020d760-a5d5-4e04-8750-a9a54924a132'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/crossword 1_b020d760-a5d5-4e04-8750-a9a54924a132.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/crossword 1_b020d760-a5d5-4e04-8750-a9a54924a132.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/crossword 1_b020d760-a5d5-4e04-8750-a9a54924a132.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'crossword-grid-batch-019-14'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('crossword', 'grid')

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

        cells={(i,1) for i in range(4)}|{(1,j) for j in range(4)}
        edges=set()
        for x,y in cells:
            p=[(6+9*x,6+9*y),(6+9*(x+1),6+9*y),(6+9*(x+1),6+9*(y+1)),(6+9*x,6+9*(y+1))]
            for a,b in zip(p,p[1:]+p[:1]): edges.add(tuple(sorted((a,b))))
        named=[]
        for i,(a,b) in enumerate(sorted(edges)):
            name=f'edge-{i}';line(name,a,b);named.append((name,a,b))
        for i,(n,a,b) in enumerate(named):
            for m,c,d in named[i+1:]:
                if {a,b}&{c,d}: self.relate('connect',n,m)
