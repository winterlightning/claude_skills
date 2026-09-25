"""Outlined check with short left arm and broad long diagonal return. Rounded stroke joins soften deliberate polygon corners. Centerline4,8–44,40.
Construction reference: check.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1e26ac1b-672a-5b59-a650-b299e22cc422'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/check_1e26ac1b-672a-5b59-a650-b299e22cc422.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/check_1e26ac1b-672a-5b59-a650-b299e22cc422.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/check_1e26ac1b-672a-5b59-a650-b299e22cc422.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='outlined-check-mark-solo-b015-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases=()
    keywords=('outlined', 'check', 'mark')
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

        self.add_polyline('check',(4,27),(11,20),(20,28),(36,8),(44,14),(21,40),closed=True)
