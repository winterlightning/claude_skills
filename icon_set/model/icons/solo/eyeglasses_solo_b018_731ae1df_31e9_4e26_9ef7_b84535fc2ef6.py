"""Front-facing eyeglasses with equal rounded lenses and short arched bridge. Lens interiors empty. Centerline4,10–44,38.
Lucide construction reference: glasses.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='731ae1df-31e9-4e26-9ef7-b84535fc2ef6'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/eyeglasses_731ae1df-31e9-4e26-9ef7-b84535fc2ef6.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/eyeglasses_731ae1df-31e9-4e26-9ef7-b84535fc2ef6.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/eyeglasses_731ae1df-31e9-4e26-9ef7-b84535fc2ef6.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='eyeglasses-solo-b018'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives-generate", "other")
    aliases=()
    keywords=('eyeglasses',)
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

        circle('left',12,24,8);circle('right',36,24,8)
        self.add_arc('bridge',(20,24),(28,24),radius_x=4,sweep=True);self.relate('connect','left','bridge');self.relate('connect','right','bridge')
