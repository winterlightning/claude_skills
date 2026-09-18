"""Hamburger with domed bun, broad middle filling and rounded lower bun. Three layers separated by8-unit band. Centerline4,8–44,40.
Lucide construction reference: sandwich.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='be3b26b6-b45d-4812-8c00-261ef430b1ad'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hamburger_be3b26b6-b45d-4812-8c00-261ef430b1ad.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/hamburger_be3b26b6-b45d-4812-8c00-261ef430b1ad.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-018/references/hamburger_be3b26b6-b45d-4812-8c00-261ef430b1ad.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='hamburger-solo-solo-b018'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/everyday"
    aliases=()
    keywords=('hamburger', 'solo')
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

        path('burger',(4,24),[('B',(4,14),(12,8),(24,8)),('B',(36,8),(44,14),(44,24)),('L',(44,32)),('A',8,8,True,(36,40)),('L',(12,40)),('A',8,8,True,(4,32)),('L',(4,24))],True)
        for y in (24,32):self.add_line('layer'+str(y),(4,y),(44,y));self.relate('connect','burger','layer'+str(y))
