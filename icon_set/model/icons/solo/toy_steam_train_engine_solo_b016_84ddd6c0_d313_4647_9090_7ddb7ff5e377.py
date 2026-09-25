"""Side-view toy locomotive, chimney at left, tall cab right and two wheels. Window and wheel hubs omitted as sub-resolution details. Centerline6,6–42,42.
Lucide construction reference: train-front.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='84ddd6c0-d313-4647-9090-7ddb7ff5e377'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys train_84ddd6c0-d313-4647-9090-7ddb7ff5e377.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='toy-steam-train-engine-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    categories = ("primitives", "kids")
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

        self.add_polyline('body',(6,28),(6,20),(14,20),(24,20),(24,6),(40,6),(40,28),(34,28),(13,28),(6,28))
        self.add_polyline('chimney',(6,12),(14,12),(14,20));self.relate('connect','body','chimney')
        for x in (13,34):
         circle('wheel'+str(x),x,35,7);self.relate('connect','body','wheel'+str(x))
        self.add_line('roof',(24,6),(42,6));self.relate('connect','roof','body')
