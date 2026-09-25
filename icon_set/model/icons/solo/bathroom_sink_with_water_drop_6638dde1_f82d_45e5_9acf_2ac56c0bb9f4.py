"""Rounded basin, a hooked faucet, drain trap, and detached water drop. Plumbing remains asymmetrical.
Omissions: Secondary pipe wall omitted to preserve clearance.
Construction references: no useful direct Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='6638dde1-f82d-45e5-9acf-2ac56c0bb9f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__bathroom-sink-with-water-drop/20260924T171046Z-thuan-mac/reference/home improvement 10_6638dde1-f82d-45e5-9acf-2ac56c0bb9f4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bathroom-sink-with-water-drop'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('home', 'improvement', '10')

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
        self.path('basin',(20,18),[('L',(42,18)),('C',(31,29),(42,25),(38,29)),('C',(20,18),(24,29),(20,25))],True)
        self.path('faucet',(26,10),[('A',(34,10),4,4,True),('L',(34,18))])
        self.relate('connect','faucet','basin')
        self.path('drain',(31,29),[('L',(31,36)),('A',(39,36),4,4,False),('L',(39,33)),('L',(42,33))])
        self.relate('connect','drain','basin')
        self.path('drop',(12,28),[('C',(18,36),(14,31),(18,33)),('A',(6,36),6,6,True),('C',(12,28),(6,33),(10,31))],True)
