"""Cream jar: broad body and narrower rim; asymmetric cream peak curves into rim.
Native SOLO48; SQUARE envelope. Construction reference: none; smooth tangent contour principles.
Retained raised rim and left-curling dollop; no label added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35786485-a3d0-4f1c-8bb6-3eaad7429935'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/face cream_35786485-a3d0-4f1c-8bb6-3eaad7429935.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/face cream_35786485-a3d0-4f1c-8bb6-3eaad7429935.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/face cream_35786485-a3d0-4f1c-8bb6-3eaad7429935.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'face-cream-jar-batch-019-07'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('face', 'cream', 'jar')

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

        rect('jar',6,26,42,42,3,cuts=((10,26),(38,26)))
        self.add_polyline('rim',(10,26),(10,18),(12,18),(36,18),(38,18),(38,26))
        self.relate('connect','jar','rim')
        self.add_bezier('cream',(12,18),((13,11),(26,15),(23,6)),((30,9),(35,12),(36,18)))
        self.relate('connect','rim','cream')
