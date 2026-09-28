"""Volleyball net with two posts and a regular 4-by-3 mesh. Gentle sag reduced to level strands for open8-unit cells. Centerline4,8–44,40.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ebcea186-c719-4114-bdb5-259abc380960'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/net rope_ebcea186-c719-4114-bdb5-259abc380960.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='volleyball-net-solo-b016'
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

        for x in (4,14,24,34,44):
         ys=(8,16,24,32,40) if x in (4,44) else (8,16,24,32)
         self.add_polyline('v'+str(x),*((x,y) for y in ys))
        for y in (8,16,24,32):
         self.add_polyline('h'+str(y),*((x,y) for x in (4,14,24,34,44)))
         for x in (4,14,24,34,44):self.relate('connect','h'+str(y),'v'+str(x))
