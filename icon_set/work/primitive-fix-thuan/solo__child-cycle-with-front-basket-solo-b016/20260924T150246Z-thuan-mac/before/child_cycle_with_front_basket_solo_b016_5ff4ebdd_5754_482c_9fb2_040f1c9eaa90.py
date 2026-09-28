"""Child cycle with two visible wheels, high-backed seat, upright front stem and open basket. Reduce frame to clean shared strokes, no small hubs. Centerline4,8–44,40.
Lucide construction reference: bike.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5ff4ebdd-5754-482c-9fb2-040f1c9eaa90'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='child-cycle-with-front-basket-solo-b016'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/toys"
    aliases=()
    keywords=('child', 'cycle', 'with', 'front', 'basket')
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

        circle('rear',11,33,7);circle('front',37,33,7)
        self.add_polyline('frame',(11,26),(11,18),(24,18),(29,16),(37,16),(37,26))
        self.add_line('backrest',(11,8),(11,18));self.relate('connect','backrest','frame')
        self.relate('connect','rear','frame');self.relate('connect','front','frame')
        self.add_polyline('basket',(29,16),(29,8),(44,8),(44,16),(37,16));self.relate('connect','basket','frame')
