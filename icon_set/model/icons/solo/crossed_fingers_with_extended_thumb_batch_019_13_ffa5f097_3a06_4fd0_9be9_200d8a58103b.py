"""Hand: crossing pair above a rounded palm and left-projecting thumb; deliberate anatomical asymmetry.
Native SOLO48; VRECT_L envelope. Construction reference: hand / hand-metal.
Two curled fingertips reduced to broad bumps; retained extended thumb and crossed fingers. Human reference inspected; head-gap rule is inapplicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffa5f097-3a06-4fd0-9be9-200d8a58103b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'crossed-fingers-with-extended-thumb-batch-019-13'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crossed', 'fingers', 'with', 'extended', 'thumb')

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

        self.add_bezier('outline',(16,25),((16,20),(18,17),(20,14)),((22,11),(22,12),(24,9)),((25,8),(25,7),(26,6)),((29,2),(37,6),(33,12)),((31,16),(29,19),(28,22)),((30,19),(34,20),(34,26)),((37,22),(40,24),(40,29)),((40,40),(34,44),(24,44)),((19,44),(15,41),(12,36)),((8,31),(8,29),(8,27)),((8,22),(12,22),(16,25)))
        self.add_contour('skin','outline',closed=True)
        self.add_bezier('back-finger',(20,14),((15,8),(12,4),(17,4)),((20,4),(22,7),(24,9)))
        self.relate('connect','skin','back-finger')
        line('thumb-crease',(16,25),(21,30))
        self.relate('connect','skin','thumb-crease')
