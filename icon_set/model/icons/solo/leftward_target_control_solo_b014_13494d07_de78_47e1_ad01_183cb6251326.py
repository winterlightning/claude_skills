"""Target ring opens at the left around a smaller control node; left arrow remains inside. Radius20 envelope centered24,24; node radius3. The node is separated rather than falsely connected.
Lucide construction reference: circle-arrow-left.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '13494d07-de78-47e1-ad01-183cb6251326'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-014/references/cursor move target left_13494d07-de78-47e1-ad01-183cb6251326.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'leftward-target-control-solo-b014'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('leftward', 'target', 'control')
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

        self.add_arc('ring',(8,12),(8,36),radius_x=20,large_arc=True,sweep=True)
        circle('node',8,24,3)
        self.add_polyline('arrowhead',(30,18),(24,24),(30,30))
        self.add_line('shaft',(24,24),(34,24))
        self.relate('connect','arrowhead','shaft')
