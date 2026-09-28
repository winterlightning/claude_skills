"""Open gauge semicircle and short diagonal pointer crossing near right end. Upper arc radius20, pointer uses shared cardinal endpoint for certified attachment.
Lucide construction reference: gauge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9d3425c4-0090-4fdf-b40b-9f93695f8ca8'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/adjustable_9d3425c4-0090-4fdf-b40b-9f93695f8ca8.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/adjustable_9d3425c4-0090-4fdf-b40b-9f93695f8ca8.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-017/references/adjustable_9d3425c4-0090-4fdf-b40b-9f93695f8ca8.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='curved-gauge-indicator-solo-b017'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('curved', 'gauge', 'indicator')
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

        path('arc',(4,24),[('A',20,20,True,(24,4)),('A',20,20,True,(44,24))])
        self.add_polyline('pointer',(36,32),(44,24));self.relate('connect','arc','pointer')
