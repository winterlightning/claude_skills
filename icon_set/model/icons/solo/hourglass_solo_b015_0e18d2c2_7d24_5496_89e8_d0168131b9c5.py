"""Mirrored empty hourglass with smooth pinched chambers and broad rails. Centerline box8,4–40,44. Omit double rail outlines to preserve chamber space.
Lucide construction reference: hourglass.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0e18d2c2-7d24-5496-89e8-d0168131b9c5'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/hourglass_0e18d2c2-7d24-5496-89e8-d0168131b9c5.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='hourglass-solo-b015'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
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

        self.add_polyline('top',(8,4),(12,4),(36,4),(40,4))
        self.add_polyline('bottom',(8,44),(12,44),(36,44),(40,44))
        for side in (-1,1):
         x=24+side*12;w=24+side*4
         path('side'+str(side),(x,4),[('L',(x,10)),('B',(x,18),(w,18),(w,24)),('B',(w,30),(x,30),(x,38)),('L',(x,44))])
         self.relate('connect','top','side'+str(side));self.relate('connect','bottom','side'+str(side))
