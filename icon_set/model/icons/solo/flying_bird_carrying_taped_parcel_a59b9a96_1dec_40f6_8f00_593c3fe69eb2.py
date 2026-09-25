"""Flying bird with raised wing, round head, pointed beak and suspended rectangular parcel.
Omissions: Parcel tape and eye omitted due to limited interior clearance.
Construction references: ['bird'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a59b9a96-1dec-40f6-8f00-593c3fe69eb2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dropshipper bird box_a59b9a96-1dec-40f6-8f00-593c3fe69eb2.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='flying-bird-carrying-taped-parcel'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('dropshipper', 'bird', 'box')

    def path(self, name, start, commands, closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{name}-{i}'; ids.append(eid)
            if c[0]=='L': self.add_line(eid,here,c[1])
            elif c[0]=='A': self.add_arc(eid,here,c[1],radius_x=c[2],radius_y=c[3],sweep=c[4],large_arc=c[5] if len(c)>5 else False)
            elif c[0]=='C': self.add_bezier(eid,here,(c[2],c[3],c[1]))
            here=c[1]
        self.add_contour(name,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,x,y,w,h,r):
        self.path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)

    def build(self):
        self.path('bird',(6,6),[('C',(24,16),(15,6),(23,8)),('C',(35,11),(23,7),(31,6)),('L',(42,16)),('L',(36,19)),('C',(24,28),(35,25),(30,28)),('L',(18,28)),('L',(6,28)),('L',(12,20)),('C',(6,6),(8,18),(6,12))],True)
        self.path('parcel',(18,28),[('L',(18,42)),('L',(32,42)),('L',(32,28))])
        self.relate('connect','bird','parcel')
