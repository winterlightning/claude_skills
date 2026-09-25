"""Elevated playhouse beside a simplified branching tree. Ladder joins house sill; arched entrance omitted to keep clear rung spacing. Centerline6,6–42,42.
Lucide construction reference: tree-deciduous; house.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='69d37e4e-d972-4edd-9487-a2d5344250c0'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='treehouse-with-ladder-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
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

        self.add_polyline('tree',(6,42),(6,25),(6,14))
        self.add_polyline('branch',(6,25),(10,21));self.relate('connect','tree','branch')
        path('crown',(6,14),[('B',(6,8),(9,6),(14,6))]);self.relate('connect','crown','tree')
        self.add_polyline('house',(20,18),(31,6),(42,18),(42,28),(36,28),(26,28),(20,28),closed=True)
        self.add_polyline('left',(26,28),(26,36),(26,42));self.add_polyline('right',(36,28),(36,36),(36,42))
        self.add_line('rung',(26,36),(36,36))
        for n in ('left','right'):self.relate('connect','house',n);self.relate('connect','rung',n)
