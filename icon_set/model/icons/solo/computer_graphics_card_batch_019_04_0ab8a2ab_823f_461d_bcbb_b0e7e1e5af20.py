"""GPU: rounded board; one circular fan; four pins on an 8-unit series.
Native SOLO48; HRECT_L envelope. Construction reference: gpu.
Fan reduced to one circular aperture; four connector pins retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/gpu mining_0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/gpu mining_0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/gpu mining_0ab8a2ab-823f-461d-bcbb-b0e7e1e5af20.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'computer-graphics-card-batch-019-04'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('computer', 'graphics', 'card')

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

        rect('board',4,8,44,32,4,cuts=tuple((12+8*i,32) for i in range(4)))
        circle('fan',16,20,3)
        line('detail',(29,20),(35,20))
        for i in range(4):
            x=12+8*i
            line(f'pin-{i}',(x,32),(x,40))
            self.relate('connect','board',f'pin-{i}')
