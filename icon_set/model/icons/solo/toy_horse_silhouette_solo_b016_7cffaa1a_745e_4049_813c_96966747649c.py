"""Left-facing toy horse with projecting muzzle, upright ear, two broad legs and thin tail. Single coherent silhouette; no rocking base added. Centerline4,8–44,40.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7cffaa1a-745e-4049-813c-96966747649c'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='toy-horse-silhouette-solo-b016'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/toys"
    aliases=()
    keywords=('toy', 'horse', 'silhouette')
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

        path('horse',(10,8),[('L',(9,13)),('L',(4,17)),('L',(4,23)),('L',(12,23)),('L',(14,28)),('L',(8,40)),('L',(18,40)),('L',(23,32)),('L',(29,32)),('L',(34,40)),('L',(44,40)),('L',(38,27)),('L',(38,23)),('L',(22,23)),('B',(21,15),(18,10),(10,8))],True)
