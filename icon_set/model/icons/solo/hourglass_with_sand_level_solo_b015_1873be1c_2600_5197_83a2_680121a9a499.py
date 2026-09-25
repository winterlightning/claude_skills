"""Crossed hourglass with short sand line high in upper chamber. Mirrored curved walls and broad rails. Centerline8,4–40,44.
Lucide construction reference: hourglass.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1873be1c-2600-5197-83a2-680121a9a499'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/hourglass_1873be1c-2600-5197-83a2-680121a9a499.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='hourglass-with-sand-level-solo-b015'
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

        self.add_polyline('top',(8,4),(10,4),(38,4),(40,4))
        self.add_polyline('bottom',(8,44),(10,44),(38,44),(40,44))
        for side in (-1,1):
         x=24+side*14;z=24-side*14
         path('glass'+str(side),(x,4),[('L',(x,9)),('B',(x,21),(24,20),(24,24)),('B',(24,28),(z,31),(z,39)),('L',(z,44))])
         self.relate('connect','top','glass'+str(side));self.relate('connect','bottom','glass'+str(side))
        self.relate('connect','glass-1','glass1')
        self.add_line('sand',(22,12),(26,12))
