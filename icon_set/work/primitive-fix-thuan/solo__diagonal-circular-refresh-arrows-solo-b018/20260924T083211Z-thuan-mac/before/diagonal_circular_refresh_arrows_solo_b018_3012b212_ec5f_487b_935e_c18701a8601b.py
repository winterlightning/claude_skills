"""Two clockwise circular arrows with opposed diagonal breaks. Radius20 circle with diagonal endpoint offsets12,16; heads turn inward.
Lucide construction reference: refresh-cw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3012b212-ec5f-487b-935e-c18701a8601b'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/arrows spin_3012b212-ec5f-487b-935e-c18701a8601b.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/arrows spin_3012b212-ec5f-487b-935e-c18701a8601b.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/arrows spin_3012b212-ec5f-487b-935e-c18701a8601b.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='diagonal-circular-refresh-arrows-solo-b018'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('diagonal', 'circular', 'refresh', 'arrows')
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

        self.add_arc('upper',(4,24),(36,8),radius_x=20,sweep=True)
        self.add_arc('lower',(44,24),(12,40),radius_x=20,sweep=True)
        self.add_polyline('tophead',(24,8),(36,8),(36,20));self.relate('connect','upper','tophead')
        self.add_polyline('bottomhead',(24,40),(12,40),(12,28));self.relate('connect','lower','bottomhead')
