"""Cylinder: broad elliptical top and curved lower edge, symmetric walls.
Native SOLO48; HRECT_L envelope. Construction reference: database.
Inset side seams merged into clear cylinder walls; broad curved cap and base preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '960eb0e0-a911-4c9c-883a-ff622c45b802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/virtual environment 1_960eb0e0-a911-4c9c-883a-ff622c45b802.svg'
LEGACY_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/virtual environment 1_960eb0e0-a911-4c9c-883a-ff622c45b802.svg'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-019/references/virtual environment 1_960eb0e0-a911-4c9c-883a-ff622c45b802.svg'
AUTHOR = 'gpt-6'


class Batch019Icon(Solo48):
    icon_id = 'database-cylinder-batch-019-15'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('database', 'cylinder')

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

        arc('top-front',(4,16),(44,16),20,8,False)
        arc('top-back',(44,16),(4,16),20,8,False)
        self.add_contour('top','top-front','top-back',closed=True)
        line('right',(44,16),(44,32))
        arc('bottom',(44,32),(4,32),20,8,True)
        line('left',(4,32),(4,16))
        self.add_contour('body','right','bottom','left')
        self.relate('connect','top','body')
