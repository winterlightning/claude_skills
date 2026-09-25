"""Spinning top, symmetric sloping shoulders and tapering base around a broad band. Grip and spindle reduced to short strokes. Centerline6,6–42,42.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ff9c76b0-7c19-5556-95e9-4a21e04b0161'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='traditional-spinning-top-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    aliases=()
    keywords=('traditional', 'spinning', 'top')
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

        self.add_polyline('top',(6,20),(24,10),(42,20),(42,28),(24,38),(6,28),closed=True)
        self.add_line('band',(6,28),(42,28));self.relate('connect','top','band')
        self.add_line('grip',(24,6),(24,10));self.relate('connect','grip','top')
        self.add_line('spindle',(24,38),(24,42));self.relate('connect','spindle','top')
