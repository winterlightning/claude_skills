"""Spinning top with rounded broad band, sloping shoulders and tapered underside. Grip and bottom spindle simplified to strokes. Centerline4,8–44,40.
Construction reference: No useful exact Lucide match; supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ff9c76b0-7c19-5556-95e9-4a21e04b0161'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/spinning top_ff9c76b0-7c19-5556-95e9-4a21e04b0161.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='traditional-spinning-top-solo-b016-r02'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/toys"
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

        path('band',(8,20),[('L',(24,20)),('L',(40,20)),('A',4,4,True,(44,24)),('A',4,4,True,(40,28)),('L',(8,28)),('A',4,4,True,(4,24)),('A',4,4,True,(8,20))],True)
        self.add_polyline('upper',(8,20),(24,12),(40,20));self.add_polyline('lower',(8,28),(24,36),(40,28))
        for n in ('upper','lower'):self.relate('connect','band',n)
        self.add_line('grip',(24,8),(24,12));self.relate('connect','upper','grip')
        self.add_line('tip',(24,36),(24,40));self.relate('connect','lower','tip')
