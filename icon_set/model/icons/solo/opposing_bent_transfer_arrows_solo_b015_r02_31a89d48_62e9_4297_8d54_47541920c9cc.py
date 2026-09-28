"""Opposing bent arrows with rounded tails; interrupted tails shorten to leave clear gaps around opposing heads. Centerline4,8–44,40.
Construction reference: arrow-up-down.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='31a89d48-62e9-4297-8d54-47541920c9cc'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/refresh_31a89d48-62e9-4297-8d54-47541920c9cc.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/refresh_31a89d48-62e9-4297-8d54-47541920c9cc.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/refresh_31a89d48-62e9-4297-8d54-47541920c9cc.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='opposing-bent-transfer-arrows-solo-b015-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases=()
    keywords=('opposing', 'bent', 'transfer', 'arrows')
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

        path('up',(12,8),[('L',(12,27)),('A',5,5,False,(17,32)),('L',(19,32))])
        path('down',(36,40),[('L',(36,21)),('A',5,5,False,(31,16)),('L',(29,16))])
        self.add_polyline('uph',(4,16),(12,8),(20,16));self.add_polyline('downh',(28,32),(36,40),(44,32))
        self.relate('connect','up','uph');self.relate('connect','down','downh')
