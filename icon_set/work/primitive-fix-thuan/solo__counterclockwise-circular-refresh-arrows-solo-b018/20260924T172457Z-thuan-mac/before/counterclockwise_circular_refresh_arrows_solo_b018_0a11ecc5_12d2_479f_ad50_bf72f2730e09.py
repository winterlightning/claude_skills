"""Counterclockwise circular arrows, upper left endpoint points down and lower right endpoint points up. Radius20 circle, directional heads deliberately asymmetric.
Lucide construction reference: refresh-ccw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0a11ecc5-12d2-479f-ad50-bf72f2730e09'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='counterclockwise-circular-refresh-arrows-solo-b018'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('counterclockwise', 'circular', 'refresh', 'arrows')
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

        self.add_arc('upper',(44,24),(12,8),radius_x=20,sweep=False)
        self.add_arc('lower',(4,24),(36,40),radius_x=20,sweep=False)
        self.add_polyline('lefthead',(24,8),(12,8),(12,20));self.relate('connect','upper','lefthead')
        self.add_polyline('righthead',(24,40),(36,40),(36,28));self.relate('connect','lower','righthead')
