"""Long sun-lounger seat with reclining right back and two splayed legs. Centerline4,8–44,40. Deliberate side-view asymmetry.
Lucide construction reference: armchair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f6e5bd8a-5088-4e44-940d-be3c568ff2da'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sunbed_f6e5bd8a-5088-4e44-940d-be3c568ff2da.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/sunbed_f6e5bd8a-5088-4e44-940d-be3c568ff2da.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/sunbed_f6e5bd8a-5088-4e44-940d-be3c568ff2da.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='reclining-sun-lounger-solo-b017'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=('reclining', 'sun', 'lounger')
    def build(self):

        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r));members=[]
            for i in range(4):
                m=n+str(i);self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r);members.append(m)
            self.add_contour(n,*members,closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        self.add_polyline('seat',(4,28),(10,28),(32,28),(44,8))
        self.add_line('frontleg',(10,28),(4,40));self.add_line('rearleg',(32,28),(40,40))
        self.relate('connect','seat','frontleg');self.relate('connect','seat','rearleg')
