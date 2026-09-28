"""Volleyball net with tall posts and a generous three-by-two mesh. Fewer cords preserve clear openings; sag reduced to horizontal strands. Centerline4,8–44,40.
Construction reference: No useful exact Lucide match; supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ebcea186-c719-4114-bdb5-259abc380960'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='volleyball-net-solo-b016-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    categories = ("primitives", "kids")
    aliases=()
    keywords=('volleyball', 'net')
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

        xs=(4,17,31,44);ys=(10,20,30)
        for x in xs:
         points=[(x,y) for y in ((8,10,20,30,40) if x in (4,44) else ys)]
         self.add_polyline('v'+str(x),*points)
        for y in ys:
         self.add_polyline('h'+str(y),*((x,y) for x in xs))
         for x in xs:self.relate('connect','h'+str(y),'v'+str(x))
