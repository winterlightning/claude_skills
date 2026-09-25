"""House with open bottom rectangular doorway. One continuous facade shares roof nodes. Centerline6,6–42,42.
Lucide construction reference: house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='359d205e-3e65-4681-9176-4cc7661ec8be'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_359d205e-3e65-4681-9176-4cc7661ec8be.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_359d205e-3e65-4681-9176-4cc7661ec8be.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/house_359d205e-3e65-4681-9176-4cc7661ec8be.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='house-with-open-rectangular-entrance-solo-b015'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "interface-essential"
    categories = ("interface-essential", "other", "primitives-generate")
    aliases=()
    keywords=('house', 'with', 'open', 'rectangular', 'entrance')
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

        self.add_polyline('roof',(6,24),(10,20),(24,6),(38,20),(42,24))
        self.add_polyline('walls',(10,20),(10,42),(18,42),(18,29),(30,29),(30,42),(38,42),(38,20))
        self.relate('connect','roof','walls')
