"""Equal outlined triangles point up/down across a wide central gap. Axis24 with mirrored definitions. Centerline8,4–40,44.
Construction reference: arrow-up-down.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='194c7896-d2b7-5216-9507-6c3057e3f666'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/scroll vertical_194c7896-d2b7-5216-9507-6c3057e3f666.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/scroll vertical_194c7896-d2b7-5216-9507-6c3057e3f666.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/scroll vertical_194c7896-d2b7-5216-9507-6c3057e3f666.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='opposing-vertical-triangles-solo-b015-r02'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases=()
    keywords=('opposing', 'vertical', 'triangles')
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

        for sign in (-1,1):self.add_polyline('triangle'+str(sign),(8,24+sign*7),(24,24+sign*20),(40,24+sign*7),closed=True)
