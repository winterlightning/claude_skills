"""Hand: crossed raised fingers and folded thumb, rounded palm; deliberate anatomical asymmetry.
Native SOLO48; VRECT_L envelope. Construction reference: hand / hand-metal.
Simplified curled-finger creases; retained crossing and horizontal folded thumb. Shared human reference inspected; no detached head is present.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05f00c7f-9195-41aa-b8b1-c15ae7c59bd3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/finger crossed 1_05f00c7f-9195-41aa-b8b1-c15ae7c59bd3.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/finger crossed 1_05f00c7f-9195-41aa-b8b1-c15ae7c59bd3.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/finger crossed 1_05f00c7f-9195-41aa-b8b1-c15ae7c59bd3.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'crossed-fingers-with-folded-thumb-batch-019-12'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crossed', 'fingers', 'with', 'folded', 'thumb')

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

        self.add_bezier('outline',(8,31),((8,24),(14,20),(18,14)),((20,11),(20,12),(22,9)),((23,8),(23,7),(24,6)),((27,2),(35,6),(31,12)),((29,16),(27,19),(26,22)),((29,17),(34,18),(34,24)),((38,19),(40,23),(40,28)),((40,38),(35,44),(25,44)),((16,44),(8,41),(8,31)))
        self.add_contour('skin','outline',closed=True)
        self.add_bezier('back-finger',(18,14),((13,8),(10,4),(15,4)),((18,4),(20,7),(22,9)))
        self.relate('connect','skin','back-finger')
        self.add_bezier('thumb',(8,31),((13,28),(18,28),(26,28)),((33,28),(33,35),(26,35)))
        self.relate('connect','skin','thumb')
