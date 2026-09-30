"""Small elevated treehouse with peaked roof and ladder beside tree. Tree crown reduced to branching contour; door omitted to keep ladder rungs clear. Centerline4,8–44,40.
Construction reference: tree-deciduous; house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='69d37e4e-d972-4edd-9487-a2d5344250c0'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='treehouse-with-ladder-solo-b016-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    categories = ("primitives", "kids")
    aliases=()
    keywords=('treehouse', 'with', 'ladder')
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

        self.add_polyline('trunk',(4,40),(4,25),(4,17))
        path('crown',(4,17),[('B',(4,11),(7,8),(12,8))]);self.relate('connect','trunk','crown')
        self.add_line('branch',(4,25),(11,21));self.relate('connect','trunk','branch')
        self.add_polyline('house',(21,18),(33,8),(44,18),(44,26),(38,26),(27,26),(21,26),closed=True)
        for x in (27,38):self.add_polyline('ladder'+str(x),(x,26),(x,34),(x,40));self.relate('connect','house','ladder'+str(x))
        self.add_line('rung',(27,34),(38,34));self.relate('connect','rung','ladder27');self.relate('connect','rung','ladder38')
