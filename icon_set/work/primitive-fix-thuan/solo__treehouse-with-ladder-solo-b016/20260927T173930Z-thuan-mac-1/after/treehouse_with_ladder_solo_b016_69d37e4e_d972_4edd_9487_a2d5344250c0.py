"""Elevated playhouse beside a simplified branching tree. Ladder joins house sill; arched entrance omitted to keep clear rung spacing. Centerline6,6–42,42.
Lucide construction reference: tree-deciduous; house.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='69d37e4e-d972-4edd-9487-a2d5344250c0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__treehouse-with-ladder-solo-b016/20260927T173930Z-thuan-mac-1/reference/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
AUTHOR = 'gpt-6'
class BatchIcon(Solo48):
    icon_id='treehouse-with-ladder-solo-b016'
    keyshape=Keyshape.SQUARE
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

        # Rounded tree canopy and attached trunk; house and ladder use one roof axis.
        circle('crown',12,14,6)
        self.add_line('trunk-upper',(12,20),(12,34))
        self.add_line('trunk-lower',(12,34),(12,42))
        self.add_line('branch',(12,34),(18,28))
        self.relate('connect','crown','trunk-upper')
        self.relate('connect','trunk-upper','trunk-lower','branch')
        self.add_polyline('house',(26,16),(34,6),(42,16),(42,24),(26,24),closed=True)
        self.add_line('ladder-left',(30,24),(30,42))
        self.add_line('ladder-right',(38,24),(38,42))
        self.add_line('rung',(30,34),(38,34))
        for rail in ('ladder-left','ladder-right'):
            self.relate('connect','house',rail)
            self.relate('connect','rung',rail)
