"""Left-facing toy horse with broad rounded muzzle, short ear and two splayed feet. Thin tail omitted where it crowds the haunch; no rocking base invented. Centerline4,8–44,40.
Construction reference: No useful exact Lucide match; supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7cffaa1a-745e-4049-813c-96966747649c'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys rocking horse 1_7cffaa1a-745e-4049-813c-96966747649c.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='toy-horse-silhouette-solo-b016-r02'
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

        path('horse',(12,8),[('L',(10,14)),('L',(8,17)),('A',4,4,False,(4,21)),('L',(4,24)),('L',(12,24)),('L',(14,29)),('L',(8,40)),('L',(19,40)),('L',(24,32)),('L',(29,32)),('L',(34,40)),('L',(44,40)),('L',(38,27)),('L',(38,24)),('L',(23,24)),('B',(22,15),(19,10),(12,8))],True)
