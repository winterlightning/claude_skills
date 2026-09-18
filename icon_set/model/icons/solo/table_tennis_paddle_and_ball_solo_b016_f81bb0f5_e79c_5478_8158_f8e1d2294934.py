"""Round paddle with integrated diagonal handle, diagonal face seam, and separate ball. Centerline6,6–42,42; simplify handle to one sturdy stroke.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f81bb0f5-e79c-5478-8158-f8e1d2294934'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys ping pong_f81bb0f5-e79c-5478-8158-f8e1d2294934.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='table-tennis-paddle-and-ball-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/toys"
    aliases=()
    keywords=('table', 'tennis', 'paddle', 'and', 'ball')
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

        circle('paddle',22,18,12)
        self.add_line('handle',(6,42),(22,30));self.relate('connect','paddle','handle')
        circle('ball',38,38,4)
