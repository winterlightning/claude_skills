"""Tree with three-lobed crown, straight trunk and right branch carrying two swing ropes. Centerline6,6–42,42; natural asymmetry preserves swing.
Lucide construction reference: tree-deciduous.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='tree-with-hanging-swing-solo-b016'
    keyshape=Keyshape.SQUARE
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

        path('crown',(6,25),[('B',(6,25),(6,21),(6,17)),('B',(6,13),(9,11),(12,11)),('B',(12,8),(15,6),(19,6)),('B',(23,6),(26,8),(26,11)),('B',(32,11),(32,19),(28,21))])
        self.add_polyline('trunk',(16,20),(16,30),(16,42))
        self.add_polyline('branch',(16,30),(22,30),(30,30),(40,30),(42,30));self.relate('connect','trunk','branch')
        self.add_polyline('swing',(30,30),(30,42),(40,42),(40,30));self.relate('connect','branch','swing')
