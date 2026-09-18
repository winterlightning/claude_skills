"""Up/down arrows mirrored about y24 and detached horizontal divider. Join short shafts to heads for legibility at48. Centerline10,4–38,44.
Lucide construction reference: arrow-up-down.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='dfb60b37-8f2a-452c-872d-06287e677376'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/expand vertical 2_dfb60b37-8f2a-452c-872d-06287e677376.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/expand vertical 2_dfb60b37-8f2a-452c-872d-06287e677376.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-015/references/expand vertical 2_dfb60b37-8f2a-452c-872d-06287e677376.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='outward-arrows-from-horizontal-divider-solo-b015'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/controls"
    aliases=()
    keywords=('outward', 'arrows', 'from', 'horizontal', 'divider')
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

        self.add_line('divider',(10,24),(38,24))
        for sign in (-1,1):
         tip=24+sign*20;inner=24+sign*8
         self.add_polyline('head'+str(sign),(10,inner),(24,tip),(38,inner))
         self.add_line('shaft'+str(sign),(24,tip),(24,inner));self.relate('connect','head'+str(sign),'shaft'+str(sign))
