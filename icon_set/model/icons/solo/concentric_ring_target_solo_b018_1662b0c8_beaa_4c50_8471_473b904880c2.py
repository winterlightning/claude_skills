"""Concentric target with radial cardinal links. Three rings reduced to two to preserve large empty center and8-unit annular clearance. Outer20 and inner10 radii.
Lucide construction reference: target.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1662b0c8-beaa-4c50-8471-473b904880c2'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/chinese board_1662b0c8-beaa-4c50-8471-473b904880c2.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/chinese board_1662b0c8-beaa-4c50-8471-473b904880c2.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/chinese board_1662b0c8-beaa-4c50-8471-473b904880c2.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='concentric-ring-target-solo-b018'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('concentric', 'ring', 'target')
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

        circle('outer',24,24,20);circle('inner',24,24,10)
        for n,a,b in [('n',(24,4),(24,14)),('s',(24,44),(24,34)),('w',(4,24),(14,24)),('e',(44,24),(34,24))]:
         self.add_line(n,a,b);self.relate('connect','outer',n);self.relate('connect','inner',n)
