"""Sand timer with crossed curved chamber walls and short upper sand line. Spacious shoulders preserve sand clearance. Centerline8,4–40,44.
Construction reference: hourglass.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1873be1c-2600-5197-83a2-680121a9a499'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='hourglass-with-sand-level-solo-b015-r02'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    aliases=()
    keywords=('hourglass', 'with', 'sand', 'level')
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

        for y in (4,44):self.add_polyline('rail'+str(y),(8,y),(10,y),(38,y),(40,y))
        for side in (-1,1):
         x=24+side*14;z=24-side*14
         path('wall'+str(side),(x,4),[('L',(x,10)),('B',(x,22),(24,20),(24,24)),('B',(24,28),(z,31),(z,38)),('L',(z,44))])
         for y in (4,44):self.relate('connect','wall'+str(side),'rail'+str(y))
        self.relate('connect','wall-1','wall1');self.add_line('sand',(23,13),(25,13))
