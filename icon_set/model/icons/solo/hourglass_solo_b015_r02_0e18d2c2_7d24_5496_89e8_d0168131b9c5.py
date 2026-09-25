"""Empty hourglass: mirrored curved sides with a wide waist; single-stroke rails replace doubled rims. Centerline10,4–38,44.
Construction reference: hourglass.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0e18d2c2-7d24-5496-89e8-d0168131b9c5'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='hourglass-solo-b015-r02'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases=()
    keywords=('hourglass',)
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

        for y in (4,44):self.add_polyline('rail'+str(y),(10,y),(12,y),(36,y),(38,y))
        for side in (-1,1):
         x=24+side*12;w=24+side*5
         path('wall'+str(side),(x,4),[('L',(x,11)),('B',(x,18),(w,19),(w,24)),('B',(w,29),(x,30),(x,37)),('L',(x,44))])
         for y in (4,44):self.relate('connect','wall'+str(side),'rail'+str(y))
