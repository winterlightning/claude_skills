"""Page-down shaft, two crossbars and a downward arrowhead. Crossbar spacing8; shared shaft junctions preserve exact joins. Ink box (8,2)-(40,46).
Lucide construction reference: arrow-left-right.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ed8b450-36d8-5fd5-817f-a4884e9b3b71'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/keyboard page down_8ed8b450-36d8-5fd5-817f-a4884e9b3b71.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/keyboard page down_8ed8b450-36d8-5fd5-817f-a4884e9b3b71.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/keyboard page down_8ed8b450-36d8-5fd5-817f-a4884e9b3b71.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'page-down-arrow-solo-b014'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/controls"
    aliases = ()
    keywords = ('page', 'down', 'arrow')
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

        self.add_polyline('shaft',(24,4),(24,14),(24,22),(24,44))
        for i,y in enumerate((14,22)):
         self.add_polyline('bar'+str(i),(14,y),(24,y),(34,y))
         self.relate('connect','shaft','bar'+str(i))
        self.add_polyline('head',(10,30),(24,44),(38,30))
        self.relate('connect','shaft','head')
