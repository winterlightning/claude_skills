"""Return arrow: three-quarter circular arc; angular arrowhead at the left end.
Native SOLO48; SQUARE envelope. Construction reference: rotate-ccw.
Wide lower-left opening and counterclockwise direction preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '567f7df5-55ba-4b86-8f69-4c5a4f43e848'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/go backward_567f7df5-55ba-4b86-8f69-4c5a4f43e848.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/go backward_567f7df5-55ba-4b86-8f69-4c5a4f43e848.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/go backward_567f7df5-55ba-4b86-8f69-4c5a4f43e848.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'counterclockwise-circular-arrow-batch-019-08'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('counterclockwise', 'circular', 'arrow')

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

        self.add_arc('sweep',(24,42),(6,24),radius_x=18,large_arc=True,sweep=False)
        self.add_polyline('head',(6,14),(6,24),(16,24))
        self.relate('connect','sweep','head')
