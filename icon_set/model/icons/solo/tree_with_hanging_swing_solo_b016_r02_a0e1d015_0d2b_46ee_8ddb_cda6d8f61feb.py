"""Tree with lobed open crown, straight trunk and right swing with two ropes. Branch below foliage leaves clean clearance. Centerline4,8–44,40.
Construction reference: tree-deciduous.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='tree-with-hanging-swing-solo-b016-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/toys"
    aliases=()
    keywords=('tree', 'with', 'hanging', 'swing')
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

        path('crown',(4,24),[('L',(4,18)),('B',(4,14),(8,12),(10,12)),('B',(10,9),(14,8),(18,8)),('B',(22,8),(26,9),(26,12)),('B',(32,12),(32,18),(29,20))])
        self.add_polyline('trunk',(15,21),(15,29),(15,40))
        self.add_polyline('branch',(15,29),(30,29),(41,29),(44,29));self.relate('connect','trunk','branch')
        self.add_polyline('swing',(30,29),(30,40),(41,40),(41,29));self.relate('connect','branch','swing')
