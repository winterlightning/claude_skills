"""Side-view locomotive with chimney, rear cab and two round wheels. Cab window and hubs omitted for open interior. Centerline4,8–44,40.
Construction reference: train-front.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='84ddd6c0-d313-4647-9090-7ddb7ff5e377'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='toy-steam-train-engine-solo-b016-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    aliases=()
    keywords=('toy', 'steam', 'train', 'engine')
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

        self.add_polyline('body',(4,28),(4,20),(13,20),(25,20),(25,8),(42,8),(42,28),(37,28),(11,28),(4,28))
        self.add_polyline('chimney',(5,12),(13,12),(13,20));self.relate('connect','body','chimney')
        for x in (11,37):circle('wheel'+str(x),x,34,6);self.relate('connect','body','wheel'+str(x))
        self.add_line('roof',(25,8),(44,8));self.relate('connect','roof','body')
