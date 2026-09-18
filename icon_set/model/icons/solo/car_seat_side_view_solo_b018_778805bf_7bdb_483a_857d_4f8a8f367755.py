"""Padded side-view car seat, tall back merging into broad low cushion. Single smooth contour with ample upholstery thickness. Centerline6,6–42,42.
Lucide construction reference: armchair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='778805bf-7bdb-483a-857d-4f8a8f367755'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/seat car_778805bf-7bdb-483a-857d-4f8a8f367755.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/seat car_778805bf-7bdb-483a-857d-4f8a8f367755.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/seat car_778805bf-7bdb-483a-857d-4f8a8f367755.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='car-seat-side-view-solo-b018'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('car', 'seat', 'side', 'view')
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

        path('seat',(6,12),[('B',(6,8),(7,6),(10,6)),('B',(16,6),(15,21),(21,27)),('B',(27,33),(32,32),(37,32)),('A',5,5,True,(42,37)),('A',5,5,True,(37,42)),('L',(22,42)),('B',(10,42),(6,34),(6,12))],True)
